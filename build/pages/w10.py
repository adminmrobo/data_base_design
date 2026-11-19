# 10주차 — SQL ② 데이터 조작 (교재 7장 3~5절)
SETUP = ("CREATE DATABASE market; USE market; "
 "CREATE TABLE customer_table (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), age INT, rank VARCHAR(10), job VARCHAR(20), credit INT); "
 "INSERT INTO customer_table VALUES ('apple','jane',20,'gold','student',1000),('banana','kim',25,'vip','nurse',2500),('carrot','duke',28,'gold','teacher',4500),('orange','albert',22,'silver','student',0),('melon','dragon',35,'gold','clerk',5000),('peach','jack',31,'silver','doctor',300),('pear','robert',NULL,'silver','clerk',500); "
 "CREATE TABLE product_table (product_num VARCHAR(5) PRIMARY KEY, product_name VARCHAR(20), inventory INT, price INT, company VARCHAR(20)); "
 "INSERT INTO product_table VALUES ('p01','mandu',5000,4500,'daehan'),('p02','nuddle',2500,5500,'minkuk'),('p03','pie',3600,2600,'hanbit'),('p04','chocolate',1250,2500,'hanbit'),('p05','spicynuddle',2200,1200,'daehan'),('p06','japannuddle',1000,1550,'minkuk'),('p07','biscuit',1650,1500,'hanbit'); "
 "CREATE TABLE order_table (order_num VARCHAR(5) PRIMARY KEY, order_customer VARCHAR(20), order_product VARCHAR(5), quantity INT, address VARCHAR(20), order_date DATE, FOREIGN KEY (order_customer) REFERENCES customer_table(id), FOREIGN KEY (order_product) REFERENCES product_table(product_num)); "
 "INSERT INTO order_table VALUES ('q01','apple','p03',10,'seoul','2022-01-01'),('q02','melon','p01',5,'incheon','2022-01-10'),('q03','banana','p06',45,'kyongkido','2022-01-11'),('q04','carrot','p02',8,'busan','2022-02-01'),('q05','melon','p06',36,'kyongkido','2022-02-20'),('q06','banana','p01',19,'chungbuk','2022-03-02'),('q07','apple','p03',22,'seoul','2022-03-15'),('q08','pear','p02',50,'kangwon','2022-04-10'),('q09','banana','p04',15,'chennam','2022-04-11'),('q10','carrot','p03',20,'kyongkido','2022-05-22');")
