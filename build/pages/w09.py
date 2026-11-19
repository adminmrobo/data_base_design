# 9주차 — SQL ① 데이터 정의 (교재 7장 1~2절)
PAGE = dict(
num='09', slug='sql_ddl', kind='lecture', short='9주', chip='09주차',
title='SQL ① 데이터 정의', title_en='SQL data definition (DDL)',
subtitle='CREATE · ALTER · DROP과 제약 조건 — 노션 「SQL 기본 문법」 따라 하기',
toc='SQL의 분류(DDL·DML·DCL·TCL), CREATE TABLE의 다섯 부분, NOT NULL·DEFAULT·PRIMARY KEY·UNIQUE·FOREIGN KEY·CHECK, ON DELETE 옵션, ALTER·DROP·TRUNCATE',
kicker='데이터베이스 설계 · 9주차 · 교재 7장',
question='표를 만드는 순간에 “앞으로 들어올 잘못된 값”까지 막을 수 있을까?',
desc='데이터베이스 설계 9주차: SQL의 소개와 분류, CREATE TABLE(속성·키·제약 조건), 참조 무결성 옵션(ON DELETE/UPDATE), ALTER TABLE·DROP TABLE·TRUNCATE. 노션 SQL 기본 문법 실습과 페이지 안 SQL 실습실.',
intro='<p>8주차까지는 표를 <b>그리고 설명</b>했습니다. 이제 직접 <b>만듭니다</b>. SQL 중 표의 구조를 만들고 고치고 지우는 부분을 데이터 정의어(DDL)라고 합니다. 오늘의 핵심은 문법보다 <b>제약 조건</b>입니다 — 표를 만들 때 “빈칸 금지, 중복 금지, 0 이상만, 있는 고객만”을 함께 적어 두면, 그 뒤로 들어오는 수만 줄의 잘못된 값을 DBMS가 대신 막아 줍니다.</p>',
kpis=[('4종','DDL · DML · DCL · TCL'),('5부분','CREATE TABLE: 속성 · 기본키 · 대체키 · 외래키 · CHECK'),('3+1','ON DELETE: NO ACTION · CASCADE · SET NULL (· SET DEFAULT)'),('3개','노션 실습 페이지 연결')],
hero_talk=[
 ('doc','front','오늘부터 손에 키보드를 든다. 다만 <b>CREATE TABLE 한 줄이 설계의 결론</b>이라는 걸 잊지 마라.'),
 ('asst','smile','노션 실습 그대로 따라 하면 되죠? 저는 한글 칸 이름에서 오류 났던 게 기억나요.'),
 ('fly','clip','그건 인코딩 문제였지(utf8mb4). 오늘은 그런 함정도 같이 짚자. 노션 자료에도 고칠 곳이 두 군데 있어.'),
 ('robo','smile','나는 제약 조건을 전부 걸 거야! NOT NULL, CHECK, 외래키… 많을수록 든든하지!')],
crew=[('doc','front','DDL 문법과 제약 정리, 판정'),('asst','smile','노션 실습 진행, 숫자 발표'),('fly','clip','자료 속 오류·함정 찾기'),('robo','smile','“제약은 많을수록”파 (오늘 쓸모 있음)')],
recap='6주차: 기본키는 NULL·중복 금지(개체 무결성), 외래키는 있는 값만(참조 무결성). 오늘은 이 규칙을 <b>SQL 문장으로 적는 법</b>을 배웁니다.',
notion=[('SQL 기본 문법 (노션)', NOTION+'1ab17a4520ed8157b748e6104aa8e2c9', 'company 데이터베이스 · employees 표 — 실습 #1 ~ #2-10'),
        ('SQL 기본 문법 (교재 예제 코드 수정)', NOTION+'1ab17a4520ed815294ccd69faa520526', 'market 데이터베이스 · 제약 조건(CHECK·PK·FK) 실습'),
        ('SQL 문법 정리 (DCL, TCL 추가)', NOTION+'1ab17a4520ed8198b223c82808756ddd', 'DDL·DML·DCL·TCL·DQL 한 장 정리')],
why=[('구조가 먼저','어떤 칸에 어떤 값이 들어갈지 정하지 않으면 SELECT도 INSERT도 할 수 없습니다.'),
     ('규칙을 표에 새긴다','입력 프로그램마다 검사 코드를 짜면 하나는 빠뜨립니다(3주차). 표에 새긴 규칙은 어떤 경로로 들어와도 지켜집니다.'),
     ('고치는 법도 설계','운영 중인 표에 칸을 더하고 이름을 바꾸는 일(ALTER)은 날마다 일어납니다. 지우는 일(DROP)은 되돌릴 수 없습니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>분류</th><th>하는 일</th><th>명령</th><th>이 과목</th></tr></thead><tbody>
<tr><td>DDL 데이터 정의어</td><td>테이블 생성·변경·삭제</td><td>CREATE, ALTER, DROP, TRUNCATE</td><td><b>9주 (오늘)</b></td></tr>
<tr><td>DML 데이터 조작어</td><td>검색·삽입·수정·삭제</td><td>SELECT, INSERT, UPDATE, DELETE</td><td>10주</td></tr>
<tr><td>DCL 데이터 제어어</td><td>접근·사용 권한 부여·취소</td><td>GRANT, REVOKE</td><td>13주</td></tr>
<tr><td>TCL 트랜잭션 제어어</td><td>작업 단위 확정·취소</td><td>COMMIT, ROLLBACK</td><td>13주</td></tr></tbody></table></div>
<p>SQL은 연구용 관계 DBMS인 System R의 언어 SEQUEL에서 유래했고, ANSI·ISO가 표준을 계속 다듬고 있습니다. <b>대화식 SQL</b>(DBMS에 직접 입력)과 <b>삽입 SQL</b>(프로그램 안에 넣어 실행)로 씁니다. 세미콜론(;)이 문장의 끝이고, 키워드는 대소문자를 구분하지 않습니다.</p>''',
steps=[
dict(id='lv1', short='분류·자료형', title='SQL의 분류와 자료형 — 문장마다 이름표 붙이기', concept='SQL의 분류', en='sql statement categories', cid='lab:concept/sql-categories',
 tag='연구실: 문장 분류 카드', analogy='공구함의 칸',
 situation='노션 「SQL 문법 정리」에는 CREATE, TRUNCATE, INSERT, GRANT, COMMIT, SELECT가 한꺼번에 나옵니다. 각 문장은 어느 서랍에 들어갈까요? 그리고 나이·가격·이름·날짜 칸은 어떤 자료형이어야 할까요?',
 pair=(('연구실에서는','공구함에 칸이 나뉘어 있듯, SQL 문장도 하는 일로 나뉩니다. 구조를 만드는 공구(DDL), 내용을 다루는 공구(DML), 권한을 다루는 공구(DCL), 작업을 확정·취소하는 공구(TCL).'),
       ('SQL에서는','자료형은 6주차의 <b>도메인</b>입니다. <code>INT</code>(정수), <code>DECIMAL(10,2)</code>(소수 고정), <code>VARCHAR(n)</code>(가변 길이 글자, 최대 n), <code>CHAR(n)</code>(고정 길이), <code>DATE</code>(\'YYYY-MM-DD\'). 문자와 날짜 값은 작은따옴표로 감쌉니다.')),
 panel='''<p style="margin-top:0">문장을 눌러 서랍을 고르세요. 누를 때마다 DDL → DML → DCL → TCL 순서로 바뀝니다.</p><div class="chips" id="cls9"></div><div class="ctrl"><button type="button" class="bt primary" id="cls9c">채점</button></div><div class="insight" id="cls9o"></div>''',
 panel_title='직접 해 보기 — 문장 분류',
 sim='SQL 문장 분류 카드',
 explain='<p><b>함정 두 개:</b> ① <code>TRUNCATE</code>는 데이터를 지우지만 <b>DDL</b>입니다(표를 비우고 다시 만드는 구조 작업, 되돌리기 어려움). ② <code>SELECT</code>는 교재에서 DML로 분류하지만, 노션 정리처럼 따로 <b>DQL</b>(질의어)로 부르기도 합니다. 시험에서는 교재 분류(DML)를 따르세요.</p>',
 limit='서랍은 나눴습니다. 이제 DDL의 첫 공구, CREATE TABLE로 실제 표를 만들어 봅니다.', limit_label='표를 만드는 문법을 아직 쓰지 않음',
 say=('fly','point','VARCHAR(50)의 50은 “글자 수 상한”이야. 넘치면 MariaDB는 오류(Data too long)를 내.'),
 quiz=[dict(q='다음 중 DDL(데이터 정의어)이 아닌 것은?',o=['CREATE','ALTER','TRUNCATE','UPDATE'],a=3,why='UPDATE는 데이터를 수정하는 DML입니다. TRUNCATE는 DDL입니다.'),
       dict(q='사용자에게 테이블 조회 권한을 주는 GRANT는 어느 분류인가?',o=['DDL','DML','DCL','TCL'],a=2,why='권한 부여·취소(GRANT, REVOKE)는 데이터 제어어 DCL입니다.')]),
dict(id='lv2', short='CREATE', title='CREATE TABLE — 속성·키·제약을 한 번에', concept='CREATE TABLE', en='create table statement', cid='lab:concept/create-table',
 tag='연구실: 노션 실습 #1·#2', analogy='입사 서류 양식 만들기',
 situation='노션 실습 #1: <code>company</code> 데이터베이스를 만들고 직원 표를 만듭니다. 교재는 같은 문장에 기본키·대체키·외래키·CHECK까지 적는 다섯 부분 구조를 제시합니다. 둘을 함께 해 봅니다.',
 pair=(('연구실에서는','입사 서류 양식을 만들 때 칸 이름과 칸 크기(속성·자료형)를 정하고, “이름은 필수”(NOT NULL), “사번은 겹치면 안 됨”(PRIMARY KEY), “나이는 18 이상”(CHECK)을 양식에 인쇄해 둡니다.'),
       ('SQL에서는','<code>CREATE TABLE 이름 ( ① 속성 자료형 [NOT NULL] [DEFAULT 값], ② PRIMARY KEY(…), ③ UNIQUE(…), ④ FOREIGN KEY(…) REFERENCES 표(…), ⑤ CHECK(…) );</code> — UNIQUE(대체키)는 기본키와 달리 NULL을 허용합니다.')),
 panel='<div class="sqllab" id="lab9a" data-lab="lab9a"></div><p class="cvcap">①~④는 노션 「SQL 기본 문법」 실습 #1·#2-1·#2-2a·#2-2b 그대로, ⑤·⑥은 교재 판매 데이터베이스의 고객 표를 제약 조건과 함께 만든 것이고, ⑦~⑨는 그 규칙을 하나씩 어겨 보는 버튼입니다.</p>',
 panel_title='SQL 실습실 — 표 만들고 제약 확인하기',
 sim='CREATE TABLE과 제약 조건 실습',
 explain='<p><b>손으로 먼저:</b> ⑦~⑨는 각각 어느 규칙에 막힐까요? ⑦ 같은 아이디 apple을 또 넣음 → 기본키 중복 ✗ ⑧ 이름 NULL → NOT NULL ✗ ⑨ 나이 −3 → CHECK ✗. 반대로 등급을 생략하면 DEFAULT \'silver\'가 들어가 통과합니다. 실습실은 MariaDB 명령줄처럼 첫 오류에서 멈추므로, 위반 문장은 버튼 하나에 하나씩 두었습니다.</p><p><b>한글 칸 이름 주의(노션 실습 #2-7):</b> MariaDB의 문자 집합이 utf8mb4가 아니면 한글 값·이름에서 오류가 납니다. 노션은 <code>SHOW CREATE DATABASE</code>로 확인하고 <code>MODIFY COLUMN … CHARACTER SET utf8mb4</code>로 고쳤습니다. 설치 때 UTF8 체크(how_to_start_db 미션 1)를 해 두면 피할 수 있습니다.</p>',
 limit='고객 표와 주문 표가 외래키로 이어져 있을 때, 고객을 지우면 그 고객의 주문은 어떻게 될까요?', limit_label='부모 튜플 삭제 시 처리 방법을 정하지 않음',
 say=('asst','spark','DEFAULT를 걸어 두니까 등급을 안 적어도 silver가 들어가네요. 입력하는 사람이 편해졌어요!'),
 quiz=[dict(q='기본키와 달리 NULL 값을 허용하면서 유일성을 보장하는 키워드는?',o=['PRIMARY KEY','UNIQUE','FOREIGN KEY','CHECK'],a=1,why='UNIQUE는 대체키를 지정하며 NULL을 허용합니다.'),
       dict(q='적립금 INT DEFAULT 0 으로 만든 표에 적립금을 빼고 INSERT 하면 적립금 값은?',o=['NULL','0','오류','빈 문자열'],a=1,why='값을 생략하면 DEFAULT로 지정한 0이 들어갑니다.')]),
dict(id='lv3', short='ON DELETE', title='참조 무결성 옵션 — 부모를 지우면 자식은?', concept='참조 무결성 옵션', en='referential actions', cid='lab:concept/referential-actions',
 tag='연구실: 홍보부가 없어지면', analogy='동아리가 해체되면',
 situation='교재의 예: 부서 표의 홍보부를 지우려 합니다. 사원 표에는 홍보부 소속 정소화 사원이 있습니다. 홍보부를 지우면 정소화 사원은 어떻게 되어야 할까요?',
 pair=(('연구실에서는','동아리가 해체될 때 규칙은 여러 가지일 수 있습니다: 회원이 남아 있으면 해체 금지 / 회원 명단도 함께 폐기 / 회원은 남기고 소속만 비움.'),
       ('SQL에서는','외래키에 옵션을 붙입니다. <b>ON DELETE NO ACTION</b>(=RESTRICT, 삭제 금지, 기본값) · <b>CASCADE</b>(자식도 함께 삭제) · <b>SET NULL</b>(자식의 외래키를 NULL로) · <b>SET DEFAULT</b>(기본값으로). ON UPDATE도 같은 방식입니다.')),
 panel='''<div class="ctrl"><button type="button" class="bt" data-od="RESTRICT" aria-pressed="true">NO ACTION</button><button type="button" class="bt" data-od="CASCADE">CASCADE</button><button type="button" class="bt" data-od="SET NULL">SET NULL</button><button type="button" class="bt primary" id="od9go">홍보부 삭제 실행</button><button type="button" class="bt" id="od9r">처음으로</button></div><div class="two"><div id="od9a"></div><div id="od9b"></div></div><div class="insight" id="od9o"></div><pre id="od9sql" style="font-size:13px"></pre>''',
 panel_title='직접 해 보기 — 옵션 세 가지 비교',
 sim='ON DELETE 옵션 비교',
 explain='<p>세 옵션 모두 <b>참조 무결성을 지킵니다</b>. 다만 지키는 방법이 다릅니다 — 삭제를 막거나(NO ACTION), 함께 지우거나(CASCADE), 연결을 끊거나(SET NULL). 어떤 것을 고를지는 업무 규칙이 정합니다: 주문 기록은 회계상 남겨야 하니 CASCADE는 위험하고, 게시글의 댓글은 글과 함께 지워도 됩니다.</p><p style="font-size:14px;color:#5b6874">참고: MariaDB(InnoDB)는 SET DEFAULT를 문법으로는 받지만 실제로는 지원하지 않습니다. 실습은 세 가지로 합니다.</p>',
 aicheck='<p>AI에게 “외래키 걸 때 ON DELETE CASCADE 붙이는 게 좋죠?”라고 물으면 “편리합니다”라고 답하기 쉽습니다. 질문을 바꿔 보세요: “<b>고객을 지우면 주문·결제 기록이 함께 사라져도 되는가?</b>” 편리함과 기록 보존은 다른 문제입니다.</p>',
 limit='표를 만든 뒤에도 칸을 더하고 이름을 바꾸고, 필요 없으면 지워야 합니다. 그 일을 하는 문장은?', limit_label='이미 만든 표의 구조를 바꾸거나 지우지 못함',
 say=('robo','wow','같은 “홍보부 삭제”인데 결과가 세 가지! 옵션 한 단어가 이렇게 큰 차이를 만드네!'),
 quiz=[dict(q='부서를 삭제할 때 그 부서 소속 사원 튜플도 함께 삭제되게 하는 옵션은?',o=['ON DELETE NO ACTION','ON DELETE CASCADE','ON DELETE SET NULL','ON DELETE SET DEFAULT'],a=1,why='CASCADE는 관련 튜플을 함께 삭제합니다.'),
       dict(q='사원 3명이 홍보부(외래키)를 참조할 때 ON DELETE SET NULL로 홍보부를 지우면 남는 사원 수와 그들의 소속부서 값은? (계산)',o=['0명','3명, 소속부서 NULL','3명, 소속부서 홍보부','1명'],a=1,why='SET NULL은 자식 튜플을 남기고 외래키만 NULL로 바꿉니다.')]),
dict(id='lv4', short='ALTER·DROP', title='ALTER · DROP · TRUNCATE — 고치고 지우기 (노션 자료 바로잡기)', concept='ALTER TABLE과 DROP TABLE', en='alter and drop table', cid='lab:concept/alter-drop',
 tag='연구실: 노션 실습 #2-4 ~ #2-10', analogy='양식 고치기와 폐기',
 situation='노션 실습은 연봉 칸을 추가했다가 근속년수로 바꾸고(#2-4, #2-5), 칸을 지우고(#2-6), 승진대상 칸에 CHECK를 걸고(#2-7), 마지막에 표를 지웁니다(#2-10). 그런데 #2-6과 #2-7의 코드는 그대로 실행하면 오류가 납니다. 왜일까요?',
 pair=(('연구실에서는','쓰던 양식에 칸을 추가하는 것은 쉽지만, 칸을 지우거나 양식 자체를 폐기하면 거기 적힌 내용도 사라집니다. 다른 서류가 그 양식을 참조하고 있으면 폐기할 수 없습니다.'),
       ('SQL에서는','<code>ALTER TABLE 표 ADD 속성 자료형</code> · <code>DROP COLUMN 속성</code> · <code>CHANGE 옛이름 새이름 자료형</code>(MariaDB) · <code>RENAME COLUMN a TO b</code> · <code>ADD CONSTRAINT 이름 …</code> · <code>DROP CONSTRAINT 이름</code>. <code>DROP TABLE</code>은 구조째 삭제, <code>TRUNCATE</code>는 구조는 두고 행만 전부 삭제.')),
 panel='<div class="sqllab" id="lab9b" data-lab="lab9b"></div>',
 panel_title='SQL 실습실 — 노션 실습을 실행하고 바로잡기',
 sim='ALTER·DROP 실습과 자료 오류 수정',
 explain='<p><b>#2-6 바로잡기:</b> 노션 코드 <code>DROP TABLE customers; DROP COLUMN 근속년수;</code>는 두 가지가 틀렸습니다. ① 지울 대상은 customers가 아니라 employees의 칸이고 ② <code>DROP COLUMN</code>은 혼자 쓸 수 없고 <code>ALTER TABLE employees DROP COLUMN 근속년수;</code>로 써야 합니다.</p><p><b>#2-7 바로잡기:</b> <code>CHECK (직급 = \'Manager\' AND 부서 = \'Sales\')</code>는 “<b>모든 줄</b>이 Sales의 Manager여야 한다”는 뜻이라, 이미 들어 있는 다른 직원들 때문에 거부됩니다(인코딩 문제와 별개). 원래 의도인 “Sales의 Manager만 승진 대상으로 표시”는 제약이 아니라 <code>UPDATE … SET 승진대상 = \'대상\' WHERE …</code>로 합니다. 실습실 ④·⑤에서 확인하세요.</p>',
 aicheck='<p>이번 칸의 두 오류는 강의 자료를 옮기다 생긴 것입니다. AI가 써 준 SQL도 마찬가지로 <b>실행해 보기 전에는 맞는지 모릅니다</b>. 확인 순서: ① 문장이 문법상 혼자 설 수 있나(DROP COLUMN 단독 ✗) ② 제약 조건이 “모든 줄”에 대해 말이 되나(CHECK는 행마다 검사) ③ 실행 결과의 행 수·오류 번호가 예상과 같은가.</p>',
 limit='표는 만들고 고칠 수 있게 됐습니다. 이제 그 안의 데이터를 넣고, 찾고, 바꾸고, 지울 차례 — 10주차 DML입니다.', limit_label='표 안의 데이터를 다루는 문장(DML)은 아직',
 quiz=[dict(q='employees 표에서 근속년수 칸을 지우는 올바른 문장은?',o=['DROP COLUMN 근속년수;','DROP TABLE 근속년수;','ALTER TABLE employees DROP COLUMN 근속년수;','DELETE 근속년수 FROM employees;'],a=2,why='칸 삭제는 ALTER TABLE … DROP COLUMN입니다. 노션 #2-6의 코드는 이렇게 고쳐 읽으세요.'),
       dict(q='DROP TABLE과 TRUNCATE TABLE의 차이로 옳은 것은?',o=['둘 다 구조를 남긴다','DROP은 구조째 삭제, TRUNCATE는 구조는 두고 행만 전부 삭제','TRUNCATE는 DML이다','DROP은 행 하나만 지운다'],a=1,why='TRUNCATE는 표를 비우되 구조는 남깁니다. 둘 다 DDL입니다.')]),
],
duel=dict(q='제약 조건 — 표에 새길까, 입력 프로그램에 맡길까?',
 intro='같은 고객 표를 두 가지로 만들고, 잘못된 입력 10건을 차례로 넣어 봅니다(중복 아이디, 빈 이름, 음수 나이, 없는 등급, 글자 수 초과…). 초파리는 “제약 없이 단순하게, 검사는 입력 화면에서”, 주판봇은 “NOT NULL·PK·CHECK·길이 제한을 모두 표에”. 페이지 안 SQL 엔진으로 실제로 실행해 막힌 건수를 셉니다.',
 fly_pick='제약 없이 단순한 표 (검사는 화면에서)', fly_line='표는 가볍게. 이상한 값은 입력 화면에서 거르면 되지.',
 robo_pick='NOT NULL · PK · CHECK · 길이 제한 모두', robo_line='규칙은 많을수록 든든해! 표에 다 새겨 둘 거야!',
 metric='잘못된 입력 10건 중 DB가 막아 낸 건수 (입력 화면을 거치지 않은 일괄 입력 기준)', step=1,
 after='<div id="duel9t"></div>',
 run='return PAGE.duel();',
 announce='return "일괄 입력 10건 중 초파리 표는 <b>"+r.fly+"건</b>, 주판봇 표는 <b>"+r.robo+"건</b>을 막았어요. 엑셀에서 한꺼번에 붙여 넣은 자료는 입력 화면을 거치지 않았거든요.";',
 verdict='return "규칙은 표에 새겨야 어느 길로 들어와도 지켜진다. 제약을 빠짐없이 건 주판봇 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>핵심 문법</th><th>기억할 점</th></tr></thead><tbody>
<tr><td>1 분류</td><td>DDL · DML · DCL · TCL</td><td>TRUNCATE는 DDL, SELECT는 DML(DQL로도 부름)</td></tr>
<tr><td>2 CREATE</td><td>속성 자료형 NOT NULL DEFAULT / PRIMARY KEY / UNIQUE / FOREIGN KEY … REFERENCES / CHECK</td><td>UNIQUE는 NULL 허용, 한글은 utf8mb4</td></tr>
<tr><td>3 옵션</td><td>ON DELETE · ON UPDATE + NO ACTION · CASCADE · SET NULL · SET DEFAULT</td><td>무엇을 고를지는 업무 규칙이 결정</td></tr>
<tr><td>4 ALTER·DROP</td><td>ADD · DROP COLUMN · CHANGE · RENAME COLUMN · ADD/DROP CONSTRAINT / DROP TABLE / TRUNCATE</td><td>참조되는 표·칸은 바로 못 지움</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 서류 양식</b> 종이 양식은 고쳐도 지난 서류가 그대로지만, ALTER TABLE은 이미 들어 있는 모든 행에 즉시 적용됩니다(CHECK를 걸면 기존 행도 검사).</div><div><b>대결의 한계</b> 실무에서는 표의 제약과 입력 화면의 검사를 <b>둘 다</b> 둡니다. 화면 검사는 친절한 안내를, 표의 제약은 최후의 방어를 맡습니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① DDL은 구조, DML은 내용 ② 규칙은 CREATE TABLE에 새긴다 ③ 지우기 전에 누가 참조하는지 본다.'),
       ('robo','happy','제약을 다 걸어 둔 표가 10건을 모두 막았어! 규칙은 많을수록 든든하다니까!'),
       ('fly','coffee','인정. 대신 규칙이 업무와 맞는지는 꼭 확인해. 노션 #2-7처럼 “모든 줄”에 안 맞는 CHECK도 있었잖아.'),
       ('asst','proud','노션 자료의 오타 두 개를 찾아서 고쳤어요! 다음 주엔 SELECT로 데이터를 꺼내 봐요.')],
next_note='<p class="recap"><b>다음 회차 — 10주차 「SQL ② 데이터 조작과 조인」:</b> SELECT·WHERE·LIKE·GROUP BY·ORDER BY, INSERT·UPDATE·DELETE, 조인과 하위 질의, 뷰.</p>',
gloss={'자료형':('자료형(데이터 타입)','용어','칸에 들어갈 값의 종류와 크기. INT, DECIMAL, VARCHAR, CHAR, DATE 등.','data-type','lv1'),
 'VARCHAR':('VARCHAR(n)','명령어','최대 n글자까지 저장하는 가변 길이 문자 자료형.','varchar','lv1'),
 'TRUNCATE':('TRUNCATE','명령어','표의 구조는 남기고 모든 행을 지우는 DDL 명령.','truncate','lv1'),
 'NOT NULL':('NOT NULL','명령어','그 칸이 비어 있을 수 없게 하는 제약.','not-null','lv2'),
 'DEFAULT':('DEFAULT','명령어','값을 생략했을 때 들어갈 기본값을 정하는 키워드.','default','lv2'),
 'UNIQUE':('UNIQUE','명령어','대체키 지정. 값이 유일해야 하지만 NULL은 허용.','unique','lv2'),
 'CHECK':('CHECK','명령어','각 행이 만족해야 할 조건을 지정하는 제약.','check-constraint','lv2'),
 'utf8mb4':('utf8mb4','용어','MariaDB에서 한글·이모지를 온전히 저장하는 문자 집합.','utf8mb4','lv2'),
 'CASCADE':('ON DELETE CASCADE','명령어','부모 튜플을 지우면 참조하는 자식 튜플도 함께 지우는 옵션.','cascade','lv3'),
 'SET NULL':('ON DELETE SET NULL','명령어','부모를 지우면 자식의 외래키 값을 NULL로 바꾸는 옵션.','set-null','lv3'),
 'ALTER TABLE':('ALTER TABLE','명령어','이미 있는 표의 구조(칸·제약)를 바꾸는 DDL 명령.','alter-table','lv4')},
facts=[('F01','SQL은 System R을 위한 언어 SEQUEL에서 유래, ANSI·ISO에서 표준화','문헌 사실','kim3ed','lv1','7장 1절 (교안)'),
       ('F02','CREATE TABLE은 속성 정의, 기본키, 대체키, 외래키, 무결성 제약 조건 다섯 부분으로 구성','문헌 사실','kim3ed','lv2','7장 2절 (교안)'),
       ('F03','UNIQUE로 지정한 대체키는 유일성을 가지며 기본키와 달리 널 값이 허용됨','문헌 사실','kim3ed','lv2','7장 2절'),
       ('F04','ON DELETE 옵션: NO ACTION, CASCADE, SET NULL, SET DEFAULT','문헌 사실','kim3ed','lv3','7장 2절 (교안 18쪽)'),
       ('F05','노션 실습#2-6의 코드 “DROP TABLE customers; DROP COLUMN 근속년수;”는 ALTER TABLE employees DROP COLUMN 근속년수로 고쳐야 실행됨','문헌 사실','ahn2025sqlbasic','lv4','실습#2-6'),
       ('F06','노션 실습#2-7은 인코딩 오류 시 SHOW CREATE DATABASE로 확인하고 utf8mb4로 MODIFY','문헌 사실','ahn2025sqlbasic','lv2','실습#2-7')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='ahn2025sqlbasic',type='webpage',title='SQL 기본 문법',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed8157b748e6104aa8e2c9',role='primary'),
      dict(id='ahn2025sqltext',type='webpage',title='SQL 기본 문법 (교재 예제 코드 수정)',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed815294ccd69faa520526',role='primary'),
      dict(id='ahn2025dcltcl',type='webpage',title='SQL 문법 정리 (DCL, TCL 추가)',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed8198b223c82808756ddd',role='background')],
models=['employees·고객 표 데이터 (노션·교재 예제)','부서·사원 ON DELETE 실험 데이터 (교재 홍보부 예를 바탕으로 한 예시)','대결의 잘못된 입력 10건 (예시) — 실행은 페이지 안 SQL 엔진'],
cover_alt='작업대 위에서 빈 표 양식에 자물쇠 모양의 규칙 스티커를 붙이는 장면을 네 캐릭터가 지켜보는 표지 (대체 그림)',
prereq=['08'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var ST=[['CREATE TABLE courses (…);','DDL'],['TRUNCATE TABLE students;','DDL'],['INSERT INTO students …;','DML'],['UPDATE students SET grade = 4 …;','DML'],['SELECT * FROM students;','DML'],['GRANT SELECT ON students TO …;','DCL'],['REVOKE DELETE ON students FROM …;','DCL'],['COMMIT;','TCL'],['ROLLBACK;','TCL'],['ALTER TABLE students ADD phone …;','DDL']],K=['DDL','DML','DCL','TCL'],pick={};
function c9(){$('#cls9').innerHTML=ST.map(function(s,i){return '<button type="button" class="bt" data-i="'+i+'"><code>'+s[0]+'</code> '+(pick[i]?'<span class="pill">'+pick[i]+'</span>':'')+'</button>';}).join('');
 $$('#cls9 button').forEach(function(b){b.onclick=function(){var i=+b.dataset.i,k=K.indexOf(pick[i]);pick[i]=K[(k+1)%K.length];c9();};});}
$('#cls9c').onclick=function(){var ok=0,bad=[];ST.forEach(function(s,i){if(pick[i]===s[1])ok++;else bad.push(s[0].split(' ')[0]+'→'+s[1]);});$('#cls9o').innerHTML='맞힘 <b>'+ok+'/10</b>'+(bad.length?'<br>다시: '+bad.join(' · '):'');};c9();
/* ON DELETE */
var od='RESTRICT';
function setup(){var db=new MiniSQL.DB();db.run("CREATE DATABASE corp; USE corp; CREATE TABLE 부서 (부서번호 VARCHAR(3) PRIMARY KEY, 부서이름 VARCHAR(10)); CREATE TABLE 사원 (사원번호 VARCHAR(4) PRIMARY KEY, 이름 VARCHAR(10), 소속부서 VARCHAR(3), FOREIGN KEY (소속부서) REFERENCES 부서(부서번호) ON DELETE "+od+"); INSERT INTO 부서 VALUES ('D1','홍보부'),('D2','개발부'); INSERT INTO 사원 VALUES ('E1','정소화','D1'),('E2','김용욱','D2'),('E3','고명석','D2');");return db;}
var db9;function show9(msg){function t(n){var r=db9.run('SELECT * FROM '+n+';')[0];return LAB.tableHTML(r.cols,r.rows,{cap:n+' ('+r.rows.length+'줄)'});}$('#od9a').innerHTML=t('부서');$('#od9b').innerHTML=t('사원');$('#od9o').innerHTML=msg;
 $('#od9sql').textContent='FOREIGN KEY (소속부서) REFERENCES 부서(부서번호)\n  ON DELETE '+(od==='RESTRICT'?'NO ACTION':od)+'\n\nDELETE FROM 부서 WHERE 부서번호 = \'D1\';';}
function r9(){db9=setup();show9('옵션을 고르고 「홍보부 삭제 실행」을 누르세요.');}
$$('#lv3 [data-od]').forEach(function(b){b.onclick=function(){od=b.dataset.od;$$('#lv3 [data-od]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});r9();};});
$('#od9go').onclick=function(){var r=db9.run("DELETE FROM 부서 WHERE 부서번호 = 'D1';")[0];
 show9(r.err?'<b style="color:#c9302c">삭제 거부</b> — '+LAB.esc(r.err)+'<br>홍보부 소속 사원이 남아 있어 부서를 지울 수 없습니다(NO ACTION).':(od==='CASCADE'?'<b>홍보부 삭제됨</b> — 정소화 사원도 함께 삭제되었습니다(CASCADE).':'<b>홍보부 삭제됨</b> — 정소화 사원은 남고 소속부서가 NULL이 되었습니다(SET NULL).'));};
$('#od9r').onclick=r9;r9();
/* 대결 */
var BAD=[["('apple','jane',20,'gold')",'아이디 중복'],["('kiwi',NULL,30,'gold')",'이름 빈칸'],["('lime','sora',-3,'silver')",'음수 나이'],["('plum','dan',25,'diamond')",'없는 등급'],["('fig','abcdefghijklmnopqrstuvwxyz0123',22,'vip')",'이름 30자 (20자 초과)'],["(NULL,'mia',27,'gold')",'아이디 빈칸'],["('date','eve',150,'gold')",'나이 150'],["('yuzu','ann',33,NULL)",'등급 빈칸'],["('kiwi2','bo','스물','gold')",'나이에 글자'],["('APPLE','jon',41,'vip')",'대소문자만 다른 중복']];
PAGE.duel=function(){var loose=new MiniSQL.DB(),strict=new MiniSQL.DB();
 loose.run("CREATE DATABASE s; USE s; CREATE TABLE customer (id VARCHAR(255), name VARCHAR(255), age VARCHAR(255), rank VARCHAR(255)); INSERT INTO customer VALUES ('apple','jane','20','gold');");
 strict.run("CREATE DATABASE s; USE s; CREATE TABLE customer (id VARCHAR(10) PRIMARY KEY, name VARCHAR(20) NOT NULL, age INT CHECK (age BETWEEN 0 AND 120), rank VARCHAR(10) NOT NULL CHECK (rank IN ('silver','gold','vip'))); INSERT INTO customer VALUES ('apple','jane',20,'gold');");
 var f=0,r=0,rows=[];BAD.forEach(function(b){var a=loose.run('INSERT INTO customer VALUES '+b[0]+';')[0],c=strict.run('INSERT INTO customer VALUES '+b[0]+';')[0];if(a.err)f++;if(c.err)r++;rows.push([b[1],a.err?'막음':'들어감',c.err?'막음':'들어감']);});
 document.getElementById('duel9t').innerHTML=LAB.tableHTML(['잘못된 입력','제약 없는 표','제약 건 표'],rows,{cls:function(x){return x[2]==='막음'?'hl':'bad';}});
 return {fly:f,robo:r,flyTxt:f+'/10',roboTxt:r+'/10'};};
''',
labs='''lab9a:{presets:[{t:"① DB 만들기 (#1)",q:"CREATE DATABASE company;\\nUSE company;"},{t:"② 직원 표 (#2-1)",q:"CREATE TABLE employees (\\n  직원ID INT PRIMARY KEY,\\n  이름 VARCHAR(50),\\n  부서 VARCHAR(50),\\n  직급 VARCHAR(50)\\n);"},{t:"③ 10명 입력 (#2-2a)",q:"INSERT INTO employees (직원ID, 이름, 부서, 직급)\\nVALUES\\n  (1, 'John Doe', 'Sales', 'Manager'),\\n  (2, 'Jane Smith', 'Marketing', 'Analyst'),\\n  (3, 'David Lee', 'HR', 'Assistant'),\\n  (4, 'Sarah Kim', 'Sales', 'Clerk'),\\n  (5, 'Michael Wu', 'Finance', 'Manager'),\\n  (6, 'Emily Chen', 'Marketing', 'Clerk'),\\n  (7, 'Ryan Park', 'HR', 'Analyst'),\\n  (8, 'Lisa Wang', 'Finance', 'Assistant'),\\n  (9, 'Eric Liu', 'Sales', 'Clerk'),\\n  (10, 'Amy Lee', 'Marketing', 'Manager');\\nSELECT * FROM employees;"},{t:"④ 한 명 추가 (#2-2b)",q:"INSERT INTO employees (직원ID, 이름, 부서, 직급) VALUES (11, 'Alex Kim', 'Marketing', 'Clerk');\\nSELECT COUNT(*) AS 직원수 FROM employees;"},{t:"⑤ 교재 고객 표 + 제약",q:"CREATE TABLE 고객 (\\n  고객아이디 VARCHAR(20) NOT NULL,\\n  고객이름 VARCHAR(10) NOT NULL,\\n  나이 INT,\\n  등급 VARCHAR(10) NOT NULL DEFAULT 'silver',\\n  직업 VARCHAR(20),\\n  적립금 INT DEFAULT 0,\\n  PRIMARY KEY (고객아이디),\\n  CHECK (나이 >= 0)\\n);\\nDESCRIBE 고객;"},{t:"⑥ 정상 입력",q:"INSERT INTO 고객 (고객아이디, 고객이름, 나이, 직업) VALUES ('apple', '정소화', 20, '학생');\\nSELECT * FROM 고객;"},{t:"⑦ 위반 1 — 기본키 중복",q:"INSERT INTO 고객 VALUES ('apple', '김선우', 25, 'vip', '간호사', 2500);"},{t:"⑧ 위반 2 — NOT NULL",q:"INSERT INTO 고객 (고객아이디, 고객이름, 나이) VALUES ('banana', NULL, 30);"},{t:"⑨ 위반 3 — CHECK",q:"INSERT INTO 고객 (고객아이디, 고객이름, 나이) VALUES ('carrot', '고명석', -3);"}],ready:"빈 실습실입니다. ①부터 차례로 누르세요. 노션 「SQL 기본 문법」과 같은 순서입니다."},
lab9b:{setup:"CREATE DATABASE company; USE company; CREATE TABLE employees (직원ID INT PRIMARY KEY, 이름 VARCHAR(50), 부서 VARCHAR(50), 직급 VARCHAR(50)); INSERT INTO employees VALUES (1,'John Doe','Sales','Manager'),(2,'Jane Smith','Marketing','Analyst'),(3,'David Lee','HR','Assistant'),(4,'Sarah Kim','Sales','Clerk'),(5,'Michael Wu','Finance','Manager'),(6,'Emily Chen','Marketing','Clerk'),(7,'Ryan Park','HR','Analyst'),(8,'Lisa Wang','Finance','Assistant'),(9,'Eric Liu','Sales','Clerk'),(10,'Amy Lee','Marketing','Manager');",
presets:[{t:"#2-4 연봉 칸 추가",q:"ALTER TABLE employees ADD COLUMN 연봉 INT;\\nSELECT * FROM employees;"},{t:"#2-5 연봉 → 근속년수",q:"ALTER TABLE employees\\nCHANGE COLUMN 연봉 근속년수 INT;\\nDESCRIBE employees;"},{t:"#2-6 노션 코드 ① DROP TABLE",q:"DROP TABLE customers;"},{t:"#2-6 노션 코드 ② DROP COLUMN",q:"DROP COLUMN 근속년수;"},{t:"#2-6 바로잡은 코드",q:"ALTER TABLE employees DROP COLUMN 근속년수;\\nDESCRIBE employees;"},{t:"#2-7 노션 CHECK 그대로",q:"ALTER TABLE employees ADD COLUMN 승진대상 VARCHAR(50);\\nALTER TABLE employees\\nADD CONSTRAINT chk_promotion_target CHECK (직급 = 'Manager' AND 부서 = 'Sales');"},{t:"#2-7 의도대로 (UPDATE)",q:"UPDATE employees SET 승진대상 = '대상'\\nWHERE 직급 = 'Manager' AND 부서 = 'Sales';\\nUPDATE employees SET 승진대상 = '비대상'\\nWHERE 승진대상 IS NULL;\\nSELECT 이름, 부서, 직급, 승진대상 FROM employees;"},{t:"TRUNCATE (행만 비우기)",q:"TRUNCATE TABLE employees;\\nSELECT COUNT(*) AS 남은행 FROM employees;\\nDESCRIBE employees;"},{t:"#2-10 표 삭제 (마지막에)",q:"DROP TABLE employees;\\nSHOW TABLES;"}],
ready:"노션 실습 #2-2a까지 끝난 상태(직원 10명)입니다. 위에서부터 차례로 — #2-6·#2-7은 “그대로”를 먼저 실행해 오류를 보고, 바로잡은 코드로 넘어가세요."}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'SQL 문장을 하는 일에 따라 DDL·DML·DCL·TCL로 나눈 것과, 칸의 도메인을 정하는 자료형.','lv2':'속성·기본키·대체키·외래키·CHECK를 정의해 표를 만드는 DDL 문.','lv3':'참조되는 부모 튜플을 삭제·변경할 때 자식 튜플을 어떻게 처리할지 정하는 외래키 옵션(NO ACTION·CASCADE·SET NULL·SET DEFAULT).','lv4':'이미 있는 표의 칸·제약을 바꾸는 ALTER TABLE과, 표를 지우는 DROP TABLE·TRUNCATE.'}[s['id']]
