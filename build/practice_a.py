# 실전 연습장 (1~8주) — 회차 마지막의 동작 대시보드
PRACTICE = {}

PRACTICE['01'] = dict(
title='편의점 하루 데이터 흐름 계기판', en='convenience store data flow dashboard',
scenario='<p>여러분은 동네 편의점 점장입니다. 손님이 계산대에서 바코드를 한 번 찍을 때마다 <b>판매·재고·포인트</b> 세 곳에 기록이 남습니다. 손님 수, 한 사람이 사는 물건 수, 포인트 회원 비율을 바꾸며 하루 동안 데이터가 얼마나 쌓이는지 보세요.</p>',
html='''<div class="dpanel dctl"><label>시간당 손님 <input type="range" id="zp1c" min="5" max="120" value="40"><b id="zp1cv"></b></label>
<label>1인 구매 품목 <input type="range" id="zp1i" min="1" max="8" value="3"><b id="zp1iv"></b></label>
<label>포인트 회원 비율 <input type="range" id="zp1p" min="0" max="100" value="45"><b id="zp1pv"></b></label>
<label>영업 시간 <select id="zp1h"><option value="12">12시간</option><option value="18" selected>18시간</option><option value="24">24시간</option></select></label></div>
<div class="dk-row" id="zp1k"></div>
<div class="dpanel"><h4>시간대별 새 기록 수 (행)</h4><canvas class="dch" id="zp1ch" role="img" aria-label="시간대별 판매·재고·포인트 기록 수 막대 그래프"></canvas><p class="cvcap" id="zp1note"></p></div>''',
tasks=['손님 40명·품목 3개·18시간일 때 하루 판매 기록이 몇 행인지 그래프 전에 손으로 계산해 보기 (40 × 3 × 18 = ?)','포인트 회원 비율을 0%와 100%로 바꿔 포인트 기록이 어떻게 변하는지 확인하기','“한 달이면 몇 행?”을 KPI로 확인하고, 엑셀 한 시트(약 104만 행)에 몇 달이 들어가는지 말해 보기'],
js=r'''
var $=LAB.$;function v(id){return +$(id).value;}
function draw(){var c=v('#zp1c'),it=v('#zp1i'),p=v('#zp1p')/100,h=v('#zp1h');
 $('#zp1cv').textContent=c+'명';$('#zp1iv').textContent=it+'개';$('#zp1pv').textContent=Math.round(p*100)+'%';
 var labs=[],sa=[],st=[],pt=[],peak=function(t){return t>=7&&t<=9||t>=12&&t<=13||t>=18&&t<=20?1.6:(t<6?0.3:0.9);};
 for(var t=0;t<h;t++){var hr=(7+t)%24,k=c*peak(hr);labs.push(hr+'시');sa.push(Math.round(k*it));st.push(Math.round(k*it));pt.push(Math.round(k*p));}
 var S=function(a){return a.reduce(function(x,y){return x+y;},0);},day=S(sa)+S(st)+S(pt);
 LAB.kpis($('#zp1k'),[['하루 판매 기록',S(sa).toLocaleString()+'행','바코드 1번 = 1행'],['재고 변경',S(st).toLocaleString()+'행','판매마다 재고 −1'],['포인트 적립',S(pt).toLocaleString()+'행','회원만'],['한 달 (30일)',(day*30).toLocaleString()+'행',(day*30>1048576?'엑셀 한 시트 초과':'엑셀 한 시트 안'),day*30>1048576?'bad':'good']]);
 LAB.chart($('#zp1ch'),{labels:labs,series:[{name:'판매',data:sa},{name:'재고',data:st},{name:'포인트',data:pt}]});
 $('#zp1note').textContent='출퇴근·점심 시간대는 손님이 1.6배라고 가정한 설명용 모형입니다. 바코드 한 번이 세 개의 표(판매·재고·포인트)를 동시에 바꾼다는 점이 데이터베이스가 필요한 이유입니다.';}
['#zp1c','#zp1i','#zp1p','#zp1h'].forEach(function(id){$(id).addEventListener('input',draw);});draw();addEventListener('resize',draw);
''')