PAGE = dict(
num='10', slug='sql_dml', kind='lecture', short='10주', chip='10주차',
title='SQL ② 데이터 조작과 조인', title_en='SQL data manipulation, joins and views',
subtitle='SELECT로 묻고, INSERT·UPDATE·DELETE로 바꾸고, 뷰로 보여 주기',
toc='SELECT(조건·LIKE·NULL·정렬), 집계 함수와 GROUP BY·HAVING, 조인과 부속 질의, INSERT·UPDATE·DELETE, 뷰와 삽입 SQL — 노션 market 데이터로',
kicker='데이터베이스 설계 · 10주차 · 교재 7장',
question='“가장 많이 주문한 고객은 누구?” — 이 질문을 SQL 한 문장으로 쓸 수 있을까?',
desc='데이터베이스 설계 10주차: SELECT 문(기본·산술식·조건·LIKE·NULL·정렬), 집계 함수와 GROUP BY·HAVING, 조인과 외부 조인, 부속 질의(단일 행·다중 행·EXISTS), INSERT·UPDATE·DELETE, 뷰, 삽입 SQL. 노션 market 데이터 실습.',
intro='<p>9주차에 만든 표에 이제 질문을 던집니다. SQL의 SELECT는 7주차의 관계 대수를 영어 문장처럼 쓴 것입니다 — <code>SELECT</code>(π) <code>FROM</code>(×·⋈) <code>WHERE</code>(σ). 여기에 <b>묶어서 세기</b>(GROUP BY)와 <b>질문 안의 질문</b>(부속 질의)이 더해지면 대부분의 업무 질문에 답할 수 있습니다. 실습 데이터는 노션 「교재 예제 코드 수정」의 고객 7명·제품 7개·주문 10건입니다.</p>',
kpis=[('7 · 7 · 10','고객 · 제품 · 주문 (노션 market)'),('5개','집계 함수 COUNT·SUM·AVG·MAX·MIN'),('2종','부속 질의: 단일 행 · 다중 행'),('4문장','SELECT · INSERT · UPDATE · DELETE')],
hero_talk=[
 ('doc','front','SELECT 문의 순서를 외워라: <b>SELECT – FROM – WHERE – GROUP BY – HAVING – ORDER BY</b>. 쓰는 순서와 실행 순서가 다르다는 것도.'),
 ('asst','smile','실행 순서가 다르다고요? 위에서부터 읽는 게 아니에요?'),
 ('fly','clip','DBMS는 FROM부터 봐. 표가 있어야 줄을 고르고(WHERE), 묶고(GROUP BY), 칸을 고르지(SELECT). 그래서 SELECT에서 붙인 별명을 WHERE에서 못 써.'),
 ('robo','smile','나는 JOIN이 좋아! 표 두 개를 붙이면 정보가 두 배야!')],
crew=[('doc','front','SELECT 절 순서·실행 순서 정리'),('asst','smile','실습 진행, 손계산 발표'),('fly','clip','NULL·중복·WHERE 빠진 UPDATE 경계'),('robo','smile','JOIN 애호가')],
recap='9주차: CREATE TABLE로 market의 세 표를 만들고 PK·FK를 걸었습니다(노션 #3-2). 7주차: σ는 WHERE, π는 SELECT, ⋈은 JOIN. 오늘은 그 표들에 질문합니다.',
notion=[('SQL 기본 문법 (교재 예제 코드 수정)', NOTION+'1ab17a4520ed815294ccd69faa520526', 'market 데이터베이스 — 오늘 실습 데이터의 원본'),
        ('SQL 기본 문법 (노션) #3 DML', NOTION+'1ab17a4520ed8157b748e6104aa8e2c9', '실습#3-1 SELECT, #3-1b·c 조건, #3-2 LIKE, #2-8·#2-9 UPDATE'),
        ('10주차 : 정규화 (노션 — SQL 실습 모음)', NOTION+'1ab17a4520ed81d8a67ec7b5a8b5df74', 'SQL 기본 문법 세 페이지가 묶여 있는 회차 페이지'),
        ('07주차 : 미니 콘테스트 — DB 활용 사례', NOTION+'1ab17a4520ed812db206f94ea4d0668b', '주가 데이터 로보어드바이저 성과 평가 Colab (응용 과제)')],
why=[('업무 질문은 대부분 SELECT','“이번 달 VIP 매출”, “재고가 바닥난 상품”, “한 번도 주문 안 한 고객” — 모두 SELECT 한 문장입니다.'),
     ('바꾸는 문장은 위험하다','UPDATE·DELETE에서 WHERE를 빠뜨리면 모든 행이 바뀝니다. 결과를 미리 SELECT로 확인하는 습관이 필요합니다.'),
     ('보여 줄 것만 보여 준다','뷰는 4주차의 외부 스키마를 SQL로 만든 것입니다. 복잡한 질의를 숨기고 권한을 나눕니다.')],
bigpicture='<div class="flow"><span class="chip">1 FROM / JOIN</span><span class="arr">→</span><span class="chip">2 WHERE</span><span class="arr">→</span><span class="chip">3 GROUP BY</span><span class="arr">→</span><span class="chip">4 HAVING</span><span class="arr">→</span><span class="chip">5 SELECT</span><span class="arr">→</span><span class="chip">6 ORDER BY</span><span class="arr">→</span><span class="chip">7 LIMIT</span></div><p>위는 DBMS가 <b>논리적으로 처리하는 순서</b>입니다(쓰는 순서는 SELECT가 맨 앞). 이 순서를 알면 “WHERE에 집계 함수를 못 쓰는 이유”(아직 묶기 전), “ORDER BY에서는 SELECT의 별명을 쓸 수 있는 이유”(SELECT 다음)가 저절로 풀립니다.</p>',
steps=[
dict(id='lv1', short='SELECT', title='SELECT — 조건·LIKE·NULL·정렬', concept='SELECT 문', en='select statement', cid='lab:concept/select-statement',
 tag='연구실: market 고객 표', analogy='도서관 검색창',
 situation='점장이 묻습니다. “gold 등급 고객의 이름과 적립금을 적립금 많은 순으로 보여 줘. 그리고 나이를 모르는 고객은 누구지?”',
 pair=(('연구실에서는','도서관 검색창에 조건을 넣고(“제목에 데이터”), 보고 싶은 칸만 고르고(제목·저자), 정렬 기준을 고르는 것(최신순)과 같습니다.'),
       ('SQL에서는','<code>SELECT 칸 FROM 표 WHERE 조건 ORDER BY 칸 DESC;</code> — 조건에는 비교·논리 연산자, <code>LIKE \'R%\'</code>(R로 시작, %는 0자 이상, _는 1자), <code>IS NULL</code>(NULL은 = 로 비교하면 늘 거짓)을 씁니다. <code>DISTINCT</code>는 중복 제거, <code>AS</code>는 결과 칸 이름 바꾸기.')),
 panel='<div class="sqllab" id="lab10a" data-lab="lab10a"></div>',
 panel_title='SQL 실습실 — 노션 실습 #3-1 · #3-2를 market 데이터로',
 sim='SELECT 조건·정렬 실습',
 explain='<p><b>손으로 먼저:</b> gold 고객은 jane(1000), duke(4500), dragon(5000) 세 명 → 적립금 내림차순이면 dragon, duke, jane. 「① gold 고객」 결과와 비교하세요.</p><p><b>NULL 함정:</b> <code>WHERE age = NULL</code>은 robert를 찾지 못합니다(NULL과의 비교는 참도 거짓도 아닌 “모름”). 반드시 <code>IS NULL</code>. 또 <code>credit * 1.1</code> 같은 <b>산술식</b>은 결과에서만 계산될 뿐 표의 값은 바뀌지 않습니다.</p>',
 aicheck='<p><b>교재와 MariaDB가 다른 곳:</b> 교재는 “널 값은 오름차순에서 맨 마지막, 내림차순에서 맨 먼저”라고 설명합니다(오라클 기준). <b>MariaDB·MySQL은 반대</b>로, 오름차순에서 NULL을 맨 앞에 둡니다. 「④ 나이순 정렬」을 실행해 robert가 어디에 나오는지 확인하세요. 같은 SQL도 DBMS마다 세부 동작이 다를 수 있으니, AI가 “표준에 따르면…”이라고 할 때 쓰는 DBMS에서 직접 확인하는 습관이 필요합니다.</p>',
 limit='한 줄씩 보는 것은 됐습니다. 그런데 “등급별 평균 적립금”처럼 여러 줄을 묶어 한 숫자로 만들려면?', limit_label='여러 행을 묶어 요약하지 못함',
 say=('fly','point','age = NULL은 0줄, age IS NULL은 1줄. 이 차이를 모르면 “나이 미입력 고객 0명”이라는 틀린 보고서가 나가.'),
 quiz=[dict(q='이름이 R로 시작하는 고객을 찾는 조건은?',o=["name = 'R%'","name LIKE 'R%'","name LIKE '%R'","name IN ('R')"],a=1,why="LIKE 'R%'는 R로 시작하는 문자열. '%R'은 R로 끝나는 문자열입니다."),
       dict(q='age가 NULL인 고객을 찾는 올바른 조건은?',o=['age = NULL','age == NULL','age IS NULL',"age = ''"],a=2,why='NULL은 비교 연산자로 비교하면 결과가 참이 되지 않습니다. IS NULL을 씁니다.')]),
dict(id='lv2', short='집계', title='집계 함수와 GROUP BY · HAVING — 묶어서 세기', concept='집계와 그룹', en='aggregation and grouping', cid='lab:concept/aggregation-grouping',
 tag='연구실: 제품별 주문 수량', analogy='반별 성적 집계',
 situation='노션 order_table의 주문 10건을 제품별로 묶어 총 수량을 내고, 총 수량이 50개 이상인 제품만 남기려 합니다.',
 pair=(('연구실에서는','반별로 학생을 모아(그룹) 평균 점수를 내고, “평균 80점 이상인 반만” 시상합니다. 학생 한 명 조건(WHERE)과 반 단위 조건(HAVING)은 다릅니다.'),
       ('SQL에서는','<code>COUNT</code>·<code>SUM</code>·<code>AVG</code>·<code>MAX</code>·<code>MIN</code>은 <b>NULL을 빼고</b> 계산합니다. <code>GROUP BY</code>로 묶고, 묶음에 대한 조건은 <code>HAVING</code>에. 집계 함수는 WHERE에 쓸 수 없고, SELECT에는 묶은 칸이나 집계 결과만 씁니다.')),
 panel='''<div class="sqllab" id="lab10b" data-lab="lab10b"></div>
<h3 style="margin-top:14px">손으로 한 번 — 제품별 수량 합계</h3><div id="g10"></div><div class="ctrl"><button type="button" class="bt" id="g10go">한 단계씩 묶기</button><button type="button" class="bt" id="g10r">처음으로</button></div><div class="insight" id="g10o"></div>''',
 panel_title='SQL 실습실 + 손계산 — GROUP BY',
 sim='GROUP BY 단계별 손계산',
 explain='<p><b>손으로 먼저:</b> p03은 10+22+20 = <b>52</b>, p06은 45+36 = <b>81</b>, p02는 8+50 = <b>58</b>, p01은 5+19 = <b>24</b>, p04는 <b>15</b>. HAVING SUM ≥ 50이면 p03, p06, p02 세 제품. 「한 단계씩 묶기」와 실습실 ③이 같은 답인지 보세요.</p><p><b>COUNT(*) vs COUNT(age):</b> 고객 7명 중 robert의 나이가 NULL이라 <code>COUNT(*)</code>=7, <code>COUNT(age)</code>=6, <code>AVG(age)</code>는 6명의 평균입니다. “평균 나이”를 보고할 때 몇 명의 평균인지 함께 적어야 하는 이유입니다.</p>',
 limit='한 표 안에서는 묶고 셀 수 있습니다. 그런데 “고객 이름별 주문 수량”은 이름이 고객 표에, 수량이 주문 표에 있습니다.', limit_label='여러 표에 걸친 질문에 답하지 못함',
 say=('asst','report','제품별 합계: p06 81, p02 58, p03 52, p01 24, p04 15 — 50개 이상은 세 제품이에요!'),
 quiz=[dict(q='집계 함수를 사용한 조건(예: SUM(quantity) >= 50)을 쓸 수 있는 절은?',o=['WHERE','HAVING','FROM','ORDER BY만'],a=1,why='집계 함수 조건은 그룹이 만들어진 뒤인 HAVING에 씁니다. WHERE는 그룹을 만들기 전에 실행됩니다.'),
       dict(q='고객 7명 중 1명의 나이가 NULL일 때 COUNT(age)의 결과는? (계산)',o=['7','6','1','NULL'],a=1,why='집계 함수는 NULL을 제외하고 계산하므로 6입니다. COUNT(*)는 7.')]),
dict(id='lv3', short='조인·부속', title='조인과 부속 질의 — 표를 잇거나, 질문 안에 질문을', concept='조인 검색과 부속 질의', en='joins and subqueries', cid='lab:concept/join-subquery',
 tag='연구실: 고객·제품·주문 세 표', analogy='두 장부 맞대기',
 situation='“banana 고객이 주문한 제품의 이름은?” — 이름은 제품 표에, 주문 기록은 주문 표에 있습니다. 표를 이어서(조인) 풀 수도, 질문을 두 번 해서(부속 질의) 풀 수도 있습니다.',
 pair=(('연구실에서는','주문서의 고객 아이디를 들고 고객 명부를 펼쳐 이름을 찾는 일(조인), 또는 “banana가 산 제품 번호 목록”을 먼저 뽑고 그 목록으로 제품을 찾는 일(부속 질의).'),
       ('SQL에서는','조인: <code>FROM 주문 o JOIN 제품 p ON o.order_product = p.product_num</code> (조인 속성은 이름이 달라도 도메인이 같아야 함, 보통 외래키). 부속 질의: 괄호 속 SELECT. <b>단일 행</b>(값 하나)은 =, &gt; 같은 비교 연산자, <b>다중 행</b>은 <code>IN</code>, <code>NOT IN</code>, <code>EXISTS</code>.')),
 panel='<div class="sqllab" id="lab10c" data-lab="lab10c"></div>',
 panel_title='SQL 실습실 — 조인 · 외부 조인 · 부속 질의',
 sim='조인과 부속 질의 실습',
 explain='<p><b>손으로 먼저:</b> banana의 주문은 q03(p06), q06(p01), q09(p04) → 제품 이름은 japannuddle, mandu, chocolate 세 개. 「① 조인」과 「② 부속 질의 IN」이 같은 세 줄을 내는지 확인하세요. 같은 질문을 여러 방법으로 쓸 수 있다는 것이 교재의 정리입니다 — “질의 내용은 다양하게 표현 가능하므로 사용자가 자유롭게 선택”.</p><p>「④ 한 번도 주문 안 한 고객」은 외부 조인 + IS NULL, 또는 NOT IN, 또는 NOT EXISTS로 쓸 수 있습니다. 세 버튼의 결과가 같은지(orange, peach) 보세요.</p>',
 limit='질문은 자유롭게 할 수 있게 됐습니다. 이제 데이터를 넣고, 고치고, 지우는 문장과, 자주 쓰는 질문을 저장해 두는 방법(뷰)을 봅니다.', limit_label='데이터 변경과 질의 저장(뷰)을 아직 다루지 않음',
 say=('robo','wow','조인으로 풀어도, 부속 질의로 풀어도 같은 세 제품! 길은 달라도 도착지는 같네!'),
 quiz=[dict(q='부속 질의의 결과가 여러 행일 때 상위 질의와 연결하는 데 쓸 수 없는 것은?',o=['IN','NOT IN','EXISTS','= (단독 비교)'],a=3,why='다중 행 부속 질의에는 비교 연산자를 단독으로 쓸 수 없습니다(“Subquery returns more than 1 row” 오류).'),
       dict(q='고객 7명 중 주문 기록이 있는 고객이 5명일 때, customer LEFT JOIN order … WHERE 주문번호 IS NULL의 결과 행 수는? (계산)',o=['0','2','5','7'],a=1,why='주문이 없는 고객 7−5 = 2명(orange, peach)만 오른쪽이 NULL로 남습니다.')]),
dict(id='lv4', short='변경·뷰', title='INSERT · UPDATE · DELETE, 그리고 뷰와 삽입 SQL', concept='데이터 변경과 뷰', en='data modification and views', cid='lab:concept/dml-view',
 tag='연구실: 노션 #2-3 · #2-8 · #2-9', analogy='명부 고치기와 열람용 사본',
 situation='노션 실습은 직원을 추가하고(#2-2b), 지우고(#2-3), 9번 직원을 Manager로 승진시켰습니다(#2-9). 그런데 #2-9에서 WHERE를 빠뜨렸다면? 그리고 매번 긴 조인을 쓰기 귀찮다면?',
 pair=(('연구실에서는','명부를 고칠 때는 <b>누구를</b> 고칠지 먼저 짚어야 합니다. 그리고 손님에게는 원본 명부 대신 필요한 칸만 뽑은 <b>열람용 사본</b>을 보여 줍니다.'),
       ('SQL에서는','<code>INSERT INTO 표(칸…) VALUES (…)</code> · <code>UPDATE 표 SET 칸=값 WHERE …</code> · <code>DELETE FROM 표 WHERE …</code> — WHERE가 없으면 <b>모든 행</b>. <b>뷰</b>는 SELECT를 이름 붙여 저장한 가상 테이블. <b>삽입 SQL</b>은 프로그램 안에 넣은 SQL로, 여러 행 결과는 <b>커서</b>로 한 줄씩 받습니다.')),
 panel='<div class="sqllab" id="lab10d" data-lab="lab10d"></div>',
 panel_title='SQL 실습실 — 바꾸기 전에 SELECT로 확인',
 sim='UPDATE·DELETE와 뷰 실습',
 explain='<p><b>안전 수칙:</b> UPDATE·DELETE를 쓰기 전에 <b>같은 WHERE로 SELECT를 먼저</b> 실행해 몇 줄이 걸리는지 보세요. 「① 먼저 확인」 → 「② 수정」 순서입니다. 「③ WHERE 빠뜨림」은 실습실에서만 해 보세요 — 결과 메시지의 “7 rows affected”가 사고의 크기입니다. (13주차 트랜잭션을 쓰면 되돌릴 수 있습니다.)</p><p><b>뷰의 장점(교재):</b> 질의문을 쉽게 작성(긴 조인을 이름 하나로) · 데이터 보안(필요한 칸만 공개) · 여러 사용자의 요구에 맞는 데이터 제공 · 관리가 편함. 단, 집계·DISTINCT·GROUP BY가 들어간 뷰처럼 원래 표의 행과 1:1로 대응하지 않는 뷰는 INSERT·UPDATE·DELETE가 제한됩니다.</p>',
 formula_title='삽입 SQL — 파이썬 프로그램 안의 SQL (미리 보기)',
 formula='<pre># pip install pymysql  (MariaDB 접속)\nimport pymysql\nconn = pymysql.connect(host="localhost", port=3306, user="root",\n                       password="설치할 때 정한 비밀번호", db="market", charset="utf8mb4")\ncur = conn.cursor()                         # 커서: 결과를 한 줄씩 받는 손잡이\ncur.execute("SELECT name, credit FROM customer_table WHERE rank = %s", ("gold",))\nfor name, credit in cur.fetchall():        # 여러 행 → 반복문으로 하나씩\n    print(name, credit)\nconn.close()</pre><p>프로그램 변수 <code>"gold"</code>를 SQL 문자열에 직접 붙이지 않고 <code>%s</code> 자리로 넘기는 것이 안전합니다(SQL 주입 공격 방지).</p>',
 aicheck='<p>AI에게 “gold 고객 적립금을 10% 올리는 SQL”을 부탁하면 대부분 맞게 써 줍니다. 하지만 가끔 <code>UPDATE customer_table SET credit = credit * 1.1;</code>처럼 <b>WHERE가 빠진</b> 답이 나옵니다. 실행 전 체크리스트: ① WHERE가 있는가 ② 같은 조건의 SELECT 결과 행 수가 예상과 같은가 ③ 트랜잭션 안에서 실행하는가.</p>',
 limit='SQL로 표를 만들고 질문하고 고칠 수 있게 됐습니다. 그런데 “어떤 표를 만들지”는 어떻게 정할까요? 요구 분석부터 구현까지의 설계 5단계 — 11주차.', limit_label='설계 전체 과정 속에서 SQL의 위치를 아직 모름',
 quiz=[dict(q='WHERE 절 없이 DELETE FROM customer_table; 를 실행하면?',o=['아무 일도 없다','첫 번째 행만 지운다','모든 행을 지운다(구조는 남음)','표를 삭제한다'],a=2,why='WHERE가 없으면 모든 행이 대상입니다. 표 구조는 남고(DROP과 다름), 외래키 제약이 있으면 거부될 수도 있습니다.'),
       dict(q='뷰의 장점으로 거리가 먼 것은?',o=['복잡한 질의를 간단히 쓸 수 있다','필요한 데이터만 보여 줘 보안에 도움이 된다','데이터를 두 번 저장해 속도가 늘 빨라진다','사용자별 요구에 맞는 데이터를 제공한다'],a=2,why='일반 뷰는 데이터를 따로 저장하지 않는 가상 테이블입니다(조회할 때마다 정의된 질의를 실행).')]),
],
duel=dict(q='같은 질문, 두 문장 — JOIN vs 부속 질의(IN)',
 intro='“한 번이라도 주문한 고객의 이름”을 구합니다. 주판봇은 고객과 주문을 <b>JOIN</b>하고, 초파리는 주문 표의 고객 아이디 목록으로 <b>IN 부속 질의</b>를 씁니다. 판정 기준은 “결과에 담긴 서로 다른 고객 수”입니다. 페이지 안 SQL 엔진으로 실제로 실행합니다.',
 fly_pick='부속 질의 IN', fly_line='고객 표는 한 번만 훑고, 주문 목록에 있는지만 물어보면 돼.',
 robo_pick='고객 ⋈ 주문 JOIN', robo_line='두 표를 이어 붙이면 다 나오지! JOIN이 제일 확실해!',
 metric='결과에 담긴 서로 다른 고객 수', margin=0, step=2,
 after='<div id="duel10t"></div>',
 run='return PAGE.duel();',
 announce='return "서로 다른 고객 수는 초파리 <b>"+r.fly+"명</b>, 주판봇 <b>"+r.robo+"명</b>으로 같아요. 다만 주판봇의 결과는 <b>"+r.rows+"줄</b>이었어요 — 주문한 횟수만큼 같은 고객이 반복됐거든요.";',
 verdict='return "같은 고객을 찾았으니 이번 판은 나눠 갖는다. 다만 JOIN으로 명단을 낼 때는 DISTINCT를 붙여야 같은 사람이 여러 번 나오지 않는다.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>문법</th><th>함정</th></tr></thead><tbody>
<tr><td>1 SELECT</td><td>WHERE · LIKE(% _) · IS NULL · ORDER BY ASC/DESC · DISTINCT · AS</td><td>= NULL은 0줄, NULL 정렬 위치는 DBMS마다 다름</td></tr>
<tr><td>2 집계</td><td>COUNT·SUM·AVG·MAX·MIN, GROUP BY, HAVING</td><td>집계는 NULL 제외, WHERE에 집계 불가</td></tr>
<tr><td>3 조인·부속</td><td>JOIN … ON, LEFT JOIN, (SELECT …), IN, NOT IN, EXISTS</td><td>다중 행 부속 질의에 = 불가, JOIN은 중복 행</td></tr>
<tr><td>4 변경·뷰</td><td>INSERT · UPDATE · DELETE · CREATE VIEW · 커서</td><td>WHERE 빠진 UPDATE/DELETE, 집계 뷰는 변경 제한</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 열람용 사본</b> 뷰는 사본이 아니라 “보는 창”입니다. 원본이 바뀌면 뷰의 결과도 즉시 바뀝니다.</div><div><b>실습의 한계</b> 페이지 실습실은 교육용 모의 엔진입니다. 실제 MariaDB에서는 실행 계획·인덱스·문자 집합 때문에 같은 문장도 속도·정렬이 다를 수 있습니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY ② 집계는 NULL을 뺀다 ③ 바꾸기 전에 같은 WHERE로 SELECT.'),
       ('asst','report','대결은 무승부! 둘 다 5명을 찾았고, JOIN 결과는 10줄이라 DISTINCT가 필요했어요.'),
       ('fly','coffee','길은 여럿이야. 다만 결과 “줄 수”가 예상과 다르면 멈춰서 이유를 찾아.'),
       ('robo','meh','JOIN이 틀린 건 아니었지만 같은 이름이 반복되는 줄은 몰랐어. DISTINCT, 기억할게.')],
next_note='<p class="recap"><b>다음 회차 — 11주차 「데이터베이스 설계 5단계」:</b> 요구 사항 분석 → 개념적 → 논리적(ERD→릴레이션 변환 규칙) → 물리적 설계 → 구현. 한빛 마트 사례.</p>',
gloss={'LIKE':('LIKE','명령어','문자열의 일부가 일치하는지 검사. %는 0자 이상, _는 정확히 1자.','like','lv1'),
 'IS NULL':('IS NULL','명령어','값이 NULL인지 검사. = NULL은 쓰지 않는다.','is-null','lv1'),
 'ORDER BY':('ORDER BY','명령어','결과를 정렬. ASC(오름차순, 기본) / DESC(내림차순).','order-by','lv1'),
 'DISTINCT':('DISTINCT','명령어','결과에서 중복 행을 제거.','distinct','lv1'),
 '집계 함수':('집계 함수','용어','여러 행을 하나의 값으로 계산(COUNT, SUM, AVG, MAX, MIN). NULL은 제외.','aggregate-function','lv2'),
 'GROUP BY':('GROUP BY','명령어','같은 값을 가진 행끼리 묶어 그룹별로 집계.','group-by','lv2'),
 'HAVING':('HAVING','명령어','그룹에 대한 조건. 집계 함수를 쓸 수 있다.','having','lv2'),
 '부속 질의':('부속 질의(서브쿼리)','용어','SELECT 문 안에 괄호로 넣은 또 다른 SELECT 문.','subquery','lv3'),
 '조인 속성':('조인 속성','용어','두 표를 잇는 데 쓰는 속성. 이름은 달라도 도메인이 같아야 하며 보통 외래키.','join-attribute','lv3'),
 '커서':('커서','용어','삽입 SQL에서 여러 행의 결과를 한 줄씩 차례로 받는 장치.','cursor','lv4'),
 '삽입 SQL':('삽입 SQL','용어','응용 프로그램 안에 넣어 실행하는 SQL.','embedded-sql','lv4')},
facts=[('F01','집계 함수는 널인 속성 값은 제외하고 계산하며, WHERE 절에서는 사용할 수 없고 SELECT·HAVING 절에서만 사용','문헌 사실','kim3ed','lv2','7장 3절 (교안)'),
       ('F02','교재: 널 값은 오름차순에서 맨 마지막, 내림차순에서 맨 먼저 출력','문헌 사실','kim3ed','lv1','7장 3절 정렬 검색 (교안)'),
       ('F03','MariaDB·MySQL은 오름차순 정렬에서 NULL을 맨 앞에 둔다','문헌 사실','mariadbdocs','lv1','ORDER BY 문서'),
       ('F04','다중 행 부속 질의문은 비교 연산자를 단독으로 사용할 수 없고 IN·NOT IN·EXISTS 등을 사용','문헌 사실','kim3ed','lv3','7장 3절 부속 질의'),
       ('F05','질의 내용은 다양하게 표현 가능하므로 사용자가 자유롭게 선택','문헌 사실','kim3ed','lv3','7장 3절 (교안)')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='출판 연도 미확인'),
      dict(id='ahn2025sqltext',type='webpage',title='SQL 기본 문법 (교재 예제 코드 수정)',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed815294ccd69faa520526',role='primary'),
      dict(id='ahn2025sqlbasic',type='webpage',title='SQL 기본 문법',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed8157b748e6104aa8e2c9',role='primary'),
      dict(id='mariadbdocs',type='webpage',title='ORDER BY — MariaDB Documentation',author=[{'literal':'MariaDB Foundation'}],URL='https://mariadb.com/kb/en/order-by/',role='background',verified={'title':True,'authors':True,'year':False},note='NULL 정렬 위치 확인용')],
models=['market 고객·제품·주문 데이터 (노션 「교재 예제 코드 수정」 기준; 노션 INSERT 문의 오타 mikuk는 표 값 minkuk으로 통일)','GROUP BY 단계별 손계산 그림','삽입 SQL 파이썬 예 (pymysql, 설명용 — 이 페이지에서는 실행되지 않음)'],
cover_alt='주문 장부와 고객 명부가 나란히 펼쳐지고 그 위로 질문 말풍선이 떠 있는 장면을 네 캐릭터가 보는 표지 (대체 그림)',
cover_svg='<svg width="300" height="140" viewBox="0 0 300 140"><rect x="10" y="40" width="110" height="90" rx="6" fill="#fff" stroke="#9aa5b1"/><rect x="180" y="40" width="110" height="90" rx="6" fill="#fff" stroke="#9aa5b1"/>'+''.join('<line x1="20" y1="%d" x2="110" y2="%d" stroke="#d5dbe2"/><line x1="190" y1="%d" x2="280" y2="%d" stroke="#d5dbe2"/>'%(60+i*16,60+i*16,60+i*16,60+i*16) for i in range(4))+'<path d="M110 76 C150 60 150 92 190 76" stroke="#13733a" stroke-width="2" fill="none"/><rect x="95" y="4" width="110" height="28" rx="14" fill="#e6eefb" stroke="#1e55c8"/><text x="120" y="23" font-size="14" fill="#1e55c8">SELECT ?</text></svg>',
prereq=['09'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var ORD=[['q01','apple','p03',10],['q02','melon','p01',5],['q03','banana','p06',45],['q04','carrot','p02',8],['q05','melon','p06',36],['q06','banana','p01',19],['q07','apple','p03',22],['q08','pear','p02',50],['q09','banana','p04',15],['q10','carrot','p03',20]],step=0;
function g10(){var rows=ORD.slice();if(step>=1)rows.sort(function(a,b){return a[2]<b[2]?-1:a[2]>b[2]?1:0;});
 if(step<2){$('#g10').innerHTML=LAB.tableHTML(['주문','고객','제품','수량'],rows,{cap:step?'1단계: 제품끼리 모으기 (정렬)':'주문 10건'});
  $('#g10o').innerHTML=step?'같은 제품끼리 붙었습니다. 다음 단계에서 묶음마다 수량을 더합니다.':'「한 단계씩 묶기」를 누르세요.';return;}
 var g={};ORD.forEach(function(o){g[o[2]]=(g[o[2]]||0)+o[3];});var keys=Object.keys(g).sort();
 var out=keys.map(function(k){return [k,ORD.filter(function(o){return o[2]===k;}).map(function(o){return o[3];}).join(' + '),g[k]];});
 $('#g10').innerHTML=LAB.tableHTML(['제품','더한 값','SUM(quantity)'],out,{cap:step===2?'2단계: 묶음마다 SUM':'3단계: HAVING SUM >= 50',cls:function(r){return step===3?(r[2]>=50?'hl':'dim'):'';}});
 $('#g10o').innerHTML=step===2?'다섯 묶음이 생겼습니다. 이제 HAVING으로 묶음을 거릅니다.':'HAVING SUM(quantity) >= 50 → <b>'+out.filter(function(r){return r[2]>=50;}).map(function(r){return r[0];}).join(', ')+'</b> (3개). 실습실 ③과 비교하세요.';}
$('#g10go').onclick=function(){step=Math.min(3,step+1);g10();};$('#g10r').onclick=function(){step=0;g10();};g10();
PAGE.duel=function(){var db=new MiniSQL.DB();db.run(__SETUP__);
 var a=db.run("SELECT name FROM customer_table WHERE id IN (SELECT order_customer FROM order_table);")[0],b=db.run("SELECT c.name FROM customer_table c JOIN order_table o ON c.id = o.order_customer;")[0];
 var fly=new Set(a.rows.map(function(r){return r[0];})).size,robo=new Set(b.rows.map(function(r){return r[0];})).size;
 document.getElementById('duel10t').innerHTML=LAB.tableHTML(['IN 결과'],a.rows,{cap:'초파리 ('+a.rows.length+'줄)'})+LAB.tableHTML(['JOIN 결과'],b.rows,{cap:'주판봇 ('+b.rows.length+'줄)'});
 return {fly:fly,robo:robo,flyTxt:fly+'명',roboTxt:robo+'명',rows:b.rows.length};};
'''.replace('__SETUP__', '"' + SETUP.replace('"', '\\"') + '"'),
labs=('lab10a:{setup:%s,presets:[{t:"① gold 고객 (적립금 순)",q:"SELECT name, credit\\nFROM customer_table\\nWHERE rank = \'gold\'\\nORDER BY credit DESC;"},{t:"② R·r로 시작하는 이름 (#3-2)",q:"SELECT * FROM customer_table WHERE name LIKE \'r%%\';"},{t:"③ 나이 모름 — 두 가지",q:"SELECT name FROM customer_table WHERE age = NULL;\\nSELECT name FROM customer_table WHERE age IS NULL;"},{t:"④ 나이순 정렬 (NULL 위치)",q:"SELECT name, age FROM customer_table ORDER BY age;"},{t:"⑤ 산술식·별명",q:"SELECT name, credit, credit * 1.1 AS 인상후\\nFROM customer_table WHERE rank = \'vip\';"},{t:"⑥ 등급 종류 DISTINCT",q:"SELECT DISTINCT rank FROM customer_table;"},{t:"⑦ 두 조건 AND (#3-1c 형식)",q:"SELECT * FROM customer_table\\nWHERE job = \'student\' AND credit >= 1000;"}],ready:"노션 market 데이터(고객 7·제품 7·주문 10)가 준비되어 있습니다."},'
      'lab10b:{setup:%s,presets:[{t:"① 집계 다섯 가지",q:"SELECT COUNT(*) AS 고객수, COUNT(age) AS 나이있음, AVG(age) AS 평균나이,\\n       MAX(credit) AS 최대적립, MIN(credit) AS 최소적립\\nFROM customer_table;"},{t:"② 제품별 수량 합계",q:"SELECT order_product, SUM(quantity) AS 총수량\\nFROM order_table\\nGROUP BY order_product;"},{t:"③ HAVING 50 이상",q:"SELECT order_product, SUM(quantity) AS 총수량\\nFROM order_table\\nGROUP BY order_product\\nHAVING SUM(quantity) >= 50\\nORDER BY 총수량 DESC;"},{t:"④ WHERE에 집계 (오류)",q:"SELECT order_product FROM order_table\\nWHERE SUM(quantity) >= 50\\nGROUP BY order_product;"},{t:"⑤ 등급별 평균 적립금",q:"SELECT rank, COUNT(*) AS 인원, AVG(credit) AS 평균적립\\nFROM customer_table\\nGROUP BY rank;"},{t:"⑥ 제조사 수 DISTINCT",q:"SELECT COUNT(company) AS 그냥세기, COUNT(DISTINCT company) AS 서로다른\\nFROM product_table;"}],ready:"같은 market 데이터입니다. ②·③을 실행하기 전에 아래 손계산을 먼저 해 보세요."},'
      'lab10c:{setup:%s,presets:[{t:"① 조인: banana의 제품",q:"SELECT p.product_name\\nFROM order_table o\\nJOIN product_table p ON o.order_product = p.product_num\\nWHERE o.order_customer = \'banana\';"},{t:"② 부속 질의 IN",q:"SELECT product_name FROM product_table\\nWHERE product_num IN (\\n  SELECT order_product FROM order_table\\n  WHERE order_customer = \'banana\');"},{t:"③ 단일 행: 최대 적립금",q:"SELECT name, credit FROM customer_table\\nWHERE credit = (SELECT MAX(credit) FROM customer_table);"},{t:"④ 주문 없는 고객 (외부 조인)",q:"SELECT c.name\\nFROM customer_table c\\nLEFT JOIN order_table o ON c.id = o.order_customer\\nWHERE o.order_num IS NULL;"},{t:"④ 같은 질문 NOT IN",q:"SELECT name FROM customer_table\\nWHERE id NOT IN (SELECT order_customer FROM order_table);"},{t:"④ 같은 질문 NOT EXISTS",q:"SELECT name FROM customer_table c\\nWHERE NOT EXISTS (\\n  SELECT 1 FROM order_table o WHERE o.order_customer = c.id);"},{t:"⑤ 세 표 조인 + 집계",q:"SELECT c.name, SUM(o.quantity * p.price) AS 주문금액\\nFROM order_table o\\nJOIN customer_table c ON o.order_customer = c.id\\nJOIN product_table p ON o.order_product = p.product_num\\nGROUP BY c.name\\nORDER BY 주문금액 DESC;"},{t:"⑥ = 에 여러 행 (오류)",q:"SELECT product_name FROM product_table\\nWHERE product_num = (SELECT order_product FROM order_table WHERE order_customer = \'banana\');"}],ready:"고객·제품·주문 세 표가 외래키로 이어져 있습니다."},'
      'lab10d:{setup:%s,presets:[{t:"① 먼저 확인 (SELECT)",q:"SELECT id, name, credit FROM customer_table WHERE rank = \'gold\';"},{t:"② gold 적립금 10%% 인상",q:"UPDATE customer_table SET credit = credit * 1.1 WHERE rank = \'gold\';\\nSELECT id, name, credit FROM customer_table WHERE rank = \'gold\';"},{t:"③ WHERE 빠뜨림 (사고)",q:"UPDATE customer_table SET credit = 0;\\nSELECT name, credit FROM customer_table;"},{t:"④ 새 고객 INSERT",q:"INSERT INTO customer_table (id, name, age, rank, job, credit)\\nVALUES (\'grape\', \'sora\', 27, \'silver\', \'designer\', 800);\\nSELECT COUNT(*) AS 고객수 FROM customer_table;"},{t:"⑤ 주문 없는 고객 DELETE",q:"DELETE FROM customer_table WHERE id = \'orange\';\\nSELECT id FROM customer_table;"},{t:"⑥ 뷰 만들기",q:"CREATE VIEW 우수고객 AS\\nSELECT c.name, SUM(o.quantity) AS 총주문\\nFROM customer_table c JOIN order_table o ON c.id = o.order_customer\\nGROUP BY c.name\\nHAVING SUM(o.quantity) >= 40;\\nSELECT * FROM 우수고객;"}],ready:"같은 market 데이터입니다. ③은 일부러 사고를 내 보는 버튼 — 「처음 상태로」로 언제든 되돌릴 수 있습니다."}') % tuple(['"' + SETUP.replace('"', '\\"') + '"'] * 4),
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'SELECT·FROM·WHERE·ORDER BY로 조건에 맞는 행과 칸을 골라 정렬해 보여 주는 질의.','lv2':'집계 함수로 여러 행을 하나의 값으로 계산하고 GROUP BY·HAVING으로 그룹별 집계·조건을 거는 것.','lv3':'여러 표를 조인 속성으로 이어 검색하거나, 괄호 속 SELECT(부속 질의)의 결과로 상위 질의를 수행하는 것.','lv4':'INSERT·UPDATE·DELETE로 데이터를 바꾸고, 뷰로 질의를 가상 테이블로 저장하며, 삽입 SQL로 프로그램에서 SQL을 쓰는 것.'}[s['id']]
