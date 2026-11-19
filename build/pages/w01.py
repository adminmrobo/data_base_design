# 1주차 — 과목 사용 설명서 · 생활 속 데이터베이스 · 실습 환경
PAGE = dict(
num='01', slug='course_guide', kind='lecture', short='1주', chip='01주차',
title='과목 사용 설명서', title_en='Course guide and everyday databases',
subtitle='생활 속 데이터베이스에서 실습 환경까지',
toc='편의점 계산대에서 출발해, 엑셀과 DB의 차이·실습 도구·15주 지도를 한 번에',
kicker='데이터베이스 설계 · 1주차 · 오리엔테이션',
question='오늘 아침부터 지금까지, 나는 몇 개의 데이터베이스를 지나왔을까?',
desc='데이터베이스 설계 1주차: 생활 속 데이터베이스, 스프레드시트와의 차이, 실습 도구(MariaDB·PostgreSQL·Orange), 15주 강의 지도.',
intro='<p>교통카드를 찍고, 편의점에서 삼각김밥을 사고, 학교 포털에서 시간표를 열었다면 이미 데이터베이스를 세 번 이상 썼습니다. 이 과목은 그 뒤편에서 <b>데이터를 어떤 모양으로 담아야 틀리지 않고 빨리 꺼낼 수 있는지</b>를 배웁니다. 1주차는 수강을 계속할지 판단할 수 있도록, 과목 전체를 미리 한 번 걸어 보는 튜토리얼입니다.</p>',
kpis=[('15회차','본강의 13 + 중간·기말 리뷰 2'),('4줄','오늘 처음 실행해 볼 SQL'),('3306 · 5432','MariaDB · PostgreSQL 문 번호(포트)'),('10/40/40/10','출석·중간·기말·과제 비율(%)')],
kpi_note='평가 비율은 2025-2학기 강의 개요(노션) 기준입니다. 시험 날짜는 학사 일정에 따라 바뀔 수 있습니다.',
hero_talk=[
 ('doc','front','오늘은 수업이 아니라 <b>지도 보기</b>다. 15주 동안 어디를 지나 어디에 도착하는지부터 보자.'),
 ('asst','smile','저는 엑셀로도 충분하다고 생각했는데요… 데이터베이스는 뭐가 다른 거예요?'),
 ('fly','clip','그 질문 좋다. 오늘 끝날 때 <b>“엑셀로는 안 되는 순간”</b>을 하나는 말할 수 있어야 해.'),
 ('robo','smile','데이터는 많을수록 좋지! 행이 백만 개면 기분도 백만 배야!')],
crew=[('doc','front','설명하고 판정하는 연구실 책임자'),('asst','smile','초보의 눈으로 묻고, 숫자를 발표'),('fly','clip','“정말?” 하고 의심해서 함정을 짚음'),('robo','smile','크고 많은 것을 좋아하는 확신파')],
recap='처음이라 복습할 것은 없습니다. 대신 하나만 기억하세요 — <b>데이터베이스 = 여러 사람이 함께 쓰려고, 한 곳에 정리해 둔 데이터 모음</b>. 이 문장이 2주차의 출발점입니다.',
notion=[('데이터베이스설계 (2025년 2학기) 강의 개요', NOTION+'2025-2-1ab17a4520ed81cd9040dbae826a48ad', '주차별 진도·평가 방법·교재 — 강의의 원본 안내 페이지'),
        ('01주차 : 과목사용설명서', NOTION+'1ab17a4520ed812cbdc0cc6ed9dec211', '강의 영상, pandas 참고, 활용 툴(Orange) 링크'),
        ('데이터베이스 설계사례 (업종별)', NOTION+'1ab17a4520ed81cc9c8ad60616c2e1de', '아래 4칸의 업종별 설계 표 원본')],
why=[('어디에나 있다','은행 이체, 택배 조회, 수강 신청, 게임 아이템까지 — 화면 뒤에는 거의 늘 데이터베이스가 있습니다.'),
     ('틀리면 비싸다','주소 하나가 두 곳에 다르게 저장되면 택배가 옛집으로 갑니다. 설계는 이런 실수를 구조로 막는 일입니다.'),
     ('AI 시대에 더 중요해졌다','생성 AI가 SQL을 대신 써 줘도, 테이블을 어떻게 나눌지와 결과가 맞는지 판단하는 일은 사람에게 남습니다.')],
bigpicture='''<h3>15회차 지도 — 이 과목이 가는 길</h3>
<div class="flow"><span class="chip">1 오리엔테이션</span><span class="arr">→</span><span class="chip">2 데이터와 DB</span><span class="arr">→</span><span class="chip">3 DBMS</span><span class="arr">→</span><span class="chip">4 DB 시스템</span><span class="arr">→</span><span class="chip">5 E-R 모델링</span><span class="arr">→</span><span class="chip">6 관계 모델</span><span class="arr">→</span><span class="chip">7 관계 연산</span><span class="arr">→</span><span class="chip" style="background:#e7f5ec">8 중간 REVIEW</span></div>
<div class="flow"><span class="chip">9 SQL ① 정의</span><span class="arr">→</span><span class="chip">10 SQL ② 조작·조인</span><span class="arr">→</span><span class="chip">11 설계 5단계</span><span class="arr">→</span><span class="chip">12 정규화</span><span class="arr">→</span><span class="chip">13 트랜잭션·회복</span><span class="arr">→</span><span class="chip">14 응용 기술</span><span class="arr">→</span><span class="chip" style="background:#e7f5ec">15 기말 REVIEW</span></div>
<p>앞 절반(2~7주)은 <b>“왜 이런 구조인가”</b>, 뒤 절반(9~14주)은 <b>“직접 만들고 고치기”</b>입니다. 교재는 김연희, 『데이터베이스 개론』(3판)이고 2주차가 1장, 3주차가 2장 … 순서로 한 장씩 나아갑니다.</p>
<div class="tbl"><table><thead><tr><th>평가 항목</th><th>비율</th><th>방식 (강의 개요 기준)</th></tr></thead><tbody>
<tr><td>출석</td><td>10%</td><td>대면 호명. 비대면 회차는 영상 수강 + 출결 과제</td></tr>
<tr><td>중간고사</td><td>40%</td><td>강의에서 다룬 개념·사례의 객관식·단답식, 대면 원칙</td></tr>
<tr><td>기말고사</td><td>40%</td><td>같은 방식. 시험 뒤 답안 배포, 개별 성적 확인</td></tr>
<tr><td>과제</td><td>10%</td><td>모두 개인 과제 (팀 과제 없음)</td></tr></tbody></table></div>''',
why_say=('fly','point','시험이 객관식·단답식이라고 외우기만 하면 곤란해. 문제는 늘 <b>“이 상황이면 어떻게 되나”</b>로 나오거든.'),
steps=[
dict(id='lv1', short='생활 속 DB', title='생활 속 데이터베이스 — 계산대 뒤에서 일어나는 일', concept='데이터베이스', en='database in everyday life', cid='lab:concept/database',
 def_='', tag='현장: 편의점 계산대', analogy='편의점 계산대',
 situation='편의점에서 삼각김밥 바코드를 찍었습니다. 0.3초 만에 이름과 가격이 뜨고, 영수증이 나오고, 본사 재고가 하나 줄었습니다. 이 짧은 순간에 누가 무엇을 찾아본 걸까요?',
 pair=(('현장에서는','계산대는 바코드 번호로 <b>상품 목록</b>을 찾아 가격을 읽고, <b>판매 기록</b>에 한 줄을 쓰고, <b>재고</b>에서 1을 뺍니다. 점원은 셋 중 아무것도 직접 고치지 않습니다.'),
       ('데이터베이스에서는','상품·판매·재고는 각각 <b>테이블</b>(표)입니다. 프로그램은 “이 번호의 가격을 달라”고 <b>질의</b>하고, “판매 한 줄 추가”를 요청합니다. 여러 계산대가 동시에 요청해도 값이 꼬이지 않게 DBMS가 순서를 정리합니다.')),
 panel='''<p style="margin-top:0">오늘 하루 지나온 곳을 눌러 보세요. 그 뒤에서 어떤 테이블이 쓰였는지 나옵니다.</p>
<div class="chips" id="dayChips"></div><div class="insight" id="dayOut">하나를 눌러 보세요.</div>
<div class="kpis" style="grid-template-columns:repeat(3,1fr)"><div><b id="dayN">0</b><span>오늘 만난 DB</span></div><div><b id="dayT">0</b><span>쓰인 테이블(추정)</span></div><div><b id="dayW">0</b><span>내가 쓴 행(추정)</span></div></div>''',
 panel_title='직접 해 보기 — 오늘 내가 지나온 데이터베이스',
 sim='오늘 지나온 데이터베이스 세기',
 flow=dict(id='fl1', title='바코드 한 번에 일어나는 세 가지 일', h=230, alt='상품 카드가 상품 조회, 판매 기록, 재고 감소 단계를 차례로 지나가는 애니메이션',
   cap='상품 카드(나르미)가 왼쪽에서 오른쪽으로 지나가며 바뀝니다. 마지막 칸에서 재고가 0이 되면 빨갛게 표시됩니다 — 이것이 “품절” 알림이 뜨는 순간입니다.',
   js='{stations:["바코드 찍기","상품 조회","판매 기록 +1줄","재고 −1"],items:[["8801-0001","삼각김밥 1,500원","판매#1041","재고 12→11"],["8801-0042","생수 900원","판매#1042","재고 3→2"],["8801-0077","컵라면 1,300원","판매#1043","재고 1→0"],["8801-0109","우유 1,800원","판매#1044","재고 25→24"]],bad:function(it,i){return i===3&&/→0/.test(it[3]);},stamp:"설명용 모형 · 실제 매장 데이터 아님"}'),
 explain='<p>① 바코드는 <b>열쇠(키)</b>입니다. 같은 번호는 세상에 하나뿐이라 그 번호로 상품 한 줄을 정확히 찾습니다. ② 찾기(조회)와 쓰기(기록)는 다른 일입니다. 데이터베이스는 둘 다 맡습니다. ③ 재고처럼 <b>여러 계산대가 동시에 고치는 값</b>이 가장 위험합니다. 13주차 트랜잭션에서 다시 만납니다.</p>',
 limit='여기까지는 “표에 담아 두고 찾는다”뿐입니다. 그렇다면 엑셀 한 장과 무엇이 다를까요? 다음 칸에서 엑셀이 무너지는 순간을 직접 봅니다.', limit_label='표에 담는 것만으로는 엑셀과 구분되지 않음',
 say=('asst','spark','삼각김밥 하나에 테이블이 세 개나 움직였네요! 앞으로 영수증이 다르게 보일 것 같아요.'),
 quiz=[dict(q='편의점 계산대가 바코드 번호로 상품 가격을 찾는 일은 데이터베이스의 어떤 작업에 가장 가깝나요?',o=['데이터 삭제','데이터 조회(검색)','테이블 구조 변경','백업'],a=1,why='번호로 한 줄을 찾아 값을 읽는 일은 조회입니다. 판매 기록을 남기는 것은 삽입, 재고를 줄이는 것은 수정입니다.'),
       dict(q='여러 계산대가 동시에 같은 상품을 팔 때 가장 먼저 값이 꼬일 위험이 큰 것은?',o=['상품 이름','바코드 번호','재고 수량','매장 주소'],a=2,why='재고는 여러 곳에서 동시에 빼는 값이라, 순서를 관리하지 않으면 “둘 다 12에서 1을 빼서 11”이 되는 일이 생깁니다(13주차).')]),
dict(id='lv2', short='엑셀 vs DB', title='엑셀과 데이터베이스 — 같은 표인데 무엇이 다른가', concept='스프레드시트와 데이터베이스의 차이', en='spreadsheet versus database', cid='lab:concept/spreadsheet-vs-database',
 tag='현장: 동아리 회원 명부', analogy='동아리 회원 명부 엑셀',
 situation='동아리 회원 명부 엑셀을 회장·총무·홍보 담당이 각자 내려받아 고쳤습니다. 한 달 뒤, 같은 회원의 전화번호가 세 파일에서 모두 다릅니다. 누구 파일이 맞을까요?',
 pair=(('현장에서는','파일을 복사해 나눠 가진 순간, 같은 사실(전화번호)이 <b>세 군데에 따로</b> 저장됩니다. 한 곳만 고치면 나머지는 옛값으로 남습니다.'),
       ('데이터베이스에서는','명부는 <b>한 곳에만</b> 있고, 세 사람은 그 한 곳에 접속해 읽고 고칩니다. “전화번호 칸은 비우면 안 된다” 같은 <b>규칙</b>도 DB가 대신 지킵니다.')),
 panel='''<p style="margin-top:0">세 명이 같은 회원의 전화번호를 각자 고칩니다. 방식을 바꿔 가며 「한 달 보내기」를 눌러 보세요.</p>
<div class="ctrl"><button type="button" class="bt" id="m2x" aria-pressed="true">엑셀 파일 3개로 나눠 쓰기</button><button type="button" class="bt" id="m2d" aria-pressed="false">데이터베이스 한 곳에 접속</button><button type="button" class="bt primary" id="m2go">한 달 보내기</button><button type="button" class="bt" id="m2r">처음으로</button></div>
<div id="m2tab"></div><div class="kpis" style="grid-template-columns:repeat(3,1fr)"><div><b id="m2v">1</b><span>서로 다른 전화번호 개수</span></div><div><b id="m2e">0</b><span>고친 횟수</span></div><div><b id="m2b">0</b><span>규칙 위반으로 막힌 입력</span></div></div><div class="insight" id="m2i"></div>''',
 panel_title='직접 해 보기 — 복사본 세 개 vs 한 곳',
 sim='복사본과 단일 저장소 비교',
 explain='<p>엑셀이 나쁜 도구라서가 아닙니다. 혼자, 작은 표를, 한 번 쓰고 버릴 때는 엑셀이 더 빠릅니다. 문제는 <b>여러 사람</b>이 <b>오래</b> <b>같은 사실</b>을 고칠 때 생깁니다. 데이터베이스는 이 세 조건에서 강해지도록 만든 도구입니다.</p><div class="tbl"><table><thead><tr><th>상황</th><th>엑셀 파일</th><th>데이터베이스</th></tr></thead><tbody><tr><td>여러 명이 동시에 수정</td><td>복사본이 갈라짐</td><td>한 곳을 함께 수정, 순서 관리</td></tr><tr><td>값의 규칙(빈칸 금지 등)</td><td>사람이 눈으로 확인</td><td>제약 조건으로 자동 거부</td></tr><tr><td>행이 수십만 개</td><td>느려지고 열기 어려움</td><td>필요한 줄만 질의로 꺼냄</td></tr><tr><td>실수로 지움</td><td>이전 버전 파일을 찾아야 함</td><td>트랜잭션 롤백·백업으로 복구</td></tr></tbody></table></div>',
 aicheck='<p>생성 AI에게 “엑셀이랑 DB 차이 알려줘”라고 하면 대개 <i>“엑셀은 작은 데이터, DB는 큰 데이터”</i>라고 답합니다. 반만 맞습니다. 행이 100개뿐이어도 세 명이 동시에 고치면 DB가 필요할 수 있습니다. <b>크기보다 “함께·오래·같은 사실”</b>이 기준이라는 점을 확인하세요.</p>',
 limit='한 곳에 모으면 좋다는 건 알았습니다. 그런데 그 “한 곳”을 실제로 내 컴퓨터에 세우려면 무엇이 필요할까요?', limit_label='단일 저장소를 직접 운영할 도구가 아직 없음',
 say=('fly','arms','파일이 세 개면 정답도 세 개야. 정답이 셋이면 사실상 정답이 없는 거지.'),
 quiz=[dict(q='다음 중 엑셀 파일보다 데이터베이스가 꼭 필요한 상황은?',o=['혼자 한 번 쓰고 버릴 50줄짜리 표','세 부서가 같은 고객 정보를 매일 함께 고치는 경우','발표용 그래프 한 장 만들기','개인 가계부'],a=1,why='여러 사람·오래·같은 사실을 고치는 조건이 겹칠 때 데이터베이스의 장점이 커집니다.'),
       dict(q='위 실험에서 “서로 다른 전화번호 개수”가 3이 되었다는 것은 무엇을 뜻하나요?',o=['데이터가 늘어서 좋다','같은 사실이 세 가지로 갈라져 어느 것이 맞는지 모른다','DB가 고장 났다','전화번호가 원래 세 개다'],a=1,why='같은 사실이 여러 곳에 따로 저장되어 서로 달라진 상태를 데이터 불일치라고 부릅니다(3주차에서 정식으로 배웁니다).')]),
dict(id='lv3', short='실습 도구', title='실습 도구 지도 — 창고 둘, 작업대 하나, 그리고 첫 SQL', concept='DBMS 실습 환경', en='DBMS practice environment', cid='lab:concept/dbms-practice-environment',
 tag='연구실: 실습 책상', analogy='창고와 작업대',
 situation='이 과목의 SQL 실습은 MariaDB에서 합니다. 그런데 설치는 다음 주까지 해 오면 됩니다. 오늘은 설치 없이, 이 페이지 안의 작은 실습실에서 첫 SQL 네 줄을 실행해 봅니다.',
 pair=(('연구실에서는','데이터를 보관하는 <b>창고</b>(MariaDB, PostgreSQL)가 있고, 꺼낸 데이터를 펼쳐 보는 <b>작업대</b>(Orange, 파이썬 pandas)가 있습니다. 창고마다 문 번호(포트)가 달라 3306, 5432로 구분합니다.'),
       ('DBMS에서는','MariaDB·PostgreSQL은 <b>DBMS</b>(데이터베이스 관리 시스템)입니다. 우리는 SQL이라는 표준 언어로 “만들어라·넣어라·찾아라”를 요청하고, DBMS가 실제 파일을 다룹니다.')),
 body='''<div class="tbl"><table><thead><tr><th>도구</th><th>역할</th><th>이 과목에서 쓰는 곳</th></tr></thead><tbody>
<tr><td>MariaDB (포트 3306)</td><td>관계형 DBMS. MySQL에서 갈라져 나와 명령이 거의 같음</td><td>9·10·13주 SQL 실습의 기본 창고</td></tr>
<tr><td>PostgreSQL (포트 5432)</td><td>관계형 DBMS. 표준 SQL을 엄격하게 따름</td><td>비교 실습, 14주 응용</td></tr>
<tr><td>Orange</td><td>코드 없이 아이콘을 이어 데이터를 보는 분석 작업대</td><td>2주차 데이터 분류, 14주 응용</td></tr>
<tr><td>파이썬 pandas</td><td>표(데이터프레임)를 코드로 다루는 도구</td><td>2주차 실습, “DB와 무엇이 다른가” 비교</td></tr></tbody></table></div>
<div class="notion"><span class="nb">G</span><a href="https://adminmrobo.github.io/how_to_start_db/" target="_blank" rel="noopener">초보자도 쉽게 따라하는 DB 환경 설치 ↗</a><span>MariaDB → PostgreSQL → Orange 순서로 설치하고 접속까지 확인하는 연구실 해설 (Windows 기준)</span></div>''',
 panel='<div class="sqllab" id="lab1" data-lab="lab1"></div><p class="cvcap">순서대로 ① → ④ 버튼을 눌러 보세요. 실제 MariaDB에 그대로 붙여 넣어도 같은 결과가 나오도록 썼습니다.</p>',
 panel_title='SQL 실습실 — 설치 없이 첫 네 줄',
 sim='첫 SQL 실습실',
 explain='<p>① <code>CREATE DATABASE</code> — 창고 안에 방을 하나 만든다. ② <code>USE</code> — 그 방에 들어간다. ③ <code>CREATE TABLE</code> — 칸 이름과 종류를 정해 빈 표를 만든다. ④ <code>INSERT</code>·<code>SELECT</code> — 줄을 넣고 꺼내 본다. 문장 끝의 세미콜론(<code>;</code>)은 “여기까지가 한 문장”이라는 표시입니다.</p>',
 aicheck='<p>④번을 실행하면 <code>3 rows in set</code>이 나옵니다. 생성 AI가 써 준 SQL을 실행했을 때도 <b>“행 수가 예상과 같은가?”</b>를 먼저 보세요. 넣은 줄이 3개인데 4줄이 나오면 어딘가 중복이 있다는 신호입니다.</p>',
 limit='도구는 갖췄습니다. 하지만 같은 MariaDB로도 엉망인 표를 만들 수 있습니다. 표를 “잘” 나누는 기준은 무엇일까요?', limit_label='도구만으로는 좋은 구조가 보장되지 않음',
 say=('robo','happy','오! <code>SELECT *</code> 한 줄이면 다 나와! 별표(*)는 “전부”라는 뜻이지? 마음에 들어!'),
 quiz=[dict(q='MariaDB를 기본 포트로 설치했을 때 접속할 문 번호(포트)는?',o=['80','3306','5432','8080'],a=1,why='MariaDB(MySQL 계열)의 기본 포트는 3306, PostgreSQL은 5432입니다. 두 DBMS를 함께 설치해도 포트가 달라 충돌하지 않습니다.'),
       dict(q='SQL 문장 <code>USE shop;</code>이 하는 일은?',o=['shop 테이블을 지운다','shop 데이터베이스를 작업 대상으로 고른다','shop 데이터베이스를 새로 만든다','shop 표를 화면에 출력한다'],a=1,why='USE는 이후 문장들이 어느 데이터베이스(방)에서 실행될지 고르는 명령입니다. 만들기는 CREATE DATABASE입니다.')]),
dict(id='lv4', short='설계', title='왜 “설계” 과목인가 — 업종마다 다른 표의 모양', concept='데이터베이스 설계', en='database design overview', cid='lab:concept/database-design-overview',
 tag='현장: 일곱 업종', analogy='업종별 설계 사례',
 situation='한 쇼핑몰이 고객·상품·배송·판매자·주문 정보를 <b>열 19개짜리 표 하나</b>에 모두 넣었습니다(5주차 노션 “worst case”). 처음엔 편했는데, 판매자 전화번호가 바뀌자 주문 수만큼 줄을 고쳐야 했습니다.',
 pair=(('현장에서는','업종마다 “자주 바뀌는 것, 꼭 맞아야 하는 것, 많이 쌓이는 것”이 다릅니다. 은행은 무결성, 소셜 미디어는 빠른 조회와 확장성이 먼저입니다.'),
       ('설계에서는','무엇을 <b>개체</b>(고객, 상품, 주문…)로 보고, 개체끼리 어떤 <b>관계</b>로 잇고, 어디에 <b>규칙</b>을 걸지 정하는 일이 데이터베이스 설계입니다. 5·11·12주차의 중심 주제입니다.')),
 panel='''<p style="margin-top:0">업종을 고르면 주요 개체와 특별히 신경 쓸 점이 나옵니다 (노션 「데이터베이스 설계사례」 표).</p><div class="chips" id="indChips"></div><div id="indOut" class="insight"></div>''',
 panel_title='직접 해 보기 — 업종별 설계 사례 고르기',
 sim='업종별 설계 사례 탐색',
 explain='<p>설계는 정답이 하나인 계산 문제가 아니라 <b>선택</b>입니다. 다만 “같은 사실은 한 곳에만”, “한 줄은 한 가지 대상만” 같은 원칙이 있어 나쁜 선택은 분명히 가려집니다. 이 원칙을 5주차(모델링)와 12주차(정규화)에서 이름을 붙여 배웁니다.</p>',
 limit='설계 원칙을 말하려면 먼저 “데이터”와 “정보”, “데이터베이스”를 정확한 말로 정의해야 합니다 — 2주차의 일입니다.', limit_label='데이터·정보·데이터베이스의 정확한 정의가 아직 없음',
 quiz=[dict(q='노션 “worst case”처럼 고객·상품·판매자·주문을 표 하나에 모두 넣었을 때 생기는 문제로 가장 알맞은 것은?',o=['조회가 불가능해진다','판매자 정보가 바뀌면 그 판매자가 들어간 모든 줄을 고쳐야 한다','SQL을 쓸 수 없다','행이 줄어든다'],a=1,why='같은 판매자 정보가 주문 줄마다 반복 저장되므로, 한 번 바뀌면 여러 줄을 함께 고쳐야 합니다. 12주차의 “갱신 이상”입니다.'),
       dict(q='은행·금융 서비스 데이터베이스 설계에서 특히 강조되는 고려사항은?',o=['장기 데이터 보관만','높은 보안성과 데이터 무결성, 실시간 처리','시즌별 데이터 관리','이미지 검색'],a=1,why='계좌·거래 데이터는 한 원이라도 틀리면 안 되므로 보안·무결성·실시간 처리가 먼저입니다.')]),
],
duel=dict(q='회원 1만 명 중 한 명 찾기 — 몇 줄을 봐야 할까?',
 intro='회원 명부에서 회원번호로 한 명을 찾습니다. 두 사람의 찾는 방법이 다릅니다. 명부 크기를 바꿔 가며 “평균 몇 줄을 들여다봐야 하는지” 비교합니다.',
 fly_pick='번호순 명부를 반씩 접어 찾기', fly_line='번호순으로 정리돼 있으면 가운데를 펴서 앞인지 뒤인지만 보면 돼. 매번 절반이 사라지지.',
 robo_pick='처음부터 한 줄도 빠짐없이 훑기', robo_line='빠짐없이 다 보는 게 제일 확실하지! 많이 보면 든든하잖아!',
 metric='평균으로 들여다본 줄 수 (적을수록 이김)', higher=False, step=3,
 after='<div class="ctrl"><label>명부 크기 <input type="range" id="duelN" min="100" max="1000000" step="100" value="10000"></label><b id="duelNv">10,000명</b></div><p class="cvcap">평균 줄 수는 계산값입니다 — 훑기는 (N+1)/2, 반씩 접기는 log₂N에 가까운 값(정확히는 ⌈log₂(N+1)⌉번 이하).</p>',
 run='var N=+document.getElementById("duelN").value; var f=Math.ceil(Math.log2(N+1)); var r=(N+1)/2; return {fly:f,robo:r,flyTxt:f+"줄",roboTxt:r.toLocaleString()+"줄"};',
 announce='return "명부 "+(+document.getElementById("duelN").value).toLocaleString()+"명 기준 — 초파리 방식은 최대 <b>"+r.fly+"줄</b>, 주판봇 방식은 평균 <b>"+r.robo.toLocaleString()+"줄</b>을 봤어요.";',
 verdict='return "미리 정리해 둔 쪽이 이긴다. 데이터베이스는 찾기 쉽게 <b>미리 준비</b>(정렬·인덱스)해 둔다. 초파리 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>핵심 한 줄</th><th>다음 칸으로 넘어간 이유</th></tr></thead><tbody>
<tr><td>1 생활 속 DB</td><td>바코드 한 번에 조회·기록·수정이 함께 일어난다</td><td>표에 담는 것만으론 엑셀과 구분이 안 됨</td></tr>
<tr><td>2 엑셀 vs DB</td><td>여러 사람·오래·같은 사실 → 한 곳에 모아야 한다</td><td>한 곳을 세울 도구가 필요</td></tr>
<tr><td>3 실습 도구</td><td>창고(MariaDB 3306·PostgreSQL 5432)와 작업대(Orange·pandas)</td><td>도구만으론 좋은 구조가 안 나옴</td></tr>
<tr><td>4 설계</td><td>무엇을 개체로, 어떻게 잇고, 어디에 규칙을 걸지 정하는 선택</td><td>정확한 정의가 필요 → 2주차</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 ①</b> 편의점 계산대는 하나의 예일 뿐, 실제 POS 시스템은 매장 서버·본사 서버가 나뉜 더 복잡한 구조입니다.</div><div><b>비유의 한계 ②</b> “창고”는 저장만 하는 것처럼 들리지만, DBMS는 규칙 검사·동시 접근 정리·복구까지 맡는 관리자에 더 가깝습니다.</div><div><b>대결의 한계</b> 반씩 접기는 명부가 번호순으로 정리돼 있을 때만 됩니다. 정리(인덱스)를 유지하는 데에도 비용이 듭니다(14주차).</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 화면 뒤에는 데이터베이스가 있다 ② 여러 사람·오래·같은 사실이면 한 곳에 모은다 ③ 좋은 구조는 설계로 만든다.'),
       ('fly','arms','반씩 접기, 인정. 그런데 정리를 누가 유지하는지는 꼭 다시 물어볼 거야.'),
       ('robo','sigh','훑기도 확실하긴 했는데… 백만 명이면 오십만 줄이네. 다음엔 정리부터 할게.'),
       ('asst','proud','설치는 다음 주까지! 저는 MariaDB 비밀번호부터 종이에 적어 둘게요.')],
next_note='<p class="recap"><b>다음 회차 — 2주차 「데이터와 데이터베이스」:</b> 데이터와 정보는 어떻게 다른가, 무엇이 갖춰져야 “데이터베이스”라고 부르는가.</p>',
gloss={'데이터베이스':('데이터베이스','개념','여러 사람이 함께 쓰려고 한 곳에 통합해 저장·운영하는 데이터 모음. 2주차에 네 가지 조건으로 정확히 정의합니다.','database','lv1'),
 '테이블':('테이블','용어','행과 열로 이루어진 표. 관계형 데이터베이스는 데이터를 테이블에 담습니다.','table','lv1'),
 '질의':('질의(쿼리)','용어','데이터베이스에 “이런 데이터를 달라”고 요청하는 문장. SQL로 씁니다.','query','lv1'),
 'DBMS':('DBMS','용어','데이터베이스 관리 시스템. 데이터를 저장하고, 규칙을 지키게 하고, 여러 사용자의 요청을 정리하는 소프트웨어.','dbms','lv3'),
 '포트':('포트(문 번호)','용어','한 컴퓨터 안에서 프로그램을 구분하는 번호. MariaDB 3306, PostgreSQL 5432.','port','lv3'),
 'SQL':('SQL','용어','관계형 데이터베이스에 쓰는 표준 질의 언어. 9·10주차에 본격적으로 배웁니다.','sql','lv3'),
 '제약 조건':('제약 조건','용어','“비우면 안 된다”, “중복 금지”처럼 DB가 자동으로 지키게 하는 규칙.','constraint','lv2'),
 '개체':('개체(엔터티)','개념','데이터로 관리할 대상. 고객, 상품, 주문처럼 서로 구별되는 것.','entity','lv4'),
 '인덱스':('인덱스','용어','책 뒤의 찾아보기처럼, 특정 열로 빨리 찾도록 미리 정리해 둔 구조.','index','lv4')},
facts=[('F01','2025-2학기 평가 비율은 출석 10%, 중간 40%, 기말 40%, 과제 10%','문헌 사실','ahn2025syllabus','lv4','강의 개요 페이지 「성적평가」'),
       ('F02','시험은 강의에서 다룬 개념·사례의 객관식·단답식으로, 대면 원칙','문헌 사실','ahn2025syllabus','lv4','강의 개요 「시험 방식」'),
       ('F03','MariaDB 기본 포트는 3306, PostgreSQL 기본 포트는 5432','문헌 사실','ahn2026install','lv3','설치 해설 미션 1·2'),
       ('F04','업종별 설계 사례: 은행·금융은 높은 보안성·무결성·실시간 처리를 특별 고려사항으로 둠','문헌 사실','ahn2025cases','lv4','설계사례 표'),
       ('F05','교재는 김연희 『데이터베이스 개론』(3판)','문헌 사실','kim3ed','lv4','강의 교안 표지 각주')],
refs=[dict(id='ahn2025syllabus',type='webpage',title='데이터베이스설계 (2025년 2학기) 강의 개요',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'2025-2-1ab17a4520ed81cd9040dbae826a48ad',role='primary',supports=['lab:concept/database-design-overview']),
      dict(id='ahn2025cases',type='webpage',title='데이터베이스 설계사례 (업종별)',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed81cc9c8ad60616c2e1de',role='primary'),
      dict(id='ahn2026install',type='webpage',title='초보자도 쉽게 따라하는 DB 환경 설치',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2026]]},URL='https://adminmrobo.github.io/how_to_start_db/',role='background'),
      dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='background',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준')],
