# 3주차 — 데이터베이스 관리 시스템 (교재 2장)
PAGE = dict(
num='03', slug='dbms', kind='lecture', short='3주', chip='03주차',
title='데이터베이스 관리 시스템', title_en='Database management system',
subtitle='파일로 관리하면 왜 무너지는가, DBMS는 무엇을 대신하는가',
toc='파일 시스템의 중복·종속·회복 문제, DBMS의 정의·세 기능·장단점, 1~4세대 발전사',
kicker='데이터베이스 설계 · 3주차 · 교재 2장',
question='주소 하나를 바꿨는데 왜 택배는 옛집으로 갔을까?',
desc='데이터베이스 설계 3주차: 파일 시스템의 한계(중복, 종속, 동시 공유·보안·회복 부족, 개발의 어려움), DBMS의 정의와 정의·조작·제어 기능, 장단점, 세대별 발전.',
intro='<p>고객 김철수가 이사를 했습니다. 영업부, 마케팅부, 서비스부, 물류팀이 각자 고객 파일을 갖고 있다면, 네 파일을 모두 고쳐야 합니다. 하나라도 빠뜨리면 택배는 옛 주소로 갑니다. <b>담당자의 실수가 아니라 구조의 문제</b>입니다. 이번 회차는 그 구조를 바꾼 소프트웨어, DBMS를 다룹니다.</p>',
kpis=[('5가지','파일 시스템의 문제'),('3기능','정의 · 조작 · 제어'),('8 : 3','DBMS의 장점 : 단점'),('4세대','계층·네트워크 → 관계 → 객체 → NoSQL·NewSQL')],
hero_talk=[
 ('doc','front','파일 시스템이 나쁜 게 아니다. <b>규모가 커지면 감당이 안 되는 것</b>이다. 오늘은 그 경계를 본다.'),
 ('asst','smile','부서마다 파일을 하나씩 가지면 서로 안 부딪혀서 편할 것 같은데요?'),
 ('fly','clip','편한 건 처음 한 달이야. 같은 사실이 네 곳에 있으면, 언젠가 넷 중 하나는 틀려.'),
 ('robo','smile','복사본이 네 개면 백업도 네 개! 나는 그게 더 든든한데?')],
crew=[('doc','front','문제와 해결을 짝지어 정리'),('asst','smile','실험 진행, 숫자 발표'),('fly','clip','중복의 위험을 짚음'),('robo','smile','“복사본 = 백업”이라고 믿음')],
recap='2주차: 데이터베이스는 <b>공유·통합·저장·운영</b> 데이터의 집합입니다. 오늘은 “통합”이 깨지면 무슨 일이 생기는지, 파일 시스템에서 직접 봅니다.',
notion=[('03주차 : 데이터베이스 시스템 (노션)', NOTION+'1ab17a4520ed812bb498c10b8e28d024', '강의 영상·자료 (노션 Schedule의 3주차 칸)')],
why=[('중복은 저절로 생긴다','부서가 나뉘면 같은 고객 정보가 여러 파일에 생깁니다. 누가 잘못해서가 아니라 업무 구조가 그렇게 만듭니다.'),
     ('프로그램이 파일에 묶인다','파일 형식이 바뀌면 그 파일을 읽는 모든 프로그램을 고쳐야 합니다(종속성).'),
     ('DBMS는 이 둘을 동시에 푼다','교재는 DBMS를 “파일 시스템의 데이터 중복과 데이터 종속 문제를 해결하는 시스템”으로 정의합니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>#</th><th>파일 시스템의 문제</th><th>무슨 일이</th><th>DBMS의 답</th></tr></thead><tbody>
<tr><td>1</td><td>데이터 중복</td><td>같은 값이 여러 파일에 저장 → 하나만 고치면 불일치</td><td>통합 저장 + 제약 조건</td></tr>
<tr><td>2</td><td>데이터 종속</td><td>응용 프로그램이 파일 구성·물리적 저장 구조에 맞춰 작성됨</td><td>데이터 독립성 (4주차 3단계 구조)</td></tr>
<tr><td>3</td><td>동시 공유·보안·회복 부족</td><td>동시 수정 충돌, 권한 제어 미흡, 갱신 실패 시 어중간한 값</td><td>동시성 제어·권한 관리·롤백</td></tr>
<tr><td>4</td><td>응용 프로그램 개발이 어려움</td><td>읽기·삽입·삭제를 프로그램마다 직접 코딩</td><td>표준 질의 언어 SQL</td></tr>
<tr><td>5</td><td>무결성 유지가 어려움</td><td>값의 규칙을 프로그램마다 따로 검사</td><td>무결성 제약을 DBMS가 강제</td></tr></tbody></table></div>
<p style="font-size:14px;color:#5b6874">교안은 1~4번을 등장 배경으로 들고, 5번은 보충 정리입니다.</p>''',
steps=[
dict(id='lv1', short='중복', title='파일 시스템과 데이터 중복 — 주소가 바뀐 날', concept='데이터 중복', en='data redundancy in file systems', cid='lab:concept/data-redundancy',
 tag='현장: 부서별 고객 파일', analogy='부서별 고객 파일',
 situation='영업부·마케팅부·서비스부·물류팀이 각자 고객 파일을 갖고 있습니다. 김철수 고객이 이사를 했다는 연락이 영업부로 왔습니다. 오늘 오후, 물류팀은 어느 주소로 택배를 보낼까요?',
 pair=(('현장에서는','주소가 <b>네 파일에 따로</b> 들어 있습니다. 영업부는 바로 고쳤고, 마케팅·서비스는 메일을 보고 고쳤는데, 물류팀은 메일을 놓쳤습니다.'),
       ('파일 시스템에서는','파일 시스템은 파일을 저장해 줄 뿐, “이 값이 다른 파일에도 있는지 판단하는 일”과 “모두 고치는 일”을 대신해 주지 않습니다. 그 일은 사람 몫이고, 사람은 빠뜨립니다.')),
 panel='''<p style="margin-top:0">김철수의 새 주소를 어느 파일에 반영할지 직접 체크하고, 「택배 보내기」를 눌러 보세요.</p>
<div class="chips" id="f3"></div><div class="ctrl"><button type="button" class="bt primary" id="f3go">오후 3시 — 택배 보내기</button><button type="button" class="bt" id="f3r">처음으로</button></div>
<div id="f3t"></div><div class="insight" id="f3o">고칠 파일을 고르세요. (물류팀 파일이 실제 배송 주소로 쓰입니다)</div>''',
 panel_title='직접 해 보기 — 주소 바꾸기',
 sim='부서별 파일 주소 갱신 실험',
 flow=dict(id='fl3', title='파일 시스템에서의 하루', h=220, alt='주소 변경 요청이 영업부, 마케팅부, 서비스부를 거쳐 물류팀에서 누락되는 흐름',
   cap='마지막 칸에서 빨갛게 바뀌는 카드가 “고치지 못한 파일”입니다. 같은 사실이 여러 곳에 있으면, 한 곳의 실수가 곧 고객의 불편이 됩니다.',
   js='{stations:["09:00 영업부","09:20 마케팅부","11:40 서비스부","13:00 물류팀","15:00 배송"],items:[["새 주소 ✓","새 주소 ✓","새 주소 ✓","옛 주소 ✗","옛 주소로 배송"],["전화 변경 ✓","전화 변경 ✓","옛 번호 ✗","옛 번호 ✗","연락 실패"]],bad:function(it,i){return /✗|옛|실패/.test(it[i]);},stamp:"설명용 모형"}'),
 explain='<p>데이터 중복 자체가 죄는 아닙니다. 문제는 <b>중복을 통제할 장치가 없다</b>는 것입니다. 교안의 표현으로, 중복 데이터를 관리하려면 ① 이 값이 중복인지 “판단”하는 프로세스와 ② 모두 고치는 관리 프로세스가 필요한데, 파일 시스템에는 둘 다 없습니다. 게다가 담당자·시점·복사본·백업본 같은 DB 구조 밖의 요인이 얽혀, 사람이 다 통제하기는 사실상 어렵습니다.</p>',
 aicheck='<p>교안의 질문 “중복 데이터 관리가 DB 시스템에서만 필요할까?” — AI에게 물으면 “DB를 쓰면 중복이 사라진다”고 답하기 쉽습니다. 틀렸습니다. 쇼핑몰도 배송 주소를 <b>주문 시점의 값으로 일부러 복사</b>해 둡니다(나중에 회원 주소를 바꿔도 지난 주문의 배송지는 그대로여야 하니까). 중요한 것은 중복의 <b>제거</b>가 아니라 <b>통제</b>입니다.</p>',
 limit='중복만 문제가 아닙니다. 파일 형식이 바뀌면, 그 파일을 읽던 프로그램들은 어떻게 될까요?', limit_label='중복을 판단·통제할 장치가 없음',
 say=('fly','arms','봐. 세 곳을 고쳐도 한 곳을 놓치면 결과는 “틀림”이야. 50점이 아니라 0점.'),
 quiz=[dict(q='파일 시스템에서 같은 고객 주소가 네 파일에 저장되어 있을 때, 한 파일만 고치지 않으면 생기는 문제는?',o=['데이터 독립성','데이터 불일치(일관성 깨짐)','데이터 보안 향상','데이터 압축'],a=1,why='중복 저장된 값 중 일부만 바뀌어 서로 다른 값이 공존하는 상태를 불일치라고 합니다.'),
       dict(q='교안이 말하는 “중복 데이터 관리에 필요한 두 가지 프로세스”가 바르게 짝지어진 것은?',o=['백업과 압축','중복인지 판단하는 프로세스와 모두 고치는 관리 프로세스','삽입과 삭제','암호화와 복호화'],a=1,why='중복인지 판단하고, 판단한 값을 모두 고쳐야 합니다. 파일 시스템은 이 둘을 대신해 주지 않습니다.')]),
dict(id='lv2', short='종속', title='데이터 종속 — 파일 형식이 바뀌면 프로그램이 깨진다', concept='데이터 종속성', en='data dependency', cid='lab:concept/data-dependency',
 tag='현장: 고객 파일에 칸 하나 추가', analogy='칸 하나 끼워 넣기',
 situation='고객 파일에 “이메일” 칸을 이름과 주소 사이에 끼워 넣었습니다. 다음 날 아침, 청구서 프로그램은 주소 자리에 이메일을 인쇄했고, 배송 프로그램은 오류를 냈습니다.',
 pair=(('현장에서는','각 프로그램은 “앞에서 10글자가 이름, 그다음 30글자가 주소” 식으로 <b>파일의 생김새를 외우고</b> 있었습니다. 칸이 하나 끼어들자 외운 위치가 모두 어긋났습니다.'),
       ('DBMS에서는','프로그램은 “주소 칸을 달라”고 <b>이름으로</b> 요청하고, 실제 저장 위치는 DBMS가 압니다. 저장 구조가 바뀌어도 DBMS가 대응 관계만 고치면 프로그램은 그대로 둡니다(4주차 데이터 독립성).')),
 panel='''<p style="margin-top:0">파일 형식을 바꾸는 변경을 골라 보세요. 파일 시스템과 DBMS에서 고쳐야 할 프로그램 수가 어떻게 다른지 봅니다.</p>
<div class="chips" id="dep3"></div><div class="two"><div id="depF"></div><div id="depD"></div></div><div class="insight" id="depO"></div>''',
 panel_title='직접 해 보기 — 형식 변경의 파급',
 sim='파일 형식 변경 파급 비교',
 explain='<p><b>종속성</b>이란 응용 프로그램이 파일 데이터를 구성하는 방법과 물리적인 저장 구조에 맞게 작성되는 성질입니다. 그래서 파일 구조가 바뀌면 그 파일을 쓰는 프로그램을 모두 고쳐야 합니다. 여기에 4번 문제(개발의 어려움)가 겹칩니다 — 프로그램마다 읽기·삽입·삭제 코드를 직접 짜야 하니, 같은 기능을 여러 번 만들고 여러 번 고칩니다. DBMS는 이 일을 SQL 한 줄로 바꿉니다.</p>',
 limit='여러 사람이 <b>동시에</b> 같은 파일을 고치거나, 고치는 도중에 전기가 나가면 어떻게 될까요?', limit_label='동시 수정·실패 복구를 다루지 못함',
 say=('asst','shock','칸 하나 넣었을 뿐인데 프로그램 세 개를 다 고쳐야 한다니… 파일이 프로그램을 붙잡고 있네요.'),
 quiz=[dict(q='“응용 프로그램이 파일의 구성 방법과 물리적 저장 구조에 맞게 작성되는 성질”을 무엇이라 하나요?',o=['데이터 독립성','데이터 종속성','데이터 무결성','데이터 중복성'],a=1,why='데이터 종속성입니다. DBMS는 그 반대인 데이터 독립성을 목표로 합니다.'),
       dict(q='파일 시스템에서 고객 파일에 칸 하나를 추가했을 때, 그 파일을 쓰는 프로그램이 3개라면 몇 개를 점검·수정해야 할 가능성이 큰가요?',o=['0개','1개','3개 모두','파일만 고치면 됨'],a=2,why='모든 프로그램이 파일 구조를 직접 알고 있으므로 셋 다 점검해야 합니다.')]),
dict(id='lv3', short='회복', title='동시 공유·보안·회복 — 계좌 이체 도중에 멈추면', concept='회복과 롤백', en='recovery and rollback', cid='lab:concept/rollback',
 tag='연구실: 이체 실험', analogy='계좌 이체',
 situation='A 계좌에서 10,000원을 빼고 B 계좌에 10,000원을 넣는 중에, 두 번째 단계가 실패했습니다. 파일 시스템이라면 A에서만 돈이 사라집니다. DBMS는 어떻게 할까요?',
 pair=(('연구실에서는','실습실의 <code>account</code> 표에는 “잔액은 0 이상”이라는 규칙이 걸려 있습니다. 규칙을 어기는 단계에서 이체가 멈추도록 만들어 두었습니다.'),
       ('DBMS에서는','두 단계를 <b>하나의 작업 단위</b>(트랜잭션)로 묶고, 중간에 실패하면 시작 전 상태로 되돌립니다. 이것이 <b>롤백</b>(후진 복귀)입니다. DBMS는 업데이트 이전의 기록(저널·로그)으로 원래 상태를 되찾습니다.')),
 panel='<div class="sqllab" id="lab3" data-lab="lab3"></div><p class="cvcap">①로 잔액을 보고, ② 실패하는 이체를 실행한 뒤 다시 잔액을 보세요. 그다음 ③ 롤백을 실행하면 무엇이 달라지나요?</p>',
 panel_title='SQL 실습실 — 실패한 이체 되돌리기',
 sim='계좌 이체 롤백 실습',
 explain='<p><b>손으로 먼저:</b> A 30,000원, B 5,000원. A→B 10,000원 이체는 A 20,000 / B 15,000이 되어야 합니다. 합계는 이체 전후 모두 35,000원이어야 하죠. 그런데 B 쪽 단계가 실패하면 A 20,000 / B 5,000, 합계 25,000원 — <b>1만 원이 증발</b>합니다. 롤백 후에는 다시 A 30,000 / B 5,000, 합계 35,000원으로 돌아옵니다. 실습실에서 ④ 「합계 확인」으로 이 숫자를 직접 확인해 보세요.</p><p>보안(권한)과 동시 공유도 같은 뿌리입니다. 파일은 “열 수 있으면 다 고칠 수 있다”에 가깝지만, DBMS는 사용자별로 볼 수 있는 표·할 수 있는 일을 나눕니다(12주차 GRANT).</p>',
 limit='DBMS가 무엇을 해 주는지는 보였습니다. 그렇다면 DBMS를 한 문장으로 정의하고, 기능과 장단점을 정리해 봅시다.', limit_label='DBMS의 정의·기능·비용을 아직 정리하지 않음',
 say=('robo','wow','합계가 25,000원이 됐다가 롤백하니까 35,000원으로 돌아왔어! 돈이 사라졌다 돌아왔네!'),
 quiz=[dict(q='데이터베이스 업데이트에 오류가 생겼을 때 이전 상태로 되돌리는 것을 무엇이라 하나요?',o=['커밋(Commit)','롤백(Rollback)','인덱스(Index)','조인(Join)'],a=1,why='롤백, 후진 복귀라고도 합니다. 업데이트 이전의 저널(로그) 파일로 원래 상태로 돌립니다.'),
       dict(q='A 30,000원, B 5,000원에서 A→B 10,000원 이체 중 B 단계만 실패하고 롤백하지 않았다면 두 계좌 합계는? (계산)',o=['35,000원','30,000원','25,000원','45,000원'],a=2,why='A만 20,000원이 되고 B는 5,000원 그대로이므로 합계 25,000원. 10,000원이 사라집니다.')]),
dict(id='lv4', short='DBMS', title='DBMS의 정의·기능·장단점, 그리고 네 세대', concept='데이터베이스 관리 시스템', en='database management system', cid='lab:concept/dbms',
 tag='연구실: 연표', analogy='관리인과 창고',
 situation='오늘 본 문제를 한꺼번에 풀어 주는 소프트웨어가 DBMS입니다. 그런데 장점만 있을까요? 동네 카페 사장님에게도 DBMS가 꼭 필요할까요?',
 pair=(('연구실에서는','창고(데이터)와 손님(응용 프로그램) 사이에 <b>관리인</b>을 한 명 둔 것과 같습니다. 손님은 관리인에게만 말하고, 관리인이 꺼내고·넣고·규칙을 지키게 합니다.'),
       ('DBMS로는','<b>정의</b>(구조를 만들고 바꿈, DDL) · <b>조작</b>(넣고·찾고·고치고·지움, DML) · <b>제어</b>(무결성·보안·동시성·회복, DCL) 세 기능을 합니다.')),
 panel='''<div class="two"><div><p class="ptitle" style="color:#13733a">장점 8</p><ol style="margin:0;padding-left:20px;font-size:15px"><li>데이터 중복 통제</li><li>데이터 독립성 확보</li><li>데이터 동시 공유</li><li>데이터 보안 향상</li><li>데이터 무결성 유지</li><li>표준화</li><li>장애 시 회복</li><li>응용 프로그램 개발 비용 절감</li></ol></div>
<div><p class="ptitle" style="color:#c9302c">단점 3</p><ol style="margin:0;padding-left:20px;font-size:15px"><li>비용 (구입·운영·전문 인력)</li><li>백업과 회복 방법이 복잡</li><li>중앙 관리로 인한 취약점 (한 곳이 멈추면 모두 멈춤)</li></ol></div></div>
<h3>네 세대 — 눌러서 보기</h3><div class="chips" id="gen3"></div><div class="insight" id="gen3o"></div>''',
 panel_title='한눈에 — 장단점과 세대',
 sim='DBMS 세대 연표',
 explain='<p>세대가 바뀐 이유를 한 줄씩 기억하면 외울 것이 줄어듭니다. 계층·네트워크형은 <b>데이터를 포인터로 줄줄이 연결</b>해 구조를 바꾸기 어려웠고, 관계형은 이것을 <b>표(테이블)와 값</b>으로 바꿨습니다(6주차). 객체지향·객체관계형은 사진·도면 같은 <b>복합 객체</b>를 담으려 했고, NoSQL·NewSQL은 SNS의 해시태그처럼 <b>비정형·대용량(3V)</b> 데이터를 빠르게 다루려고 나왔습니다(14주차).</p>',
 limit='DBMS가 “데이터 독립성”을 준다고 했습니다. 정확히 어떤 구조 덕분일까요? 4주차의 3단계 스키마가 그 답입니다.', limit_label='데이터 독립성을 만드는 내부 구조를 아직 모름',
 quiz=[dict(q='DBMS의 주요 기능 세 가지가 바르게 묶인 것은?',o=['정의·조작·제어','입력·출력·저장','검색·정렬·인쇄','백업·압축·암호화'],a=0,why='정의(DDL), 조작(DML), 제어(DCL) 기능입니다.'),
       dict(q='다음 중 DBMS의 단점에 해당하는 것은?',o=['데이터 무결성 유지','표준화','중앙 관리로 인한 취약점','데이터 동시 공유'],a=2,why='모든 데이터가 한 시스템에 모이므로 그 시스템이 멈추면 모두 영향을 받습니다. 나머지는 장점입니다.')]),
],
duel=dict(q='엑셀 파일 vs DBMS — 어느 쪽이 더 싸게 먹힐까?',
 intro='초파리는 “간단한 엑셀 파일 몇 개”, 주판봇은 “제대로 된 DBMS”를 고릅니다. 1년 동안 드는 비용(도입·운영 + 불일치 수습)을 <b>설명용 비용 모형</b>으로 비교합니다. 가게 규모라는 <b>가정</b>을 바꿔 보세요.',
 fly_pick='엑셀 파일 몇 개로 버티기', fly_line='손님 50명짜리 카페에 서버까지? 파일 두 개면 충분해.',
 robo_pick='DBMS 도입', robo_line='제대로 된 시스템이 최고지! 규모가 크든 작든 DBMS!',
 metric='연간 총비용 (설명용 단위, 적을수록 이김)', higher=False, step=3,
 after='<div class="ctrl"><button type="button" class="bt" id="asA" aria-pressed="true">가정 A — 손님 50명 동네 카페</button><button type="button" class="bt" id="asB" aria-pressed="false">가정 B — 고객 5만 명 쇼핑몰</button></div><div id="costT"></div><p class="cvcap">비용 모형(설명용): 파일 = 복사본 수 × 연간 변경 수 × 누락률 5% × 수습비 + 파일 관리 인건비 / DBMS = 도입·운영 고정비 + 사용량 비례 운영비. 수치는 개념을 보여 주기 위한 예시값입니다.</p>',
 run='return PAGE.duel();',
 announce='return "가정 A(카페): 초파리 <b>"+r.a[0]+"</b> vs 주판봇 <b>"+r.a[1]+"</b> · 가정 B(쇼핑몰): 초파리 <b>"+r.b[0].toLocaleString()+"</b> vs 주판봇 <b>"+r.b[1].toLocaleString()+"</b> (설명용 단위)";',
 verdict='return "작은 카페면 파일이, 큰 쇼핑몰이면 DBMS가 싸다. DBMS의 단점 1번(비용)은 규모가 작을 때 진짜 단점이다. 조건부 판정.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>핵심</th><th>한 줄 답</th></tr></thead><tbody>
<tr><td>1 중복</td><td>같은 사실이 여러 파일에 → 불일치</td><td>통합 저장 + 제약</td></tr>
<tr><td>2 종속</td><td>프로그램이 파일 생김새를 외움 → 형식 변경 시 모두 수정</td><td>데이터 독립성</td></tr>
<tr><td>3 회복</td><td>도중 실패 시 어중간한 값</td><td>트랜잭션 + 롤백</td></tr>
<tr><td>4 DBMS</td><td>중복·종속 문제를 해결하는 시스템, 정의·조작·제어</td><td>장점 8 · 단점 3 · 4세대</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 관리인</b> 관리인은 한 명이지만 실제 DBMS는 여러 요청을 동시에 처리하고, 관리인 자신이 멈추는 상황(중앙 관리 취약점)까지 대비해야 합니다.</div><div><b>대결의 한계</b> 비용 모형의 숫자는 개념용 예시입니다. 실제 판단에는 클라우드 요금, 인력, 보안 요구까지 따져야 합니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 중복은 통제해야 한다 ② 프로그램과 데이터를 떼어 놓아야 한다 ③ 실패하면 되돌릴 수 있어야 한다 — 이 셋을 하는 것이 DBMS.'),
       ('asst','report','대결은 조건부였어요. 손님 50명이면 파일, 5만 명이면 DBMS가 쌌어요.'),
       ('fly','coffee','규모를 안 보고 “무조건 DBMS”는 반쪽짜리 답이야. 비용도 단점 목록에 있잖아.'),
       ('robo','calc','흠… 작은 가게엔 작은 도구. 그래도 가게가 커지면 나를 불러 줘!')],
next_note='<p class="recap"><b>다음 회차 — 4주차 「데이터베이스 시스템」:</b> 외부·개념·내부 3단계 스키마와 데이터 독립성, 데이터 사전, 사용자와 언어.</p>',
gloss={'데이터 중복':('데이터 중복','개념','같은 데이터가 여러 곳에 저장된 상태. 통제되지 않으면 불일치를 낳습니다.','data-redundancy','lv1'),
 '불일치':('데이터 불일치','개념','중복 저장된 같은 데이터가 서로 다른 값을 갖는 상태.','inconsistency','lv1'),
 '종속성':('데이터 종속성','개념','응용 프로그램이 파일의 구성 방법과 물리적 저장 구조에 맞춰 작성되는 성질.','data-dependency','lv2'),
 '롤백':('롤백','명령어','업데이트 오류 시 이전 상태로 되돌리는 것. 후진 복귀.','rollback','lv3'),
 '트랜잭션':('트랜잭션','개념','함께 성공하거나 함께 취소되어야 하는 작업 묶음. 13주차에 자세히.','transaction','lv3'),
 '저널':('저널(로그) 파일','용어','업데이트 이전·이후 값을 기록해 회복에 쓰는 파일.','journal-log','lv3'),
 'DDL':('DDL','용어','데이터 정의어. CREATE, ALTER, DROP처럼 구조를 정의하는 SQL.','ddl','lv4'),
 'DML':('DML','용어','데이터 조작어. SELECT, INSERT, UPDATE, DELETE.','dml','lv4'),
 'DCL':('DCL','용어','데이터 제어어. GRANT, REVOKE처럼 권한 등을 제어하는 SQL.','dcl','lv4'),
 'NoSQL':('NoSQL','용어','표 구조에 얽매이지 않고 문서·키-값·그래프 등으로 대용량·비정형 데이터를 다루는 DBMS 계열.','nosql','lv4')},
facts=[('F01','DBMS는 파일 시스템의 데이터 중복과 데이터 종속 문제를 해결하는 시스템','문헌 사실','kim3ed','lv4','2장 (교안 인용)'),
       ('F02','DBMS의 주요 기능은 정의·조작·제어','문헌 사실','kim3ed','lv4','2장'),
       ('F03','DBMS 장점 8가지(중복 통제, 독립성, 동시 공유, 보안, 무결성, 표준화, 회복, 개발비 절감)와 단점 3가지(비용, 복잡한 백업·회복, 중앙 관리 취약점)','문헌 사실','ahn2025w03','lv4','3주차 교안'),
       ('F04','롤백은 업데이트 오류 시 업데이트 이전 저널 파일로 이전 상태로 되돌리는 것','문헌 사실','ahn2025w03','lv3','3주차 교안 등장 배경 3'),
       ('F05','응용 프로그램이 파일의 구성 방법과 물리적 저장 구조에 맞게 작성됨(종속)','문헌 사실','kim3ed','lv2','2장 (교안 43쪽 인용)')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='ahn2025w03',type='report',title='데이터베이스설계 3주차 강의 교안: 데이터베이스 관리 시스템',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025rpg',type='report',title='RPG 용사의 전설 — 데이터베이스 설계자의 실무 프로젝트 가이드',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='background',note='파일 시스템의 한계 분석 사례')],
models=['부서별 파일 주소 갱신 실험 (모의)','형식 변경 파급 표 (설명용 예)','account 테이블 잔액 (예시값)','엑셀 vs DBMS 비용 모형 (설명용 예시값, 실제 가격 아님)'],
cover_alt='부서별 서류철 네 개에 같은 주소가 다르게 적혀 있고, 가운데 하나의 금고로 화살표가 모이는 장면 (대체 그림)',
prereq=['02'],
js=r'''
var $=LAB.$,$$=LAB.$$;
/* 칸1 */
var DEPT=['영업부','마케팅부','서비스부','물류팀'],up=[1,0,0,0];
function d3(){$('#f3').innerHTML=DEPT.map(function(d,i){return '<button type="button" class="bt" data-i="'+i+'" aria-pressed="'+(!!up[i])+'">'+d+' 파일 고치기</button>';}).join('');
 $$('#f3 button').forEach(function(b){b.onclick=function(){up[+b.dataset.i]=1-up[+b.dataset.i];d3();};});
 $('#f3t').innerHTML=LAB.tableHTML(['파일','고객','주소'],DEPT.map(function(d,i){return [d+' 고객.xls','김철수',up[i]?'부산시 해운대구 (새 주소)':'서울시 마포구 (옛 주소)'];}),{cls:function(r){return /옛/.test(r[2])?'bad':'hl';}});}
$('#f3go').onclick=function(){var n=up.reduce(function(a,b){return a+b;},0),dist=new Set(up).size;
 $('#f3o').innerHTML=(up[3]?'택배는 <b>새 주소</b>로 갔습니다. ':'택배는 <b style="color:#c9302c">옛 주소</b>로 갔습니다 — 물류팀 파일을 안 고쳤으니까요. ')+'고친 파일 '+n+'/4 · 서로 다른 주소 '+dist+'가지'+(dist>1?' → 회사 안에 “정답”이 둘 있습니다.':' → 모두 같습니다(이번엔 성공).');};
$('#f3r').onclick=function(){up=[1,0,0,0];d3();$('#f3o').textContent='고칠 파일을 고르세요. (물류팀 파일이 실제 배송 주소로 쓰입니다)';};
d3();
/* 칸2 */
var CH=[['이름과 주소 사이에 이메일 칸 끼워 넣기',['청구서 출력','배송 라벨','고객 통계'],[0]],['주소 칸 길이를 30자→60자로 늘리기',['청구서 출력','배송 라벨'],[0]],['파일을 고정 길이 → 쉼표 구분(CSV)으로 바꾸기',['청구서 출력','배송 라벨','고객 통계'],[0]],['저장 위치를 다른 디스크로 옮기기',['청구서 출력','배송 라벨','고객 통계'],[0]]];
var dc=$('#dep3');CH.forEach(function(c,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=c[0];b.onclick=function(){[].forEach.call(dc.children,function(x){x.setAttribute('aria-pressed',x===b);});
 $('#depF').innerHTML='<p class="ptitle" style="color:#c9302c">파일 시스템 — 고칠 프로그램 '+c[1].length+'개</p>'+c[1].map(function(p){return '<span class="pill no">'+p+'</span>';}).join('');
 $('#depD').innerHTML='<p class="ptitle" style="color:#13733a">DBMS — 고칠 프로그램 0개</p><span class="pill ok">DBMS가 대응 관계(사상)만 고침</span>';
 $('#depO').innerHTML='파일 시스템에서는 형식을 아는 프로그램 <b>'+c[1].length+'개</b>를 모두 열어 고쳐야 합니다. DBMS에서는 프로그램이 칸 이름으로만 요청하므로 그대로 둡니다. (단, 새 칸을 실제로 <i>쓰려는</i> 프로그램은 고쳐야 합니다.)';};dc.appendChild(b);});
dc.children[0].click();
/* 칸4 세대 */
var G=[['1세대 · 네트워크/계층 DBMS','1960~70년대','데이터를 부모-자식 트리(계층)나 그물(네트워크)처럼 포인터로 연결. 빠르지만 구조를 바꾸기 어렵고, 찾는 경로를 프로그램이 알아야 함.'],['2세대 · 관계 DBMS','1970년대 이론(코드, 1970) → 80년대 이후 확산','데이터를 표(릴레이션)와 값으로 표현하고 SQL로 질의. MariaDB·PostgreSQL·Oracle 등 지금 실습하는 DBMS.'],['3세대 · 객체지향/객체관계 DBMS','1980~90년대','도면·멀티미디어 같은 복합 객체를 담기 위해 객체 개념을 도입하거나(객체지향), 관계형에 객체 기능을 더함(객체관계).'],['4세대 · NoSQL / NewSQL','2000년대 후반 이후','SNS·로그 같은 비정형·대용량(3V) 데이터를 위해 표 구조를 완화(NoSQL), 또는 관계형의 일관성을 유지하며 확장성을 높임(NewSQL). 14주차.']];
var gc=$('#gen3');G.forEach(function(g,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=g[0].split(' · ')[0];b.onclick=function(){[].forEach.call(gc.children,function(x){x.setAttribute('aria-pressed',x===b);});$('#gen3o').innerHTML='<b>'+g[0]+'</b> <span style="color:#5b6874">('+g[1]+')</span><br>'+g[2];};gc.appendChild(b);});
gc.children[1].click();
/* 대결 */
var as='A';
function cost(sc){var copies=sc==='A'?2:6,changes=sc==='A'?40:20000,fix=sc==='A'?5:3,manual=sc==='A'?30:2400;
 var file=Math.round(copies*changes*0.05*fix+manual),db=Math.round(sc==='A'?600:3000+changes*0.02);return [file,db];}
function tbl(){var a=cost('A'),b=cost('B');$('#costT').innerHTML=LAB.tableHTML(['가정','엑셀 파일 (초파리)','DBMS (주판봇)'],[['A 동네 카페',a[0],a[1]],['B 쇼핑몰',b[0].toLocaleString(),b[1].toLocaleString()]],{cls:function(r){return (r[0][0]===as)?'hl':'dim';}});}
$('#asA').onclick=function(){as='A';$('#asA').setAttribute('aria-pressed','true');$('#asB').setAttribute('aria-pressed','false');tbl();};
$('#asB').onclick=function(){as='B';$('#asB').setAttribute('aria-pressed','true');$('#asA').setAttribute('aria-pressed','false');tbl();};
tbl();
PAGE.duel=function(){var a=cost('A'),b=cost('B'),cur=as==='A'?a:b;return {fly:cur[0],robo:cur[1],flyTxt:cur[0].toLocaleString(),roboTxt:cur[1].toLocaleString(),cond:true,a:a,b:b};};
''',
labs='''lab3:{setup:"CREATE DATABASE bank; USE bank; CREATE TABLE account (acc_id CHAR(1) PRIMARY KEY, owner VARCHAR(20), balance INT, CONSTRAINT chk_balance CHECK (balance >= 0)); INSERT INTO account VALUES ('A','김하나',30000),('B','이두리',5000);",
presets:[{t:"① 잔액 보기",q:"SELECT * FROM account;"},{t:"② 실패하는 이체 (롤백 없이)",q:"-- A에서 10,000원 빼기 (성공)\\nUPDATE account SET balance = balance - 10000 WHERE acc_id = 'A';\\n-- B에 넣다가 실수로 -100,000을 넣어 규칙 위반 (실패)\\nUPDATE account SET balance = balance - 100000 WHERE acc_id = 'B';"},{t:"③ 트랜잭션으로 묶고 롤백",q:"START TRANSACTION;\\nUPDATE account SET balance = balance - 10000 WHERE acc_id = 'A';\\nUPDATE account SET balance = balance - 100000 WHERE acc_id = 'B';"},{t:"③-2 실패했으니 되돌리기",q:"ROLLBACK;\\nSELECT * FROM account;"},{t:"④ 합계 확인",q:"SELECT SUM(balance) AS 합계 FROM account;"}],
ready:"bank 데이터베이스에 A(30,000원)·B(5,000원) 계좌가 있습니다. ②를 실행한 뒤 ④로 합계를 보고, 「처음 상태로」→ ③ → ③-2 → ④ 순서로 비교하세요."}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'같은 데이터가 여러 파일에 저장되어, 통제하지 않으면 값이 서로 달라지는 문제.','lv2':'응용 프로그램이 파일의 구성과 물리적 저장 구조에 맞춰 작성되어, 구조가 바뀌면 프로그램도 고쳐야 하는 성질.','lv3':'업데이트 도중 오류가 나면 이전 기록(저널)으로 시작 전 상태로 되돌리는 것.','lv4':'파일 시스템의 데이터 중복과 종속 문제를 해결하는 시스템. 정의·조작·제어 기능을 가진다.'}[s['id']]
