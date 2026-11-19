# 실전 연습장 (9~15주)
PRACTICE = {}

PRACTICE['09'] = dict(
title='제약 조건 설계 콘솔 — 내 CREATE TABLE로 40건 받아 보기', en='constraint design console',
scenario='<p>쇼핑몰 회원 표를 직접 설계합니다. 왼쪽의 <code>CREATE TABLE</code>을 고쳐 「검사 실행」을 누르면, 정상 가입 20건과 잘못된 가입 20건(아이디 중복·이름 없음·나이 음수·등급 오타·적립금 없음)이 <b>실습실 엔진에 실제로</b> 들어갑니다. 나쁜 데이터는 막고, 좋은 데이터는 통과시키는 것이 목표입니다.</p>',
html='''<div class="two"><div class="dpanel"><h4>내 회원 표 설계</h4><textarea class="dq" id="zp9sql" spellcheck="false">CREATE TABLE 회원 (
  아이디 VARCHAR(20),
  이름 VARCHAR(10),
  나이 INT,
  등급 VARCHAR(10),
  적립금 INT
);</textarea><div class="dctl"><button type="button" class="bt primary" id="zp9go">검사 실행</button><button type="button" class="bt" id="zp9hint">모범 설계 보기</button></div><p id="zp9msg" class="cvcap"></p></div>
<div class="dpanel"><h4>결과</h4><div class="dk-row" id="zp9k"></div></div></div>
<div class="dpanel"><h4>위반 종류별 — 막음 vs 통과해 버림</h4><canvas class="dch" id="zp9ch" role="img" aria-label="위반 종류별로 막은 건수와 통과한 건수 막대 그래프"></canvas></div>''',
tasks=['처음 설계(제약 없음) 그대로 실행해 “통과해 버린 나쁜 데이터” 수 확인하기','PRIMARY KEY, NOT NULL, CHECK, DEFAULT를 하나씩 더하며 막대가 어떻게 바뀌는지 보기','“정상인데 거부됨”이 0이면서 “나쁜데 통과”도 0인 설계를 만들기 (등급은 bronze·silver·gold·vip만)'],
js=r'''
var $=LAB.$;
var GOOD=[],BAD=[];(function(){var nm=['가람','나래','다솜','라온','마루','바다','사랑','아라','자람','하늘'];
 for(var i=0;i<20;i++)GOOD.push("INSERT INTO 회원 (아이디, 이름, 나이, 등급"+(i%3?", 적립금":"")+") VALUES ('u"+(100+i)+"', '"+nm[i%10]+"', "+(19+i)+", '"+['bronze','silver','gold','vip'][i%4]+"'"+(i%3?", "+(i*100):"")+")");
 var kinds=[['아이디 중복',function(i){return "INSERT INTO 회원 (아이디, 이름, 나이, 등급, 적립금) VALUES ('u10"+(i%5)+"', '중복', 30, 'gold', 0)";}],
  ['이름 없음',function(i){return "INSERT INTO 회원 (아이디, 이름, 나이, 등급, 적립금) VALUES ('n"+i+"', NULL, 30, 'gold', 0)";}],
  ['나이 음수',function(i){return "INSERT INTO 회원 (아이디, 이름, 나이, 등급, 적립금) VALUES ('a"+i+"', '음수', -"+(i+1)+", 'gold', 0)";}],
  ['등급 오타',function(i){return "INSERT INTO 회원 (아이디, 이름, 나이, 등급, 적립금) VALUES ('g"+i+"', '오타', 30, '"+['gld','VIPP','silvr','platinum'][i%4]+"', 0)";}],
  ['아이디 없음',function(i){return "INSERT INTO 회원 (아이디, 이름, 나이, 등급, 적립금) VALUES (NULL, '무명', 30, 'gold', 0)";}]];
 kinds.forEach(function(k){for(var i=0;i<4;i++)BAD.push([k[0],k[1](i)]);});})();
var KINDS=['아이디 중복','이름 없음','나이 음수','등급 오타','아이디 없음'];
function go(){var db=LAB.DB();try{db.run('CREATE DATABASE m; USE m;');db.run($('#zp9sql').value);}catch(e){$('#zp9msg').innerHTML='<span class="ng">설계 오류</span> '+e.message;return;}
 $('#zp9msg').textContent='';var gOK=0,gRej=[],blk={},pass={};KINDS.forEach(function(k){blk[k]=0;pass[k]=0;});
 GOOD.forEach(function(s){try{db.exec(s);gOK++;}catch(e){gRej.push(e.message);}});
 BAD.forEach(function(b){try{db.exec(b[1]);pass[b[0]]++;}catch(e){blk[b[0]]++;}});
 var slip=KINDS.reduce(function(a,k){return a+pass[k];},0);
 var dflt=LAB.sqlRows(db,"SELECT COUNT(*) FROM 회원 WHERE 적립금 IS NULL");dflt=dflt?+dflt.rows[0][0]:0;
 LAB.kpis($('#zp9k'),[['정상 통과',gOK+'/20','',gOK===20?'good':'bad'],['나쁜 데이터 막음',(20-slip)+'/20','',slip?'warn':'good'],['나쁜데 통과',slip+'건','',slip?'bad':'good'],['적립금 NULL',dflt+'명','DEFAULT 0이면 0',dflt?'warn':'good']]);
 if(gRej.length)$('#zp9msg').innerHTML='<span class="ng">정상 가입 '+gRej.length+'건이 거부됨</span> — 예: '+LAB.esc(gRej[0]);
 LAB.chart($('#zp9ch'),{labels:KINDS,series:[{name:'막음',data:KINDS.map(function(k){return blk[k];}),color:'#13733a'},{name:'통과해 버림',data:KINDS.map(function(k){return pass[k];}),color:'#c93030'}],ymax:4});}
$('#zp9go').onclick=go;
$('#zp9hint').onclick=function(){$('#zp9sql').value="CREATE TABLE 회원 (\n  아이디 VARCHAR(20) PRIMARY KEY,\n  이름 VARCHAR(10) NOT NULL,\n  나이 INT CHECK (나이 >= 0),\n  등급 VARCHAR(10) NOT NULL DEFAULT 'silver' CHECK (등급 IN ('bronze','silver','gold','vip')),\n  적립금 INT NOT NULL DEFAULT 0\n);";go();};
go();addEventListener('resize',go);
''')