models=['편의점 상품·판매·재고 흐름 애니메이션 (설명용 모형)','“오늘 지나온 DB” 테이블·행 수 (추정 예시값)','복사본 3개 vs 한 곳 실험 (모의 시뮬레이션, 고정 시드)','SQL 실습실 결과 (브라우저 안 모의 실행)'],
cover_alt='낮의 연구실 책상 위 커다란 표와 바코드 스캐너를 네 캐릭터가 둘러싼 표지 (대체 그림)',
prereq=[],
js=r'''
var $=LAB.$;
/* 칸1: 오늘 지나온 DB */
var D=[['교통카드','카드 잔액·승하차 기록',2,2],['편의점','상품·판매·재고',3,2],['학교 포털','학생·수강·시간표',3,1],['메신저','사용자·대화방·메시지',3,15],['음악 앱','곡·재생목록·재생 기록',3,20],['택배 조회','송장·배송 단계',2,0],['은행 앱','계좌·거래',2,1],['배달 앱','가게·메뉴·주문·리뷰',4,3]];
var on={},C=$('#dayChips');
D.forEach(function(d,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=d[0];b.setAttribute('aria-pressed','false');
 b.onclick=function(){on[i]=!on[i];b.setAttribute('aria-pressed',on[i]);$('#dayOut').innerHTML='<b>'+d[0]+'</b> 뒤의 테이블(예): '+d[1]+' — 내가 남긴 행(예시값) '+d[3]+'줄';
 var n=0,t=0,w=0;Object.keys(on).forEach(function(k){if(on[k]){n++;t+=D[k][2];w+=D[k][3];}});$('#dayN').textContent=n;$('#dayT').textContent=t;$('#dayW').textContent=w;};C.appendChild(b);});
/* 칸2: 복사본 vs 한 곳 */
var mode='x',R=LAB.rng(7),st;
function init2(){st={files:[['회장','010-1111-2222'],['총무','010-1111-2222'],['홍보','010-1111-2222']],db:'010-1111-2222',edits:0,blocked:0,month:0};draw2();}
function draw2(){var v,rows;
 if(mode==='x'){rows=st.files.map(function(f){return [f[0]+'의 파일','김하나',f[1]];});v=new Set(st.files.map(function(f){return f[1];})).size;}
 else {rows=[['공용 DB','김하나',st.db]];v=1;}
 $('#m2tab').innerHTML=LAB.tableHTML(['저장 위치','회원','전화번호'],rows,{cap:mode==='x'?'엑셀 복사본 3개':'데이터베이스 1곳',cls:function(r){return v>1?'bad':'';}});
 $('#m2v').textContent=v;$('#m2e').textContent=st.edits;$('#m2b').textContent=st.blocked;
 $('#m2i').innerHTML=st.month?('한 달 '+st.month+'번 지남 — '+(mode==='x'?(v>1?'같은 회원의 번호가 '+v+'가지로 갈라졌습니다. 어느 것이 맞는지 아무도 모릅니다.':'아직은 운 좋게 같습니다. 한 달 더 보내 보세요.'):'세 사람이 모두 같은 한 줄을 고쳤으므로 번호는 늘 하나입니다. 빈 번호 입력은 규칙(제약 조건)이 막았습니다.')):'방식을 고르고 「한 달 보내기」를 누르세요.';}
$('#m2go').onclick=function(){st.month++;for(var k=0;k<3;k++){var who=Math.floor(R()*3),num=R()<.18?'':'010-'+(1000+Math.floor(R()*9000))+'-'+(1000+Math.floor(R()*9000));
 if(R()<.55){st.edits++; if(mode==='x'){st.files[who][1]=num||st.files[who][1];} else { if(!num)st.blocked++; else st.db=num; }}}draw2();};
$('#m2r').onclick=init2;
[['m2x','x'],['m2d','d']].forEach(function(p){$('#'+p[0]).onclick=function(){mode=p[1];$('#m2x').setAttribute('aria-pressed',mode==='x');$('#m2d').setAttribute('aria-pressed',mode==='d');init2();};});
init2();
/* 칸4: 업종 */
var IND=[['전자상거래','제품, 주문, 고객, 재고 관리','제품, 카테고리, 고객, 주문, 장바구니, 리뷰','대량의 트랜잭션 처리, 확장성, 보안'],['은행·금융','계좌 관리, 거래 기록, 고객 정보','고객, 계좌, 거래, 대출, 투자 상품','높은 보안성, 데이터 무결성, 실시간 처리'],['의료·헬스케어','환자 기록, 진료 정보, 약물 관리','환자, 의사, 진료 기록, 처방전, 약물','데이터 프라이버시, 장기 데이터 저장, 복잡한 관계 모델링'],['교육 기관','학생 정보, 수업 관리, 성적 관리','학생, 교사, 과목, 수업, 성적, 학과','다양한 관계 모델링, 학기별 데이터 관리'],['제조업','생산 계획, 재고 관리, 공급망 관리','제품, 원자재, 공급업체, 생산 라인, 주문','실시간 재고 추적, 생산 효율성 분석'],['호텔·여행','예약 관리, 고객 서비스, 객실 관리','고객, 예약, 객실, 서비스, 직원','실시간 예약 시스템, 시즌별 데이터 관리'],['소셜 미디어','사용자 프로필, 게시물, 상호작용','사용자, 게시물, 댓글, 좋아요, 팔로우 관계','대용량 데이터 처리, 빠른 검색 및 조회, 확장성']];
var IC=$('#indChips');IND.forEach(function(d,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=d[0];b.onclick=function(){[].forEach.call(IC.children,function(x){x.setAttribute('aria-pressed',x===b);});
 $('#indOut').innerHTML='<b>'+d[0]+'</b><br>주요 특징: '+d[1]+'<br>주요 개체: '+d[2].split(', ').map(function(x){return '<span class="pill">'+x+'</span>';}).join('')+'<br>특별 고려사항: <b>'+d[3]+'</b>';};IC.appendChild(b);});
IC.children[0].click();
/* 대결 슬라이더 */
var dn=$('#duelN');dn.oninput=function(){$('#duelNv').textContent=(+dn.value).toLocaleString()+'명';};
''',
labs='''lab1:{presets:[{t:"① 방 만들기",q:"CREATE DATABASE shop;\\nUSE shop;"},{t:"② 표 만들기",q:"CREATE TABLE product (\\n  barcode VARCHAR(20) PRIMARY KEY,\\n  name    VARCHAR(50),\\n  price   INT\\n);"},{t:"③ 줄 넣기",q:"INSERT INTO product VALUES\\n  ('8801-0001', '삼각김밥', 1500),\\n  ('8801-0042', '생수', 900),\\n  ('8801-0077', '컵라면', 1300);"},{t:"④ 꺼내 보기",q:"SELECT * FROM product;"},{t:"⑤ 한 줄만 찾기",q:"SELECT name, price FROM product WHERE barcode = '8801-0042';"}],ready:"아직 아무것도 없는 빈 창고입니다. ① 버튼부터 차례로 눌러 보세요.",start:""}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'여러 사람이 함께 쓰려고 한 곳에 통합해 저장·운영하는 데이터 모음.','lv2':'여러 사람·오래·같은 사실을 다룰 때 파일 복사본은 갈라지고, 데이터베이스는 한 곳을 함께 고친다는 차이.','lv3':'데이터를 저장하는 DBMS(MariaDB·PostgreSQL)와 분석 작업대(Orange·pandas)로 이루어진 이 과목의 실습 환경.','lv4':'무엇을 개체로 보고 어떻게 잇고 어디에 규칙을 걸지 정하는 일.'}[s['id']]
