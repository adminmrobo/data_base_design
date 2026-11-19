# 6주차 — 관계 데이터 모델 (교재 5장)
PAGE = dict(
num='06', slug='relational_model', kind='lecture', short='6주', chip='06주차',
title='관계 데이터 모델', title_en='The relational data model',
subtitle='표 한 장의 규칙 — 릴레이션, 다섯 가지 키, 무결성',
toc='릴레이션·속성·튜플·도메인·차수·카디널리티, 릴레이션의 네 특징, 슈퍼키·후보키·기본키·대체키·외래키, 개체·참조 무결성',
kicker='데이터베이스 설계 · 6주차 · 교재 5장',
question='“김철수”가 두 명이면, 이 표는 누구를 가리키고 있는 걸까?',
desc='데이터베이스 설계 6주차: 관계 데이터 모델의 용어(릴레이션, 속성, 튜플, 도메인, NULL, 차수, 카디널리티), 릴레이션의 특징, 키의 종류와 기본키 선택 기준, 개체·참조 무결성 제약. 노션 SQL 실습(교재 예제 수정)과 연결.',
intro='<p>1970년 코드(E. F. Codd)는 데이터를 <b>표(릴레이션)와 값</b>만으로 표현하자고 제안했습니다. 오늘 실습하는 MariaDB도 이 모델 위에 있습니다. 표는 누구나 그릴 수 있지만, 데이터베이스의 표에는 규칙이 있습니다 — 같은 줄이 두 번 있으면 안 되고, 한 칸에는 값이 하나여야 하고, 모든 줄은 <b>키</b>로 하나씩 가려낼 수 있어야 합니다.</p>',
kpis=[('5종','슈퍼 · 후보 · 기본 · 대체 · 외래키'),('4특징','튜플 유일 · 튜플 무순서 · 속성 무순서 · 원자값'),('2제약','개체 무결성 · 참조 무결성'),('1970','코드의 관계 데이터 모델 제안')],
hero_talk=[
 ('doc','front','표에 이름표를 다는 날이다. 열은 속성, 행은 튜플, 그리고 <b>모든 줄을 가려내는 열쇠</b>가 키다.'),
 ('asst','smile','이름으로 찾으면 되지 않아요? 학번은 외우기 어렵잖아요.'),
 ('fly','clip','이름이 같은 사람이 둘이면? 키는 “외우기 쉬운 값”이 아니라 “<b>절대 겹치지 않는 값</b>”이어야 해.'),
 ('robo','smile','키는 많을수록 든든하지! 열 다섯 개를 다 묶어서 키로 쓰면 절대 안 겹치잖아!')],
crew=[('doc','front','용어와 규칙 정리, 판정'),('asst','smile','이름 vs 학번을 묻는 초보 눈높이'),('fly','clip','유일성·최소성 따지기'),('robo','smile','“다 묶으면 안전”파')],
recap='5주차: 도서관 ERD — 회원·도서·대여·카테고리와 1:N 관계. 오늘은 그 그림을 <b>표와 키</b>의 말로 다시 씁니다.',
notion=[('05주차 : 관계 데이터 모델 (노션)', NOTION+'1ab17a4520ed8171a2aaea71542abcc0', '강의 영상, 「데이터 베이스 설계 : worst case」'),
        ('SQL 기본 문법 (교재 예제 코드 수정)', NOTION+'1ab17a4520ed815294ccd69faa520526', '실습 #2-5 기본키, #3-2 외래키 — 4칸 실습실의 원본'),
        ('속성의 원자성 예시 (노션)', NOTION+'28217a4520ed804a8e34d6ced8765057', '2칸 “속성의 원자성” 보충')],
why=[('모든 RDBMS의 공통 언어','MariaDB·PostgreSQL·Oracle은 모두 릴레이션·키·무결성이라는 같은 말을 씁니다.'),
     ('키가 무결성을 지킨다','“같은 학생이 두 번 등록”, “없는 고객의 주문” 같은 오류를 키 제약이 자동으로 막습니다.'),
     ('시험의 핵심','다섯 가지 키와 두 무결성은 중간고사의 가장 확실한 출제 범위입니다.')],
bigpicture='<div class="tbl"><table><thead><tr><th>모델의 말</th><th>표의 말</th><th>파일의 말</th></tr></thead><tbody><tr><td>릴레이션</td><td>테이블</td><td>파일</td></tr><tr><td>속성(attribute)</td><td>열(column)</td><td>필드</td></tr><tr><td>튜플(tuple)</td><td>행(row)</td><td>레코드</td></tr><tr><td>도메인</td><td>열의 자료형·허용 범위</td><td>—</td></tr></tbody></table></div>',
steps=[
dict(id='lv1', short='용어', title='릴레이션의 용어 — 속성, 튜플, 도메인, 차수, 카디널리티', concept='릴레이션', en='relation', cid='lab:concept/relation',
 tag='현장: 쇼핑몰 고객 표', analogy='출석부',
 situation='노션 실습의 <code>customer_table</code>을 봅니다. 칸이 몇 개, 줄이 몇 개인지 세는 데에도 이름이 있습니다. 그리고 robert의 나이 칸은 왜 비어 있을까요?',
 pair=(('현장에서는','출석부의 세로 칸(이름, 학번, 출석)이 <b>속성</b>, 학생 한 줄이 <b>튜플</b>, 출석 칸에 쓸 수 있는 값(○, ×, 지)의 모음이 <b>도메인</b>입니다.'),
       ('관계 모델에서는','<b>차수</b>(degree) = 속성의 개수, <b>카디널리티</b>(cardinality) = 튜플의 개수. <b>NULL</b>은 값을 모르거나 해당 값이 없음을 뜻하며, 0이나 빈 문자열과 다릅니다.')),
 panel='''<p style="margin-top:0">열 이름이나 줄을 눌러 보세요. 아래 버튼으로 줄·칸을 늘려 차수와 카디널리티가 어떻게 바뀌는지 봅니다.</p>
<div id="rel6"></div><div class="ctrl"><button type="button" class="bt" id="rel6r">튜플 하나 추가</button><button type="button" class="bt" id="rel6c">속성 하나 추가 (email)</button><button type="button" class="bt" id="rel6x">처음으로</button></div>
<div class="kpis" style="grid-template-columns:repeat(2,1fr)"><div><b id="rel6d">6</b><span>차수 (속성 수)</span></div><div><b id="rel6k">7</b><span>카디널리티 (튜플 수)</span></div></div><div class="insight" id="rel6o">표의 아무 곳이나 눌러 보세요.</div>''',
 panel_title='직접 해 보기 — 표에 이름표 붙이기',
 sim='차수와 카디널리티 세기',
 explain='<p><b>릴레이션 스키마</b>는 <code>customer(id, name, age, rank, job, credit)</code>처럼 이름과 속성의 목록 — 잘 안 바뀌는 설계도입니다. <b>릴레이션 인스턴스</b>는 어느 순간의 튜플들 — 계속 바뀝니다. 그래서 차수는 스키마의 성질(잘 안 바뀜), 카디널리티는 인스턴스의 성질(계속 바뀜)입니다.</p><p><b>도메인</b>을 자료형으로 정해 두면(나이는 INT) 잘못된 값과 잘못된 연산을 막을 수 있습니다. “나이 + 이름” 같은 계산은 시작부터 거부됩니다.</p>',
 limit='용어는 붙였지만, 아무 표나 릴레이션은 아닙니다. 같은 줄이 두 번 있거나, 한 칸에 전화번호 두 개가 들어 있다면?', limit_label='릴레이션이 지켜야 할 규칙을 아직 모름',
 say=('fly','point','NULL은 “0”도 “빈칸 글자”도 아니야. “모름”이야. 그래서 NULL = NULL도 참이 아니지(10주차에서 확인).'),
 quiz=[dict(q='릴레이션에서 속성의 전체 개수를 무엇이라 하나요?',o=['카디널리티','차수','도메인','인스턴스'],a=1,why='차수(degree)는 속성 수, 카디널리티는 튜플 수입니다.'),
       dict(q='속성 6개, 튜플 7개인 표에 새 고객 2명을 추가하면 카디널리티는? (계산)',o=['6','7','8','9'],a=3,why='튜플이 7+2 = 9개가 됩니다. 차수는 6 그대로입니다.')]),
dict(id='lv2', short='특징', title='릴레이션의 네 가지 특징 — 아무 표나 릴레이션은 아니다', concept='릴레이션의 특징', en='properties of a relation', cid='lab:concept/relation-properties',
 tag='연구실: 규칙 위반 찾기', analogy='출석부 검사',
 situation='조수가 만든 회원 표를 박사가 검사합니다. 같은 줄이 두 번 있고, 한 칸에 전화번호 두 개가 쉼표로 들어 있습니다. 줄 순서를 바꾸면 다른 표일까요?',
 pair=(('연구실에서는','출석부에 같은 학생이 두 번 적혀 있으면 출석률이 틀어집니다. 한 칸에 “○, ×”를 같이 적으면 그날 출석인지 결석인지 알 수 없습니다.'),
       ('관계 모델에서는','① <b>튜플의 유일성</b>: 같은 튜플이 둘 있을 수 없음 ② <b>튜플의 무순서</b>: 줄 순서는 의미 없음 ③ <b>속성의 무순서</b>: 칸 순서도 의미 없음 ④ <b>속성의 원자성</b>: 한 칸에는 더 쪼갤 수 없는 값 하나만.')),
 panel='''<div id="prop6"></div><div class="ctrl"><button type="button" class="bt" id="p6a">중복 줄 지우기</button><button type="button" class="bt" id="p6b">전화번호 칸 쪼개기</button><button type="button" class="bt" id="p6c">줄 순서 섞기</button><button type="button" class="bt" id="p6d">칸 순서 바꾸기</button><button type="button" class="bt" id="p6x">처음으로</button></div><div class="insight" id="prop6o"></div>''',
 panel_title='직접 해 보기 — 규칙 위반 고치기',
 sim='릴레이션 특징 위반 고치기',
 explain='<p>섞기·바꾸기 버튼은 <b>아무것도 위반하지 않습니다</b>. 줄과 칸의 순서는 원래 의미가 없기 때문입니다. 그래서 SQL에서 “3번째 줄”은 존재하지 않고, 순서가 필요하면 <code>ORDER BY</code>로 매번 요청합니다(10주차). 반면 중복 줄과 여러 값이 든 칸은 진짜 위반입니다.</p><p>원자성을 어긴 칸(<code>010-1234, 02-555</code>)은 “02로 시작하는 번호를 가진 회원”을 찾기 어렵게 만듭니다. 12주차 제1정규형이 바로 이 규칙입니다.</p>',
 limit='중복 줄을 막으려면, 줄을 서로 구별할 수 있는 기준이 있어야 합니다. 그 기준이 키입니다.', limit_label='튜플을 구별할 기준(키)이 없음',
 say=('asst','shock','줄 순서를 섞어도 같은 표라니… 그럼 엑셀의 “3행”이라는 말은 DB에선 의미가 없는 거네요!'),
 quiz=[dict(q='릴레이션의 특징이 아닌 것은?',o=['튜플의 유일성','튜플의 순서가 중요함','속성의 원자성','속성의 무순서'],a=1,why='튜플 사이의 순서는 의미가 없습니다(튜플의 무순서).'),
       dict(q='한 칸에 “등산, 독서”처럼 여러 값을 넣으면 어긋나는 특징은?',o=['튜플의 유일성','속성의 원자성','튜플의 무순서','속성의 무순서'],a=1,why='속성 값은 더 쪼갤 수 없는 원자값이어야 합니다.')]),
dict(id='lv3', short='키', title='다섯 가지 키 — 슈퍼키에서 외래키까지', concept='키', en='keys in the relational model', cid='lab:concept/relational-keys',
 tag='연구실: 키 찾기 실험', analogy='사람을 가려내는 단서',
 situation='고객 표에서 한 사람을 정확히 가려내려면 어떤 칸(들)을 보면 될까요? 이름은 겹칠 수 있고, 아이디와 이메일은 겹치지 않습니다. 아이디+이름도 겹치지 않지만, 굳이 둘을 묶을 필요가 있을까요?',
 pair=(('연구실에서는','범인을 가려내는 단서: “키 170cm”는 여러 명, “지문”은 한 명. “지문+신발 크기”도 한 명을 가리키지만 신발 크기는 군더더기입니다.'),
       ('관계 모델에서는','<b>슈퍼키</b>: 유일성만 만족 / <b>후보키</b>: 유일성 + 최소성 / <b>기본키</b>: 후보키 중 하나 선택 / <b>대체키</b>: 선택되지 않은 후보키 / <b>외래키</b>: 다른 릴레이션의 기본키를 참조하는 속성.')),
 panel='''<p style="margin-top:0">칸을 골라 「검사」를 누르면, 그 조합이 아래 표의 모든 줄을 구별하는지(유일성)와 군더더기가 없는지(최소성)를 계산합니다.</p>
<div class="chips" id="key6"></div><div class="ctrl"><button type="button" class="bt primary" id="key6go">검사</button><button type="button" class="bt" id="key6all">모든 후보키 찾기</button></div><div id="key6t"></div><div class="insight" id="key6o"></div>''',
 panel_title='직접 해 보기 — 키 판정기',
 sim='슈퍼키·후보키 판정기',
 explain='<p><b>손으로 한 번:</b> {이름}은 김철수가 둘이라 유일성 ✗. {아이디}는 모두 달라 유일성 ✓, 한 칸이라 최소성 ✓ → 후보키. {아이디, 이름}은 유일성 ✓이지만 이름을 빼도 여전히 유일하므로 최소성 ✗ → 슈퍼키일 뿐 후보키가 아님.</p><div class="tbl"><table><thead><tr><th>기본키 선택 기준 (교안)</th><th>이유</th></tr></thead><tbody><tr><td>NULL이 될 수 있는 속성이 포함된 후보키는 부적합</td><td>값이 없으면 그 줄을 가려낼 수 없음</td></tr><tr><td>값이 자주 바뀌는 속성이 포함된 후보키는 부적합</td><td>바뀔 때마다 그 값을 참조하는 외래키도 고쳐야 함</td></tr><tr><td>단순한 후보키(속성 수가 적은 것)를 선택</td><td>조인·비교·저장이 쉬움</td></tr></tbody></table></div>',
 aicheck='<p>“이메일을 기본키로 써도 되나요?”라고 AI에게 물으면 “유일하니 가능합니다”라고만 답하기 쉽습니다. 기준 2를 확인하세요 — 이메일은 <b>바뀔 수 있습니다</b>. 그래서 보통 이메일은 대체키(UNIQUE)로 두고, 바뀌지 않는 아이디·번호를 기본키로 씁니다.</p>',
 limit='키는 정했습니다. 그런데 기본키에 NULL을 넣거나, 외래키에 없는 고객 아이디를 넣으면 누가 막아 줄까요?', limit_label='키가 지켜지도록 강제하는 규칙이 없음',
 say=('robo','meh','열 다섯 개를 다 묶으면 유일하긴 한데… 최소성에서 떨어지는구나. 군더더기였어.'),
 quiz=[dict(q='유일성과 최소성을 모두 만족하는 키는?',o=['슈퍼키','후보키','외래키','복합 속성'],a=1,why='후보키는 유일성과 최소성을 모두 만족합니다. 슈퍼키는 유일성만 만족합니다.'),
       dict(q='후보키 {고객아이디}, {이메일} 중 고객아이디를 기본키로 정했다면 이메일은?',o=['슈퍼키가 아니다','대체키','외래키','기본키'],a=1,why='기본키로 선택되지 않은 후보키를 대체키라 합니다.')]),
dict(id='lv4', short='무결성', title='무결성 제약 — DBMS가 대신 지켜 주는 규칙', concept='무결성 제약 조건', en='integrity constraints', cid='lab:concept/integrity-constraints',
 tag='연구실: 노션 실습 그대로', analogy='출입 관리',
 situation='노션 실습 「교재 예제 코드 수정」에서 <code>order_table</code>에 외래키를 걸다가 오류가 났습니다(실습#3-2C). 왜 <code>customer_table</code>에는 걸렸는데 <code>product_table</code>에는 안 걸렸을까요?',
 pair=(('연구실에서는','건물 출입증(기본키)이 없는 사람은 들어올 수 없고, 방문증(외래키)에 적힌 직원이 실제로 있어야 방문이 허락됩니다.'),
       ('관계 모델에서는','<b>개체 무결성</b>: 기본키를 이루는 속성은 NULL일 수 없다(중복도 불가). <b>참조 무결성</b>: 외래키는 참조할 수 없는 값을 가질 수 없다 — 참조하는 표의 기본키 값이거나 NULL이어야 한다.')),
 panel='<div class="sqllab" id="lab6" data-lab="lab6"></div><p class="cvcap">노션 실습 순서 그대로입니다. ③에서 일부러 오류가 납니다. 오류 메시지를 읽고 ④로 원인을 찾은 뒤 ⑤로 고치세요.</p>',
 panel_title='SQL 실습실 — 노션 실습 #2-5 · #3-2 따라 하기',
 sim='개체·참조 무결성 실습',
 explain='<p>③의 오류는 “<b>참조되는 쪽이 기본키(또는 UNIQUE)가 아니다</b>”입니다. 외래키가 가리키는 값은 그쪽 표에서 한 줄을 정확히 가리켜야 하기 때문입니다. <code>DESCRIBE</code>로 보면 <code>customer_table.id</code>에는 Key=PRI가 있고 <code>product_num</code>에는 없습니다. ⑤에서 기본키를 걸면 외래키가 걸립니다.</p><p>⑥은 참조 무결성이 <b>입력</b>을 막는 장면(없는 고객 grape), ⑦은 <b>삭제</b>를 막는 장면(주문이 남아 있는 apple 삭제)입니다. 도메인 무결성(값이 정해진 범위 안에 있어야 함)은 실습 #2-4의 CHECK 제약이 담당합니다.</p>',
 limit='표와 키, 무결성까지 갖췄습니다. 이제 이 표들로 “질문”을 하려면 무엇이 필요할까요? 표를 입력받아 표를 돌려주는 연산 — 7주차 관계 대수입니다.', limit_label='표에서 원하는 결과를 뽑아내는 연산을 아직 모름',
 quiz=[dict(q='“기본키를 구성하는 속성은 NULL 값을 가질 수 없다”는 제약은?',o=['참조 무결성','개체 무결성','도메인 무결성','사용자 정의 무결성'],a=1,why='개체 무결성 제약입니다. 기본키가 없는 튜플은 구별할 수 없기 때문입니다.'),
       dict(q='외래키를 설정하려 할 때 “errno: 150, incorrectly formed” 오류가 난 가장 흔한 원인은?',o=['외래키 이름이 길어서','참조되는 열이 기본키나 UNIQUE가 아니어서','테이블에 데이터가 없어서','SELECT 권한이 없어서'],a=1,why='노션 실습#3-2C의 원인입니다. product_num에 기본키를 먼저 설정해야 합니다.')]),
],
duel=dict(q='수강 표의 기본키 — 복합키 vs 대리키',
 intro='수강(학번, 과목코드, 성적) 표의 기본키를 정합니다. 초파리는 <b>(학번, 과목코드)</b> 복합키, 주판봇은 새 칸 <b>수강ID</b>(1, 2, 3… 자동 번호)를 만들자고 합니다. 판정 기준은 “모든 줄을 하나씩 구별하는가(유일성 검사 통과율)”입니다.',
 fly_pick='(학번, 과목코드) 복합키', fly_line='있는 칸 두 개로 이미 한 줄이 정해져. 새 칸을 만들 필요가 없어.',
 robo_pick='수강ID 대리키 (자동 번호)', robo_line='숫자 하나짜리 키가 짧고 빠르지! 번호는 절대 안 겹쳐!',
 metric='유일성 검사 통과율 (%)', margin=0, step=2,
 after='<div class="insight" id="duel6x" style="display:none"></div>',
 run='document.getElementById("duel6x").style.display="block";document.getElementById("duel6x").innerHTML="덧붙임: 대리키만 두면 <b>(20250101, DB설계)</b>를 두 번 넣어도 수강ID가 달라 막히지 않습니다. 대리키를 쓸 때는 (학번, 과목코드)에 UNIQUE를 따로 걸어야 중복 신청을 막습니다.";return {fly:100,robo:100,flyTxt:"100%",roboTxt:"100%"};',
 announce='return "두 방식 모두 지금 있는 수강 기록을 <b>100%</b> 구별했어요. 유일성 기준으로는 차이가 없어요.";',
 verdict='return "식별은 둘 다 된다. 다만 대리키를 쓰면 원래의 후보키(학번, 과목코드)를 UNIQUE로 남겨 둬야 한다. 이번 판은 나눠 갖는다.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>핵심</th><th>시험 포인트</th></tr></thead><tbody>
<tr><td>1 용어</td><td>속성=열, 튜플=행, 도메인=허용 값, 차수=열 수, 카디널리티=행 수, NULL=모름</td><td>차수·카디널리티 계산</td></tr>
<tr><td>2 특징</td><td>튜플 유일, 튜플·속성 무순서, 원자값</td><td>특징이 아닌 것 고르기</td></tr>
<tr><td>3 키</td><td>슈퍼(유일) ⊃ 후보(유일+최소) ⊃ 기본(선택) / 대체(나머지) / 외래(참조)</td><td>유일성·최소성 판정, 기본키 선택 기준</td></tr>
<tr><td>4 무결성</td><td>개체: PK에 NULL·중복 금지 / 참조: FK는 PK 값 또는 NULL</td><td>어느 제약 위반인지 고르기</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 지문</b> 지문은 사람에게 원래 있지만, 데이터베이스의 키는 설계자가 정하는 것입니다. 대리키처럼 일부러 만들기도 합니다.</div><div><b>대결의 한계</b> 대리키 vs 복합키는 실무에서 오래된 논쟁입니다. 이 페이지는 “유일성”만 판정했고, 조인 성능·변경 용이성은 다루지 않았습니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 표의 규칙 넷 — 유일·무순서·무순서·원자 ② 후보키 = 유일 + 최소 ③ PK는 NULL 금지, FK는 있는 값만.'),
       ('asst','report','대결은 무승부였어요. 둘 다 100% 구별했고, 대리키는 UNIQUE를 덧붙이기로 했어요.'),
       ('fly','coffee','무승부라도 배운 건 있지. “구별”과 “중복 신청 막기”는 다른 문제야.'),
       ('robo','meh','짧은 번호 키도 쓸 만하다는 걸 인정받았으니 됐어. UNIQUE는 꼭 챙길게.')],
next_note='<p class="recap"><b>다음 회차 — 7주차 「관계 데이터 연산」:</b> 셀렉트·프로젝트·조인·디비전 — 표를 넣으면 표가 나오는 계산.</p>',
gloss={'튜플':('튜플','용어','릴레이션의 행. 개체 하나에 대한 값들의 모임.','tuple','lv1'),
 '도메인':('도메인','개념','속성 하나가 가질 수 있는 모든 값의 집합. 보통 자료형으로 정의.','domain','lv1'),
 '차수':('차수(degree)','용어','릴레이션의 속성 개수.','degree','lv1'),
 '카디널리티':('카디널리티','용어','릴레이션의 튜플 개수.','cardinality','lv1'),
 'NULL':('NULL','기호','값을 모르거나 해당 값이 없음. 0이나 빈 문자열과 다르다.','null','lv1'),
 '원자성':('속성의 원자성','개념','속성 값은 더 쪼갤 수 없는 값 하나여야 한다는 릴레이션의 특징.','atomicity-of-attribute','lv2'),
 '슈퍼키':('슈퍼키','용어','유일성을 만족하는 속성(집합).','super-key','lv3'),
 '후보키':('후보키','용어','유일성과 최소성을 만족하는 속성(집합).','candidate-key','lv3'),
 '기본키':('기본키','용어','후보키 중 대표로 선택한 키. NULL·중복 불가.','primary-key','lv3'),
 '대체키':('대체키','용어','기본키로 선택되지 않은 후보키.','alternate-key','lv3'),
 '외래키':('외래키','용어','다른 릴레이션의 기본키를 참조하는 속성(집합).','foreign-key','lv3'),
 '참조 무결성':('참조 무결성','개념','외래키는 참조할 수 없는 값을 가질 수 없다는 제약.','referential-integrity','lv4'),
 '개체 무결성':('개체 무결성','개념','기본키를 구성하는 속성은 NULL일 수 없다는 제약.','entity-integrity','lv4')},
facts=[('F01','관계 데이터 모델은 1970년 E. F. Codd가 제안','문헌 사실','codd1970relational','lv1','논문 자체'),
       ('F02','차수는 속성의 전체 개수, 카디널리티는 튜플의 전체 개수','문헌 사실','kim3ed','lv1','5장 (교안 인용)'),
       ('F03','릴레이션의 특징: 튜플의 유일성·무순서, 속성의 무순서·원자성','문헌 사실','kim3ed','lv2','5장 (교안 인용)'),
       ('F04','기본키 선택 기준: NULL 가능 속성 포함 후보키 부적합, 자주 변경되는 속성 포함 부적합, 단순한 후보키 선택','문헌 사실','ahn2025w04','lv3','4주차 교안 「기본키 선택의 기준」'),
       ('F05','외래키를 설정하려면 참조하는 열이 기본키 또는 고유 제약 조건으로 지정되어 있어야 함','문헌 사실','ahn2025sqltext','lv4','노션 실습#3-2C 해설')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='codd1970relational',type='article-journal',title='A Relational Model of Data for Large Shared Data Banks',author=[{'family':'Codd','given':'E. F.'}],issued={'date-parts':[[1970]]},**{'container-title':'Communications of the ACM','volume':'13','issue':'6','page':'377-387'},role='background',verified={'title':True,'authors':True,'year':True,'venue':True,'doi':False}),
      dict(id='ahn2025w04',type='report',title='데이터베이스설계 4주차 강의 교안: 관계 데이터 모델',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025sqltext',type='webpage',title='SQL 기본 문법 (교재 예제 코드 수정)',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed815294ccd69faa520526',role='primary')],