PRACTICE['02'] = dict(
title='도서관 데이터 분류 · 중복 진단판', en='library data classification dashboard',
scenario='<p>도서관에 하루 동안 들어오는 데이터 20건이 차례로 도착합니다. 각각을 <b>정형 · 반정형 · 비정형</b>으로 분류하고, 같은 회원 정보를 부서마다 따로 저장할 때 중복이 얼마나 늘어나는지 함께 봅니다.</p>',
html='''<div class="two"><div class="dpanel"><h4>도착한 데이터 <span id="zp2n"></span></h4><p id="zp2item" style="font-size:17px;min-height:52px"></p>
<div class="dctl"><button type="button" class="bt" data-c="정형">정형</button><button type="button" class="bt" data-c="반정형">반정형</button><button type="button" class="bt" data-c="비정형">비정형</button><button type="button" class="bt" id="zp2r">처음부터</button></div><p id="zp2fb" class="cvcap"></p></div>
<div class="dpanel"><h4>분류 결과</h4><div class="dk-row" id="zp2k"></div></div></div>
<div class="dpanel"><h4>중복 진단 — 회원 정보를 부서마다 따로 저장하면</h4><div class="dctl"><label>회원 수 <input type="range" id="zp2m" min="100" max="5000" step="100" value="1200"><b id="zp2mv"></b></label><label>회원 정보를 가진 부서 <input type="range" id="zp2d" min="1" max="6" value="4"><b id="zp2dv"></b></label><label>월 주소 변경 비율 <input type="range" id="zp2u" min="0" max="10" value="2"><b id="zp2uv"></b></label></div>
<canvas class="dch" id="zp2ch" role="img" aria-label="부서 수에 따른 저장 행 수와 고쳐야 할 행 수 비교 그래프"></canvas></div>''',
tasks=['20건을 모두 분류하고 정답률 확인하기 (틀린 항목은 해설 읽기)','부서를 1개(데이터베이스 하나에 통합)와 6개로 바꿔 “한 달에 고쳐야 할 행”을 비교하기','“JSON 주문 기록”이 왜 반정형인지 한 문장으로 말해 보기'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var IT=[['회원 명부 표 (회원번호·이름·전화)','정형','칸이 정해진 표'],['도서 대출 기록 표','정형','행과 열이 고정'],['도서 표지 사진','비정형','칸이 없는 이미지'],['XML로 받은 출판사 신간 목록','반정형','태그로 구조를 설명'],['이용자 후기 게시글','비정형','자유로운 글'],['JSON 형식의 전자책 대출 로그','반정형','키:값 구조가 데이터 안에 있음'],['열람실 CCTV 영상','비정형','영상'],['연체료 수납 엑셀 시트','정형','칸이 고정된 표'],['도서 메타데이터 HTML 페이지','반정형','태그 구조'],['강연 녹음 파일','비정형','음성'],['좌석 예약 표','정형','칸 고정'],['출입 게이트 센서 로그 (JSON)','반정형','키:값'],['회원 문의 이메일 본문','비정형','자유 글'],['도서 분류 번호 표','정형','칸 고정'],['SNS 홍보 게시물 반응 데이터(API JSON)','반정형','키:값'],['손글씨 희망 도서 신청서 스캔','비정형','이미지'],['직원 근무표','정형','칸 고정'],['RSS 신간 알림 피드','반정형','XML 태그'],['독서 모임 사진','비정형','이미지'],['도서 구입 예산 표','정형','칸 고정']];
var k=0,cnt={'정형':0,'반정형':0,'비정형':0},ok=0;
function show(){if(k>=IT.length){$('#zp2item').innerHTML='<b>끝!</b> 20건 중 '+ok+'건 정답 ('+Math.round(ok/20*100)+'%)';}else{$('#zp2item').textContent=IT[k][0];}$('#zp2n').textContent='('+Math.min(k+1,20)+'/20)';
 LAB.kpis($('#zp2k'),[['정형',cnt['정형']+'건'],['반정형',cnt['반정형']+'건'],['비정형',cnt['비정형']+'건'],['정답률',k?Math.round(ok/k*100)+'%':'—','',k&&ok/k<0.7?'warn':'good']]);}
$$('#dash [data-c]').forEach(function(b){b.onclick=function(){if(k>=IT.length)return;var it=IT[k],c=b.dataset.c;cnt[c]++;if(c===it[1])ok++;$('#zp2fb').innerHTML=(c===it[1]?'<span class="ok">정답</span> ':'<span class="ng">정답은 '+it[1]+'</span> ')+'— '+it[2];k++;show();};});
$('#zp2r').onclick=function(){k=0;ok=0;cnt={'정형':0,'반정형':0,'비정형':0};$('#zp2fb').textContent='';show();};show();
function dup(){var m=+$('#zp2m').value,d=+$('#zp2d').value,u=+$('#zp2u').value/100;$('#zp2mv').textContent=m.toLocaleString()+'명';$('#zp2dv').textContent=d+'곳';$('#zp2uv').textContent=Math.round(u*100)+'%';
 var labs=[],a=[],b=[];for(var i=1;i<=6;i++){labs.push(i+'곳');a.push(m*i);b.push(Math.round(m*u*i));}
 LAB.chart($('#zp2ch'),{labels:labs,series:[{name:'저장된 회원 행',data:a},{name:'한 달에 고쳐야 할 행',data:b,color:'#c93030'}]});}
['#zp2m','#zp2d','#zp2u'].forEach(function(id){$(id).addEventListener('input',dup);});dup();addEventListener('resize',dup);
''')

PRACTICE['03'] = dict(
title='파일 시스템 vs DBMS — 30일 운영 시뮬레이터', en='file system vs dbms operations simulator',
scenario='<p>고객 주소를 영업·마케팅·서비스·물류 네 부서가 각자 파일로 가지고 있습니다. 주소 변경 요청이 매일 들어오고, 담당자가 다른 부서에 알리는 것을 가끔 잊습니다. 같은 30일을 <b>파일 시스템</b>과 <b>DBMS</b>(한 곳만 고치면 됨)로 돌려 불일치가 어떻게 쌓이는지 비교하세요.</p>',
html='''<div class="dpanel dctl"><label>부서 수 <input type="range" id="zp3d" min="2" max="8" value="4"><b id="zp3dv"></b></label><label>하루 주소 변경 <input type="range" id="zp3r" min="1" max="40" value="12"><b id="zp3rv"></b></label><label>전달 누락 확률 <input type="range" id="zp3m" min="0" max="30" value="8"><b id="zp3mv"></b></label><label>정전 사고 <select id="zp3c"><option value="0">없음</option><option value="15" selected>15일째 1번</option></select></label><button type="button" class="bt primary" id="zp3go">30일 돌리기</button></div>
<div class="dk-row" id="zp3k"></div><div class="dpanel"><h4>누적 불일치 고객 수</h4><canvas class="dch" id="zp3ch" role="img" aria-label="파일 시스템과 DBMS의 30일 누적 불일치 고객 수 선 그래프"></canvas><p class="cvcap">무작위 수는 고정 시드로 매번 같은 결과가 나옵니다. 정전 날에는 파일 시스템의 쓰다 만 변경이 남고, DBMS는 ROLLBACK·회복으로 되돌린다고 가정한 설명용 모형입니다.</p></div>''',
tasks=['누락 확률 0%에서도 파일 시스템이 DBMS보다 손이 많이 가는 이유를 KPI의 “고친 파일 수”로 설명하기','부서 수를 2 → 8로 늘리며 불일치가 어떻게 커지는지 보기','정전 사고를 켜고 끄며 두 방식의 차이를 3주차 은행 송금 실습과 연결해 말해 보기'],
js=r'''
var $=LAB.$;
function run(){var d=+$('#zp3d').value,r=+$('#zp3r').value,m=+$('#zp3m').value/100,crash=+$('#zp3c').value;
 $('#zp3dv').textContent=d+'곳';$('#zp3rv').textContent=r+'건';$('#zp3mv').textContent=Math.round(m*100)+'%';
 var R=LAB.rng(303),bad=0,edits=0,F=[],D=[],labs=[];
 for(var day=1;day<=30;day++){for(var i=0;i<r;i++){edits+=d;for(var j=1;j<d;j++){if(R()<m){bad++;break;}}}
  if(day===crash)bad+=Math.round(r*0.5);labs.push(day+'일');F.push(bad);D.push(0);}
 LAB.kpis($('#zp3k'),[['파일 시스템 불일치',bad+'명','30일 누적','bad'],['DBMS 불일치','0명','한 곳만 고침','good'],['파일 시스템이 고친 파일',edits.toLocaleString()+'번','변경 × 부서 수'],['DBMS가 고친 행',(r*30).toLocaleString()+'번','변경 1건 = 1행']]);
 LAB.chart($('#zp3ch'),{type:'line',labels:labs,series:[{name:'파일 시스템',data:F,color:'#c93030'},{name:'DBMS',data:D,color:'#13733a'}]});}
$('#zp3go').onclick=run;['#zp3d','#zp3r','#zp3m','#zp3c'].forEach(function(id){$(id).addEventListener('input',run);});run();addEventListener('resize',run);
''')

PRACTICE['04'] = dict(
title='스키마 변경 영향 계산기', en='schema change impact calculator',
scenario='<p>학사 시스템에 앱이 여러 개(수강 신청, 성적 조회, 장학금, 도서관 연동 …) 붙어 있습니다. 데이터베이스 쪽에서 변경이 생길 때 <b>3단계 구조와 사상</b>이 있으면 어디만 고치면 되는지, 없으면 몇 개의 앱을 고쳐야 하는지 계산해 봅니다.</p>',
html='''<div class="dpanel dctl"><label>연결된 앱 수 <input type="range" id="zp4a" min="1" max="30" value="12"><b id="zp4av"></b></label><label>그 칸을 쓰는 앱 비율 <input type="range" id="zp4u" min="10" max="100" step="10" value="50"><b id="zp4uv"></b></label><label>앱 1개 수정 시간 <input type="range" id="zp4h" min="1" max="16" value="6"><b id="zp4hv"></b></label></div>
<div class="dpanel"><h4>변경 사건을 고르세요</h4><div class="dctl" id="zp4ev"></div><p id="zp4ex" class="cvcap"></p></div>
<div class="dk-row" id="zp4k"></div><div class="dpanel"><h4>고쳐야 하는 곳 — 3단계 구조 있음 vs 없음 (수정 시간, 시간)</h4><canvas class="dch" id="zp4ch" role="img" aria-label="변경 사건별 수정 시간 비교 막대 그래프"></canvas></div>''',
tasks=['“칸 이름 변경(전화번호 → 연락처)”을 골라 논리적 독립성이 무엇을 아껴 주는지 수정 시간으로 말하기','“저장 장치 교체”에서 바뀌는 사상이 어느 것인지(외부/개념 vs 개념/내부) 확인하기','앱 수를 30개로 늘렸을 때 독립성이 없으면 며칠(8시간 = 1일)이 드는지 계산하기'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var EV=[['칸 이름 변경 (전화번호 → 연락처)','논리적','외부/개념 사상 한 줄만 고침 (뷰의 별칭)',1],['표 하나를 둘로 분리','논리적','외부/개념 사상(뷰 재정의)만 고침',2],['칸 추가 (이메일)','논리적','쓰지 않는 앱은 그대로 — 뷰에 없으면 영향 없음',0.5],['저장 장치 교체 (HDD → SSD)','물리적','개념/내부 사상만 고침 — 앱·개념 스키마 그대로',0.5],['색인 추가','물리적','내부 스키마만 — 앱은 몰라도 됨',0.5]];
var ev=0;$('#zp4ev').innerHTML=EV.map(function(e,i){return '<button type="button" class="bt" data-e="'+i+'">'+e[0]+'</button>';}).join('');
$$('#zp4ev [data-e]').forEach(function(b){b.onclick=function(){ev=+b.dataset.e;$$('#zp4ev [data-e]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});calc();};});
function calc(){var a=+$('#zp4a').value,u=+$('#zp4u').value/100,h=+$('#zp4h').value;$('#zp4av').textContent=a+'개';$('#zp4uv').textContent=Math.round(u*100)+'%';$('#zp4hv').textContent=h+'시간';
 var e=EV[ev],touched=Math.ceil(a*u),without=touched*h,withI=e[3]*h;
 $('#zp4ex').innerHTML='<b>'+e[1]+' 독립성</b> — '+e[2];
 LAB.kpis($('#zp4k'),[['영향받는 앱',touched+'개'],['독립성 없음',without+'시간',(without/8).toFixed(1)+'일','bad'],['3단계 구조 있음',withI+'시간','사상만 수정','good'],['아낀 시간',Math.max(0,without-withI)+'시간']]);
 LAB.chart($('#zp4ch'),{labels:EV.map(function(x,i){return '사건 '+(i+1);}),series:[{name:'독립성 없음',data:EV.map(function(){return Math.ceil(a*u)*h;}),color:'#c93030'},{name:'3단계 구조 있음',data:EV.map(function(x){return x[3]*h;}),color:'#13733a'}]});}
['#zp4a','#zp4u','#zp4h'].forEach(function(id){$(id).addEventListener('input',calc);});$$('#zp4ev [data-e]')[0].click();addEventListener('resize',calc);
''')

PRACTICE['05'] = dict(
title='수강 신청 ERD 검증 대시보드', en='course registration erd checker',
scenario='<p>수강 신청 시스템의 요구 사항 6개가 있습니다. 관계마다 대응 수(1:1, 1:N, N:M)를 고르면, 대시보드가 그 설계로 <b>예시 데이터 12건</b>을 실제로 넣어 보고 어느 요구 사항이 깨지는지, 테이블이 몇 개 필요한지 계산합니다.</p>',
html='''<div class="dpanel" id="zp5rel"></div><div class="dk-row" id="zp5k"></div>
<div class="two"><div class="dpanel"><h4>예시 데이터 넣어 보기</h4><div id="zp5log" style="font-size:14px;max-height:260px;overflow:auto"></div></div><div class="dpanel"><h4>이 설계의 테이블</h4><div id="zp5tb" style="font-size:14px"></div></div></div>''',
tasks=['처음에는 일부러 “학생–과목 = 1:N”으로 두고 몇 건이 막히는지 보기','모든 관계를 요구 사항에 맞게 고쳐 위반 0건 만들기','테이블 수가 5주차 대결의 정답(3개 + α)과 어떻게 연결되는지 설명하기'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var REL=[['학생','수강','과목','nm','요구 1: 학생은 여러 과목을, 과목은 여러 학생이 수강'],['교수','담당','과목','1n','요구 2: 교수 한 명이 여러 과목, 과목은 교수 한 명'],['학과','소속','학생','1n','요구 3: 학과 하나에 여러 학생, 학생은 한 학과'],['학과','소속','교수','1n','요구 4: 학과 하나에 여러 교수, 교수는 한 학과'],['교수','학과장','학과','11','요구 5: 학과장은 교수 한 명, 교수는 최대 한 학과의 장']];
var pick={0:'1n',1:'1n',2:'1n',3:'1n',4:'1n'};
$('#zp5rel').innerHTML='<h4>관계의 대응 수 고르기</h4>'+REL.map(function(r,i){return '<div class="dctl" style="margin:4px 0"><b style="min-width:170px">'+r[0]+' —'+r[1]+'— '+r[2]+'</b>'+['11','1n','nm'].map(function(c){return '<button type="button" class="bt" data-r="'+i+'" data-c="'+c+'">'+{'11':'1:1','1n':'1:N','nm':'N:M'}[c]+'</button>';}).join('')+'<small style="color:#5b6874">'+r[4]+'</small></div>';}).join('');
var DATA=[[0,'김하늘','DB설계'],[0,'김하늘','자료구조'],[0,'이바다','DB설계'],[0,'박산','DB설계'],[0,'이바다','운영체제'],[1,'정교수','DB설계'],[1,'정교수','자료구조'],[2,'컴공','김하늘'],[2,'컴공','이바다'],[3,'컴공','정교수'],[3,'컴공','한교수'],[4,'정교수','컴공']];
function check(){var viol=0,log=[],seenL={},seenR={};
 DATA.forEach(function(d){var r=REL[d[0]],c=pick[d[0]],ok=true,why='';
  var kL=d[0]+'|'+d[1],kR=d[0]+'|'+d[2];
  if(c==='11'){if(seenL[kL]&&seenL[kL]!==d[2]){ok=false;why=d[1]+'이(가) 이미 다른 '+r[2]+'와 연결';} if(seenR[kR]&&seenR[kR]!==d[1]){ok=false;why=d[2]+'이(가) 이미 다른 '+r[0]+'와 연결';}}
  if(c==='1n'){if(seenR[kR]&&seenR[kR]!==d[1]){ok=false;why=d[2]+'은(는) '+r[0]+' 하나만 가질 수 있는데 둘째 연결';}}
  if(ok){seenL[kL]=seenL[kL]||d[2];seenR[kR]=seenR[kR]||d[1];} else viol++;
  log.push((ok?'<span class="ok">✓</span> ':'<span class="ng">✗</span> ')+d[1]+' — '+r[1]+' — '+d[2]+(ok?'':' <small>('+why+')</small>'));});
 var right=REL.filter(function(r,i){return pick[i]===r[3];}).length,nm=REL.filter(function(r,i){return pick[i]==='nm';}).length;
 var ents=['학생','과목','교수','학과'],tables=ents.length+nm;
 LAB.kpis($('#zp5k'),[['막힌 데이터',viol+'건','12건 중',viol?'bad':'good'],['요구와 맞는 관계',right+'/5','',right===5?'good':'warn'],['테이블 수',tables+'개','개체 4 + N:M '+nm],['외래키 수',REL.filter(function(r,i){return pick[i]!=='nm';}).length+REL.filter(function(r,i){return pick[i]==='nm';}).length*2+'개']]);
 $('#zp5log').innerHTML=log.join('<br>');
 $('#zp5tb').innerHTML=ents.map(function(e){var fk=REL.map(function(r,i){var c=pick[i];return c==='1n'&&r[2]===e?r[0]+'번호(FK)':(c==='11'&&r[2]===e?r[0]+'번호(FK, UNIQUE)':'');}).filter(Boolean);return '<code>'+e+'(<u>'+e+'번호</u>'+(fk.length?', '+fk.join(', '):'')+', …)</code>';}).join('<br>')+REL.map(function(r,i){return pick[i]==='nm'?'<br><code>'+r[1]+'(<u>'+r[0]+'번호, '+r[2]+'번호</u>)</code> ← N:M 연결 표':'';}).join('');}
$$('#zp5rel [data-r]').forEach(function(b){b.onclick=function(){pick[b.dataset.r]=b.dataset.c;$$('#zp5rel [data-r="'+b.dataset.r+'"]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});check();};});
Object.keys(pick).forEach(function(i){$$('#zp5rel [data-r="'+i+'"][data-c="'+pick[i]+'"]')[0].setAttribute('aria-pressed','true');});check();
''')

PRACTICE['06'] = dict(
title='무결성 검사대 — 들어오는 데이터 걸러내기', en='integrity checkpoint dashboard',
scenario='<p>학생 표와 수강 표에 새 데이터 30건이 들어옵니다. 그중 일부에는 기본키 누락, 중복, 없는 학생을 가리키는 외래키 같은 문제가 섞여 있습니다. 제약 조건 스위치를 켜고 끄며 <b>실제 SQL 엔진</b>(실습실 엔진)에 넣어 보고, 표에 남는 나쁜 데이터를 세어 보세요.</p>',
html='''<div class="dpanel dctl"><label><input type="checkbox" id="zp6pk" checked> 기본키 (NOT NULL + UNIQUE)</label><label><input type="checkbox" id="zp6fk" checked> 외래키 (수강 → 학생)</label><label><input type="checkbox" id="zp6ck" checked> CHECK (학년 1~4)</label><button type="button" class="bt primary" id="zp6go">30건 넣기</button></div>
<div class="dk-row" id="zp6k"></div><div class="two"><div class="dpanel"><h4>처리 기록</h4><div id="zp6log" style="font-size:13px;max-height:280px;overflow:auto"></div></div><div class="dpanel"><h4>남은 나쁜 데이터 종류</h4><canvas class="dch" id="zp6ch" role="img" aria-label="남은 나쁜 데이터 종류별 개수 막대 그래프"></canvas></div></div>''',
tasks=['세 스위치를 모두 끄고 넣은 뒤, 남은 나쁜 데이터 종류를 읽기','기본키만 켜고 다시 넣어 개체 무결성이 막는 것 확인하기','외래키를 켜면 “없는 학생의 수강”이 0이 되는지 확인하고 오류 번호(1452)를 기록에서 찾기'],
js=r'''
var $=LAB.$;
var ROWS=[];(function(){var R=LAB.rng(606),names=['김','이','박','최','정','강','조','윤'];for(var i=0;i<30;i++){var r=R(),t;
 if(i%10===3)t=['S',null,names[i%8]+'민',2];else if(i%10===6)t=['S',100+((i*7)%5),names[i%8]+'준',2];else if(i%10===8)t=['S',300+i,names[i%8]+'우',7];else if(i%10===9)t=['E',900+i,'DB'];else if(i%2)t=['E',100+(i%5),['DB','OS','자료구조'][i%3]];else t=['S',200+i,names[i%8]+'서',1+(i%4)];ROWS.push(t);}})();
function q(v){return v===null?'NULL':(typeof v==='number'?v:"'"+v+"'");}
function go(){var pk=$('#zp6pk').checked,fk=$('#zp6fk').checked,ck=$('#zp6ck').checked,db=LAB.DB();
 db.run("CREATE DATABASE u; USE u; CREATE TABLE 학생 (학번 INT"+(pk?" PRIMARY KEY":"")+", 이름 VARCHAR(10), 학년 INT"+(ck?" CHECK (학년 BETWEEN 1 AND 4)":"")+"); INSERT INTO 학생 VALUES (100,'가람',1),(101,'나래',2),(102,'다솜',3),(103,'라온',4),(104,'마루',2);"+
  "CREATE TABLE 수강 (학번 INT, 과목 VARCHAR(10)"+(fk?", FOREIGN KEY (학번) REFERENCES 학생(학번)":"")+");");
 var ok=0,rej=0,log=[];
 ROWS.forEach(function(r){var sql=r[0]==='S'?'INSERT INTO 학생 VALUES ('+q(r[1])+', '+q(r[2])+', '+q(r[3])+')':'INSERT INTO 수강 (학번, 과목) VALUES ('+q(r[1])+', '+q(r[2])+')';
  try{db.exec(sql);ok++;log.push('<span class="ok">OK</span> <code>'+sql+'</code>');}catch(e){rej++;log.push('<span class="ng">거부</span> <code>'+sql+'</code><br><small>'+e.message+'</small>');}});
 var c=function(s){var r=LAB.sqlRows(db,s);return r?+r.rows[0][0]:0;};
 var bad=[c('SELECT COUNT(*) FROM 학생 WHERE 학번 IS NULL'),c('SELECT COUNT(*) FROM (SELECT 학번 FROM 학생 WHERE 학번 IS NOT NULL GROUP BY 학번 HAVING COUNT(*) > 1) d'),c('SELECT COUNT(*) FROM 학생 WHERE 학년 NOT BETWEEN 1 AND 4'),c('SELECT COUNT(*) FROM 수강 WHERE 학번 NOT IN (SELECT 학번 FROM 학생 WHERE 학번 IS NOT NULL)')];
 var tot=bad.reduce(function(a,b){return a+b;},0);
 LAB.kpis($('#zp6k'),[['받아들인 행',ok+'건'],['거부한 행',rej+'건','오류로 막힘'],['표에 남은 나쁜 데이터',tot+'건','',tot?'bad':'good'],['켜진 제약',[pk,fk,ck].filter(Boolean).length+'/3']]);
 $('#zp6log').innerHTML=log.join('<br>');LAB.chart($('#zp6ch'),{labels:['기본키 NULL','중복 학번','학년 범위 밖','없는 학생의 수강'],series:[{name:'남은 행',data:bad,color:'#c93030'}],ymax:6});}
$('#zp6go').onclick=go;['#zp6pk','#zp6fk','#zp6ck'].forEach(function(id){$(id).addEventListener('change',go);});go();addEventListener('resize',go);
''')

PRACTICE['07'] = dict(
title='질의 처리 순서 비교기 — 먼저 거를까, 먼저 붙일까', en='query plan comparison dashboard',
scenario='<p>주문 표와 고객 표를 조인한 뒤 “VIP 고객의 주문”만 고르는 질의가 있습니다. <b>σ(셀렉트)를 먼저</b> 하고 ⋈(조인)할 때와, <b>⋈ 먼저</b> 하고 σ할 때 중간 결과의 크기가 얼마나 다른지 표 크기와 선택률을 바꿔 가며 계산합니다.</p>',
html='''<div class="dpanel dctl"><label>고객 수 <input type="range" id="zp7c" min="100" max="20000" step="100" value="2000"><b id="zp7cv"></b></label><label>고객당 주문 <input type="range" id="zp7o" min="1" max="30" value="8"><b id="zp7ov"></b></label><label>VIP 비율 <input type="range" id="zp7v" min="1" max="100" value="5"><b id="zp7vv"></b></label></div>
<div class="dk-row" id="zp7k"></div><div class="dpanel"><h4>단계별로 다루는 행 수 (로그 눈금 아님)</h4><canvas class="dch" id="zp7ch" role="img" aria-label="두 처리 순서의 단계별 행 수 막대 그래프"></canvas><p class="cvcap" id="zp7n"></p></div>''',
tasks=['기본값에서 두 순서의 “전체 비교 횟수”를 손으로 먼저 계산해 보기 (힌트: 조인 비교 = 왼쪽 행 × 오른쪽 행)','VIP 비율을 100%로 올리면 왜 두 방법의 차이가 사라지는지 설명하기','실제 DBMS의 질의 최적화기가 σ를 먼저 내리는 이유를 한 문장으로 말하기'],
js=r'''
var $=LAB.$;
function f(){var c=+$('#zp7c').value,o=+$('#zp7o').value,v=+$('#zp7v').value/100,ord=c*o,vip=Math.round(c*v);
 $('#zp7cv').textContent=c.toLocaleString()+'명';$('#zp7ov').textContent=o+'건';$('#zp7vv').textContent=Math.round(v*100)+'%';
 var A1=c,A2=vip,A3=vip*o,cmpA=c+vip*ord, B1=ord,B2=ord,B3=vip*o,cmpB=c*ord+ord;
 LAB.kpis($('#zp7k'),[['주문 표 크기',ord.toLocaleString()+'행'],['σ 먼저 — 비교 횟수',cmpA.toLocaleString(),'고객 거르기 + VIP×주문','good'],['⋈ 먼저 — 비교 횟수',cmpB.toLocaleString(),'고객×주문 + 결과 거르기','bad'],['차이',(cmpB/Math.max(1,cmpA)).toFixed(1)+'배']]);
 LAB.chart($('#zp7ch'),{labels:['1단계 결과','2단계 결과','최종 결과'],series:[{name:'σ 먼저',data:[A2,A3,A3],color:'#13733a'},{name:'⋈ 먼저',data:[B1,B2,B3],color:'#c93030'}]});
 $('#zp7n').textContent='비교 횟수는 중첩 반복 조인(색인 없음)을 가정한 단순 모형입니다. 결과 행 수는 두 방법이 같다는 점(최종 '+A3.toLocaleString()+'행)에 주목하세요 — 순서는 비용만 바꾸고 답은 바꾸지 않습니다.';}
['#zp7c','#zp7o','#zp7v'].forEach(function(id){$(id).addEventListener('input',f);});f();addEventListener('resize',f);
''')

PRACTICE['08'] = dict(
title='중간고사 약점 진단 대시보드', en='midterm weakness dashboard',
scenario='<p>이 페이지의 퀴즈(각 칸 퀴즈 + 모의 20문항)를 풀면 <b>주차별 정답률</b>이 여기에 모입니다. 가장 약한 주차와 정의형·상황형 중 어느 쪽에 약한지 보고, 돌아갈 페이지를 고르세요. 아직 풀지 않았다면 「예시 학생으로 보기」를 눌러 보세요.</p>',
html='''<div class="dpanel dctl"><button type="button" class="bt primary" id="zp8r">내 풀이 결과 불러오기</button><button type="button" class="bt" id="zp8d">예시 학생으로 보기</button><span id="zp8s" class="cvcap"></span></div>
<div class="dk-row" id="zp8k"></div><div class="dpanel"><h4>주차별 정답률 (%)</h4><canvas class="dch" id="zp8ch" role="img" aria-label="주차별 정답률 막대 그래프"></canvas></div><div class="dpanel" id="zp8go"></div>''',
tasks=['모의 20문항을 모두 풀고 「내 풀이 결과 불러오기」 누르기','정답률이 가장 낮은 주차 페이지를 열어 그 칸의 퀴즈를 다시 풀기','정의형과 상황형 중 낮은 쪽을 보고, 상황형이 낮다면 대결·실습 장면을 다시 보기'],
js=r'''
var $=LAB.$;
var FILE={1:'w01_course_guide.html',2:'w02_data_and_database.html',3:'w03_dbms.html',4:'w04_database_system.html',5:'w05_er_modeling.html',6:'w06_relational_model.html',7:'w07_relational_operations.html'};
function wk(q){var m=(q.why||'').match(/\((\d)(?:·\d)?주차\)/);return m?+m[1]:0;}
function collect(demo){var by={},ty={def:[0,0],case:[0,0]},n=0;
 var qs=(window.QUIZ&&QUIZ.mock)||[];var R=LAB.rng(808);
 qs.forEach(function(q,i){var w=wk(q);if(!w)return;var key='mock:'+i,st=window.QSTAT&&QSTAT.by&&QSTAT.by[key];var ans=demo?(R()<[0,.9,.85,.7,.55,.6,.75,.45][w]):(st?st.ok:null);if(ans===null)return;n++;
  by[w]=by[w]||[0,0];by[w][1]++;if(ans)by[w][0]++;});
 return {by:by,n:n};}
function draw(demo){var r=collect(demo),labs=[],data=[],worst=null;
 for(var w=1;w<=7;w++){var b=r.by[w];labs.push(w+'주');var p=b?Math.round(b[0]/b[1]*100):0;data.push(p);if(b&&(worst===null||p<data[worst-1]))worst=w;}
 $('#zp8s').textContent=r.n?(demo?'예시 학생(가상) 결과':'내가 푼 '+r.n+'문항 기준'):'아직 푼 모의 문항이 없습니다 — 아래 모의 20을 먼저 풀거나 예시 학생으로 보세요.';
 var tot=data.reduce(function(a,b){return a+b;},0)/7;
 LAB.kpis($('#zp8k'),[['푼 문항',r.n+'/20'],['평균 정답률',r.n?Math.round(tot)+'%':'—'],['가장 약한 주차',worst?worst+'주차':'—','',worst?'bad':''],['목표','80%','주차마다']]);
 LAB.chart($('#zp8ch'),{labels:labs,series:[{name:'정답률',data:data}],ymax:100,yfmt:function(v){return Math.round(v)+'%';}});
 $('#zp8go').innerHTML=worst?'<b>다시 볼 곳:</b> <a href="'+FILE[worst]+'">'+worst+'주차 페이지</a> — 그 페이지의 칸 퀴즈부터 다시 풀고, 대결 장면의 판정 이유를 소리 내어 설명해 보세요.':'';}
$('#zp8r').onclick=function(){draw(false);};$('#zp8d').onclick=function(){draw(true);};draw(true);addEventListener('resize',function(){draw(true);});
''')
