# 15주차 — 기말 REVIEW (9~14주)
MOCK = [
 ('def', dict(q='테이블 구조를 만들고 바꾸고 지우는 SQL 명령의 묶음은?',o=['DML','DDL','DCL','TCL'],a=1,why='CREATE·ALTER·DROP은 데이터 정의어(DDL). (9주차)')),
 ('case', dict(q='고객 표의 나이에 -3이 들어가지 않게 하려면 CREATE TABLE에 무엇을 쓰나?',o=['DEFAULT 0','CHECK (나이 >= 0)','UNIQUE','NOT NULL'],a=1,why='값의 범위 규칙은 CHECK 제약 조건입니다. (9주차)')),
 ('case', dict(q='주문이 있는 고객을 지우면 주문도 함께 지워지게 하려면 외래키에 무엇을 붙이나?',o=['ON DELETE RESTRICT','ON DELETE SET NULL','ON DELETE CASCADE','ON UPDATE NO ACTION'],a=2,why='CASCADE는 참조하는 행도 함께 삭제합니다. (9주차)')),
 ('def', dict(q='DROP TABLE과 달리 테이블 구조는 남기고 모든 행만 지우는 명령은?',o=['DELETE TABLE','TRUNCATE TABLE','ALTER TABLE','REVOKE'],a=1,why='TRUNCATE는 구조를 유지하고 데이터만 비웁니다(노션 #1-4). (9·13주차)')),
 ('case', dict(q='“주문 수량 합계가 50 이상인 상품”을 구하려 WHERE SUM(quantity) >= 50을 썼더니 오류가 났다. 고칠 곳은?',o=['ORDER BY로 옮긴다','HAVING으로 옮긴다','SELECT에 DISTINCT를 붙인다','LIMIT을 붙인다'],a=1,why='집계 조건은 그룹을 만든 뒤 거르는 HAVING에 씁니다. (10주차)')),
 ('def', dict(q='SELECT 문의 실행 순서로 옳은 것은?',o=['SELECT → FROM → WHERE','FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY','WHERE → FROM → SELECT','ORDER BY → SELECT → FROM'],a=1,why='표를 정하고(FROM) 줄을 거르고(WHERE) 묶고(GROUP BY) 묶음을 거른 뒤(HAVING) 칸을 고르고(SELECT) 정렬(ORDER BY). (10주차)')),
 ('case', dict(q='= 뒤의 부속 질의가 여러 행을 돌려줘 오류가 났다. 가장 알맞은 수정은?',o=['= 를 IN 으로','= 를 LIKE 로','부속 질의에 ORDER BY 추가','GROUP BY 추가'],a=0,why='여러 값과 비교할 때는 IN을 씁니다. (10주차)')),
 ('def', dict(q='데이터베이스 설계 단계 중 DBMS의 종류와 무관하게 E-R 다이어그램을 만드는 단계는?',o=['요구 사항 분석','개념적 설계','논리적 설계','물리적 설계'],a=1,why='개념적 설계의 결과물이 E-R 다이어그램(개념적 스키마)입니다. (11주차)')),
 ('case', dict(q='개체 3개, N:M 관계 1개, 1:N 관계 2개인 ERD를 규칙대로 변환하면 릴레이션은 몇 개인가?',o=['3','4','6','7'],a=1,why='개체 3개 + N:M 관계 1개 = 4개. 1:N 관계는 N쪽 외래키로 처리. (11주차)')),
 ('case', dict(q='1:1 관계에서 한쪽만 필수 참여일 때 외래키는 어디에 두나?',o=['선택 참여 쪽','필수 참여 쪽','양쪽 모두','별도 릴레이션'],a=1,why='필수 참여 쪽에 두면 NULL이 생기지 않습니다(규칙 4-2). (11주차)')),
 ('def', dict(q='다중값 속성(연락처 여러 개)을 변환하는 규칙은?',o=['한 칸에 쉼표로 저장','원래 개체에 칸을 여러 개 추가','별도 릴레이션으로 분리','삭제'],a=2,why='규칙 5: 원래 개체의 기본키와 함께 별도 릴레이션. (11·12주차)')),
 ('case', dict(q='대여 기록을 모두 지웠더니 그 회원의 정보까지 사라졌다. 어떤 이상 현상인가?',o=['삽입 이상','갱신 이상','삭제 이상','교착 상태'],a=2,why='지우면 안 되는 정보까지 함께 사라지는 삭제 이상. (12주차)')),
 ('def', dict(q='기본키의 일부에만 종속되는 속성을 없앤 정규형은?',o=['1NF','2NF','3NF','BCNF'],a=1,why='부분 함수 종속 제거 → 2NF. (12주차)')),
 ('case', dict(q='대출(대출번호, 회원ID, 회원등급)에서 대출번호 → 회원ID → 회원등급이다. 3NF로 만들려면?',o=['회원등급을 지운다','회원(회원ID, 회원등급)을 분리한다','대출번호를 지운다','그대로 둔다'],a=1,why='이행 종속을 없애기 위해 회원 릴레이션을 분리합니다. (12주차)')),
 ('def', dict(q='모든 결정자가 후보키인 정규형은?',o=['2NF','3NF','BCNF','4NF'],a=2,why='BCNF(보이스-코드 정규형). (12주차)')),
 ('def', dict(q='트랜잭션의 “전부 아니면 전무” 성질은?',o=['원자성','일관성','격리성','지속성'],a=0,why='원자성(Atomicity). (13주차)')),
 ('case', dict(q='장애 직후 로그에 <T2, start>와 변경 기록은 있지만 <T2, commit>이 없다(즉시 갱신). T2는?',o=['REDO','UNDO','아무것도 안 함','COMMIT'],a=1,why='완료되지 않은 트랜잭션은 UNDO. (13주차)')),
 ('case', dict(q='잔액 1,000에서 T1(+300)과 T2(+500)가 잠금 없이 T1 read, T2 read, T1 write, T2 write 순으로 실행됐다. 최종 잔액은?',o=['1,300','1,500','1,800','2,800'],a=1,why='T1의 쓰기가 덮인 갱신 분실 — 1,500. (13주차)')),
 ('def', dict(q='빅데이터 3V에 속하지 않는 것은?',o=['Volume','Velocity','Variety','Version'],a=3,why='Volume·Velocity·Variety. (14주차)')),
 ('case', dict(q='행 1,000,000개 중 하나를 찾을 때 정렬된 색인을 반씩 좁혀 찾으면 최악 약 몇 번 비교하나?',o=['약 20번','약 1,000번','약 500,000번','약 1,000,000번'],a=0,why='2²⁰ ≈ 1,048,576 → 약 20번. (14주차)')),
]
SETUP = ("CREATE DATABASE hanbit; USE hanbit; "
 "CREATE TABLE 회원 (회원아이디 VARCHAR(20) PRIMARY KEY, 이름 VARCHAR(10) NOT NULL, 나이 INT CHECK (나이 >= 0), 등급 VARCHAR(10) NOT NULL DEFAULT 'silver', 적립금 INT NOT NULL DEFAULT 0); "
 "CREATE TABLE 상품 (상품번호 CHAR(3) PRIMARY KEY, 상품명 VARCHAR(20), 재고량 INT CHECK (재고량 >= 0), 단가 INT, 제조업체 VARCHAR(20)); "
 "CREATE TABLE 주문 (주문번호 CHAR(3) PRIMARY KEY, 회원아이디 VARCHAR(20) NOT NULL, 상품번호 CHAR(3) NOT NULL, 수량 INT, 주문일자 DATE, FOREIGN KEY (회원아이디) REFERENCES 회원(회원아이디) ON DELETE CASCADE, FOREIGN KEY (상품번호) REFERENCES 상품(상품번호)); "
 "INSERT INTO 회원 VALUES ('apple','정소화',20,'gold',1000),('banana','김선우',25,'vip',2500),('carrot','고명석',28,'gold',4500),('orange','김용욱',22,'silver',0),('melon','성원용',35,'gold',5000); "
 "INSERT INTO 상품 VALUES ('p01','그냥만두',5000,4500,'대한식품'),('p02','매운쫄면',2500,5500,'민국푸드'),('p03','쿵떡파이',3600,2600,'한빛제과'),('p04','맛난초콜릿',1250,2500,'한빛제과'),('p05','얼큰라면',2200,1200,'대한식품'); "
 "INSERT INTO 주문 VALUES ('o01','apple','p03',10,'2022-01-01'),('o02','melon','p01',5,'2022-01-10'),('o03','banana','p01',45,'2022-01-11'),('o04','carrot','p03',8,'2022-02-01'),('o05','melon','p02',36,'2022-02-20'),('o06','banana','p04',19,'2022-03-02'),('o07','apple','p01',22,'2022-03-15'),('o08','carrot','p05',30,'2022-04-01');")