PRACTICE['10'] = dict(
title='한빛 마트 매출 대시보드 — 질의를 만들면 그래프가 그려진다', en='sales dashboard query builder',
scenario='<p>한빛 마트의 주문 60건(1~6월)이 실습실 엔진에 들어 있습니다. 위의 선택지로 <b>묶을 기준·셀 값·조건</b>을 고르면 SQL이 만들어지고 실제로 실행되어 표와 막대그래프가 그려집니다. 만들어진 SQL을 직접 고쳐 실행할 수도 있습니다.</p>',
html='''<div class="dpanel dctl"><label>묶을 기준 <select id="zp10g"><option value="p.상품명">상품</option><option value="m.이름">회원</option><option value="p.제조업체">제조업체</option><option value="MONTH(o.주문일자)">월</option><option value="m.등급">회원 등급</option></select></label>
<label>값 <select id="zp10m"><option value="SUM(o.수량)">수량 합계</option><option value="SUM(o.수량 * p.단가)">매출액 합계</option><option value="COUNT(*)">주문 건수</option><option value="ROUND(AVG(o.수량), 1)">평균 수량</option></select></label>
<label>기간 <select id="zp10w"><option value="">전체</option><option value="WHERE MONTH(o.주문일자) BETWEEN 1 AND 3">1~3월</option><option value="WHERE MONTH(o.주문일자) BETWEEN 4 AND 6">4~6월</option></select></label>
<label>HAVING ≥ <input type="number" id="zp10h" value="0" min="0" style="width:90px"></label><button type="button" class="bt primary" id="zp10b">질의 만들기·실행</button></div>
<div class="two"><div class="dpanel"><h4>SQL (고쳐서 실행 가능)</h4><textarea class="dq" id="zp10q" spellcheck="false"></textarea><div class="dctl"><button type="button" class="bt" id="zp10run">이 SQL 실행</button></div><p id="zp10e" class="cvcap"></p></div><div class="dpanel"><h4>결과 표</h4><div id="zp10t" style="max-height:260px;overflow:auto"></div></div></div>
<div class="dk-row" id="zp10k"></div><div class="dpanel"><h4>결과 그래프</h4><canvas class="dch" id="zp10ch" role="img" aria-label="질의 결과 막대 그래프"></canvas></div>''',
tasks=['“제조업체별 매출액 합계”를 만들고 1위 제조업체 찾기','월별 주문 건수를 보고 가장 바쁜 달을 말하기 — 그다음 SQL에서 ORDER BY를 지우면 표가 어떻게 바뀌는지 보기','HAVING을 써서 “수량 합계 100 이상인 상품”만 남기고, 같은 조건을 WHERE에 쓰면 왜 오류가 나는지 직접 고쳐 실행해 확인하기'],
labs='',
js=r'''
var $=LAB.$,db=LAB.DB();
(function(){var R=LAB.rng(1010),mem=[['apple','정소화','gold'],['banana','김선우','vip'],['carrot','고명석','gold'],['orange','김용욱','silver'],['melon','성원용','gold'],['peach','오형준','silver']],
 prd=[['p01','그냥만두',4500,'대한식품'],['p02','매운쫄면',5500,'민국푸드'],['p03','쿵떡파이',2600,'한빛제과'],['p04','맛난초콜릿',2500,'한빛제과'],['p05','얼큰라면',1200,'대한식품'],['p06','통통우동',1500,'민국푸드']];
 var s="CREATE DATABASE hb; USE hb; CREATE TABLE 회원 (회원아이디 VARCHAR(20) PRIMARY KEY, 이름 VARCHAR(10), 등급 VARCHAR(10)); CREATE TABLE 상품 (상품번호 CHAR(3) PRIMARY KEY, 상품명 VARCHAR(20), 단가 INT, 제조업체 VARCHAR(20)); CREATE TABLE 주문 (주문번호 CHAR(4) PRIMARY KEY, 회원아이디 VARCHAR(20), 상품번호 CHAR(3), 수량 INT, 주문일자 DATE, FOREIGN KEY (회원아이디) REFERENCES 회원(회원아이디), FOREIGN KEY (상품번호) REFERENCES 상품(상품번호));";
 s+="INSERT INTO 회원 VALUES "+mem.map(function(m){return "('"+m.join("','")+"')";}).join(',')+";";
 s+="INSERT INTO 상품 VALUES "+prd.map(function(p){return "('"+p[0]+"','"+p[1]+"',"+p[2]+",'"+p[3]+"')";}).join(',')+";";
 var o=[];for(var i=1;i<=60;i++){var mo=1+Math.floor(R()*6),d=1+Math.floor(R()*28);o.push("('o"+(i<10?'0':'')+i+"','"+mem[Math.floor(R()*6)][0]+"','"+prd[Math.floor(R()*R()*6)][0]+"',"+(1+Math.floor(R()*20))+",'2022-0"+mo+"-"+(d<10?'0':'')+d+"')");}
 s+="INSERT INTO 주문 VALUES "+o.join(',')+";";db.run(s);})();
function build(){var g=$('#zp10g').value,m=$('#zp10m').value,w=$('#zp10w').value,h=+$('#zp10h').value;
 return 'SELECT '+g+' AS 기준, '+m+' AS 값\nFROM 주문 o\nJOIN 회원 m ON o.회원아이디 = m.회원아이디\nJOIN 상품 p ON o.상품번호 = p.상품번호\n'+(w?w+'\n':'')+'GROUP BY '+g+'\n'+(h>0?'HAVING '+m+' >= '+h+'\n':'')+'ORDER BY 값 DESC;';}
function run(){var q=$('#zp10q').value,r;$('#zp10e').textContent='';
 try{r=LAB.sqlRows(db,q);}catch(e){$('#zp10e').innerHTML='<span class="ng">오류</span> '+LAB.esc(e.message);return;}
 if(!r){$('#zp10e').textContent='SELECT 결과가 없습니다.';return;}
 $('#zp10t').innerHTML=LAB.tableHTML(r.cols,r.rows.map(function(x){return x.map(function(v){return v==null?'NULL':MiniSQL.show(v);});}));
 var vals=r.rows.map(function(x){return +x[x.length-1]||0;}),tot=vals.reduce(function(a,b){return a+b;},0);
 LAB.kpis($('#zp10k'),[['결과 행',r.rows.length+'행'],['값 합계',Math.round(tot).toLocaleString()],['1위',r.rows.length?MiniSQL.show(r.rows[0][0]):'—','',''],['1위 비중',tot?Math.round(vals[0]/tot*100)+'%':'—']]);
 LAB.chart($('#zp10ch'),{labels:r.rows.map(function(x){return MiniSQL.show(x[0]);}),series:[{name:r.cols[r.cols.length-1],data:vals}]});}
$('#zp10b').onclick=function(){$('#zp10q').value=build();run();};$('#zp10run').onclick=run;
$('#zp10q').value=build();run();addEventListener('resize',run);
''')