models=['customer_table·product_table·order_table 데이터 (노션 실습 예제 그대로)','릴레이션 특징 위반 표 (설명용 예)','키 판정기 고객 표 (예시 데이터)','대결의 수강 기록 (예시)'],
cover_alt='책상 위에 커다란 표가 펼쳐져 있고 맨 왼쪽 칸 위에 황금 열쇠가 놓인 장면을 네 캐릭터가 들여다보는 표지 (대체 그림)',
prereq=['05'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var BASE=[['apple','jane',20,'gold','student',1000],['banana','kim',25,'vip','nurse',2500],['carrot','duke',28,'gold','teacher',4500],['orange','albert',22,'silver','student',0],['melon','dragon',35,'gold','clerk',5000],['peach','jack',31,'silver','doctor',300],['pear','robert',null,'silver','clerk',500]];
var cols,rows;function r6(){cols=['id','name','age','rank','job','credit'];rows=BASE.map(function(r){return r.slice();});d6();}
function d6(){$('#rel6').innerHTML=LAB.tableHTML(cols,rows,{cap:'customer_table (노션 실습 예제)'});$('#rel6d').textContent=cols.length;$('#rel6k').textContent=rows.length;
 $$('#rel6 th').forEach(function(th,i){th.style.cursor='pointer';th.onclick=function(){$('#rel6o').innerHTML='<b>'+cols[i]+'</b> 열 = <b>속성</b>. 도메인 예: '+({id:'영문 글자 문자열 VARCHAR(255)',name:'이름 문자열',age:'0 이상의 정수 INT (NULL 허용)',rank:'{gold, vip, silver}',job:'직업 문자열',credit:'0 이상의 정수 DECIMAL(10,0)',email:'이메일 형식 문자열'}[cols[i]]||'문자열');};});
 $$('#rel6 tbody tr').forEach(function(tr,i){tr.style.cursor='pointer';tr.onclick=function(){var r=rows[i];$('#rel6o').innerHTML='<b>'+r[0]+'</b> 줄 = <b>튜플</b> 하나. '+(r[2]==null?'age가 <b>NULL</b> — 나이를 모르는 상태입니다(0살이 아님).':'');};});}
$('#rel6r').onclick=function(){rows.push(['grape','sora',27,'silver','designer',800].concat(cols.length>6?['sora@x.kr']:[]));d6();$('#rel6o').innerHTML='튜플이 늘었습니다 → <b>카디널리티</b>만 변함. 인스턴스가 바뀐 것.';};
$('#rel6c').onclick=function(){if(cols.length>6)return;cols.push('email');rows.forEach(function(r){r.push(null);});d6();$('#rel6o').innerHTML='속성이 늘었습니다 → <b>차수</b>가 변함. 스키마가 바뀐 것(ALTER TABLE). 기존 줄의 email은 NULL.';};
$('#rel6x').onclick=r6;r6();
/* 칸2 */
var P0={cols:['회원번호','이름','전화번호','지역'],rows:[['M1','김하나','010-1234, 02-555','서울'],['M2','이두리','010-2222','부산'],['M1','김하나','010-1234, 02-555','서울'],['M3','박세나','010-3333','대구']]},P;
function p6r(){P=JSON.parse(JSON.stringify(P0));p6d('처음 상태 — 위반 두 가지를 찾아 고쳐 보세요.');}
function viol(){var v=[],seen={};P.rows.forEach(function(r){var k=JSON.stringify(r);if(seen[k])v.push('튜플의 유일성');seen[k]=1;});var pi=P.cols.indexOf('전화번호');if(pi>=0&&P.rows.some(function(r){return /,/.test(r[pi]);}))v.push('속성의 원자성');return v;}
function p6d(msg){var v=viol();$('#prop6').innerHTML=LAB.tableHTML(P.cols,P.rows,{cls:function(r){return /,/.test(r.join('|'))?'bad':'';}});
 $('#prop6o').innerHTML=msg+'<br>현재 위반: '+(v.length?v.map(function(x){return '<span class="pill no">'+x+'</span>';}).join(''):'<span class="pill ok">없음 — 릴레이션입니다</span>');}
$('#p6a').onclick=function(){var seen={};P.rows=P.rows.filter(function(r){var k=JSON.stringify(r);if(seen[k])return false;seen[k]=1;return true;});p6d('중복 튜플을 지웠습니다.');};
$('#p6b').onclick=function(){var pi=P.cols.indexOf('전화번호');if(pi<0)return;var nr=[];P.rows.forEach(function(r){String(r[pi]).split(', ').forEach(function(ph){var x=r.slice();x[pi]=ph;nr.push(x);});});P.rows=nr;p6d('한 칸에 하나씩 쪼갰습니다. (줄이 늘어난 대신 원자성은 지켜짐 — 더 좋은 방법은 전화번호 표를 따로 두는 것, 11·12주차)');};
$('#p6c').onclick=function(){P.rows.reverse();p6d('줄 순서를 뒤집었습니다 — 위반이 새로 생기지 않습니다(튜플의 무순서).');};
$('#p6d').onclick=function(){var ix=P.cols.map(function(c,i){return i;}).reverse();P.cols=ix.map(function(i){return P.cols[i];});P.rows=P.rows.map(function(r){return ix.map(function(i){return r[i];});});p6d('칸 순서를 뒤집었습니다 — 같은 릴레이션입니다(속성의 무순서).');};
$('#p6x').onclick=p6r;p6r();
/* 칸3 키 판정 */
var KC=['아이디','이름','이메일','전화','생년월일'],KR=[['u01','김철수','kim1@a.kr','010-1','1999-01-02'],['u02','이영희','lee@a.kr','010-2','2000-03-04'],['u03','김철수','kim2@a.kr','010-3','1999-01-02'],['u04','박지민','park@a.kr','010-2','2001-05-06'],['u05','최수아','choi@a.kr',null,'2000-03-04']],sel={};
var kc=$('#key6');KC.forEach(function(c,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=c;b.setAttribute('aria-pressed','false');b.onclick=function(){sel[i]=!sel[i];b.setAttribute('aria-pressed',!!sel[i]);};kc.appendChild(b);});
$('#key6t').innerHTML=LAB.tableHTML(KC,KR,{cap:'고객 (예시 데이터 5줄)'});
function uniq(ix){var s={};for(var r=0;r<KR.length;r++){var vals=ix.map(function(i){return KR[r][i];});if(vals.some(function(v){return v==null;}))return false;var k=vals.join('|');if(s[k])return false;s[k]=1;}return true;}
function minimal(ix){return ix.every(function(_,j){var sub=ix.filter(function(_,k){return k!==j;});return !sub.length||!uniq(sub);});}
$('#key6go').onclick=function(){var ix=Object.keys(sel).filter(function(k){return sel[k];}).map(Number);if(!ix.length){$('#key6o').textContent='칸을 하나 이상 고르세요.';return;}
 var u=uniq(ix),m=u&&minimal(ix),nm=ix.map(function(i){return KC[i];}).join(', ');
 $('#key6o').innerHTML='{'+nm+'} — 유일성 '+(u?'✓':'✗')+' · 최소성 '+(u?(m?'✓':'✗ (빼도 유일한 칸이 있음)'):'—')+' → <b>'+(u?(m?'후보키':'슈퍼키 (후보키 아님)'):'키가 아님')+'</b>'+(ix.indexOf(3)>=0?'<br>전화 칸에는 NULL이 있어 유일성 검사에서 떨어집니다(값이 없는 줄은 구별할 수 없음).':'');};
$('#key6all').onclick=function(){var out=[];for(var m=1;m<32;m++){var ix=[];for(var i=0;i<5;i++)if(m&(1<<i))ix.push(i);if(uniq(ix)&&minimal(ix))out.push('{'+ix.map(function(i){return KC[i];}).join(', ')+'}');}
 $('#key6o').innerHTML='이 데이터에서 후보키: <b>'+out.join(' · ')+'</b><br>기본키 추천: {아이디} — 짧고, 잘 안 바뀌고, NULL이 없습니다. 이메일은 바뀔 수 있어 대체키로 둡니다. <span style="font-size:13px">({이름, 생년월일}이 후보키로 나오는 것은 이 5줄이 우연히 그렇기 때문 — 데이터가 늘면 깨질 수 있어 의미상 후보키로 보지 않습니다.)</span>';};
''',
labs='''lab6:{setup:"CREATE DATABASE market; USE market; CREATE TABLE customer_table (id VARCHAR(255), name VARCHAR(255), age INT, rank VARCHAR(255), job VARCHAR(255), credit DECIMAL(10, 0)); INSERT INTO customer_table VALUES ('apple','jane',20,'gold','student',1000),('banana','kim',25,'vip','nurse',2500),('carrot','duke',28,'gold','teacher',4500),('orange','albert',22,'silver','student',0),('melon','dragon',35,'gold','clerk',5000),('peach','jack',31,'silver','doctor',300),('pear','robert',NULL,'silver','clerk',500); CREATE TABLE product_table (product_num VARCHAR(255), product_name VARCHAR(255), inventory INT, price INT, company VARCHAR(255)); INSERT INTO product_table VALUES ('p01','mandu',5000,4500,'daehan'),('p02','nuddle',2500,5500,'minkuk'),('p03','pie',3600,2600,'hanbit'),('p04','chocolate',1250,2500,'hanbit'),('p05','spicynuddle',2200,1200,'daehan'),('p06','japannuddle',1000,1550,'minkuk'),('p07','biscuit',1650,1500,'hanbit'); CREATE TABLE order_table (order_num VARCHAR(255) NOT NULL, order_customer VARCHAR(255), order_product VARCHAR(255), quantity INT, address VARCHAR(255), order_date DATE);",
presets:[{t:"① 실습#2-5A 고객 기본키",q:"ALTER TABLE customer_table\\nADD CONSTRAINT pk_customer_id PRIMARY KEY (id);"},{t:"② 실습#2-5B 중복 시도",q:"UPDATE customer_table\\nSET id = 'banana'\\nWHERE id = 'apple';"},{t:"③ 실습#3-2 주문 기본키·외래키",q:"ALTER TABLE order_table\\nADD CONSTRAINT pk_order_num PRIMARY KEY (order_num);\\nALTER TABLE order_table\\nADD CONSTRAINT fk_order_customer\\nFOREIGN KEY (order_customer) REFERENCES customer_table(id);\\nALTER TABLE order_table\\nADD CONSTRAINT fk_order_product\\nFOREIGN KEY (order_product) REFERENCES product_table(product_num);"},{t:"④ 원인 찾기 DESCRIBE",q:"DESCRIBE product_table;\\nDESCRIBE customer_table;"},{t:"⑤ 기본키 추가 후 다시",q:"ALTER TABLE product_table\\nADD CONSTRAINT pk_product_num PRIMARY KEY (product_num);\\nALTER TABLE order_table\\nADD CONSTRAINT fk_order_product\\nFOREIGN KEY (order_product) REFERENCES product_table(product_num);\\nDESCRIBE order_table;"},{t:"⑥ 없는 고객의 주문",q:"INSERT INTO order_table VALUES ('q01','apple','p03',10,'seoul','2022-01-01');\\nINSERT INTO order_table VALUES ('q99','grape','p01',1,'jeju','2022-06-01');"},{t:"⑦ 주문이 있는 고객 지우기",q:"DELETE FROM customer_table WHERE id = 'apple';"}],
ready:"노션 「교재 예제 코드 수정」의 market 데이터베이스(고객·제품·주문 표)를 키 없이 만들어 두었습니다. ①부터 순서대로."}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'행(튜플)과 열(속성)로 이루어진 표로, 관계 데이터 모델에서 데이터를 저장하는 기본 단위.','lv2':'튜플의 유일성, 튜플의 무순서, 속성의 무순서, 속성의 원자성.','lv3':'튜플을 구별하는 속성(집합): 슈퍼키·후보키·기본키·대체키, 그리고 다른 표를 참조하는 외래키.','lv4':'개체 무결성(기본키 NULL 금지)과 참조 무결성(외래키는 존재하는 값만) 등 DBMS가 강제하는 규칙.'}[s['id']]