PAGE = dict(
num='15', slug='final_review', kind='review', short='15주', chip='15주차 · REVIEW',
title='기말 REVIEW', title_en='Final review (weeks 9-14)',
subtitle='9~14주차를 한 장의 지도, 한빛 마트 종합 실습, 모의 문제 20개로',
toc='SQL(DDL·DML)·설계 5단계와 변환 규칙·정규화·트랜잭션과 회복·병행 제어·응용 기술을 지도·낱말 카드·종합 SQL 실습·모의 문제 20개로 복습',
toc_faces=[('doc','front'),('asst','proud'),('sia','smile')],
kicker='데이터베이스 설계 · 15주차 · 기말 대비 REVIEW',
question='표를 만들고(SQL), 그리고(설계), 고치고(정규화), 지키는(트랜잭션) 흐름을 한 번에 말할 수 있을까?',
desc='데이터베이스 설계 15주차 기말 REVIEW: 9~14주차(SQL 데이터 정의·조작, 데이터베이스 설계 5단계와 변환 규칙, 정규화, 트랜잭션·회복·병행 제어, 응용 기술) 핵심 정리, 낱말 카드, 한빛 마트 종합 SQL 실습, 모의 문제 20개.',
intro='<p>기말고사도 강의에서 다룬 개념과 사례의 <b>객관식·단답식</b>입니다(강의 개요). 이 페이지는 새 내용을 배우지 않습니다. 9~14주를 <b>네 묶음</b>으로 다시 걷고, 묶음마다 “헷갈리는 짝”을 정리한 뒤, 한빛 마트 데이터로 <b>SQL 종합 실습</b>을 하고, 맨 아래 <b>모의 문제 20개</b>로 점검합니다. 해설 끝의 (n주차)가 돌아갈 페이지입니다. 1~7주 범위는 <a href="w08_midterm_review.html">중간 REVIEW</a>에 있습니다.</p>',
kpis=[('6주','범위: 9~14주차 (교재 7~11장)'),('4묶음','SQL · 설계 · 정규화 · 트랜잭션과 응용'),('20문항','모의 문제 (정의형 · 상황·계산형)'),('16장','낱말 카드')],
kpi_note='시험 날짜·장소·범위는 학사 일정과 강의 공지를 따릅니다. 이 페이지는 복습용이며 모의 문제는 실제 시험 문제가 아닙니다.',
hero_talk=[
 ('doc','front','후반부의 한 줄: <b>요구를 그림으로(설계) → 표로(SQL DDL) → 나쁜 구조는 쪼개고(정규화) → 꺼내 쓰고(DML) → 동시에·장애에도 지킨다(트랜잭션)</b>.'),
 ('asst','smile','SQL은 실습실에서 많이 쳐 봐서 자신 있어요. 정규화가 제일 헷갈려요.'),
 ('fly','clip','정규화는 “이 칸은 누가 결정하나?”만 물으면 돼. 오늘 대결이 그걸 보여 줄 거야.'),
 ('sia','smile','저는 오늘 인턴으로 같이 복습해요! 모의 문제 끝까지 풀어 볼게요.'),
 ('doc','front','틀린 문항은 실패가 아니라 돌아갈 주차를 알려 주는 표지판이다. 막히면 해설 끝 (n주차)로 가면 된다.')],
crew=[('doc','front','묶음별 핵심과 헷갈리는 짝 정리, 판정'),('asst','smile','실습 진행, 점수 발표'),('fly','clip','단계별로 정규화하는 쪽 (오늘 대결)'),('robo','smile','결정자로 한 번에 묶는 쪽 (오늘 대결)'),('sia','smile','인턴 시아 — 같이 복습 (판정·숫자 발표는 하지 않음)')],
recap='9~14주 한 줄 흐름: <b>CREATE·제약 조건</b>으로 규칙을 새긴 표를 만들고 → <b>SELECT·집계·JOIN·부속 질의</b>로 꺼내고 → 처음부터 <b>요구 분석 → ERD → 변환 규칙</b>으로 설계하며 → <b>이상 현상</b>은 함수 종속을 보고 <b>정규형</b>으로 고치고 → <b>트랜잭션</b>으로 장애와 동시 수정에서 지키고 → 표에 안 맞는 데이터는 <b>NoSQL·색인·웨어하우스</b>로.',
notion=[('15주차 : 기말고사 (노션)', NOTION+'1ab17a4520ed81fcbd0feda07fa804cc', '기말고사 회차 페이지 — 시험 공지는 강의 공지를 따름'),
        ('SQL 기본 문법 (교재 예제 코드 수정) (노션)', NOTION+'1ab17a4520ed815294ccd69faa520526', '9·10주 실습의 원본'),
        ('SQL 문법 정리 (DCL, TCL 추가) (노션)', NOTION+'1ab17a4520ed8198b223c82808756ddd', '13주 실습의 원본')],
why_title='이 REVIEW를 쓰는 법',
why=[('지도 먼저','아래 표의 한 줄 요약을 소리 내어 읽어 보세요. 막히는 줄이 복습할 주차입니다.'),
     ('실습실은 손으로','④ 묶음의 SQL 버튼은 누르기 전에 결과 행 수를 먼저 적어 보세요.'),
     ('틀린 문항이 지도','모의 문제 해설 끝의 (n주차) 페이지로 돌아가 그 칸의 퀴즈를 다시 풉니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>주차</th><th>교재</th><th>한 줄 요약</th><th>대결 결과 (교훈)</th><th>페이지</th></tr></thead><tbody>
<tr><td>9</td><td>7장</td><td>CREATE·ALTER·DROP, PK·FK·UNIQUE·CHECK·NOT NULL·DEFAULT, ON DELETE</td><td>주판봇 승 (규칙은 표에 새긴다)</td><td><a href="w09_sql_ddl.html">열기</a></td></tr>
<tr><td>10</td><td>7장</td><td>SELECT·WHERE·집계·GROUP BY·HAVING·JOIN·부속 질의, INSERT·UPDATE·DELETE, 뷰</td><td>무승부 (IN과 JOIN — 중복에 주의)</td><td><a href="w10_sql_dml.html">열기</a></td></tr>
<tr><td>11</td><td>8장</td><td>요구 분석 → 개념 → 논리(변환 규칙 5) → 물리 → 구현, 한빛 마트</td><td>초파리 승 (설계 먼저)</td><td><a href="w11_database_design_process.html">열기</a></td></tr>
<tr><td>12</td><td>9장</td><td>이상 현상 3, 함수 종속, 1NF→2NF→3NF→BCNF, 반정규화</td><td>조건부 (조회 위주 vs 변경 위주)</td><td><a href="w12_normalization.html">열기</a></td></tr>
<tr><td>13</td><td>10장</td><td>ACID, COMMIT·ROLLBACK, 로그 REDO·UNDO, 갱신 분실·로킹·2PL</td><td>초파리 승 (잠금 없으면 입금이 사라짐)</td><td><a href="w13_transaction_recovery_concurrency.html">열기</a></td></tr>
<tr><td>14</td><td>—</td><td>비정형·3V, NoSQL·NewSQL, 문서형, 색인, OLTP·OLAP</td><td>주판봇 승 (피드는 문서형이 덜 읽음)</td><td><a href="w14_database_applications.html">열기</a></td></tr></tbody></table></div><p style="font-size:14px;color:#5b6874">교재 장 번호는 강의 진도에 맞춘 대응이며, 14주차는 강의 교안·노션 자료 중심입니다.</p>''',
why_say=('sia','smile','9~14주 대결 결과 칸을 보니 초파리 2승, 주판봇 2승, 무승부와 조건부가 한 번씩이에요. 늘 이기는 방식은 없다는 거죠?'),
steps=[
dict(id='lv1', short='SQL', title='묶음 ① SQL — 데이터 정의와 조작 (9~10주)', concept='SQL 복습', en='review of sql', cid='lab:concept/review-sql',
 tag='복습: 9~10주차 · 한빛 마트 종합 실습', analogy='표 만들기와 표 읽기',
 situation='시험에는 “이 SQL의 결과는?”, “오류가 나는 이유는?”, “빈칸에 들어갈 절은?”이 나옵니다. 아래 실습실의 버튼을 누르기 전에 결과를 먼저 예상해 보세요.',
 pair=(('핵심','<b>정의(DDL)</b> CREATE · ALTER · DROP · TRUNCATE<br><b>제약</b> PRIMARY KEY · FOREIGN KEY(ON DELETE CASCADE / SET NULL / RESTRICT) · UNIQUE · NOT NULL · CHECK · DEFAULT<br><b>조작(DML)</b> SELECT · INSERT · UPDATE · DELETE<br><b>실행 순서</b> FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY'),
       ('헷갈리는 짝','<b>WHERE</b>(줄 거르기, 집계 불가) vs <b>HAVING</b>(묶음 거르기) · <b>=</b>(값 하나) vs <b>IN</b>(여러 값) · <b>COUNT(*)</b>(NULL 포함) vs <b>COUNT(칸)</b>(NULL 제외) · <b>DELETE</b>(행, WHERE 가능) vs <b>DROP</b>(표 자체) vs <b>TRUNCATE</b>(모든 행)')),
 panel='<div class="sqllab" id="lab15" data-lab="lab15"></div>', panel_title='SQL 종합 실습 — 한빛 마트 (회원 5 · 상품 5 · 주문 8)',
 sim='기말 SQL 종합 실습',
 explain='<p><b>손으로 먼저:</b> ② 「상품별 주문 수량 합계 ≥ 30」은 p01(5+45+22=72), p02(36), p03(10+8=18), p04(19), p05(30) → 조건을 만족하는 상품은 p01·p02·p05 세 개입니다. 실습실 결과와 맞는지 확인하세요. ⑤의 CASCADE는 회원을 지우면 그 회원의 주문도 함께 사라지는 것을 보여 줍니다(9주차 ON DELETE 비교).</p>',
 limit='SQL은 정리했습니다. 다음 묶음은 그 표를 처음에 어떻게 설계하는가입니다.', limit_label='설계 단계 복습이 남음',
 quiz=[dict(q='SELECT 상품번호, SUM(수량) FROM 주문 GROUP BY 상품번호 HAVING SUM(수량) >= 30; 의 결과 행 수는? (위 데이터)',o=['2','3','4','5'],a=1,why='p01 72, p02 36, p05 30이 조건을 만족 — 3행입니다.'),
       dict(q='회원 표의 기본키를 참조하는 주문 표 외래키에 ON DELETE CASCADE가 있다. 회원 melon을 지우면?',o=['오류로 거부된다','melon의 주문도 함께 삭제된다','주문의 회원아이디가 NULL이 된다','아무 변화 없다'],a=1,why='CASCADE는 참조하는 행을 함께 삭제합니다. RESTRICT면 거부, SET NULL이면 NULL.')]),
dict(id='lv2', short='설계', title='묶음 ② 데이터베이스 설계와 변환 규칙 (11주)', concept='설계 5단계 복습', en='review of database design', cid='lab:concept/review-design',
 tag='복습: 11주차', analogy='주문서 → 설계도 → 시공',
 situation='단계 순서와 결과물 짝, 그리고 “이 ERD 조각은 릴레이션 몇 개?”가 단골입니다.',
 pair=(('핵심','요구 사항 분석(명세서) → 개념적 설계(E-R 다이어그램) → 논리적 설계(릴레이션 스키마) → 물리적 설계(자료형·색인) → 구현(SQL). 변환 규칙: ① 개체 ② N:M → 새 릴레이션 ③ 1:N → N쪽 FK ④ 1:1 → 한쪽 FK ⑤ 다중값 → 별도 릴레이션'),
       ('헷갈리는 짝','<b>개념적</b>(DBMS 무관, ERD) vs <b>논리적</b>(DBMS 종류에 맞춤, 릴레이션) · 1:N은 <b>새 표 없음</b>, N:M은 <b>새 표</b> · 약한 개체의 FK는 <b>기본키에 포함</b> · 1:1 모두 필수면 <b>합침</b>')),
 panel='''<p style="margin-top:0">ERD 조각마다 적용할 규칙과 새로 생기는 릴레이션 수를 떠올린 뒤 눌러 확인하세요.</p><div class="chips" id="er15"></div><div class="insight" id="er15o"></div>''',
 panel_title='짝 맞추기 — ERD 조각 → 변환 규칙',
 sim='ERD 조각 변환 규칙 복습',
 explain='<p><b>릴레이션 수 세기 공식(이 강의의 규칙대로):</b> 개체 수 + N:M 관계 수 + 다중값 속성 수 (+ 1:1 모두 필수로 합친 경우 −1). 한빛 마트는 4 + 1 + 0 = 5였습니다.</p>',
 limit='설계까지 복습했습니다. 다음은 이미 만든 표가 나쁜 구조인지 판정하는 정규화입니다.', limit_label='정규화 복습이 남음',
 quiz=[dict(q='설계 단계와 결과물의 짝으로 옳지 않은 것은?',o=['요구 사항 분석 — 요구 사항 명세서','개념적 설계 — E-R 다이어그램','논리적 설계 — 색인 목록','구현 — SQL로 만든 데이터베이스'],a=2,why='논리적 설계의 결과물은 릴레이션 스키마입니다. 색인은 물리적 설계.'),
       dict(q='개체 4개, N:M 관계 2개, 1:N 관계 1개, 다중값 속성 1개. 릴레이션 수는? (계산)',o=['5','6','7','8'],a=2,why='4 + 2 + 1 = 7. 1:N은 외래키로 처리.')]),
dict(id='lv3', short='정규화', title='묶음 ③ 정규화 (12주)', concept='정규화 복습', en='review of normalization', cid='lab:concept/review-normalization',
 tag='복습: 12주차', analogy='한 사실은 한 곳에',
 situation='“어떤 이상 현상인가?”, “몇 정규형인가?”, “어떻게 분해하나?”가 나옵니다. 낱말 카드로 용어를 먼저 점검하세요.',
 pair=(('핵심','이상 현상: 삽입·갱신·삭제 / 함수 종속 X → Y(결정자 X) / 1NF 원자값 → 2NF 부분 종속 제거 → 3NF 이행 종속 제거 → BCNF 모든 결정자가 후보키 / 무손실 분해 / 반정규화는 조회 위주일 때'),
       ('헷갈리는 짝','<b>부분</b> 종속(기본키 일부에 종속, 2NF) vs <b>이행</b> 종속(X→Y→Z, 3NF) · <b>3NF</b> vs <b>BCNF</b>(후보키가 아닌 결정자가 남았나) · 1NF는 중복을 <b>줄이지 않음</b>')),
 panel='<div class="flash" data-cards="c1"></div>', panel_title='낱말 카드 — 눌러서 뒤집기 (9~14주 16장)',
 sim='9~14주 낱말 카드',
 explain='<p><b>판정 순서 한 줄:</b> ① 한 칸에 값이 여럿? → 1NF 아님 ② 기본키가 여러 칸인데 일부만으로 정해지는 칸? → 2NF 아님 ③ 기본키가 아닌 칸이 다른 칸을 정하나? → 3NF 아님 ④ 후보키가 아닌 결정자가 있나? → BCNF 아님.</p>',
 aicheck='<p>AI에게 “도서대출(대출번호, 회원ID, 회원이름, 회원등급, 도서ID)를 정규화해 줘”라고 하면 “이미 3NF입니다”라는 답이 나오기도 합니다. 위 판정 순서 ③을 직접 적용해 보세요: 회원ID → 회원이름·회원등급이 있으므로 이행 종속 — 3NF가 아닙니다(12주 4칸). AI의 정규화 결과는 <b>함수 종속 목록을 먼저 적게 하고</b> 그 목록으로 검사하세요.</p>',
 limit='구조까지 복습했습니다. 마지막 묶음은 그 구조를 동시에·장애 속에서 지키는 법과 응용 기술입니다.', limit_label='트랜잭션·응용 기술 복습이 남음',
 quiz=[dict(q='수강(학번, 과목번호, 이름, 성적)에서 학번 → 이름이다. 몇 정규형 위반인가?',o=['1NF','2NF','3NF','BCNF만'],a=1,why='기본키 {학번, 과목번호}의 일부(학번)에 이름이 종속 — 부분 종속, 2NF 위반.'),
       dict(q='1NF 표로 바꾸면 중복은?',o=['반드시 사라진다','오히려 늘 수 있다','항상 그대로다','표가 하나로 합쳐진다'],a=1,why='다중값을 줄로 펼치면 다른 칸이 반복되어 중복이 늘 수 있습니다(12주 3칸: 3줄 → 5줄).')]),
dict(id='lv4', short='트랜잭션·응용', title='묶음 ④ 트랜잭션·회복·병행 제어와 응용 기술 (13~14주)', concept='트랜잭션과 응용 기술 복습', en='review of transactions and applications', cid='lab:concept/review-transaction-application',
 tag='복습: 13~14주차', analogy='전표와 상자',
 situation='상황 문장을 주고 “어느 ACID 성질?”, “REDO인가 UNDO인가?”, “OLTP인가 OLAP인가?”를 묻는 문제가 나옵니다.',
 pair=(('핵심','ACID / TCL: START TRANSACTION·COMMIT·ROLLBACK, DCL: GRANT·REVOKE / 회복: 커밋 있음 → REDO, 없음 → UNDO, 검사 시점 이전 커밋 → 없음 / 병행 제어: 갱신 분실 → 로킹, 2PL, 교착 상태 / 응용: 3V, NoSQL(키-값·문서·열·그래프), 색인, OLTP vs OLAP'),
       ('헷갈리는 짝','<b>원자성</b>(전부/전무) vs <b>지속성</b>(커밋 후 영구) · <b>REDO</b>(커밋됨, 다시 반영) vs <b>UNDO</b>(미완료, 되돌림) · <b>2PL</b>은 직렬 가능성 보장, 교착 상태는 <b>막지 못함</b> · 색인은 조회 빠름, <b>쓰기 비용</b> 증가')),
 panel='''<p style="margin-top:0">상황을 누르면 답과 근거가 나옵니다. 누르기 전에 먼저 말해 보세요.</p><div class="chips" id="sc15"></div><div class="insight" id="sc15o"></div>''',
 panel_title='상황 카드 — 어느 개념인가',
 sim='트랜잭션·응용 상황 판정',
 explain='<p>13주의 질문은 “<b>무엇이 지키는가</b>”(회복 vs 병행 제어), 14주의 질문은 “<b>데이터 모양과 쓰는 방식</b>”(표 vs 문서, 운영 vs 분석)으로 정리됩니다.</p>',
 aicheck='<p>AI가 “2단계 로킹을 쓰면 교착 상태가 생기지 않는다”라고 요약하는 경우가 있습니다. 반대입니다 — 2PL은 직렬 가능성을 보장하지만 교착 상태는 생길 수 있습니다(13주 4칸). AI 요약을 볼 때는 “보장한다/막는다” 같은 단정 표현부터 교재와 대조하세요.</p>',
 limit='여기까지가 기말 범위입니다. 아래 대결과 모의 문제 20개로 마무리하세요.', limit_label='모의 문제로 최종 점검',
 quiz=[dict(q='COMMIT 직후 정전이 났는데 재시작 후 결과가 남아 있었다. 어느 성질인가?',o=['원자성','일관성','격리성','지속성'],a=3,why='커밋된 결과의 영구 보존 — 지속성.'),
       dict(q='2단계 로킹 규약에 대한 설명으로 옳은 것은?',o=['교착 상태를 완전히 막는다','직렬 가능성을 보장하지만 교착 상태는 생길 수 있다','unlock 뒤에 다시 lock할 수 있다','읽기에는 쓰지 않는다'],a=1,why='확장 단계 → 축소 단계. 직렬 가능성은 보장, 교착 상태는 별도로 처리.')]),
],
nav_extra=[('mock','모의 20')],
extra_sections=['''<section class="level" id="mock"><div class="wrap"><h2>모의 문제 20 — 객관식</h2>
<p>정의형과 상황·계산형이 섞여 있습니다. 해설 끝의 (n주차)가 돌아갈 페이지입니다. 이 문항은 연습용이며 실제 시험 문제가 아닙니다.</p>
<div class="quiz" data-quiz="mock"></div>
<div class="say"><img data-who="sia" data-mood="smile" width="56" height="56" alt="" aria-hidden="true"><div class="bub"><span class="who w-sia">인턴 시아</span><p>계산형은 손으로 한 번 더 세어 봤어요. 틀린 문항의 주차 페이지로 돌아가 그 칸의 퀴즈를 다시 풀면 돼요!</p></div></div>
</div></section>'''],
extra_quiz={'mock':[m[1] for m in MOCK]},
duel=dict(q='정규화 — 단계별(1NF→2NF→3NF) vs 결정자로 한 번에',
 intro='12주의 도서 대여 비정규 표(대여번호·도서ID·도서명·회원ID·회원명·연락처·대여일)를 3NF로 만듭니다. 초파리는 <b>1NF → 2NF → 3NF 단계별로</b>, 주판봇은 <b>함수 종속의 결정자마다 표 하나씩 한 번에</b> 묶습니다. 결과 스키마를 비교합니다.',
 fly_pick='단계별 — 1NF → 2NF → 3NF', fly_line='한 단계씩 확인해야 빠뜨리지 않지.',
 robo_pick='결정자로 한 번에 묶기', robo_line='누가 무엇을 결정하는지만 알면 바로 표가 나오잖아!',
 metric='최종 릴레이션 수 · 남은 이상 현상 (같으면 무승부)', higher=False, step=3,
 after='<div id="duel15t"></div>',
 run='return PAGE.duel();',
 announce='return "초파리 <b>"+r.fly+"개</b> 표, 주판봇 <b>"+r.robo+"개</b> 표 — 표 구성이 "+(r.same?"<b>똑같았어요</b>":"달랐어요")+". 남은 이상 현상은 둘 다 0개.";',
 verdict='return "같은 함수 종속에서 출발하면 같은 스키마에 도착한다. 단계는 빠뜨리지 않게 돕는 점검표, 결정자는 그 점검의 핵심. 무승부.";'),
summary='''<div class="tbl"><table><thead><tr><th>헷갈리는 짝</th><th>구별하는 한마디</th></tr></thead><tbody>
<tr><td>WHERE / HAVING</td><td>줄 거르기 / 묶음 거르기(집계)</td></tr>
<tr><td>DELETE / DROP / TRUNCATE</td><td>골라 지우기 / 표 자체 / 모든 행(구조 유지)</td></tr>
<tr><td>CASCADE / SET NULL / RESTRICT</td><td>같이 지움 / NULL로 / 거부</td></tr>
<tr><td>개념적 / 논리적 설계</td><td>ERD(DBMS 무관) / 릴레이션 스키마</td></tr>
<tr><td>1:N / N:M 변환</td><td>N쪽에 FK / 새 릴레이션</td></tr>
<tr><td>부분 / 이행 종속</td><td>기본키 일부에 종속(2NF) / X→Y→Z(3NF)</td></tr>
<tr><td>REDO / UNDO</td><td>커밋됨 → 다시 반영 / 미완료 → 되돌림</td></tr>
<tr><td>OLTP / OLAP</td><td>운영(짧은 거래) / 분석(대량 집계)</td></tr></tbody></table></div>
<div class="cards"><div><b>대결의 한계</b> 이 표는 함수 종속이 분명했기 때문에 두 방법이 같은 답에 도착했습니다. 종속을 잘못 찾으면 어느 방법이든 틀린 스키마가 나옵니다. 또 BCNF 분해는 경우에 따라 함수 종속 일부를 잃을 수 있어 “한 번에”가 늘 간단하지는 않습니다.</div></div>''',
outro=[('doc','front','한 학기의 세 줄: ① 데이터를 함께 쓰려면 DB와 DBMS ② 요구 → ERD → 릴레이션 → 정규화 → SQL ③ 트랜잭션으로 지키고, 데이터 모양에 맞는 도구를 고른다.'),
       ('fly','coffee','이번엔 비겼네. 결국 둘 다 “이 칸은 누가 결정하나?”를 물었으니까.'),
       ('robo','happy','한 학기 동안 4번이나 이겼어! 실격도 한 번 있었지만… 이번엔 비겼으니 지진 않았다고!'),
       ('asst','proud','모의 20문항 다 풀었어요! 틀린 건 12주랑 13주 페이지로 돌아가서 다시 볼게요. 모두 시험 잘 봐요!')],
next_note='<p class="recap"><b>한 학기 지도:</b> <a href="../index.html">강의 첫 화면</a>에서 1~15주차를 다시 열 수 있습니다. 1~7주 복습은 <a href="w08_midterm_review.html">중간 REVIEW</a>.</p>',
gloss={'HAVING':('HAVING','용어','GROUP BY로 묶은 결과를 집계 조건으로 거르는 절.','having-clause','lv1'),
 'CASCADE':('ON DELETE CASCADE','용어','참조되는 행을 지우면 참조하는 행도 함께 지우는 외래키 옵션.','on-delete-cascade','lv1'),
 '변환 규칙':('변환 규칙','개념','E-R 다이어그램을 릴레이션 스키마로 바꾸는 다섯 규칙.','mapping-rules-review','lv2'),
 '함수 종속':('함수 종속','개념','X의 값이 Y의 값을 하나로 결정하는 관계 X → Y.','functional-dependency-review','lv3'),
 'REDO':('REDO','용어','커밋된 트랜잭션의 변경을 로그의 변경 후 값으로 다시 반영하는 회복 작업.','redo','lv4'),
 'UNDO':('UNDO','용어','미완료 트랜잭션의 변경을 로그의 변경 전 값으로 되돌리는 회복 작업.','undo','lv4')},
facts=[('F01','시험은 강의에서 다룬 주요 개념·사례의 객관식·단답식','문헌 사실','ahn2025syllabus','lv1','강의 개요 「시험 방식」'),
       ('F02','15주차는 기말고사 회차','문헌 사실','ahn2025w15','lv1','노션 Schedule'),
       ('F03','성적 반영: 출석 10%, 중간고사 40%, 기말고사 40%, 과제 10%','문헌 사실','ahn2025syllabus','lv1','강의 개요 「성적평가」')],
refs=[dict(id='ahn2025syllabus',type='webpage',title='데이터베이스설계 (2025년 2학기) 강의 개요',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'2025-2-1ab17a4520ed81cd9040dbae826a48ad',role='primary'),
      dict(id='ahn2025w15',type='webpage',title='15주차 : 기말고사',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed81fcbd0feda07fa804cc',role='primary'),
      dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='background',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='ahn2025w04erd',type='report',title='데이터베이스 설계 4주차 — ERD 작성, 관계 데이터 모델링, 정규화 과정 및 실무 적용',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='background')],
models=['모의 문제 20개 (이 페이지가 만든 연습 문제 — 실제 시험 문제 아님)','한빛 마트 종합 실습 데이터 (교재 8장 사례를 따라 만든 예시값)','대결의 두 분해 결과 (12주 도서 대여 예제의 함수 종속으로 계산)'],
cover_alt='연구실 복도 끝 두 번째 초록 문이 열려 있고, 그 안 벽에 9~14번 방의 지도와 졸업 모자가 걸린 표지 (대체 그림)',
prereq=['14','08'],
cards={'c1':[['DDL','CREATE · ALTER · DROP · TRUNCATE — 구조'],['DML','SELECT · INSERT · UPDATE · DELETE — 데이터'],['DCL / TCL','GRANT · REVOKE / COMMIT · ROLLBACK'],['CHECK','값의 범위 규칙 (나이 >= 0)'],['HAVING','묶음(그룹)을 집계 조건으로 거르기'],['IN vs =','여러 값 비교 vs 값 하나 비교'],['개념적 설계','요구 → E-R 다이어그램 (DBMS 무관)'],['규칙 2','N:M 관계 → 새 릴레이션 (양쪽 PK가 FK)'],['규칙 3','1:N 관계 → N쪽에 FK (새 표 없음)'],['갱신 이상','중복 값 일부만 바뀌어 불일치'],['2NF','부분 함수 종속 제거'],['3NF','이행 함수 종속 제거'],['BCNF','모든 결정자가 후보키'],['ACID','원자성 · 일관성 · 격리성 · 지속성'],['REDO / UNDO','커밋됨 → 다시 / 미완료 → 되돌림'],['OLTP / OLAP','운영(짧은 거래) / 분석(대량 집계)']]},
js=r'''
var $=LAB.$,$$=LAB.$$;
var ER=[['[학생] N —◇수강◇— M [과목]','규칙 2 — 수강(학번 FK, 과목번호 FK) 새 릴레이션. +1개'],['[학과] 1 —◇소속◇— N [학생]','규칙 3 — 학생에 학과번호 FK. 새 표 0개'],['[사원] 1 —◇부양◇— N [[부양가족]] (약한 개체)','규칙 3-2 — 부양가족(사원번호 FK, 이름)이 기본키. 개체 자체가 1개'],['[사원] 1 —◇관리◇— 1 [부서] (부서는 필수 참여)','규칙 4-2 — 필수 참여 쪽(부서)에 관리자 사원번호 FK. 새 표 0개'],['[회원] 연락처{ } (이중 타원)','규칙 5 — 회원연락처(회원아이디 FK, 연락처) 별도 릴레이션. +1개']];
var er=$('#er15');ER.forEach(function(e){var b=document.createElement('button');b.type='button';b.className='bt';b.style.textAlign='left';b.textContent=e[0];b.onclick=function(){[].forEach.call(er.children,function(x){x.setAttribute('aria-pressed',x===b);});$('#er15o').innerHTML=e[1];};er.appendChild(b);});
var SC=[['출금 후 입금에서 오류 → 출금도 취소','원자성 (회복 기능) — 13주 1칸'],['로그: <T7, start> … 장애 (commit 없음)','UNDO — 13주 3칸'],['검사 시점 이후 <T8, commit>','REDO — 13주 3칸'],['두 창구 동시 입금, 한 건이 사라짐','갱신 분실 → 로킹 — 13주 4칸'],['T1은 Y를, T2는 X를 기다리며 서로 멈춤','교착 상태 — 한쪽을 철회해 해결'],['글마다 태그 개수가 다른 SNS 피드','문서형(NoSQL) 검토 — 14주 2칸'],['3년치 지역·월별 매출 분석','OLAP · 데이터 웨어하우스 — 14주 4칸'],['인벤토리 조회 3초 → 0.1초','색인 추가 (RPG 사례) — 14주 3칸']];
var sc=$('#sc15');SC.forEach(function(e){var b=document.createElement('button');b.type='button';b.className='bt';b.style.textAlign='left';b.textContent=e[0];b.onclick=function(){[].forEach.call(sc.children,function(x){x.setAttribute('aria-pressed',x===b);});$('#sc15o').innerHTML='<b>'+e[1]+'</b>';};sc.appendChild(b);});
/* 대결: 함수 종속에서 두 방법으로 스키마 계산 */
var FD=[['대여번호',['도서ID','회원ID','대여일']],['도서ID',['도서명']],['회원ID',['회원명']]],MV={'회원ID':'연락처'};
function key(t){return t[0]+'('+t[1].join(', ')+')';}
function byDeterminant(){var out=FD.map(function(f){return [f[0],[f[0]].concat(f[1])];});Object.keys(MV).forEach(function(k){out.push([k+'+'+MV[k],[k,MV[k]]]);});return out.map(function(t){return t[1];});}
function stepwise(){var log=[],t1=['대여번호','도서ID','도서명','회원ID','회원명','연락처','대여일'];log.push('1NF: 연락처를 원자값으로 → 기본키 {대여번호, 연락처}');
 var rel=[['회원ID','연락처']];log.push('2NF: 연락처는 회원ID가 정하는 다중값 → 회원연락처 분리, 남은 표의 기본키 {대여번호}');
 var r=['대여번호','도서ID','도서명','회원ID','회원명','대여일'];log.push('3NF: 도서ID → 도서명, 회원ID → 회원명 (이행 종속) → 도서·회원 분리');
 rel.push(['도서ID','도서명']);rel.push(['회원ID','회원명']);rel.push(['대여번호','도서ID','회원ID','대여일']);return {rel:rel,log:log};}
PAGE.duel=function(){var A=stepwise(),B=byDeterminant();var sa=A.rel.map(function(x){return x.join(',');}).sort(),sb=B.map(function(x){return x.join(',');}).sort(),same=JSON.stringify(sa)===JSON.stringify(sb);
 $('#duel15t').innerHTML=LAB.tableHTML(['초파리 (단계별)','주판봇 (결정자별)'],sa.map(function(x,i){return ['('+x+')','('+(sb[i]||'')+')'];}),{cap:'최종 릴레이션 (가나다순 정렬) — 첫 칸이 기본키의 시작'})+'<p class="cvcap">초파리의 과정: '+A.log.join(' → ')+'</p>';
 return {fly:sa.length,robo:sb.length,flyTxt:sa.length+'개 · 이상 0',roboTxt:sb.length+'개 · 이상 0',same:same,draw:true};};
''',
labs=('lab15:{setup:%s,presets:[{t:"① 주문 + 회원 + 상품 JOIN",q:"SELECT o.주문번호, m.이름, p.상품명, o.수량\\nFROM 주문 o JOIN 회원 m ON o.회원아이디 = m.회원아이디\\nJOIN 상품 p ON o.상품번호 = p.상품번호\\nORDER BY o.주문번호;"},{t:"② GROUP BY · HAVING",q:"SELECT 상품번호, SUM(수량) AS 합계\\nFROM 주문\\nGROUP BY 상품번호\\nHAVING SUM(수량) >= 30\\nORDER BY 합계 DESC;"},{t:"③ 부속 질의 (IN)",q:"SELECT 이름, 등급 FROM 회원\\nWHERE 회원아이디 IN (SELECT 회원아이디 FROM 주문 WHERE 상품번호 = \'p01\');"},{t:"④ 뷰 만들기",q:"CREATE VIEW 우수회원 AS\\nSELECT 회원아이디, 이름, 적립금 FROM 회원 WHERE 등급 IN (\'gold\', \'vip\');\\nSELECT * FROM 우수회원 ORDER BY 적립금 DESC;"},{t:"⑤ CASCADE 확인 (트랜잭션 안에서)",q:"START TRANSACTION;\\nDELETE FROM 회원 WHERE 회원아이디 = \'melon\';\\nSELECT COUNT(*) AS 남은주문 FROM 주문;\\nROLLBACK;\\nSELECT COUNT(*) AS 롤백후주문 FROM 주문;"},{t:"⑥ 위반 — CHECK(나이)",q:"INSERT INTO 회원 (회원아이디, 이름, 나이) VALUES (\'kiwi\', \'이도윤\', -1);"},{t:"⑦ 위반 — 외래키",q:"INSERT INTO 주문 VALUES (\'o09\', \'grape\', \'p01\', 1, \'2022-05-01\');"},{t:"⑧ 위반 — CHECK(재고)",q:"UPDATE 상품 SET 재고량 = 재고량 - 3000 WHERE 상품번호 = \'p05\';"}],ready:"한빛 마트: 회원 5 · 상품 5 · 주문 8. 버튼을 누르기 전에 결과 행 수를 먼저 적어 보세요."}') % ('"' + SETUP.replace('"', '\\"') + '"'),
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'9~10주차 — SQL 데이터 정의(제약 조건)와 데이터 조작(질의·집계·조인·부속 질의·뷰).','lv2':'11주차 — 설계 5단계와 E-R 다이어그램의 릴레이션 변환 규칙.','lv3':'12주차 — 이상 현상, 함수 종속, 1NF·2NF·3NF·BCNF와 반정규화.','lv4':'13~14주차 — 트랜잭션·회복·병행 제어와 NoSQL·색인·OLAP 등 응용 기술.'}[s['id']]

# ── 5칸: 종합 실습 — SQL 자동 채점 과제 (2026-11 보강) ─────────────────
PAGE['steps'][3]['limit'] = '개념 복습은 끝났습니다. 마지막으로 한빛 마트 데이터로 SQL을 직접 써서 채점받아 봅니다.'
PAGE['steps'][3]['limit_label'] = 'SQL을 직접 써서 확인하는 종합 실습이 남음'
TASKS = [
 ('gold 등급 회원의 이름과 적립금을 적립금이 많은 순으로', "SELECT 이름, 적립금 FROM 회원 WHERE 등급 = 'gold' ORDER BY 적립금 DESC;", True, 'WHERE + ORDER BY (10주)'),
 ('제조업체별 상품 수 (제조업체, 상품수)', "SELECT 제조업체, COUNT(*) AS 상품수 FROM 상품 GROUP BY 제조업체;", False, 'GROUP BY + COUNT (10주)'),
 ('주문 수량 합계가 30 이상인 상품번호와 합계', "SELECT 상품번호, SUM(수량) AS 합계 FROM 주문 GROUP BY 상품번호 HAVING SUM(수량) >= 30;", False, 'HAVING (10주)'),
 ('한 번도 주문하지 않은 회원의 이름', "SELECT 이름 FROM 회원 WHERE 회원아이디 NOT IN (SELECT 회원아이디 FROM 주문);", False, '부속 질의 NOT IN 또는 LEFT JOIN … IS NULL (10주)'),
 ('주문번호, 주문한 회원 이름, 상품명을 주문번호 순으로', "SELECT o.주문번호, m.이름, p.상품명 FROM 주문 o JOIN 회원 m ON o.회원아이디 = m.회원아이디 JOIN 상품 p ON o.상품번호 = p.상품번호 ORDER BY o.주문번호;", True, '세 표 JOIN (7·10주)'),
 ('평균 단가보다 비싼 상품의 상품명과 단가', "SELECT 상품명, 단가 FROM 상품 WHERE 단가 > (SELECT AVG(단가) FROM 상품);", False, '스칼라 부속 질의 (10주)'),
 ('2022년 2월 1일 이후(그날 포함) 주문 건수 하나', "SELECT COUNT(*) FROM 주문 WHERE 주문일자 >= '2022-02-01';", False, '날짜 조건 (10주)'),
 ('총 주문 금액(수량 × 단가)이 가장 큰 회원의 이름과 금액 한 줄', "SELECT m.이름, SUM(o.수량 * p.단가) AS 금액 FROM 주문 o JOIN 회원 m ON o.회원아이디 = m.회원아이디 JOIN 상품 p ON o.상품번호 = p.상품번호 GROUP BY m.이름 ORDER BY 금액 DESC LIMIT 1;", True, 'JOIN + 집계 + 정렬 + LIMIT (10주)')]
PAGE['steps'].append(dict(id='lv5', short='종합 실습', title='종합 실습 — 한빛 마트 SQL 과제 8문항 (자동 채점)', concept='SQL 종합 실습', en='sql comprehensive practice', cid='lab:concept/review-sql-practice',
 tag='실습: 자동 채점', analogy='모의 실기 시험',
 situation='위 ①칸 실습실과 같은 한빛 마트 데이터(회원 5 · 상품 5 · 주문 8)입니다. 문항마다 SQL을 직접 쓰고 「채점」을 누르면, 실습실 엔진이 정답 질의와 <b>결과 표를 비교</b>해 맞았는지 알려 줍니다. 칸 이름(별칭)은 달라도 되지만 값과 칸 순서는 같아야 합니다. 정렬이 요구된 문항은 순서까지 봅니다.',
 pair=(('시험에서는','“결과를 쓰시오”, “빈칸을 채우시오” 문제는 결국 SQL이 무엇을 돌려주는지 아는지를 묻습니다. 직접 써 보고 결과를 맞혀 본 문장은 시험장에서 바로 떠오릅니다.'),
       ('채점기는','내 SQL과 정답 SQL을 같은 데이터에서 실행해 결과 행을 비교합니다. 같은 결과를 내는 다른 SQL(예: NOT IN 대신 LEFT JOIN … IS NULL)도 정답입니다 — 시험에서도 “결과”가 기준입니다.')),
 panel='<div id="gr15"></div><div class="dk-row" id="gr15k" style="margin-top:10px"></div>',
 panel_title='SQL 과제 8문항 — 쓰고 채점하기',
 sim='SQL 자동 채점 과제',
 explain='<p><b>막혔을 때:</b> 「힌트」는 쓸 문법의 이름과 주차를 알려 줍니다. 그래도 막히면 「정답 보기」를 열고, 정답을 그대로 베끼지 말고 <b>한 절씩 지워 가며</b>(ORDER BY를 빼면? HAVING을 WHERE로 바꾸면?) 결과가 어떻게 바뀌는지 보세요. 틀린 결과에서 배우는 것이 시험에 더 오래 남습니다.</p>',
 aicheck='<p>AI에게 과제 SQL을 받아 붙여 넣으면 맞을 때가 많습니다. 다만 4번처럼 <code>NOT IN</code>을 쓰는 문제에서 부속 질의 결과에 NULL이 섞이면 결과가 0행이 되는 함정이 있습니다(실제 MariaDB 동작). AI 답을 채점기에 넣어 맞더라도, “주문 표의 회원아이디에 NULL이 있으면?”을 스스로 물어보세요.</p>',
 limit='여기까지가 기말 범위입니다. 아래 대결과 모의 문제 20개, 그리고 마지막 실전 연습장에서 준비도를 확인하세요.', limit_label='모의 문제로 최종 점검',
 say=('sia','smile','8문항 다 맞히면 아래 계기판의 SQL 칸이 8/8이 돼요!'),
 quiz=[dict(q='채점기가 “행 수는 같은데 결과가 다르다”고 했다. 가장 먼저 확인할 것은?',o=['DB를 다시 만든다','SELECT의 칸 순서와 ORDER BY(정렬 요구 문항)','테이블 이름','세미콜론'],a=1,why='같은 행 수인데 다르면 칸 순서가 바뀌었거나 정렬 순서가 다른 경우가 많습니다.'),
       dict(q='“한 번도 주문하지 않은 회원”을 구하는 SQL로 알맞지 않은 것은?',o=['WHERE 회원아이디 NOT IN (SELECT 회원아이디 FROM 주문)','LEFT JOIN 주문 … WHERE 주문.주문번호 IS NULL','WHERE 회원아이디 IN (SELECT 회원아이디 FROM 주문)','WHERE NOT EXISTS (SELECT * FROM 주문 o WHERE o.회원아이디 = 회원.회원아이디)'],a=2,why='IN은 주문한 회원을 고릅니다. 나머지 셋은 주문하지 않은 회원을 고르는 같은 결과의 다른 표현입니다.')],
 **{'def': '9~10주 SQL을 한빛 마트 데이터로 직접 작성하고, 결과 표 비교로 자동 채점받는 종합 실습.'}))
PAGE['js'] += r'''
var TK=__TASKS__,SET=LABS.lab15.setup,score={};window.SQLGRADE={ok:0,total:TK.length};
LAB.$('#gr15').innerHTML=TK.map(function(t,i){return '<div class="dpanel" style="background:#fff;border:1px solid #d5dbe2;border-radius:10px;padding:10px 12px;margin:8px 0"><b>Q'+(i+1)+'.</b> '+t[0]+(t[2]?' <small style="color:#a35c00">(순서도 채점)</small>':'')+
 '<textarea class="dq" id="gr15q'+i+'" spellcheck="false" style="width:100%;min-height:64px;font:13px/1.5 ui-monospace,Consolas,monospace;border:1px solid #d5dbe2;border-radius:8px;padding:6px;margin-top:6px" placeholder="SELECT ..."></textarea>'+
 '<div class="ctrl"><button type="button" class="bt primary" data-g="'+i+'">채점</button><details style="display:inline-block"><summary class="bt">힌트</summary>'+t[3]+'</details><details style="display:inline-block"><summary class="bt">정답 보기</summary><code>'+LAB.esc(t[1])+'</code></details><span id="gr15m'+i+'"></span></div><div id="gr15r'+i+'" style="font-size:13px"></div></div>';}).join('');
function upd(){var ok=Object.keys(score).filter(function(k){return score[k];}).length;window.SQLGRADE={ok:ok,total:TK.length};LAB.kpis(LAB.$('#gr15k'),[['맞힌 문항',ok+'/'+TK.length,'',ok===TK.length?'good':(ok>=6?'warn':'')],['시도한 문항',Object.keys(score).length+'/'+TK.length]]);}
LAB.$$('#gr15 [data-g]').forEach(function(b){b.onclick=function(){var i=+b.dataset.g,db=LAB.DB();db.run(SET);var r=LAB.grade(db,LAB.$('#gr15q'+i).value,TK[i][1],{ordered:TK[i][2]});score[i]=r.ok;
 LAB.$('#gr15m'+i).innerHTML=(r.ok?' <span style="color:#13733a;font-weight:700">정답</span> ':' <span style="color:#c9302c;font-weight:700">다시</span> ')+LAB.esc(r.msg);
 LAB.$('#gr15r'+i).innerHTML=r.res?LAB.tableHTML(r.res.cols,r.res.rows.map(function(x){return x.map(function(v){return v==null?'NULL':MiniSQL.show(v);});}),{cap:'내 결과'}):'';upd();};});upd();
'''.replace('__TASKS__', __import__('json').dumps([list(t) for t in TASKS], ensure_ascii=False))
