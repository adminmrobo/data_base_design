/* ══ MiniSQL — 페이지 안에서 도는 작은 SQL 실습 엔진 (MariaDB 문법·오류 메시지를 흉내 낸 교육용 부분집합) ══
   지원: CREATE/DROP DATABASE·TABLE·VIEW, USE, SHOW DATABASES/TABLES, DESCRIBE, ALTER TABLE(ADD/DROP/CHANGE/MODIFY/RENAME COLUMN,
   ADD CONSTRAINT PK/FK/UNIQUE/CHECK), INSERT, UPDATE, DELETE, TRUNCATE, SELECT(JOIN·GROUP BY·HAVING·ORDER BY·LIMIT·UNION·하위 질의),
   START TRANSACTION/BEGIN/COMMIT/ROLLBACK, GRANT/REVOKE(모의). 실제 DBMS가 아니므로 결과는 '모의 실행'으로 표시한다. */
var MiniSQL=(function(){
'use strict';
var KW=('SELECT FROM WHERE AND OR NOT INSERT INTO VALUES UPDATE SET DELETE CREATE TABLE DROP ALTER ADD COLUMN PRIMARY KEY FOREIGN REFERENCES '+
 'CONSTRAINT CHECK UNIQUE NULL IS IN LIKE BETWEEN AS ON JOIN INNER LEFT RIGHT FULL OUTER CROSS GROUP BY HAVING ORDER ASC DESC LIMIT OFFSET UNION ALL '+
 'DISTINCT EXISTS CASE WHEN THEN ELSE END DATABASE DATABASES USE SHOW TABLES DESCRIBE DESC VIEW TRUNCATE CHANGE MODIFY RENAME TO DEFAULT '+
 'START TRANSACTION BEGIN COMMIT ROLLBACK GRANT REVOKE CASCADE RESTRICT TRUE FALSE IF NO ACTION CHARACTER CHARSET COLLATE FULL').split(' ');
var KWS={}; KW.forEach(function(k){KWS[k]=1;});
function SqlErr(code,state,msg){this.code=code;this.state=state;this.message=msg;}
function E(code,state,msg){return new SqlErr(code,state,msg);}

/* ── 토큰 ── */
function lex(src){
  var t=[],i=0,n=src.length,c;
  while(i<n){
    c=src[i];
    if(/\s/.test(c)){i++;continue;}
    if(c==='-'&&src[i+1]==='-'){while(i<n&&src[i]!=='\n')i++;continue;}
    if(c==='#'){while(i<n&&src[i]!=='\n')i++;continue;}
    if(c==='/'&&src[i+1]==='*'){var j=src.indexOf('*/',i+2); i=j<0?n:j+2; continue;}
    if(c==="'"||c==='"'){var q=c,s='';i++;
      while(i<n){ if(src[i]==='\\'&&i+1<n){s+=src[i+1];i+=2;continue;} if(src[i]===q){ if(src[i+1]===q){s+=q;i+=2;continue;} break;} s+=src[i++]; }
      if(i>=n)throw E(1064,'42000','문자열 따옴표가 닫히지 않았습니다 (near \''+s.slice(0,20)+'\')');
      i++; t.push({k:'str',v:s}); continue;}
    if(c==='`'){var j2=src.indexOf('`',i+1); if(j2<0)throw E(1064,'42000','역따옴표(`)가 닫히지 않았습니다'); t.push({k:'id',v:src.slice(i+1,j2),q:1}); i=j2+1; continue;}
    if(/[0-9]/.test(c)||(c==='.'&&/[0-9]/.test(src[i+1]||''))){var m=/^[0-9]*\.?[0-9]+(e[+-]?[0-9]+)?/i.exec(src.slice(i)); t.push({k:'num',v:parseFloat(m[0])}); i+=m[0].length; continue;}
    var mm=/^[A-Za-z_\u0080-\uffff][A-Za-z0-9_$\u0080-\uffff]*/.exec(src.slice(i));
    if(mm){var w=mm[0],u=w.toUpperCase(); t.push(KWS[u]?{k:'kw',v:u,raw:w}:{k:'id',v:w}); i+=w.length; continue;}
    var two=src.substr(i,2);
    if(two==='<>'||two==='!='||two==='<='||two==='>='||two==='||'||two==='->'){t.push({k:'op',v:two==='!='?'<>':two});i+=2;continue;}
    if('(),;.*=<>+-/%@'.indexOf(c)>=0){t.push({k:'op',v:c});i++;continue;}
    throw E(1064,'42000','알 수 없는 글자 \''+c+'\'가 있습니다');
  }
  return t;
}
/* 문장 나누기 (따옴표 안의 ; 는 무시) */
function split(src){
  var out=[],cur='',q=null;
  for(var i=0;i<src.length;i++){var c=src[i];
    if(q){cur+=c; if(c==='\\'){cur+=src[++i]||'';continue;} if(c===q)q=null; continue;}
    if(c==="'"||c==='"'||c==='`'){q=c;cur+=c;continue;}
    if(c==='-'&&src[i+1]==='-'){while(i<src.length&&src[i]!=='\n')i++; cur+='\n'; continue;}
    if(c===';'){if(cur.trim())out.push(cur.trim()); cur='';continue;}
    cur+=c;}
  if(cur.trim())out.push(cur.trim());
  return out.filter(function(s){return !/^\s*(->\s*)*$/.test(s);});
}

/* ── 파서 ── */
function P(toks){this.t=toks;this.i=0;}
P.prototype={
  pk:function(o){return this.t[this.i+(o||0)];},
  isk:function(v,o){var x=this.pk(o);return x&&x.k==='kw'&&x.v===v;},
  iso:function(v,o){var x=this.pk(o);return x&&x.k==='op'&&x.v===v;},
  near:function(){var x=this.pk(); return x?(x.raw||x.v):'문장 끝';},
  err:function(){return E(1064,'42000','SQL 문법 오류: \''+this.near()+'\' 근처를 확인하세요');},
  kw:function(v){if(!this.isk(v))throw this.err(); this.i++;},
  op:function(v){if(!this.iso(v))throw this.err(); this.i++;},
  opt:function(v){if(this.isk(v)){this.i++;return true;}return false;},
  opto:function(v){if(this.iso(v)){this.i++;return true;}return false;},
  ident:function(){var x=this.pk(); if(x&&(x.k==='id'||(x.k==='kw'&&'KEY DATABASE VIEW ACTION NO'.indexOf(x.v)<0&&!/^(SELECT|FROM|WHERE|SET|VALUES|ON|JOIN|GROUP|ORDER|HAVING|LIMIT|UNION|AND|OR|LEFT|RIGHT|INNER|AS)$/.test(x.v)))){this.i++;return x.raw||x.v;} throw this.err();},
  end:function(){return this.i>=this.t.length;},
  // 식
  expr:function(){return this.or_();},
  or_:function(){var l=this.and_(); while(this.isk('OR')||this.iso('||')){this.i++; l={t:'or',l:l,r:this.and_()};} return l;},
  and_:function(){var l=this.not_(); while(this.isk('AND')){this.i++; l={t:'and',l:l,r:this.not_()};} return l;},
  not_:function(){if(this.isk('NOT')&&!this.isk('EXISTS',1)){this.i++;return {t:'not',e:this.not_()};} return this.cmp();},
  cmp:function(){
    var l=this.add();
    for(;;){
      var x=this.pk(); if(!x)return l;
      if(x.k==='op'&&/^(=|<>|<|>|<=|>=)$/.test(x.v)){this.i++; l={t:'cmp',op:x.v,l:l,r:this.add()}; continue;}
      if(this.isk('IS')){this.i++; var neg=this.opt('NOT'); this.kw('NULL'); l={t:'isnull',e:l,neg:neg}; continue;}
      var neg2=false;
      if(this.isk('NOT')&&(this.isk('LIKE',1)||this.isk('IN',1)||this.isk('BETWEEN',1))){this.i++;neg2=true;}
      if(this.opt('LIKE')){l={t:'like',l:l,r:this.add(),neg:neg2};continue;}
      if(this.opt('BETWEEN')){var lo=this.add(); this.kw('AND'); var hi=this.add(); l={t:'between',e:l,lo:lo,hi:hi,neg:neg2};continue;}
      if(this.opt('IN')){this.op('(');
        if(this.isk('SELECT')){var sq=this.select(); this.op(')'); l={t:'insub',e:l,q:sq,neg:neg2}; continue;}
        var list=[this.expr()]; while(this.opto(','))list.push(this.expr()); this.op(')'); l={t:'in',e:l,list:list,neg:neg2}; continue;}
      return l;
    }
  },
  add:function(){var l=this.mul(); while(this.iso('+')||this.iso('-')){var o=this.t[this.i++].v; l={t:'bin',op:o,l:l,r:this.mul()};} return l;},
  mul:function(){var l=this.un(); while(this.iso('*')||this.iso('/')||this.iso('%')){var o=this.t[this.i++].v; l={t:'bin',op:o,l:l,r:this.un()};} return l;},
  un:function(){if(this.opto('-'))return {t:'neg',e:this.un()}; if(this.opto('+'))return this.un(); return this.prim();},
  prim:function(){
    var x=this.pk(); if(!x)throw this.err();
    if(x.k==='num'){this.i++;return {t:'lit',v:x.v};}
    if(x.k==='str'){this.i++;return {t:'lit',v:x.v};}
    if(x.k==='kw'&&x.v==='NULL'){this.i++;return {t:'lit',v:null};}
    if(x.k==='kw'&&(x.v==='TRUE'||x.v==='FALSE')){this.i++;return {t:'lit',v:x.v==='TRUE'?1:0};}
    if(x.k==='kw'&&x.v==='EXISTS'){this.i++; this.op('('); var q=this.select(); this.op(')'); return {t:'exists',q:q};}
    if(x.k==='kw'&&x.v==='NOT'&&this.isk('EXISTS',1)){this.i+=2; this.op('('); var q2=this.select(); this.op(')'); return {t:'not',e:{t:'exists',q:q2}};}
    if(x.k==='kw'&&x.v==='CASE'){this.i++; var ws=[],el=null;
      while(this.opt('WHEN')){var c=this.expr(); this.kw('THEN'); ws.push([c,this.expr()]);}
      if(this.opt('ELSE'))el=this.expr(); this.kw('END'); return {t:'case',ws:ws,el:el};}
    if(x.k==='op'&&x.v==='('){this.i++;
      if(this.isk('SELECT')){var sq=this.select(); this.op(')'); return {t:'sub',q:sq};}
      var e=this.expr(); this.op(')'); return e;}
    if(x.k==='op'&&x.v==='*'){this.i++;return {t:'star'};}
    if(x.k==='id'||x.k==='kw'){
      var name=x.raw||x.v; this.i++;
      if(this.iso('(')){ // 함수
        this.i++; var fn=name.toUpperCase(),args=[],dist=false;
        if(this.iso('*')){this.i++;args.push({t:'star'});}
        else if(!this.iso(')')){dist=this.opt('DISTINCT'); args.push(this.expr()); while(this.opto(','))args.push(this.expr());}
        this.op(')'); return {t:'fn',fn:fn,args:args,dist:dist};
      }
      if(x.k==='kw'&&!/^(KEY|ACTION|NO|DATABASE)$/.test(x.v)&&!x.raw)throw this.err();
      if(this.iso('.')){this.i++; if(this.iso('*')){this.i++;return {t:'star',tb:name};} return {t:'col',tb:name,c:this.ident()};}
      return {t:'col',c:name};
    }
    throw this.err();
  },
  // SELECT
  select:function(){
    var q=this.select1();
    while(this.isk('UNION')){this.i++; var all=this.opt('ALL'); this.opt('DISTINCT'); q={t:'union',l:q,r:this.select1(),all:all};}
    if(q.t==='union'){ if(this.isk('ORDER')){this.i++;this.kw('BY');q.order=this.orderList();} if(this.opt('LIMIT'))q.limit=this.limit(); }
    return q;
  },
  select1:function(){
    if(this.iso('(')){this.i++; var inner=this.select(); this.op(')'); return inner;}
    this.kw('SELECT'); var q={t:'select',distinct:false,items:[],from:[],where:null,group:null,having:null,order:null,limit:null};
    if(this.opt('DISTINCT'))q.distinct=true; else this.opt('ALL');
    do{ var e=this.expr(),al=null;
      if(this.opt('AS'))al=this.aliasTok(); else if(this.pk()&&(this.pk().k==='id'||this.pk().k==='str'))al=this.aliasTok();
      q.items.push({e:e,as:al}); }while(this.opto(','));
    if(this.opt('FROM')){
      q.from.push({src:this.tref(),join:null});
      for(;;){
        if(this.opto(',')){q.from.push({src:this.tref(),join:'cross'});continue;}
        var jt=null;
        if(this.isk('JOIN')){this.i++;jt='inner';}
        else if(this.isk('INNER')&&this.isk('JOIN',1)){this.i+=2;jt='inner';}
        else if(this.isk('CROSS')&&this.isk('JOIN',1)){this.i+=2;jt='cross';}
        else if((this.isk('LEFT')||this.isk('RIGHT')||this.isk('FULL'))){var side=this.t[this.i++].v.toLowerCase(); this.opt('OUTER'); this.kw('JOIN'); jt=side;}
        if(!jt)break;
        var src=this.tref(),on=null; if(this.opt('ON'))on=this.expr();
        q.from.push({src:src,join:jt,on:on});
      }
    }
    if(this.opt('WHERE'))q.where=this.expr();
    if(this.isk('GROUP')){this.i++;this.kw('BY'); q.group=[this.expr()]; while(this.opto(','))q.group.push(this.expr());}
    if(this.opt('HAVING'))q.having=this.expr();
    if(this.isk('ORDER')){this.i++;this.kw('BY'); q.order=this.orderList();}
    if(this.opt('LIMIT'))q.limit=this.limit();
    return q;
  },
  aliasTok:function(){var x=this.pk(); if(x.k==='str'){this.i++;return x.v;} return this.ident();},
  orderList:function(){var o=[]; do{var e=this.expr(),d=false; if(this.opt('DESC'))d=true; else this.opt('ASC'); o.push({e:e,desc:d});}while(this.opto(',')); return o;},
  limit:function(){var a=this.pk(); if(!a||a.k!=='num')throw this.err(); this.i++; var off=0,cnt=a.v;
    if(this.opto(',')){off=a.v; cnt=this.t[this.i++].v;} else if(this.opt('OFFSET')){off=this.t[this.i++].v;} return {off:off,cnt:cnt};},
  tref:function(){
    if(this.iso('(')){this.i++; var q=this.select(); this.op(')'); this.opt('AS'); return {sub:q,as:this.ident()};}
    var name=this.ident(); if(this.iso('.')){this.i++; name=this.ident();}
    var as=null; if(this.opt('AS'))as=this.ident(); else if(this.pk()&&this.pk().k==='id')as=this.ident();
    return {name:name,as:as||name};
  }
};

/* ── 값 ── */
function isNum(v){return typeof v==='number';}
function num(v){if(v==null)return null; if(typeof v==='number')return v; var f=parseFloat(v); return isNaN(f)?0:f;}
function cmpv(a,b){ // MariaDB 기본 콜레이션처럼 대소문자 무시
  if(a==null||b==null)return null;
  if(isNum(a)&&isNum(b))return a<b?-1:a>b?1:0;
  if(isNum(a)||isNum(b)){var x=num(a),y=num(b); return x<y?-1:x>y?1:0;}
  var s=String(a).toLowerCase(),u=String(b).toLowerCase(); return s<u?-1:s>u?1:0;
}
function like(v,p){ if(v==null||p==null)return null;
  var re='^'+String(p).replace(/[.+?^${}()|[\]\\]/g,'\\$&').replace(/%/g,'.*').replace(/_/g,'.')+'$';
  return new RegExp(re,'i').test(String(v))?1:0; }
function truth(v){return v!=null&&v!==0&&v!=='0'&&v!==false&&v!=='';}
function show(v){ if(v==null)return 'NULL'; if(typeof v==='number'){return Number.isInteger(v)?String(v):String(Math.round(v*10000)/10000);} return String(v); }
function clone(o){return JSON.parse(JSON.stringify(o));}
var AGG={COUNT:1,SUM:1,AVG:1,MIN:1,MAX:1};
function hasAgg(e){ if(!e||typeof e!=='object')return false; if(e.t==='fn'&&AGG[e.fn])return true; if(e.t==='sub'||e.t==='exists'||e.t==='insub')return e.t==='insub'?hasAgg(e.e):false;
  for(var k in e){var v=e[k]; if(k==='q')continue; if(Array.isArray(v)){for(var i=0;i<v.length;i++)if(hasAgg(v[i])||(Array.isArray(v[i])&&v[i].some(hasAgg)))return true;} else if(v&&typeof v==='object'&&hasAgg(v))return true;}
  return false;}
function exprName(e,src){ if(e.t==='col')return e.c; if(e.t==='lit')return show(e.v); if(e.t==='fn')return e.fn+'('+(e.args[0]&&e.args[0].t==='star'?'*':e.args.map(function(a){return exprName(a);}).join(','))+')'; if(e.t==='star')return '*'; return src||'expr'; }

/* ── 데이터베이스 ── */
function DB(){this.dbs={};this.cur=null;this.snap=null;this.tx=false;this.notes=[];}
DB.prototype={
  space:function(){ if(!this.cur)throw E(1046,'3D000','데이터베이스가 선택되지 않았습니다 (No database selected) — USE 이름; 을 먼저 실행하세요'); return this.dbs[this.cur]; },
  tbl:function(name,soft){ var sp=this.space(),k=String(name).toLowerCase(); if(sp.tables[k])return sp.tables[k]; if(soft)return null;
    throw E(1146,'42S02','Table \''+this.cur+'.'+name+'\' doesn\'t exist — 테이블이 없습니다'); },
  view:function(name){var sp=this.dbs[this.cur]; return sp?sp.views[String(name).toLowerCase()]:null;},
  run:function(sql){ // 여러 문장 실행 → 결과 배열
    var out=[],stmts=split(sql);
    for(var i=0;i<stmts.length;i++){
      try{ out.push(this.exec(stmts[i])); }
      catch(e){ if(e instanceof SqlErr){out.push({err:'ERROR '+e.code+' ('+e.state+'): '+e.message,sql:stmts[i]}); break;} throw e; }
    }
    return out;
  },
  exec:function(s){
    var p=new P(lex(s)),r;
    if(p.isk('SELECT')||p.iso('(')){var q=p.select(); if(!p.end())throw p.err(); r=this.query(q,null); r.sql=s; r.msg=r.rows.length+' rows in set'; return r;}
    var x=p.pk(); if(!x)return {msg:'(빈 문장)'};
    var v=x.k==='kw'?x.v:(x.v||'').toUpperCase();
    p.i++;
    switch(v){
      case 'CREATE': return this.create(p);
      case 'DROP': return this.drop(p);
      case 'USE': var d=p.ident(); if(!this.dbs[d.toLowerCase()])throw E(1049,'42000','Unknown database \''+d+'\''); this.cur=d.toLowerCase(); return {msg:'Database changed'};
      case 'SHOW': return this.showStmt(p);
      case 'DESCRIBE': case 'DESC': case 'EXPLAIN': return this.describe(this.tbl(p.ident()));
      case 'INSERT': return this.insert(p);
      case 'UPDATE': return this.update(p);
      case 'DELETE': return this.del(p);
      case 'ALTER': return this.alter(p);
      case 'TRUNCATE': p.opt('TABLE'); var t=this.tbl(p.ident()); this.commitImplicit(); var n=t.rows.length; t.rows=[]; return {msg:'Query OK, 0 rows affected (구조는 남고 행 '+n+'개가 모두 지워짐)'};
      case 'START': p.kw('TRANSACTION'); return this.begin();
      case 'BEGIN': return this.begin();
      case 'COMMIT': this.snap=null; this.tx=false; return {msg:'Query OK — 커밋: 변경을 영구 저장했습니다'};
      case 'ROLLBACK': if(!this.tx)return {msg:'Query OK — 열린 트랜잭션이 없어 되돌릴 것이 없습니다 (자동 커밋 상태)'};
        this.dbs=this.snap.dbs; this.cur=this.snap.cur; this.snap=null; this.tx=false; return {msg:'Query OK — 롤백: 트랜잭션 시작 전 상태로 되돌렸습니다'};
      case 'GRANT': case 'REVOKE': return {msg:'Query OK — (모의) 권한 '+(v==='GRANT'?'부여':'회수')+' 문장을 받았습니다. 이 실습실에는 사용자 계정이 없어 실제 권한은 바뀌지 않습니다', info:1};
      case 'SET': return {msg:'Query OK (모의: 설정 변수는 무시합니다)', info:1};
    }
    throw E(1064,'42000','이 실습실이 모르는 문장입니다: \''+(x.raw||x.v)+'\'');
  },
  begin:function(){ if(this.tx)this.snap=null; this.snap={dbs:clone(this.dbs),cur:this.cur}; this.tx=true; return {msg:'Query OK — 트랜잭션 시작 (COMMIT 전까지 바뀐 내용은 ROLLBACK으로 되돌릴 수 있음)'}; },
  commitImplicit:function(){ if(this.tx){this.snap=null;this.tx=false;this.notes.push('DDL 문장이 실행되어 열린 트랜잭션이 자동 커밋되었습니다 (MariaDB 규칙)');} },
  create:function(p){
    if(p.opt('DATABASE')||p.isk('SCHEMA')){ var ine=false; if(p.isk('IF')){p.i++;p.kw('NOT');p.kw('EXISTS');ine=true;}
      var d=p.ident(),k=d.toLowerCase(); if(this.dbs[k]){if(ine)return {msg:'Query OK, 1 warning (이미 있음)'}; throw E(1007,'HY000','Can\'t create database \''+d+'\'; database exists');}
      this.dbs[k]={name:d,tables:{},views:{},order:[]}; return {msg:'Query OK, 1 row affected'}; }
    if(p.opt('VIEW')){var vn=p.ident(); p.kw('AS'); var st=p.i,q=p.select(); var sp=this.space(); sp.views[vn.toLowerCase()]={name:vn,q:q}; this.query(q,null); return {msg:'Query OK, 0 rows affected (뷰 '+vn+' 생성)'};}
    p.kw('TABLE'); var ine2=false; if(p.isk('IF')){p.i++;p.kw('NOT');p.kw('EXISTS');ine2=true;}
    var name=p.ident(),sp2=this.space(),key=name.toLowerCase();
    if(sp2.tables[key]){ if(ine2)return {msg:'Query OK, 0 rows affected, 1 warning'}; throw E(1050,'42S01','Table \''+name+'\' already exists'); }
    var t={name:name,cols:[],rows:[],pk:null,uniq:[],fks:[],checks:[]};
    p.op('('); var cons=[];
    do{
      if(p.isk('PRIMARY')||p.isk('FOREIGN')||p.isk('CONSTRAINT')||p.isk('UNIQUE')||p.isk('CHECK')){ cons.push(this.constraint(p,t,true)); continue; }
      this.coldef(p,t);
    }while(p.opto(','));
    p.op(')');
    while(!p.end()){p.i++;} // ENGINE=..., CHARSET= 무시
    this.commitImplicit();
    sp2.tables[key]=t; sp2.order.push(key);
    try{ t.fks.forEach(function(f){this.checkFkTarget(f,t);},this); cons.forEach(function(k){this.applyCon(t,k,false);},this); }
    catch(e){ delete sp2.tables[key]; sp2.order.pop(); throw e; }
    return {msg:'Query OK, 0 rows affected'};
  },
  coldef:function(p,t,noPush){
    var c={name:p.ident(),type:'',len:null,notnull:false,def:undefined}; var ty=p.pk(); if(!ty)throw p.err();
    c.type=(ty.raw||ty.v).toUpperCase(); p.i++;
    if(p.opto('(')){var a=p.pk(); p.i++; c.len=a.v; if(p.opto(',')){c.scale=p.pk().v;p.i++;} p.op(')');}
    if(p.isk('UNSIGNED')||(p.pk()&&p.pk().k==='id'&&/^unsigned$/i.test(p.pk().v)))p.i++;
    for(;;){
      if(p.isk('NOT')&&p.isk('NULL',1)){p.i+=2;c.notnull=true;continue;}
      if(p.opt('NULL'))continue;
      if(p.isk('PRIMARY')){p.i++;p.kw('KEY'); t.pk={name:'PRIMARY',cols:[c.name]}; c.notnull=true; continue;}
      if(p.opt('UNIQUE')){p.opt('KEY'); t.uniq.push({name:c.name,cols:[c.name]}); continue;}
      if(p.opt('DEFAULT')){c.def=p.prim().v; continue;}
      if(p.opt('CHECK')){p.op('('); var st=p.i,e=p.expr(); p.op(')'); t.checks.push({name:t.name+'_chk_'+(t.checks.length+1),e:e}); continue;}
      if(p.opt('REFERENCES')){var rt=p.ident(); p.op('('); var rc=p.ident(); p.op(')'); var f={name:t.name+'_ibfk_'+(t.fks.length+1),cols:[c.name],ref:rt,refcols:[rc],onDelete:'RESTRICT'}; this.fkTail(p,f); t.fks.push(f); continue;}
      if(p.isk('CHARACTER')){p.i++;p.kw('SET');p.i++;continue;}
      if(p.isk('COLLATE')||p.isk('CHARSET')){p.i+=2;continue;}
      if(p.pk()&&p.pk().k==='id'&&/^(auto_increment|comment)$/i.test(p.pk().v)){var w=p.pk().v.toLowerCase(); p.i++; if(w==='comment')p.i++; else c.auto=true; continue;}
      break;
    }
    if(!noPush){ if(this.colIdx(t,c.name)>=0)throw E(1060,'42S21','Duplicate column name \''+c.name+'\''); t.cols.push(c);}
    return c;
  },
  fkTail:function(p,f){ while(p.isk('ON')){p.i++; var ev=p.t[p.i++].v; var act; if(p.opt('CASCADE'))act='CASCADE'; else if(p.isk('SET')){p.i++;p.kw('NULL');act='SET NULL';} else if(p.opt('RESTRICT'))act='RESTRICT'; else {p.kw('NO');p.kw('ACTION');act='RESTRICT';} if(ev==='DELETE')f.onDelete=act; else f.onUpdate=act;} },
  constraint:function(p,t,inCreate){
    var cname=null; if(p.opt('CONSTRAINT')){ if(!p.isk('PRIMARY')&&!p.isk('FOREIGN')&&!p.isk('UNIQUE')&&!p.isk('CHECK'))cname=p.ident(); }
    var cols=function(){p.op('('); var a=[p.ident()]; while(p.opto(','))a.push(p.ident()); p.op(')'); return a;};
    if(p.isk('PRIMARY')){p.i++;p.kw('KEY'); var pc=cols(); if(t.pk)throw E(1068,'42000','Multiple primary key defined — 기본키는 테이블에 하나만 둘 수 있습니다');
      var self=this; pc.forEach(function(c){if(self.colIdx(t,c)<0)throw E(1072,'42000','Key column \''+c+'\' doesn\'t exist in table');});
      return {kind:'pk',name:'PRIMARY',cols:pc,label:cname};}
    if(p.opt('UNIQUE')){p.opt('KEY'); return {kind:'uniq',name:cname||'u_'+t.uniq.length,cols:cols()};}
    if(p.opt('CHECK')){p.op('('); var e=p.expr(); p.op(')'); return {kind:'check',name:cname||t.name+'_chk_'+(t.checks.length+1),e:e};}
    if(p.opt('FOREIGN')){p.kw('KEY'); var fc=cols(); p.kw('REFERENCES'); var rt=p.ident(); var rc=cols();
      var f={name:cname||t.name+'_ibfk_'+(t.fks.length+1),cols:fc,ref:rt,refcols:rc,onDelete:'RESTRICT'}; this.fkTail(p,f); return {kind:'fk',f:f};}
    throw p.err();
  },
  applyCon:function(t,k,validate){
    if(!k)return;
    if(k.kind==='pk'){ if(validate){this.checkUniqueRows(t,k.cols,'PRIMARY',true);} t.pk={name:'PRIMARY',cols:k.cols,label:k.label}; var self=this; k.cols.forEach(function(c){t.cols[self.colIdx(t,c)].notnull=true;}); }
    else if(k.kind==='uniq'){ if(validate)this.checkUniqueRows(t,k.cols,k.name,false); t.uniq.push(k); }
    else if(k.kind==='check'){ if(validate){var self2=this; t.rows.forEach(function(r){ if(!self2.checkOk(t,k,r))throw E(4025,'23000','CONSTRAINT `'+k.name+'` failed for `'+(self2.cur)+'`.`'+t.name+'` — 이미 들어 있는 행이 이 조건을 어깁니다');});} t.checks.push(k); }
    else if(k.kind==='fk'){ this.checkFkTarget(k.f,t); if(validate)this.checkFkRows(t,k.f); t.fks.push(k.f); }
  },
  checkFkTarget:function(f,t){
    var rt=this.tbl(f.ref,true);
    if(!rt)throw E(1005,'HY000','Can\'t create table (errno: 150 "Foreign key constraint is incorrectly formed") — 참조할 테이블 \''+f.ref+'\'이 없습니다');
    var okKey=function(cols){return cols&&cols.length===f.refcols.length&&cols.every(function(c,i){return c.toLowerCase()===f.refcols[i].toLowerCase();});};
    if(!(rt.pk&&okKey(rt.pk.cols))&&!rt.uniq.some(function(u){return okKey(u.cols);}))
      throw E(1005,'HY000','Can\'t create table `'+this.cur+'`.`'+(t?t.name:'?')+'` (errno: 150 "Foreign key constraint is incorrectly formed") — 참조되는 열 \''+f.ref+'('+f.refcols.join(',')+')\'이 기본키나 UNIQUE가 아닙니다');
  },
  checkFkRows:function(t,f){var self=this; t.rows.forEach(function(r){self.fkOk(t,f,r);});},
  fkOk:function(t,f,r){
    var vals=f.cols.map(function(c){return r[c.toLowerCase()];}); if(vals.some(function(v){return v==null;}))return;
    var rt=this.tbl(f.ref);
    var hit=rt.rows.some(function(x){return f.refcols.every(function(c,i){return cmpv(x[c.toLowerCase()],vals[i])===0;});});
    if(!hit)throw E(1452,'23000','Cannot add or update a child row: a foreign key constraint fails (`'+this.cur+'`.`'+t.name+'`, CONSTRAINT `'+f.name+'` FOREIGN KEY (`'+f.cols.join('`,`')+'`) REFERENCES `'+f.ref+'` (`'+f.refcols.join('`,`')+'`)) — 부모 테이블에 \''+vals.join(',')+'\' 값이 없습니다');
  },
  checkUniqueRows:function(t,cols,name,isPk){
    var seen={},self=this;
    t.rows.forEach(function(r){var k=cols.map(function(c){var v=r[c.toLowerCase()]; if(v==null&&isPk)throw E(1138,'22004','기본키 열 \''+c+'\'에 NULL이 있어 기본키로 정할 수 없습니다'); return String(v).toLowerCase();}).join('\u0001');
      if(cols.some(function(c){return r[c.toLowerCase()]==null;}))return;
      if(seen[k])throw E(1062,'23000','Duplicate entry \''+cols.map(function(c){return show(r[c.toLowerCase()]);}).join('-')+'\' for key \''+name+'\''); seen[k]=1;});
  },
  checkOk:function(t,k,r){ var v=this.ev(k.e,this.rowEnv(t,r)); return v==null||truth(v); },
  rowEnv:function(t,r){var o={}; o[t.name.toLowerCase()]=r; return {rows:o,names:[t.name.toLowerCase()],outer:null,tbl:t};},
  colIdx:function(t,c){c=String(c).toLowerCase(); for(var i=0;i<t.cols.length;i++)if(t.cols[i].name.toLowerCase()===c)return i; return -1;},
  coerce:function(t,c,v){
    if(v==null)return null; var ty=c.type;
    if(/INT|DECIMAL|NUMERIC|FLOAT|DOUBLE|REAL|BIT|BOOL/.test(ty)){
      if(typeof v==='string'){ if(!/^\s*-?\d*\.?\d+(e[+-]?\d+)?\s*$/i.test(v))throw E(1366,'22007','Incorrect '+(/INT/.test(ty)?'integer':'decimal')+' value: \''+v+'\' for column `'+c.name+'` — 숫자 열에 글자를 넣었습니다'); v=parseFloat(v); }
      if(/INT/.test(ty)||(/DECIMAL|NUMERIC/.test(ty)&&!c.scale))v=Math.round(v);
      else if(/DECIMAL|NUMERIC/.test(ty)&&c.scale)v=Math.round(v*Math.pow(10,c.scale))/Math.pow(10,c.scale);
      return v;
    }
    v=String(v);
    if(/CHAR/.test(ty)&&c.len&&v.length>c.len)throw E(1406,'22001','Data too long for column \''+c.name+'\' — 최대 '+c.len+'자인데 '+v.length+'자를 넣었습니다');
    if(ty==='DATE'&&!/^\d{4}-\d{2}-\d{2}$/.test(v))throw E(1292,'22007','Incorrect date value: \''+v+'\' for column `'+c.name+'` — 날짜는 \'YYYY-MM-DD\' 형식입니다');
    return v;
  },
  validateRow:function(t,r,skip){
    var self=this;
    t.cols.forEach(function(c){var k=c.name.toLowerCase(); if(r[k]==null&&c.notnull)throw E(1048,'23000','Column \''+c.name+'\' cannot be null — 이 열은 비워 둘 수 없습니다');});
    var keys=[]; if(t.pk)keys.push({cols:t.pk.cols,name:'PRIMARY'}); t.uniq.forEach(function(u){keys.push({cols:u.cols,name:u.name});});
    keys.forEach(function(kk){
      var vals=kk.cols.map(function(c){return r[c.toLowerCase()];}); if(vals.some(function(v){return v==null;}))return;
      t.rows.forEach(function(x){ if(x===skip)return; if(kk.cols.every(function(c,i){return cmpv(x[c.toLowerCase()],vals[i])===0;}))
        throw E(1062,'23000','Duplicate entry \''+vals.map(show).join('-')+'\' for key \''+kk.name+'\' — 키 값이 이미 있습니다'); });
    });
    t.checks.forEach(function(k){ if(!self.checkOk(t,k,r))throw E(4025,'23000','CONSTRAINT `'+k.name+'` failed for `'+self.cur+'`.`'+t.name+'` — 제약 조건(CHECK)을 어기는 값입니다'); });
    t.fks.forEach(function(f){self.fkOk(t,f,r);});
  },
  insert:function(p){
    p.opt('INTO'); var t=this.tbl(p.ident()),cols=null;
    if(p.iso('(')){p.i++; cols=[p.ident()]; while(p.opto(','))cols.push(p.ident()); p.op(')');}
    cols=cols||t.cols.map(function(c){return c.name;});
    var self=this; cols.forEach(function(c){if(self.colIdx(t,c)<0)throw E(1054,'42S22','Unknown column \''+c+'\' in \'field list\'');});
    var rowsIn=[];
    if(p.opt('VALUES')||p.opt('VALUE')){
      do{ p.op('('); var vals=[]; if(!p.iso(')')){vals.push(p.expr()); while(p.opto(','))vals.push(p.expr());} p.op(')');
        if(vals.length!==cols.length)throw E(1136,'21S01','Column count doesn\'t match value count at row '+(rowsIn.length+1)+' — 열 '+cols.length+'개에 값 '+vals.length+'개');
        rowsIn.push(vals.map(function(e){return self.ev(e,{rows:{},names:[],outer:null});})); }while(p.opto(','));
    } else if(p.isk('SELECT')){ var r=this.query(p.select(),null); r.rows.forEach(function(x){rowsIn.push(x);}); }
    else throw p.err();
    var work=t.rows.slice(),added=[];
    try{
      rowsIn.forEach(function(vals){
        var row={}; t.cols.forEach(function(c){row[c.name.toLowerCase()]=c.def===undefined?null:c.def;});
        cols.forEach(function(c,i){var col=t.cols[self.colIdx(t,c)]; row[col.name.toLowerCase()]=self.coerce(t,col,vals[i]);});
        t.cols.forEach(function(c){ if(c.auto&&row[c.name.toLowerCase()]==null){var mx=0; t.rows.forEach(function(x){mx=Math.max(mx,num(x[c.name.toLowerCase()])||0);}); row[c.name.toLowerCase()]=mx+1;} });
        self.validateRow(t,row,null); t.rows.push(row); added.push(row);
      });
    }catch(e){ t.rows=work; throw e; }
    return {msg:'Query OK, '+added.length+' row'+(added.length===1?'':'s')+' affected',table:t.name,changed:added};
  },
  update:function(p){
    var t=this.tbl(p.ident()); p.kw('SET'); var sets=[],self=this;
    do{var c=p.ident(); if(this.colIdx(t,c)<0)throw E(1054,'42S22','Unknown column \''+c+'\' in \'field list\''); p.op('='); sets.push([t.cols[this.colIdx(t,c)],p.expr()]);}while(p.opto(','));
    var w=null; if(p.opt('WHERE'))w=p.expr();
    var before=clone(t.rows),n=0,changed=[],pkCols=(t.pk?t.pk.cols:[]).map(function(c){return c.toLowerCase();});
    try{
      t.rows.forEach(function(r,idx){
        var env=self.rowEnv(t,r); if(w&&!truth(self.ev(w,env)))return;
        var nr=clone(r); sets.forEach(function(s){nr[s[0].name.toLowerCase()]=self.coerce(t,s[0],self.ev(s[1],env));});
        self.validateRow(t,nr,r);
        // 이 행을 참조하는 자식이 있는데 키를 바꾸면 막는다 (RESTRICT)
        if(pkCols.length&&pkCols.some(function(c){return cmpv(r[c],nr[c])!==0;}))self.refGuard(t,r,'update');
        if(JSON.stringify(nr)!==JSON.stringify(r)){n++; changed.push(nr);} t.rows[idx]=nr;
      });
    }catch(e){t.rows=before; throw e;}
    return {msg:'Query OK, '+n+' row'+(n===1?'':'s')+' affected (Rows matched: '+n+')',table:t.name,changed:changed};
  },
  refGuard:function(t,r,why){
    var sp=this.space(),self=this,ops=[];
    Object.keys(sp.tables).forEach(function(k){var ct=sp.tables[k];
      ct.fks.forEach(function(f){ if(f.ref.toLowerCase()!==t.name.toLowerCase())return;
        var kids=ct.rows.filter(function(x){return f.refcols.every(function(c,i){return cmpv(x[f.cols[i].toLowerCase()],r[c.toLowerCase()])===0;});});
        if(!kids.length)return;
        if(why==='delete'&&f.onDelete==='CASCADE'){ops.push(function(){ct.rows=ct.rows.filter(function(x){return kids.indexOf(x)<0;});});}
        else if(why==='delete'&&f.onDelete==='SET NULL'){ops.push(function(){kids.forEach(function(x){f.cols.forEach(function(c){x[c.toLowerCase()]=null;});});});}
        else throw E(1451,'23000','Cannot '+(why==='delete'?'delete':'update')+' or update a parent row: a foreign key constraint fails (`'+self.cur+'`.`'+ct.name+'`, CONSTRAINT `'+f.name+'`) — 이 행을 참조하는 자식 행 '+kids.length+'개가 '+ct.name+'에 있습니다');
      });});
    ops.forEach(function(f){f();});
  },
  del:function(p){
    p.kw('FROM'); var t=this.tbl(p.ident()),w=null,self=this; if(p.opt('WHERE'))w=p.expr();
    var before=clone(this.dbs),keep=[],gone=[];
    try{ t.rows.forEach(function(r){ if(!w||truth(self.ev(w,self.rowEnv(t,r)))){self.refGuard(t,r,'delete'); gone.push(r);} else keep.push(r);}); }
    catch(e){this.dbs=before; throw e;}
    t.rows=keep; return {msg:'Query OK, '+gone.length+' row'+(gone.length===1?'':'s')+' affected',table:t.name};
  },
  drop:function(p){
    if(p.opt('DATABASE')){var ie=false; if(p.isk('IF')){p.i++;p.kw('EXISTS');ie=true;} var d=p.ident(); if(!this.dbs[d.toLowerCase()]){if(ie)return {msg:'Query OK, 0 rows affected, 1 warning'}; throw E(1008,'HY000','Can\'t drop database \''+d+'\'; database doesn\'t exist');} delete this.dbs[d.toLowerCase()]; if(this.cur===d.toLowerCase())this.cur=null; return {msg:'Query OK'};}
    if(p.opt('VIEW')){var vn=p.ident(); delete this.space().views[vn.toLowerCase()]; return {msg:'Query OK, 0 rows affected'};}
    if(p.isk('COLUMN')||(p.pk()&&p.pk().k==='id'&&!p.isk('TABLE')))throw E(1064,'42000','DROP 다음에는 TABLE·DATABASE·VIEW가 와야 합니다. 열을 지우려면 ALTER TABLE 테이블 DROP COLUMN 열; 로 씁니다');
    p.kw('TABLE'); var ie2=false; if(p.isk('IF')){p.i++;p.kw('EXISTS');ie2=true;}
    var sp=this.space(),names=[p.ident()]; while(p.opto(','))names.push(p.ident());
    var self=this,msgs=[];
    names.forEach(function(nm){var k=nm.toLowerCase(); if(!sp.tables[k]){ if(ie2){msgs.push('note: '+nm+' 없음');return;} throw E(1051,'42S02','Unknown table \''+self.cur+'.'+nm+'\' — 지울 테이블이 없습니다');}
      Object.keys(sp.tables).forEach(function(o){ if(o===k)return; sp.tables[o].fks.forEach(function(f){ if(f.ref.toLowerCase()===k&&names.map(function(x){return x.toLowerCase();}).indexOf(o)<0)throw E(1451,'23000','Cannot delete or update a parent row: a foreign key constraint fails — \''+sp.tables[o].name+'\' 테이블이 이 테이블을 외래키로 참조합니다');});});
    });
    this.commitImplicit();
    names.forEach(function(nm){var k=nm.toLowerCase(); delete sp.tables[k]; sp.order=sp.order.filter(function(x){return x!==k;});});
    return {msg:'Query OK, 0 rows affected'+(msgs.length?' ('+msgs.join(', ')+')':'')};
  },
  alter:function(p){
    p.kw('TABLE'); var t=this.tbl(p.ident()),self=this,did=[];
    var snapshot=clone(t);
    try{
    do{
      if(p.opt('ADD')){
        if(p.isk('CONSTRAINT')||p.isk('PRIMARY')||p.isk('FOREIGN')||p.isk('UNIQUE')||p.isk('CHECK')){ this.applyCon(t,this.constraint(p,t,false),true); did.push('제약 추가'); continue; }
        p.opt('COLUMN'); var c=this.coldef(p,t,true); if(this.colIdx(t,c.name)>=0)throw E(1060,'42S21','Duplicate column name \''+c.name+'\'');
        t.cols.push(c); t.rows.forEach(function(r){r[c.name.toLowerCase()]=c.def===undefined?null:c.def;}); if(c.notnull&&t.rows.length&&c.def===undefined)t.rows.forEach(function(r){r[c.name.toLowerCase()]=/INT|DEC|FLOAT|DOUBLE/.test(c.type)?0:'';}); did.push('열 추가'); continue;
      }
      if(p.opt('DROP')){
        if(p.opt('PRIMARY')){p.kw('KEY'); t.pk=null; continue;}
        if(p.isk('FOREIGN')){p.i++;p.kw('KEY'); var fk=p.ident(); t.fks=t.fks.filter(function(f){return f.name.toLowerCase()!==fk.toLowerCase();}); continue;}
        if(p.opt('CONSTRAINT')||p.opt('CHECK')){var cn=p.ident(); t.checks=t.checks.filter(function(k){return k.name.toLowerCase()!==cn.toLowerCase();}); t.fks=t.fks.filter(function(f){return f.name.toLowerCase()!==cn.toLowerCase();}); continue;}
        p.opt('COLUMN'); var dc=p.ident(),di=this.colIdx(t,dc); if(di<0)throw E(1091,'42000','Can\'t DROP COLUMN `'+dc+'`; check that it exists');
        t.cols.splice(di,1); t.rows.forEach(function(r){delete r[dc.toLowerCase()];}); if(t.pk&&t.pk.cols.some(function(x){return x.toLowerCase()===dc.toLowerCase();}))t.pk=null; did.push('열 삭제'); continue;
      }
      if(p.opt('CHANGE')){ p.opt('COLUMN'); var old=p.ident(),oi=this.colIdx(t,old); if(oi<0)throw E(1054,'42S22','Unknown column \''+old+'\' in \''+t.name+'\'');
        var nc=this.coldef(p,t,true); t.cols[oi]=nc; t.rows.forEach(function(r){var v=r[old.toLowerCase()]; delete r[old.toLowerCase()]; r[nc.name.toLowerCase()]=self.coerce(t,nc,v);});
        if(t.pk)t.pk.cols=t.pk.cols.map(function(x){return x.toLowerCase()===old.toLowerCase()?nc.name:x;}); did.push('열 바꿈'); continue; }
      if(p.opt('MODIFY')){ p.opt('COLUMN'); var mc=this.coldef(p,t,true),mi=this.colIdx(t,mc.name); if(mi<0)throw E(1054,'42S22','Unknown column \''+mc.name+'\'');
        t.cols[mi]=mc; t.rows.forEach(function(r){r[mc.name.toLowerCase()]=self.coerce(t,mc,r[mc.name.toLowerCase()]);}); did.push('열 형식 바꿈'); continue; }
      if(p.opt('RENAME')){
        if(p.opt('COLUMN')){var a=p.ident(); p.kw('TO'); var b=p.ident(),ai=this.colIdx(t,a); if(ai<0)throw E(1054,'42S22','Unknown column \''+a+'\' in \''+t.name+'\'');
          t.cols[ai].name=b; t.rows.forEach(function(r){r[b.toLowerCase()]=r[a.toLowerCase()]; delete r[a.toLowerCase()];}); if(t.pk)t.pk.cols=t.pk.cols.map(function(x){return x.toLowerCase()===a.toLowerCase()?b:x;}); did.push('열 이름 바꿈'); continue;}
        p.opt('TO'); var nn=p.ident(),sp=this.space(); delete sp.tables[t.name.toLowerCase()]; sp.order=sp.order.map(function(x){return x===t.name.toLowerCase()?nn.toLowerCase():x;}); t.name=nn; sp.tables[nn.toLowerCase()]=t; continue;
      }
      throw p.err();
    }while(p.opto(','));
    }catch(e){ var sp2=this.space(); sp2.tables[snapshot.name.toLowerCase()]=snapshot; throw e; }
    this.commitImplicit();
    return {msg:'Query OK, '+t.rows.length+' rows affected · Records: '+t.rows.length+' Duplicates: 0 Warnings: 0',table:t.name};
  },
  showStmt:function(p){
    if(p.opt('DATABASES')){var self=this; return {cols:['Database'],rows:['information_schema','mysql','performance_schema'].concat(Object.keys(this.dbs).map(function(k){return self.dbs[k].name;})).map(function(x){return [x];}),msg:''};}
    if(p.opt('TABLES')){var sp=this.space(); return {cols:['Tables_in_'+this.cur],rows:sp.order.map(function(k){return [sp.tables[k].name];}).concat(Object.keys(sp.views).map(function(k){return [sp.views[k].name+' (VIEW)'];})),msg:''};}
    if(p.opt('CREATE')){ if(p.opt('DATABASE')){var d=p.ident(); return {cols:['Database','Create Database'],rows:[[d,'CREATE DATABASE `'+d+'` /*!40100 DEFAULT CHARACTER SET utf8mb4 */']],msg:''};} p.opt('TABLE'); var t=this.tbl(p.ident()); return {cols:['Table','Create Table'],rows:[[t.name,this.ddl(t)]],msg:''};}
    if(p.pk()&&/^(full|columns)$/i.test(p.pk().v)){ if(/full/i.test(p.pk().v))p.i++; p.i++; p.kw('FROM'); return this.describe(this.tbl(p.ident()));}
    throw p.err();
  },
  ddl:function(t){var a=t.cols.map(function(c){return '  `'+c.name+'` '+c.type.toLowerCase()+(c.len?'('+c.len+(c.scale!=null?','+c.scale:'')+')':'')+(c.notnull?' NOT NULL':' DEFAULT NULL');});
    if(t.pk)a.push('  PRIMARY KEY (`'+t.pk.cols.join('`,`')+'`)'); t.fks.forEach(function(f){a.push('  CONSTRAINT `'+f.name+'` FOREIGN KEY (`'+f.cols.join('`,`')+'`) REFERENCES `'+f.ref+'` (`'+f.refcols.join('`,`')+'`)');});
    t.checks.forEach(function(k){a.push('  CONSTRAINT `'+k.name+'` CHECK (...)');}); return 'CREATE TABLE `'+t.name+'` (\n'+a.join(',\n')+'\n)';},
  describe:function(t){
    var fkc={}; t.fks.forEach(function(f){f.cols.forEach(function(c){fkc[c.toLowerCase()]=1;});});
    var pkc={}; if(t.pk)t.pk.cols.forEach(function(c){pkc[c.toLowerCase()]=1;});
    var uq={}; t.uniq.forEach(function(u){if(u.cols.length===1)uq[u.cols[0].toLowerCase()]=1;});
    return {cols:['Field','Type','Null','Key','Default','Extra'],rows:t.cols.map(function(c){var k=c.name.toLowerCase();
      return [c.name,c.type.toLowerCase()+(c.len?'('+c.len+(c.scale!=null?','+c.scale:'')+')':''),c.notnull?'NO':'YES',pkc[k]?'PRI':uq[k]?'UNI':fkc[k]?'MUL':'',c.def===undefined?null:c.def,c.auto?'auto_increment':''];}),msg:t.cols.length+' rows in set'};
  },
  /* ── 질의 ── */
  source:function(ref,outer){
    if(ref.sub){var r=this.query(ref.sub,outer); var k=ref.as.toLowerCase(); return {alias:k,cols:r.cols,rows:r.rows.map(function(x){var o={}; r.cols.forEach(function(c,i){o[c.toLowerCase()]=x[i];}); return o;})};}
    var v=this.view(ref.name);
    if(v){var rv; try{rv=this.query(v.q,null);}catch(x){ if(x instanceof SqlErr&&(x.code===1054||x.code===1146))throw E(1356,'HY000','View \''+this.cur+'.'+v.name+'\' references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them — 뷰가 가리키는 표·칸이 바뀌었습니다'); throw x; } return {alias:ref.as.toLowerCase(),cols:rv.cols,rows:rv.rows.map(function(x){var o={}; rv.cols.forEach(function(c,i){o[c.toLowerCase()]=x[i];}); return o;})};}
    var t=this.tbl(ref.name); return {alias:ref.as.toLowerCase(),cols:t.cols.map(function(c){return c.name;}),rows:t.rows};
  },
  query:function(q,outer){
    if(q.t==='union'){
      var a=this.query(q.l,outer),b=this.query(q.r,outer);
      if(a.cols.length!==b.cols.length)throw E(1222,'21000','The used SELECT statements have a different number of columns — UNION 양쪽의 열 수가 다릅니다');
      var rows=a.rows.concat(b.rows);
      if(!q.all){var seen={}; rows=rows.filter(function(r){var k=JSON.stringify(r.map(function(v){return v==null?null:String(v).toLowerCase();})); if(seen[k])return false; seen[k]=1; return true;});}
      var res={cols:a.cols,rows:rows};
      if(q.order){var self=this; res.rows=res.rows.slice().sort(function(x,y){for(var i=0;i<q.order.length;i++){var o=q.order[i],ix=o.e.t==='lit'?o.e.v-1:a.cols.map(function(c){return c.toLowerCase();}).indexOf((o.e.c||'').toLowerCase()); var c=cmpv(x[ix],y[ix]); if(c==null)c=x[ix]==null?(y[ix]==null?0:-1):1; if(c)return o.desc?-c:c;} return 0;});}
      if(q.limit)res.rows=res.rows.slice(q.limit.off,q.limit.off+q.limit.cnt);
      return res;
    }
    var self=this,envs,srcs=[];
    if(!q.from.length){envs=[{rows:{},names:[],outer:outer}];}
    else{
      var first=this.source(q.from[0].src,outer); srcs=[first];
      envs=first.rows.map(function(r){var o={}; o[first.alias]=r; return {rows:o,names:[first.alias],outer:outer,meta:srcs};});
      for(var j=1;j<q.from.length;j++){
        var f=q.from[j],s=this.source(f.src,outer); srcs.push(s);
        var nullRow={}; s.cols.forEach(function(c){nullRow[c.toLowerCase()]=null;});
        var leftNull=function(env){var o={}; Object.keys(env.rows).forEach(function(k){o[k]={}; Object.keys(env.rows[k]).forEach(function(c){o[k][c]=null;});}); return o;};
        var next=[],ok=function(env,r){var e2={rows:Object.assign({},env.rows),names:env.names.concat([s.alias]),outer:outer,meta:srcs}; e2.rows[s.alias]=r; return (!f.on||truth(self.ev(f.on,e2)))?e2:null;};
        if(f.join==='full')throw E(1064,'42000','MariaDB(그리고 MySQL)는 FULL OUTER JOIN을 지원하지 않습니다 — LEFT JOIN과 RIGHT JOIN 결과를 UNION으로 합쳐 같은 결과를 만듭니다');
        if(f.join==='right'){
          var used=[];
          s.rows.forEach(function(r){var hit=false; envs.forEach(function(env){var e2=ok(env,r); if(e2){next.push(e2);hit=true;}});
            if(!hit){var proto=envs[0]||{rows:{},names:[]}; var nr=leftNull(proto); if(!envs.length){srcs.slice(0,-1).forEach(function(ss){var o={}; ss.cols.forEach(function(c){o[c.toLowerCase()]=null;}); nr[ss.alias]=o;});}
              nr[s.alias]=r; next.push({rows:nr,names:(proto.names.length?proto.names:srcs.slice(0,-1).map(function(x){return x.alias;})).concat([s.alias]),outer:outer,meta:srcs});}});
        } else {
          envs.forEach(function(env){var hit=false; s.rows.forEach(function(r){var e2=ok(env,r); if(e2){next.push(e2);hit=true;}});
            if(!hit&&f.join==='left'){var e3={rows:Object.assign({},env.rows),names:env.names.concat([s.alias]),outer:outer,meta:srcs}; e3.rows[s.alias]=nullRow; next.push(e3);}});
        }
        envs=next;
      }
    }
    if(q.from.length&&!envs.length){var ne={rows:{},names:[],outer:outer}; srcs.forEach(function(s){var o={}; s.cols.forEach(function(c){o[c.toLowerCase()]=null;}); ne.rows[s.alias]=o; ne.names.push(s.alias);});
      q.items.forEach(function(it){ if(it.e.t!=='star'&&!hasAgg(it.e))self.ev(it.e,ne); }); if(q.where)self.ev(q.where,ne);}
    if(q.where)envs=envs.filter(function(env){return truth(self.ev(q.where,env));});
    // 열 펼치기
    var items=[];
    q.items.forEach(function(it){
      if(it.e.t==='star'){
        var metas=(envs[0]&&envs[0].meta)||(q.from.length?q.from.map(function(f){return self.source(f.src,outer);}):[]);
        metas.forEach(function(m){ if(it.e.tb&&it.e.tb.toLowerCase()!==m.alias)return; m.cols.forEach(function(c){items.push({e:{t:'col',tb:m.alias,c:c},name:c});});});
        if(it.e.tb&&!metas.some(function(m){return m.alias===it.e.tb.toLowerCase();}))throw E(1051,'42S02','Unknown table \''+it.e.tb+'\'');
      } else items.push({e:it.e,name:it.as||exprName(it.e)});
    });
    var isAgg=q.group||items.some(function(it){return hasAgg(it.e);})||(q.having&&hasAgg(q.having));
    var outRows=[],sortEnvs=[];
    if(isAgg){
      var groups=[],gi={};
      envs.forEach(function(env){var key=q.group?JSON.stringify(q.group.map(function(g){var v=self.evAlias(g,env,items); return v==null?null:String(v).toLowerCase();})):'all';
        if(!(key in gi)){gi[key]=groups.length; groups.push([]);} groups[gi[key]].push(env);});
      if(!q.group&&!groups.length)groups.push([]);
      groups.forEach(function(g){
        var genv={rows:g[0]?g[0].rows:{},names:g[0]?g[0].names:[],outer:outer,group:g,meta:g[0]&&g[0].meta};
        if(q.having&&!truth(self.evAlias(q.having,genv,items)))return;
        outRows.push(items.map(function(it){return self.ev(it.e,genv);})); sortEnvs.push(genv);
      });
    } else {
      envs.forEach(function(env){outRows.push(items.map(function(it){return self.ev(it.e,env);})); sortEnvs.push(env);});
    }
    var res2={cols:items.map(function(it){return it.name;}),rows:outRows};
    if(q.distinct){var seen2={},keep=[],ke=[]; res2.rows.forEach(function(r,i){var k=JSON.stringify(r.map(function(v){return v==null?null:String(v).toLowerCase();})); if(!seen2[k]){seen2[k]=1;keep.push(r);ke.push(sortEnvs[i]);}}); res2.rows=keep; sortEnvs=ke;}
    if(q.order){
      var idx=res2.rows.map(function(r,i){return i;});
      var keyOf=function(o,i){
        if(o.e.t==='lit'&&typeof o.e.v==='number')return res2.rows[i][o.e.v-1];
        if(o.e.t==='col'&&!o.e.tb){var ai=items.map(function(it){return String(it.name).toLowerCase();}).indexOf(o.e.c.toLowerCase()); if(ai>=0)return res2.rows[i][ai];}
        return self.ev(o.e,sortEnvs[i]);};
      idx.sort(function(x,y){for(var k=0;k<q.order.length;k++){var o=q.order[k],a=keyOf(o,x),b=keyOf(o,y),c;
        if(a==null||b==null)c=a==null?(b==null?0:-1):1; else c=cmpv(a,b); if(c)return o.desc?-c:c;} return x-y;});
      res2.rows=idx.map(function(i){return res2.rows[i];});
    }
    if(q.limit)res2.rows=res2.rows.slice(q.limit.off,q.limit.off+q.limit.cnt);
    return res2;
  },
  evAlias:function(e,env,items){ if(e.t==='col'&&!e.tb){ try{return this.ev(e,env);}catch(x){ var i=items.map(function(it){return String(it.name).toLowerCase();}).indexOf(e.c.toLowerCase()); if(i>=0)return this.ev(items[i].e,env); throw x; } } return this.ev(e,env); },
  lookup:function(e,env){
    var c=e.c.toLowerCase();
    for(var en=env;en;en=en.outer){
      if(e.tb){var tb=e.tb.toLowerCase(); if(en.rows&&en.rows[tb]){ if(!(c in en.rows[tb]))throw E(1054,'42S22','Unknown column \''+e.tb+'.'+e.c+'\' in \'field list\''); return en.rows[tb][c];} continue;}
      var hits=(en.names||[]).filter(function(n){return en.rows[n]&&(c in en.rows[n]);});
      if(hits.length>1)throw E(1052,'23000','Column \''+e.c+'\' in field list is ambiguous — 두 테이블에 같은 이름의 열이 있어 \'테이블.열\'로 써야 합니다');
      if(hits.length===1)return en.rows[hits[0]][c];
    }
    throw E(1054,'42S22','Unknown column \''+(e.tb?e.tb+'.':'')+e.c+'\' in \'field list\' — 그런 열이 없습니다');
  },
  ev:function(e,env){
    var self=this,v,l,r;
    switch(e.t){
      case 'lit': return e.v;
      case 'col': return this.lookup(e,env);
      case 'star': return 1;
      case 'neg': v=this.ev(e.e,env); return v==null?null:-num(v);
      case 'bin': l=this.ev(e.l,env); r=this.ev(e.r,env); if(l==null||r==null)return null; l=num(l); r=num(r);
        if(e.op==='+')return l+r; if(e.op==='-')return l-r; if(e.op==='*')return l*r; if(e.op==='/')return r===0?null:l/r; return r===0?null:l%r;
      case 'cmp': l=this.ev(e.l,env); r=this.ev(e.r,env); var c=cmpv(l,r); if(c==null)return null;
        return ({'=':c===0,'<>':c!==0,'<':c<0,'>':c>0,'<=':c<=0,'>=':c>=0})[e.op]?1:0;
      case 'and': l=this.ev(e.l,env); if(l!=null&&!truth(l))return 0; r=this.ev(e.r,env); if(r!=null&&!truth(r))return 0; return (l==null||r==null)?null:1;
      case 'or': l=this.ev(e.l,env); if(truth(l))return 1; r=this.ev(e.r,env); if(truth(r))return 1; return (l==null||r==null)?null:0;
      case 'not': v=this.ev(e.e,env); return v==null?null:(truth(v)?0:1);
      case 'isnull': v=this.ev(e.e,env); return (v==null)!==e.neg?1:0;
      case 'like': v=like(this.ev(e.l,env),this.ev(e.r,env)); return v==null?null:(e.neg?1-v:v);
      case 'between': v=this.ev(e.e,env); var a=cmpv(v,this.ev(e.lo,env)),b=cmpv(v,this.ev(e.hi,env)); if(a==null||b==null)return null; var bt=(a>=0&&b<=0)?1:0; return e.neg?1-bt:bt;
      case 'in': v=this.ev(e.e,env); if(v==null)return null; var hit=e.list.some(function(x){return cmpv(v,self.ev(x,env))===0;}); return (hit!==e.neg)?1:0;
      case 'insub': v=this.ev(e.e,env); if(v==null)return null; var rs=this.query(e.q,env); if(rs.cols.length!==1)throw E(1241,'21000','Operand should contain 1 column(s) — IN 안의 SELECT는 열 하나만 돌려줘야 합니다');
        var h=rs.rows.some(function(x){return cmpv(v,x[0])===0;}); return (h!==e.neg)?1:0;
      case 'exists': return this.query(e.q,env).rows.length?1:0;
      case 'sub': var sr=this.query(e.q,env); if(sr.rows.length>1)throw E(1242,'21000','Subquery returns more than 1 row — 값 하나가 필요한 자리에 여러 행이 나왔습니다'); return sr.rows.length?sr.rows[0][0]:null;
      case 'case': for(var i=0;i<e.ws.length;i++){if(truth(this.ev(e.ws[i][0],env)))return this.ev(e.ws[i][1],env);} return e.el?this.ev(e.el,env):null;
      case 'fn': return this.fn(e,env);
    }
    throw E(1064,'42000','알 수 없는 식');
  },
  fn:function(e,env){
    var self=this,f=e.fn;
    if(AGG[f]){
      var g=env.group; if(!g)throw E(1111,'HY000','Invalid use of group function — 집계 함수는 WHERE에 쓸 수 없습니다 (HAVING을 쓰세요)');
      if(f==='COUNT'&&e.args[0].t==='star')return g.length;
      var vals=g.map(function(x){return self.ev(e.args[0],x);}).filter(function(v){return v!=null;});
      if(e.dist){var s={}; vals=vals.filter(function(v){var k=String(v).toLowerCase(); if(s[k])return false; s[k]=1; return true;});}
      if(f==='COUNT')return vals.length; if(!vals.length)return null;
      if(f==='SUM')return vals.reduce(function(a,b){return a+num(b);},0);
      if(f==='AVG')return vals.reduce(function(a,b){return a+num(b);},0)/vals.length;
      var best=vals[0]; vals.forEach(function(v){var c=cmpv(v,best); if(f==='MIN'?c<0:c>0)best=v;}); return best;
    }
    var a=e.args.map(function(x){return self.ev(x,env);});
    switch(f){
      case 'UPPER': case 'UCASE': return a[0]==null?null:String(a[0]).toUpperCase();
      case 'LOWER': case 'LCASE': return a[0]==null?null:String(a[0]).toLowerCase();
      case 'LENGTH': case 'CHAR_LENGTH': return a[0]==null?null:String(a[0]).length;
      case 'ROUND': return a[0]==null?null:(function(x,d){var m=Math.pow(10,d||0); return Math.round(num(x)*m)/m;})(a[0],a[1]);
      case 'ABS': return a[0]==null?null:Math.abs(num(a[0]));
      case 'COALESCE': case 'IFNULL': for(var i=0;i<a.length;i++)if(a[i]!=null)return a[i]; return null;
      case 'CONCAT': return a.some(function(x){return x==null;})?null:a.join('');
      case 'NOW': return '2026-11-20 10:00:00';
      case 'CURDATE': return '2026-11-20';
      case 'YEAR': return a[0]==null?null:parseInt(String(a[0]).slice(0,4),10);
      case 'MONTH': return a[0]==null?null:parseInt(String(a[0]).slice(5,7),10);
    }
    throw E(1305,'42000','FUNCTION '+f+' does not exist — 이 실습실이 모르는 함수입니다');
  }
};
return {DB:DB,show:show,split:split};
})();
if(typeof module!=='undefined')module.exports=MiniSQL;