PRACTICE['11'] = dict(
title='카페 주문 시스템 — 요구 사항에서 테이블까지 자동 변환기', en='cafe ordering design converter',
scenario='<p>새 사례입니다. 동네 카페 체인 “콩다방”의 요구 사항 8문장을 읽고, 관계의 대응 수와 다중값 속성 처리를 고르세요. 대시보드가 <b>변환 규칙 1~5</b>로 릴레이션 스키마와 <code>CREATE TABLE</code>을 만들고, 실습실 엔진에서 실제로 실행한 뒤 예시 데이터로 <b>요구 사항 검증 질의 4개</b>를 돌립니다.</p>',
html='''<div class="dpanel"><h4>요구 사항</h4><ol style="font-size:14px;padding-left:20px;margin:0">
<li>회원은 회원번호로 식별하고 이름·전화번호를 가진다.</li><li>매장은 매장번호로 식별하고 매장명·주소를 가진다.</li><li>메뉴는 메뉴번호로 식별하고 메뉴명·가격을 가진다.</li>
<li>회원은 여러 번 주문할 수 있고, 주문 하나는 한 회원이 한다. 주문은 주문번호·주문일시를 가진다.</li><li>주문 하나에 여러 메뉴를 담을 수 있고, 메뉴는 여러 주문에 담긴다. 담을 때 수량을 기록한다.</li>
<li>주문은 한 매장에서 이루어지고, 매장 하나는 여러 주문을 받는다.</li><li>매장마다 점장은 한 명이고, 점장은 직원 중 한 명이며 한 매장만 맡는다(모든 매장에 점장이 있다).</li><li>메뉴에는 알레르기 성분이 여러 개 있을 수 있다(우유, 땅콩 …).</li></ol></div>
<div class="dpanel" id="zp11sel"></div><div class="dk-row" id="zp11k"></div>
<div class="two"><div class="dpanel"><h4>만들어진 SQL (실행됨)</h4><pre id="zp11sql" style="font-size:12.5px;white-space:pre-wrap;max-height:300px;overflow:auto;margin:0"></pre></div><div class="dpanel"><h4>요구 사항 검증</h4><div id="zp11chk" style="font-size:14px"></div></div></div>''',
tasks=['일부러 “주문–메뉴”를 1:N으로 두고 검증 ②(한 주문에 메뉴 여러 개)가 깨지는 것 보기','알레르기 성분을 “한 칸에 쉼표로”로 두면 검증 ④가 왜 어려워지는지 설명하기','모든 선택을 맞혀 검증 4/4 통과, 테이블 수가 몇 개인지 손으로 먼저 계산하고 확인하기 (개체 + N:M + 다중값)'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var Q=[['회원–주문','1n',['1n','nm'],'요구 4'],['주문–메뉴','nm',['1n','nm'],'요구 5'],['매장–주문','1n',['1n','nm'],'요구 6'],['매장–점장(직원)','11',['11','1n'],'요구 7'],['알레르기 성분','sep',['sep','csv'],'요구 8']];
var pick={0:'1n',1:'1n',2:'1n',3:'1n',4:'csv'};
var LB={'1n':'1:N','nm':'N:M','11':'1:1','sep':'별도 릴레이션','csv':'한 칸에 쉼표로'};
$('#zp11sel').innerHTML='<h4>설계 선택</h4>'+Q.map(function(q,i){return '<div class="dctl" style="margin:4px 0"><b style="min-width:150px">'+q[0]+'</b>'+q[2].map(function(c){return '<button type="button" class="bt" data-i="'+i+'" data-c="'+c+'">'+LB[c]+'</button>';}).join('')+'<small style="color:#5b6874">'+q[3]+'</small></div>';}).join('');
function gen(){var s=[],t=['회원','매장','메뉴'];
 s.push("CREATE TABLE 회원 (회원번호 INT PRIMARY KEY, 이름 VARCHAR(10), 전화번호 VARCHAR(20));");
 s.push("CREATE TABLE 직원 (직원번호 INT PRIMARY KEY, 이름 VARCHAR(10));");
 s.push("CREATE TABLE 매장 (매장번호 INT PRIMARY KEY, 매장명 VARCHAR(20), 주소 VARCHAR(40)"+(pick[3]==='11'?", 점장번호 INT NOT NULL UNIQUE, FOREIGN KEY (점장번호) REFERENCES 직원(직원번호)":"")+");");
 if(pick[3]==='1n')s.push("ALTER TABLE 직원 ADD 매장번호 INT;");
 s.push("CREATE TABLE 메뉴 (메뉴번호 INT PRIMARY KEY, 메뉴명 VARCHAR(20), 가격 INT"+(pick[4]==='csv'?", 알레르기 VARCHAR(50)":"")+");");
 if(pick[4]==='sep')s.push("CREATE TABLE 메뉴알레르기 (메뉴번호 INT, 성분 VARCHAR(10), PRIMARY KEY (메뉴번호, 성분), FOREIGN KEY (메뉴번호) REFERENCES 메뉴(메뉴번호));");
 var oc="CREATE TABLE 주문 (주문번호 INT PRIMARY KEY, 주문일시 DATE";
 if(pick[0]==='1n')oc+=", 회원번호 INT NOT NULL";if(pick[2]==='1n')oc+=", 매장번호 INT NOT NULL";if(pick[1]==='1n')oc+=", 메뉴번호 INT, 수량 INT";
 if(pick[0]==='1n')oc+=", FOREIGN KEY (회원번호) REFERENCES 회원(회원번호)";if(pick[2]==='1n')oc+=", FOREIGN KEY (매장번호) REFERENCES 매장(매장번호)";
 s.push(oc+");");
 if(pick[0]==='nm')s.push("CREATE TABLE 회원주문 (회원번호 INT, 주문번호 INT, PRIMARY KEY (회원번호, 주문번호));");
 if(pick[2]==='nm')s.push("CREATE TABLE 매장주문 (매장번호 INT, 주문번호 INT, PRIMARY KEY (매장번호, 주문번호));");
 if(pick[1]==='nm')s.push("CREATE TABLE 주문상세 (주문번호 INT, 메뉴번호 INT, 수량 INT, PRIMARY KEY (주문번호, 메뉴번호), FOREIGN KEY (주문번호) REFERENCES 주문(주문번호), FOREIGN KEY (메뉴번호) REFERENCES 메뉴(메뉴번호));");
 return s;}
function data(){var d=["INSERT INTO 회원 VALUES (1,'정소화','010-1'),(2,'김선우','010-2');","INSERT INTO 직원 (직원번호, 이름) VALUES (10,'박점장'),(11,'이점장'),(12,'최바리');","INSERT INTO 매장"+(pick[3]==='11'?" VALUES (1,'강남점','서울',10),(2,'수원점','경기',11);":" (매장번호, 매장명, 주소) VALUES (1,'강남점','서울'),(2,'수원점','경기');")];
 if(pick[3]==='1n')d.push("UPDATE 직원 SET 매장번호 = 1 WHERE 직원번호 IN (10, 12);","UPDATE 직원 SET 매장번호 = 2 WHERE 직원번호 = 11;");
 d.push("INSERT INTO 메뉴"+(pick[4]==='csv'?" VALUES (1,'라테',4500,'우유'),(2,'땅콩쿠키',2500,'땅콩, 밀, 우유'),(3,'아메리카노',3500,NULL);":" VALUES (1,'라테',4500),(2,'땅콩쿠키',2500),(3,'아메리카노',3500);"));
 if(pick[4]==='sep')d.push("INSERT INTO 메뉴알레르기 VALUES (1,'우유'),(2,'땅콩'),(2,'밀'),(2,'우유');");
 var cols=['주문번호','주문일시'];if(pick[0]==='1n')cols.push('회원번호');if(pick[2]==='1n')cols.push('매장번호');
 var rows=[[100,"'2022-03-01'",1,1],[101,"'2022-03-02'",2,2]];
 if(pick[1]==='1n'){cols.push('메뉴번호','수량');}
 d.push("INSERT INTO 주문 ("+cols.join(', ')+") VALUES "+rows.map(function(r){var v=[r[0],r[1]];if(pick[0]==='1n')v.push(r[2]);if(pick[2]==='1n')v.push(r[3]);if(pick[1]==='1n')v.push(1,2);return '('+v.join(', ')+')';}).join(', ')+";");
 if(pick[0]==='nm')d.push("INSERT INTO 회원주문 VALUES (1,100),(2,101);");if(pick[2]==='nm')d.push("INSERT INTO 매장주문 VALUES (1,100),(2,101);");
 if(pick[1]==='nm')d.push("INSERT INTO 주문상세 VALUES (100,1,2),(100,2,1),(101,3,1);");return d;}
function check(db){var C=[],t=function(name,f){try{C.push([name,f()]);}catch(e){C.push([name,false,e.message]);}};
 t('① 주문마다 회원이 정확히 한 명',function(){return pick[0]==='1n';});
 t('② 주문 100에 라테 2잔 + 땅콩쿠키 1개 담기',function(){if(pick[1]!=='nm'){db.exec("INSERT INTO 주문 (주문번호, 주문일시"+(pick[0]==='1n'?", 회원번호":"")+(pick[2]==='1n'?", 매장번호":"")+", 메뉴번호, 수량) VALUES (100,'2022-03-01'"+(pick[0]==='1n'?",1":"")+(pick[2]==='1n'?",1":"")+",2,1)");}var r=LAB.sqlRows(db,"SELECT COUNT(*) FROM 주문상세 WHERE 주문번호 = 100");return r&&+r.rows[0][0]===2;});
 t('③ 매장마다 점장 한 명, 점장 없는 매장 없음',function(){if(pick[3]!=='11')return false;var r=LAB.sqlRows(db,"SELECT COUNT(*) FROM 매장 WHERE 점장번호 IS NULL");return +r.rows[0][0]===0;});
 t('④ “우유가 든 메뉴” 정확히 찾기',function(){var r=pick[4]==='sep'?LAB.sqlRows(db,"SELECT COUNT(*) FROM 메뉴알레르기 WHERE 성분 = '우유'"):LAB.sqlRows(db,"SELECT COUNT(*) FROM 메뉴 WHERE 알레르기 = '우유'");return +r.rows[0][0]===2;});
 return C;}
function run(){var s=gen(),db=LAB.DB(),err='';db.run('CREATE DATABASE cafe; USE cafe;');
 s.forEach(function(x){try{db.exec(x);}catch(e){err=e.message;}});data().forEach(function(x){try{db.exec(x);}catch(e){err=err||e.message;}});
 var C=check(db),pass=C.filter(function(c){return c[1];}).length,tables=LAB.sqlRows(db,'SHOW TABLES').rows.length,fks=(s.join(' ').match(/FOREIGN KEY/g)||[]).length;
 $('#zp11sql').textContent=s.join('\n')+(err?'\n-- 오류: '+err:'');
 $('#zp11chk').innerHTML=C.map(function(c){return (c[1]?'<span class="ok">통과</span> ':'<span class="ng">실패</span> ')+c[0]+(c[2]?' <small>('+LAB.esc(c[2])+')</small>':'');}).join('<br>');
 LAB.kpis($('#zp11k'),[['검증 통과',pass+'/4','',pass===4?'good':'bad'],['테이블',tables+'개'],['외래키',fks+'개'],['선택 정답',Q.filter(function(q,i){return pick[i]===q[1];}).length+'/5']]);}
$$('#zp11sel [data-i]').forEach(function(b){b.onclick=function(){pick[b.dataset.i]=b.dataset.c;$$('#zp11sel [data-i="'+b.dataset.i+'"]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});run();};});
Object.keys(pick).forEach(function(i){$$('#zp11sel [data-i="'+i+'"][data-c="'+pick[i]+'"]')[0].setAttribute('aria-pressed','true');});run();
''')

PRACTICE['12'] = dict(
title='쇼핑몰 통합 표 정규화 진단기', en='normalization diagnosis dashboard',
scenario='<p>노션 “worst case”처럼 주문·회원·상품·판매자를 한 표에 담은 쇼핑몰 표(예시 데이터 24줄, 칸 12개로 줄인 예)를 정규화합니다. 분리할 표를 켜고 끄면 대시보드가 <b>중복 저장된 값</b>, <b>세 가지 사건</b>(판매자 전화번호 변경, 아직 안 팔린 신상품 등록, 어떤 회원의 유일한 주문 삭제)의 비용, 조회 때 필요한 조인 수를 계산합니다.</p>',
html='''<div class="dpanel dctl" id="zp12sw"></div><div class="dk-row" id="zp12k"></div>
<div class="two"><div class="dpanel"><h4>지금 설계의 표</h4><div id="zp12tb" style="font-size:14px"></div></div><div class="dpanel"><h4>사건별 비용 (건드리는 행 · 불가능 = 막대 끝까지)</h4><canvas class="dch" id="zp12ch" role="img" aria-label="세 사건별로 건드리는 행 수 막대 그래프"></canvas></div></div>
<div class="dpanel dctl"><label>읽기 비율 <input type="range" id="zp12r" min="0" max="100" value="80"><b id="zp12rv"></b></label><span id="zp12mix" class="cvcap"></span></div>''',
tasks=['아무것도 분리하지 않은 상태에서 세 사건의 비용을 읽고, 각각 어떤 이상 현상인지 이름 붙이기','회원·상품·판매자를 차례로 분리하며 중복 값이 몇 개 줄어드는지 기록하기','읽기 비율을 95%와 30%로 바꿔, 12주 대결처럼 “어디까지 쪼갤지”가 접근 패턴에 따라 달라지는지 확인하기'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var R=LAB.rng(1212),MEM=8,PRD=6,SEL=3,ROWS=[];for(var i=0;i<24;i++)ROWS.push({m:Math.floor(R()*MEM),p:Math.floor(R()*PRD)});ROWS[23].m=7;ROWS.forEach(function(r,i){if(i<23&&r.m===7)r.m=6;});
var sellerOf=function(p){return p%SEL;};
var SW=[['mem','회원 표 분리','회원ID → 이름·전화·등급'],['prd','상품 표 분리','상품ID → 상품명·가격·판매자ID'],['sel','판매자 표 분리','판매자ID → 상호·전화'],['det','주문 상세 분리','주문번호 → 주문일·배송지']];
var on={mem:false,prd:false,sel:false,det:false};
$('#zp12sw').innerHTML='<b style="margin-right:6px">분리할 표:</b>'+SW.map(function(s){return '<label title="'+s[2]+'"><input type="checkbox" data-s="'+s[0]+'"> '+s[1]+'</label>';}).join('');
function calc(){var n=ROWS.length,dup=0;
 var memCols=3,prdCols=3,selCols=2;
 dup+=on.mem?0:(n-new Set(ROWS.map(function(r){return r.m;})).size)*memCols;
 dup+=on.prd?0:(n-new Set(ROWS.map(function(r){return r.p;})).size)*prdCols;
 var selRows=on.sel?0:(on.prd?PRD:n);dup+=on.sel?0:(selRows-SEL)*selCols;
 var s0=0;ROWS.forEach(function(r){if(sellerOf(r.p)===0)s0++;});
 var e1=on.sel?1:(on.prd?PRD/SEL:s0),e2=on.prd?1:999,e3=on.mem?1:999;
 var tables=1+(on.mem?1:0)+(on.prd?1:0)+(on.sel?1:0)+(on.det?1:0),joins=tables-1;
 LAB.kpis($('#zp12k'),[['표 개수',tables+'개'],['중복 저장된 값',dup+'개','',dup?'warn':'good'],['주문 조회 조인',joins+'번'],['이상 현상 남음',[e1>1,e2===999,e3===999].filter(Boolean).length+'/3','',(e1>1||e2===999||e3===999)?'bad':'good']]);
 var t=['주문(주문번호'+(on.det?'':', 주문일, 배송지')+', '+(on.mem?'회원ID(FK)':'회원ID, 이름, 전화, 등급')+', '+(on.prd?'상품ID(FK)':'상품ID, 상품명, 가격, '+(on.sel?'판매자ID(FK)':'판매자ID, 상호, 판매자전화'))+', 수량)'];
 if(on.det)t.push('주문정보(주문번호, 주문일, 배송지)');if(on.mem)t.push('회원(회원ID, 이름, 전화, 등급)');if(on.prd)t.push('상품(상품ID, 상품명, 가격, '+(on.sel?'판매자ID(FK)':'판매자ID, 상호, 판매자전화')+')');if(on.sel)t.push('판매자(판매자ID, 상호, 전화)');
 $('#zp12tb').innerHTML=t.map(function(x){return '<code>'+x+'</code>';}).join('<br>');
 var cap=30;LAB.chart($('#zp12ch'),{labels:['판매자 전화 변경(갱신)','신상품 등록(삽입)','유일한 주문 삭제(삭제)'],series:[{name:'건드리는 행',data:[e1,Math.min(e2,cap),Math.min(e3,cap)],color:'#c93030'}],ymax:cap});
 var rd=+$('#zp12r').value/100;$('#zp12rv').textContent=Math.round(rd*100)+'%';
 var cost=Math.round(1000*(rd*(1+joins*0.6)+(1-rd)*(e1+dup/10)));$('#zp12mix').textContent='작업 1,000번 기준 예상 비용(설명용 모형): '+cost.toLocaleString()+' — 조인은 읽을 때, 중복은 고칠 때 비용이 됩니다.';}
$$('#zp12sw [data-s]').forEach(function(b){b.onchange=function(){on[b.dataset.s]=b.checked;calc();};});$('#zp12r').oninput=calc;calc();addEventListener('resize',calc);
''')

PRACTICE['13'] = dict(
title='게임 거래소 동시 처리 시뮬레이터', en='game marketplace concurrency simulator',
scenario='<p>RPG 「용사의 전설」 거래소입니다. 플레이어들이 동시에 골드로 아이템을 사고팝니다. <b>잠금 방식</b>, 동시 접속, 서버 장애를 바꿔 가며 60초를 돌려 보세요. 사라진 골드(갱신 분실), 복사된 아이템, 기다림, 교착 상태, 장애 뒤 REDO·UNDO 건수가 계기판에 나옵니다. 사례의 “거래/교환 시 데이터 일관성 유지”가 무엇을 막는지 숫자로 확인하는 연습입니다.</p>',
html='''<div class="dpanel dctl"><label>잠금 방식 <select id="zp13m"><option value="none">잠금 없음</option><option value="2pl" selected>2단계 로킹 (아무 순서)</option><option value="ord">2단계 로킹 + 계좌 번호 순서로 잠금</option></select></label>
<label>초당 거래 <input type="range" id="zp13t" min="2" max="40" value="16"><b id="zp13tv"></b></label><label>플레이어 수 <input type="range" id="zp13p" min="4" max="60" value="12"><b id="zp13pv"></b></label>
<label>서버 장애 <select id="zp13c"><option value="0">없음</option><option value="42" selected>42초에 1번</option></select></label><button type="button" class="bt primary" id="zp13go">60초 돌리기</button></div>
<div class="dk-row" id="zp13k"></div><div class="two"><div class="dpanel"><h4>초당 완료 거래 / 문제 건수</h4><canvas class="dch" id="zp13ch" role="img" aria-label="초당 완료 거래와 문제 건수 선 그래프"></canvas></div><div class="dpanel"><h4>장애 직후 회복 판정 (로그 기준)</h4><div id="zp13rec" style="font-size:14px"></div></div></div>''',
tasks=['“잠금 없음”으로 돌려 사라진 골드와 복사된 아이템을 기록하기 — 정상이라면 둘 다 0','2단계 로킹으로 바꾸면 문제는 0이 되지만 무엇이 생기는지(기다림·교착) 확인하기','“계좌 번호 순서로 잠금”을 고르면 교착 상태가 왜 0이 되는지 13주 4칸의 교착 예와 연결해 설명하기','장애를 켜고, REDO·UNDO 건수와 “회복 후 골드 총량이 맞는가”를 확인하기'],
js=r'''
var $=LAB.$;
function sim(){var mode=$('#zp13m').value,tps=+$('#zp13t').value,P=+$('#zp13p').value,crash=+$('#zp13c').value;$('#zp13tv').textContent=tps+'건';$('#zp13pv').textContent=P+'명';
 var R=LAB.rng(1313),done=[],prob=[],labs=[],lost=0,dup=0,waits=0,dead=0,ok=0,redo=0,undo=0,inflight=0;
 var conflictP=Math.min(0.95,tps/(P*2.2));
 for(var s=1;s<=60;s++){var d=0,pb=0;labs.push(s+'초');
  for(var k=0;k<tps;k++){var conflict=R()<conflictP;
   if(s===crash&&k>=tps-3){inflight++;continue;}
   if(mode==='none'){if(conflict){if(R()<0.5){lost++;}else{dup++;}pb++;}d++;}
   else{if(conflict){waits++;if(mode==='2pl'&&R()<0.18){dead++;pb++;continue;}}d++;}}
  if(s===crash){redo=Math.round(tps*0.6);undo=inflight;}
  ok+=d;done.push(d);prob.push(pb);}
 var tot=P*1000,afterGold=mode==='none'?tot-lost*120+dup*0:tot;
 LAB.kpis($('#zp13k'),[['완료 거래',ok.toLocaleString()+'건'],['사라진 골드(갱신 분실)',lost+'번','',lost?'bad':'good'],['복사된 아이템',dup+'개','',dup?'bad':'good'],['기다림',waits+'번','잠금 대기',waits?'warn':''],['교착 상태',dead+'번',mode==='2pl'?'한쪽 철회 후 재시도':'',dead?'warn':'good'],['골드 총량',afterGold.toLocaleString(),'시작 '+tot.toLocaleString(),afterGold===tot?'good':'bad']]);
 LAB.chart($('#zp13ch'),{type:'line',labels:labs,series:[{name:'완료',data:done,color:'#1e55c8'},{name:'문제',data:prob,color:'#c93030'}]});
 $('#zp13rec').innerHTML=crash?('<p>'+crash+'초에 장애. 검사 시점은 '+(crash-5)+'초.</p><ul><li>검사 시점 이전에 커밋된 거래: <b>처리 없음</b></li><li>검사 시점 이후 커밋된 거래 약 <b>'+redo+'건 → REDO</b></li><li>장애 순간 진행 중(커밋 없음) <b>'+undo+'건 → UNDO</b> — 판매자 골드 차감과 구매자 아이템 지급이 함께 취소</li></ul><p>'+(mode==='none'?'<span class="ng">잠금이 없어 회복 전에 이미 값이 덮여 있었습니다. 회복은 “커밋된 대로” 되돌릴 뿐, 갱신 분실까지 고치지는 못합니다.</span>':'<span class="ok">회복 후 골드 총량이 시작과 같습니다.</span>')+'</p>'):'<p>장애 없음 — 회복 작업 없음.</p>';}
$('#zp13go').onclick=sim;['#zp13m','#zp13t','#zp13p','#zp13c'].forEach(function(id){$(id).addEventListener('input',sim);});sim();addEventListener('resize',sim);
''')

PRACTICE['14'] = dict(
title='SNS 저장 방식 선택 시뮬레이터', en='sns storage choice simulator',
scenario='<p>여러분은 새 SNS 서비스의 데이터베이스 설계자입니다. 사용자 수, 하루 글 수, 읽기:쓰기 비율, 태그 이름 변경 빈도, 결제 기능 유무를 정하면 <b>관계형(3NF)</b>, <b>관계형 + 색인</b>, <b>문서형</b>, <b>혼합(결제·회원은 관계형, 피드는 문서형)</b> 네 안의 하루 작업량과 위험을 비교합니다. RPG 사례의 “캐릭터–장비는 정규화, 전투 로그는 비정규화”, “전투 실시간 데이터는 NoSQL 병행 검토”를 직접 따져 보는 연습입니다.</p>',
html='''<div class="dpanel dctl"><label>사용자 <input type="range" id="zp14u" min="1" max="100" value="20"><b id="zp14uv"></b></label><label>1인 하루 글 <input type="range" id="zp14w" min="1" max="10" value="2"><b id="zp14wv"></b></label><label>읽기:쓰기 <input type="range" id="zp14r" min="1" max="200" value="50"><b id="zp14rv"></b></label><label>월 태그 이름 변경 <input type="range" id="zp14t" min="0" max="50" value="3"><b id="zp14tv"></b></label><label><input type="checkbox" id="zp14pay" checked> 결제 기능</label></div>
<div class="dk-row" id="zp14k"></div><div class="dpanel"><h4>하루 작업량 (읽은 행·문서 + 고친 행, 설명용 모형)</h4><canvas class="dch" id="zp14ch" role="img" aria-label="네 저장 방식의 하루 작업량 막대 그래프"></canvas><p class="cvcap" id="zp14n"></p></div>''',
tasks=['기본값에서 가장 작업량이 적은 안과, 결제 기능 때문에 남는 위험을 읽기','태그 이름 변경을 50으로 올리면 문서형의 작업량이 어떻게 변하는지 보기 (12주 갱신 이상)','읽기:쓰기를 1로 낮추고 다시 비교 — 어떤 안이 앞서는지, 이유를 한 문장으로'],
js=r'''
var $=LAB.$;
function f(){var U=+$('#zp14u').value*10000,w=+$('#zp14w').value,rw=+$('#zp14r').value,tr=+$('#zp14t').value,pay=$('#zp14pay').checked;
 $('#zp14uv').textContent=(U/10000)+'만 명';$('#zp14wv').textContent=w+'개';$('#zp14rv').textContent=rw+' : 1';$('#zp14tv').textContent=tr+'번';
 var writes=U*w,reads=writes*rw,tags=3,postsPerTag=writes*30/50;
 var rel=reads*(1+2*tags)*1.0+writes*(1+tags)+tr/30*1, idx=reads*(1+2*tags)*0.35+writes*(1+tags)*1.3+tr/30, doc=reads*1+writes*1+tr/30*postsPerTag, hyb=reads*1+writes*1.1+tr/30*postsPerTag*0.2;
 var V=[rel,idx,doc,hyb].map(Math.round),names=['관계형(3NF)','관계형+색인','문서형','혼합'],best=V.indexOf(Math.min.apply(null,V));
 LAB.kpis($('#zp14k'),[['하루 글',writes.toLocaleString()+'건'],['하루 읽기',reads.toLocaleString()+'회'],['작업량 최소',names[best],'',''],['결제 트랜잭션 위험',pay?(best===2?'높음':'낮음'):'해당 없음',pay&&best===2?'문서형만 쓰면 다중 문서 트랜잭션 설계 필요':'',pay&&best===2?'bad':'good']]);
 LAB.chart($('#zp14ch'),{labels:names,series:[{name:'하루 작업량',data:V}]});
 $('#zp14n').textContent='글 하나에 태그 3개, 색인은 조회를 약 1/3로 줄이고 쓰기를 30% 늘린다고 가정한 설명용 모형입니다. 실제 성능은 캐시·하드웨어·질의에 따라 달라집니다.';}
['#zp14u','#zp14w','#zp14r','#zp14t','#zp14pay'].forEach(function(id){$(id).addEventListener('input',f);});f();addEventListener('resize',f);
''')

PRACTICE['15'] = dict(
title='기말 대비 종합 계기판', en='final exam readiness dashboard',
scenario='<p>이 페이지에서 푼 것이 모두 모입니다: 모의 20문항의 <b>주차별 정답률</b>(9~14주)과 위 ⑤칸 <b>SQL 자동 채점 과제</b> 점수. 둘을 합쳐 준비도를 보여 주고, 다시 볼 페이지를 골라 줍니다. 아직 풀지 않았다면 「예시 학생으로 보기」를 누르세요.</p>',
html='''<div class="dpanel dctl"><button type="button" class="bt primary" id="zp15r">내 결과 불러오기</button><button type="button" class="bt" id="zp15d">예시 학생으로 보기</button><span id="zp15s" class="cvcap"></span></div>
<div class="dk-row" id="zp15k"></div><div class="two"><div class="dpanel"><h4>주차별 정답률 (%)</h4><canvas class="dch" id="zp15ch" role="img" aria-label="9~14주차 정답률 막대 그래프"></canvas></div><div class="dpanel"><h4>다시 볼 곳</h4><div id="zp15go" style="font-size:15px"></div></div></div>''',
tasks=['모의 20문항과 ⑤칸 SQL 과제 8개를 먼저 풀기','「내 결과 불러오기」로 준비도 확인 — 70% 미만인 주차 페이지를 열기','SQL 과제에서 틀린 문항은 10주 실습실의 같은 유형 버튼을 다시 눌러 보기'],
js=r'''
var $=LAB.$;
var FILE={9:'w09_sql_ddl.html',10:'w10_sql_dml.html',11:'w11_database_design_process.html',12:'w12_normalization.html',13:'w13_transaction_recovery_concurrency.html',14:'w14_database_applications.html'};
function wk(q){var m=(q.why||'').match(/\((\d+)(?:·\d+)?주차\)/);return m?+m[1]:0;}
function draw(demo){var qs=(window.QUIZ&&QUIZ.mock)||[],R=LAB.rng(1515),by={},n=0;
 qs.forEach(function(q,i){var w=wk(q);if(w<9)return;var st=window.QSTAT&&QSTAT.by&&QSTAT.by['mock:'+i];var a=demo?(R()<{9:.85,10:.7,11:.8,12:.5,13:.65,14:.75}[w]):(st?st.ok:null);if(a===null)return;n++;by[w]=by[w]||[0,0];by[w][1]++;if(a)by[w][0]++;});
 var sql=window.SQLGRADE||{ok:0,total:8};if(demo)sql={ok:5,total:8};
 var labs=[],data=[],weak=[];for(var w=9;w<=14;w++){labs.push(w+'주');var b=by[w],p=b?Math.round(b[0]/b[1]*100):0;data.push(p);if(b&&p<70)weak.push(w);}
 var quizP=n?Math.round(data.reduce(function(a,b){return a+b;},0)/6):0,sqlP=Math.round(sql.ok/sql.total*100),ready=n?Math.round(quizP*0.6+sqlP*0.4):sqlP;
 $('#zp15s').textContent=demo?'예시 학생(가상) 결과':(n?'모의 '+n+'문항 + SQL 과제 기준':'아직 푼 모의 문항이 없습니다');
 LAB.kpis($('#zp15k'),[['모의 문항',n+'/20'],['개념 정답률',n?quizP+'%':'—'],['SQL 과제',sql.ok+'/'+sql.total,'',sqlP>=75?'good':'warn'],['준비도',n?ready+'%':'—',n?'개념 60% + SQL 40%':'모의 문항을 풀면 계산',n?(ready>=75?'good':(ready>=50?'warn':'bad')):'']]);
 LAB.chart($('#zp15ch'),{labels:labs,series:[{name:'정답률',data:data}],ymax:100,yfmt:function(v){return Math.round(v)+'%';}});
 $('#zp15go').innerHTML=weak.length?weak.map(function(w){return '<a href="'+FILE[w]+'">'+w+'주차 페이지</a> — 칸 퀴즈와 대결 판정 이유 다시 보기';}).join('<br>'):(n?'<span class="ok">모든 주차 70% 이상</span> — SQL 과제 만점에 도전하세요.':'');}
$('#zp15r').onclick=function(){draw(false);};$('#zp15d').onclick=function(){draw(true);};draw(true);addEventListener('resize',function(){draw(true);});
''')
