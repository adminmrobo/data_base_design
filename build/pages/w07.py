# 7주차 — 관계 데이터 연산 (교재 6장)
PAGE = dict(
num='07', slug='relational_operations', kind='lecture', short='7주', chip='07주차',
title='관계 데이터 연산', title_en='Relational algebra and joins',
subtitle='표를 넣으면 표가 나온다 — 셀렉트·프로젝트·집합·조인',
toc='관계 대수의 8가지 연산, 셀렉트·프로젝트, 합·교·차·카티션 곱, 조인(동등·자연·외부·세미), 디비전 — 노션 JOIN 실습',
kicker='데이터베이스 설계 · 7주차 · 교재 6장',
question='표 두 장을 겹쳐서, 원하는 줄만 남기는 방법은 몇 가지일까?',
desc='데이터베이스 설계 7주차: 관계 대수(셀렉트 σ, 프로젝트 π, 합 ∪, 교 ∩, 차 −, 카티션 곱 ×, 조인 ⋈, 디비전 ÷)와 관계 해석, SQL JOIN 실습(INNER·LEFT·RIGHT·FULL 흉내·SEMI·ANTI). 노션 「SQL 기본 문법: 연산」 연결.',
intro='<p>관계 데이터 모델의 표는 그냥 보관용이 아닙니다. 표에 연산을 걸면 <b>또 다른 표</b>가 나오고, 그 표에 다시 연산을 걸 수 있습니다(폐쇄 특성). 덧셈·곱셈처럼 표에도 계산이 있는 셈입니다. 이번 회차의 기호 여덟 개(σ π ∪ ∩ − × ⋈ ÷)는 9·10주차 SQL의 SELECT·WHERE·JOIN이 실제로 무엇을 하는지 보여 주는 설계도입니다.</p>',
kpis=[('8개','관계 대수 연산자'),('4 + 4','일반 집합 연산 + 순수 관계 연산'),('7 × 4 = 28','노션 실습 a·b의 카티션 곱 행 수'),('10가지','노션 JOIN 실습 (#3-1~#3-10)')],
hero_talk=[
 ('doc','front','오늘은 <b>표의 산수</b>를 배운다. 기호는 그리스 문자지만, 하는 일은 “고르기, 자르기, 합치기”다.'),
 ('asst','smile','σ(시그마), π(파이)… 기호만 봐도 벌써 긴장돼요.'),
 ('fly','clip','기호는 말로 먼저 풀자. σ는 “줄 고르기”, π는 “칸 고르기”. 그게 다야.'),
 ('robo','smile','나는 일단 다 곱해 놓고 고르는 게 좋아! 다 있으면 빠뜨릴 일이 없잖아!')],
crew=[('doc','front','연산자 정리, 판정'),('asst','smile','기호가 겁나는 초보 눈높이'),('fly','clip','작은 표부터 줄이자파'),('robo','smile','일단 다 곱하자파 (오늘 대결)')],
recap='6주차: 표(릴레이션)에는 키가 있고, 외래키는 다른 표의 기본키를 가리킵니다. 오늘은 그 외래키를 따라 <b>두 표를 잇는 연산(조인)</b>까지 갑니다.',
notion=[('06주차 : 관계 데이터 연산 (노션)', NOTION+'1ab17a4520ed8109aeb1cafd7b531709', '강의 영상, “연산자” 자료'),
        ('SQL 기본 문법 : 연산 (노션)', NOTION+'1ab17a4520ed812fbd9ce0ab3a3b7f1b', 'jointest 데이터베이스의 a·b 표로 UNION·JOIN 10가지 — 3·4칸 실습실의 원본')],
why=[('SQL의 뼈대','SELECT 문 하나는 사실 π(SELECT 절), σ(WHERE 절), ⋈(JOIN 절)을 이어 붙인 것입니다.'),
     ('결과를 미리 짐작','연산의 뜻을 알면 쿼리를 실행하기 전에 결과 행 수를 손으로 짐작하고, 틀린 결과를 알아챌 수 있습니다.'),
     ('성능의 감각','같은 결과도 연산 순서에 따라 중간 표의 크기가 수십 배 달라집니다 — 오늘의 대결.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>구분</th><th>연산자</th><th>기호</th><th>말로 하면</th><th>SQL에서</th></tr></thead><tbody>
<tr><td rowspan="4">일반 집합 연산</td><td>합집합</td><td>∪</td><td>둘 중 어디에든 있는 줄</td><td>UNION</td></tr>
<tr><td>교집합</td><td>∩</td><td>둘 다에 있는 줄</td><td>INTERSECT (MariaDB 10.3+) · EXISTS</td></tr>
<tr><td>차집합</td><td>−</td><td>앞에는 있고 뒤에는 없는 줄</td><td>EXCEPT · NOT EXISTS</td></tr>
<tr><td>카티션 곱</td><td>×</td><td>모든 줄의 모든 짝</td><td>FROM a, b / CROSS JOIN</td></tr>
<tr><td rowspan="4">순수 관계 연산</td><td>셀렉트</td><td>σ</td><td>조건에 맞는 줄 고르기</td><td>WHERE</td></tr>
<tr><td>프로젝트</td><td>π</td><td>필요한 칸만 남기기</td><td>SELECT 칸 목록</td></tr>
<tr><td>조인</td><td>⋈</td><td>공통 속성으로 두 표 잇기</td><td>JOIN … ON</td></tr>
<tr><td>디비전</td><td>÷</td><td>“모두”를 만족하는 줄</td><td>NOT EXISTS 두 겹</td></tr></tbody></table></div>
<p><b>합·교·차</b>는 두 표가 <b>합병 가능</b>(칸 수가 같고 대응하는 칸의 도메인이 같음)해야 쓸 수 있습니다. 관계 대수는 “어떻게 구할지”를 순서대로 적는 <b>절차적</b> 언어, 관계 해석(튜플·도메인 관계 해석)은 “무엇을 원하는지”만 적는 <b>비절차적</b> 언어입니다. SQL은 관계 해석에 가까운 쪽입니다.</p>''',
steps=[
dict(id='lv1', short='σ와 π', title='셀렉트 σ와 프로젝트 π — 줄 고르기, 칸 고르기', concept='셀렉트와 프로젝트', en='selection and projection', cid='lab:concept/selection-projection',
 tag='현장: 고객 명단에서 골라내기', analogy='명단에 형광펜·가위',
 situation='고객 명단(7명)에서 “gold 등급 고객의 이름과 적립금만” 보고 싶습니다. 줄을 고르는 일과 칸을 고르는 일은 서로 다른 연산입니다.',
 pair=(('현장에서는','명단에서 gold인 줄에만 <b>형광펜</b>을 칠하고(줄 고르기), 이름·적립금 칸만 <b>가위</b>로 오려 냅니다(칸 고르기).'),
       ('관계 대수에서는','<b>σ</b><sub>조건</sub>(R): 조건을 만족하는 튜플만 → 결과는 <b>수평 부분집합</b>. <b>π</b><sub>속성</sub>(R): 고른 속성만, 중복 튜플은 제거 → <b>수직 부분집합</b>. 둘을 겹쳐 π<sub>name,credit</sub>(σ<sub>rank=\'gold\'</sub>(customer)).')),
 panel='''<div class="ctrl"><label>σ 조건 <select id="s7c"><option value="">(없음)</option><option value="gold">rank = 'gold'</option><option value="age">age &gt;= 25</option><option value="stu">job = 'student'</option><option value="both">rank = 'gold' AND credit &gt; 2000</option></select></label></div>
<div class="chips" id="p7c"></div><div class="eq" id="s7eq"></div><div class="two"><div id="s7in"></div><div id="s7out"></div></div><div class="insight" id="s7o"></div>''',
 panel_title='직접 해 보기 — σ와 π 계산기',
 sim='셀렉트·프로젝트 계산기',
 explain='<p><b>손으로 한 번:</b> σ<sub>rank=\'gold\'</sub>(customer)는 jane, duke, dragon 세 줄 → 카디널리티 3. 여기에 π<sub>rank</sub>를 걸면 결과는 “gold” <b>한 줄</b>입니다 — 관계 대수의 π는 중복 튜플을 없애기 때문입니다. 반면 SQL의 <code>SELECT rank</code>는 중복을 그대로 두고, <code>SELECT DISTINCT rank</code>라고 써야 같아집니다. 계산기에서 rank만 골라 확인해 보세요.</p>',
 formula_title='더 깊이 — 조건식과 교환 법칙',
 formula='<p>셀렉트 조건에는 비교(=, ≠, &lt;, &gt;, ≤, ≥)와 논리(∧ AND, ∨ OR, ¬ NOT)를 씁니다. σ<sub>p1</sub>(σ<sub>p2</sub>(R)) = σ<sub>p2</sub>(σ<sub>p1</sub>(R)) = σ<sub>p1∧p2</sub>(R) — 셀렉트는 순서를 바꿔도 결과가 같습니다(교환적). 프로젝트는 π<sub>A</sub>(π<sub>A,B</sub>(R)) = π<sub>A</sub>(R)처럼 바깥쪽 속성이 안쪽에 포함되어야 합니다.</p>',
 limit='한 표 안에서는 고를 수 있게 됐습니다. 그런데 “두 표를 합치거나 비교”하려면 어떻게 할까요?', limit_label='두 릴레이션을 함께 다루지 못함',
 say=('fly','point','σ는 줄, π는 칸. 헷갈리면 σ의 S를 “Select a row”, π의 P를 “Pick a column”으로 외워.'),
 quiz=[dict(q='릴레이션에서 조건을 만족하는 튜플만 골라 수평 부분집합을 만드는 연산은?',o=['프로젝트 π','셀렉트 σ','조인 ⋈','디비전 ÷'],a=1,why='셀렉트는 줄(튜플)을 고르고, 프로젝트는 칸(속성)을 고릅니다.'),
       dict(q='customer에서 rank가 gold 3명, vip 1명, silver 3명일 때, π<sub>rank</sub>(customer)의 튜플 수는? (계산)',o=['1','3','7','4'],a=1,why='관계 대수의 프로젝트는 중복을 제거하므로 gold, vip, silver 3개입니다.')]),
dict(id='lv2', short='집합·곱', title='집합 연산과 카티션 곱 — 노션 a·b 표로', concept='일반 집합 연산', en='set operations and cartesian product', cid='lab:concept/set-operations',
 tag='연구실: 노션 실습 #3-1', analogy='두 반의 출석부 합치기',
 situation='노션 실습의 두 표: a = {2, 4, 6, 8, 10, 12, 14}, b = {4, 8, 12, 16}. 두 표를 위아래로 붙이면 몇 줄이 될까요? 중복을 빼면? 모든 짝을 만들면?',
 pair=(('연구실에서는','두 반 출석부를 이어 붙이면(합), 양쪽에 다 있는 학생(교), A반에만 있는 학생(차)이 보입니다. 두 반 학생을 한 명씩 짝지으면 모든 짝(곱)이 나옵니다.'),
       ('관계 대수에서는','합 ∪ · 교 ∩ · 차 − 는 <b>합병 가능</b>한 두 릴레이션에만 씁니다. 카티션 곱 ×는 조건 없이 모든 튜플을 짝짓습니다: 결과 차수 = 두 차수의 합, 카디널리티 = 두 카디널리티의 곱.')),
 panel='<div class="sqllab" id="lab7a" data-lab="lab7a"></div>',
 panel_title='SQL 실습실 — 노션 jointest의 a·b',
 sim='집합 연산·카티션 곱 실습',
 explain='<p><b>손으로 먼저:</b> a 7줄, b 4줄. <code>UNION ALL</code>은 7+4 = <b>11줄</b>, <code>UNION</code>은 겹치는 4·8·12를 한 번씩만 → 11−3 = <b>8줄</b>. 교집합은 {4, 8, 12} <b>3줄</b>, 차집합 a−b는 {2, 6, 10, 14} <b>4줄</b>. 카티션 곱은 7×4 = <b>28줄</b>. 실습실에서 숫자가 맞는지 확인하세요.</p>',
 aicheck='<p>노션 실습 #3-1b의 설명은 카티션 곱을 “가능한 모든 조합을 반환해 <b>중복된 결과가 많이 나타날 수 있다</b>”고 썼습니다. 정확히 말하면 28줄은 서로 다른 짝이라 “중복”은 아닙니다. 다만 <b>쓸모없는 짝이 많다</b>는 뜻으로 읽으세요. AI 설명에서도 “중복”과 “불필요한 조합”을 섞어 쓰는 경우가 많습니다.</p>',
 limit='카티션 곱은 모든 짝을 만들지만 대부분 의미 없는 짝입니다. “같은 값끼리만” 짝지으려면?', limit_label='카티션 곱은 의미 없는 짝까지 모두 만듦',
 say=('robo','wow','곱하기만 했는데 28줄! 근데 4–2, 4–6 같은 짝은… 어디에 쓰지?'),
 quiz=[dict(q='a가 7줄, b가 4줄일 때 a × b(카티션 곱)의 튜플 수는? (계산)',o=['11','28','8','3'],a=1,why='카티션 곱의 카디널리티는 두 카디널리티의 곱: 7 × 4 = 28.'),
       dict(q='합집합·교집합·차집합을 쓰려면 두 릴레이션이 어떤 조건을 만족해야 하나요?',o=['튜플 수가 같아야 한다','합병 가능(속성 수가 같고 대응 속성의 도메인이 같음)해야 한다','기본키가 같아야 한다','외래키로 연결돼 있어야 한다'],a=1,why='합병 가능성(union-compatible)이 필요합니다. 튜플 수는 달라도 됩니다.')]),
dict(id='lv3', short='조인', title='조인 — 공통 값으로 두 표를 잇는 일곱 가지 방법', concept='조인', en='join operations', cid='lab:concept/join',
 tag='연구실: 노션 실습 #3-2~#3-10', analogy='짝꿍 찾기',
 situation='a와 b에서 <b>같은 값끼리</b>만 짝지으면 4–4, 8–8, 12–12 세 쌍이 나옵니다(내부 조인). 그런데 짝이 없는 a의 2, 6, 10, 14도 보고 싶다면? 짝이 없는 것만 보고 싶다면?',
 pair=(('연구실에서는','짝꿍 찾기 게임: 짝이 있는 사람만 무대에(내부), 왼쪽 팀은 짝이 없어도 전원 무대에(왼쪽 외부), 짝이 있는 왼쪽 팀원 이름만(세미), 짝이 없는 왼쪽 팀원만(안티).'),
       ('관계 대수에서는','<b>세타 조인</b>(조건 θ로 잇기), <b>동등 조인</b>(= 조건), <b>자연 조인</b>(같은 이름의 칸으로 잇고 그 칸은 한 번만), <b>외부 조인</b>(짝 없는 튜플도 NULL과 함께 남김), <b>세미 조인</b>(짝이 있는 왼쪽 튜플만, 왼쪽 칸만). MariaDB는 FULL OUTER JOIN이 없어 LEFT와 RIGHT를 UNION으로 합칩니다.')),
 panel='<div class="sqllab" id="lab7b" data-lab="lab7b"></div><div class="flash" data-cards="join7"></div>',
 panel_title='SQL 실습실 — JOIN 여덟 가지 (노션 #3-2 ~ #3-10)',
 sim='JOIN 종류별 실습',
 flow=dict(id='fl7', title='LEFT JOIN이 짝을 찾는 과정', h=220, alt='a 표의 각 값이 b에서 짝을 찾고, 짝이 없으면 NULL과 함께 결과에 남는 흐름',
   cap='a의 값마다 b를 훑어 짝을 찾습니다. 짝이 없으면(빨강) 버리지 않고 오른쪽을 NULL로 채워 남기는 것이 LEFT (OUTER) JOIN입니다.',
   js='{stations:["a.t1","b에서 짝 찾기","결과 줄"],items:[["2","짝 없음","2 | NULL"],["4","b.t2 = 4","4 | 4"],["6","짝 없음","6 | NULL"],["8","b.t2 = 8","8 | 8"],["10","짝 없음","10 | NULL"],["12","b.t2 = 12","12 | 12"],["14","짝 없음","14 | NULL"]],bad:function(it,i){return /없음|NULL/.test(it[i]);},stamp:"노션 실습 a·b"}'),
 explain='<p><b>손으로 먼저 결과 행 수:</b> 내부 조인 3 · LEFT 7 · RIGHT 4 · FULL 8 · 세미 3 · 안티(a에만) 4 · b에만 1(16) · 양쪽 한쪽에만(FULL에서 교집합 제외) 5. 여덟 개 버튼을 눌러 맞혀 보세요. 아래 카드는 “벤 다이어그램으로 보면 어디가 칠해지나”를 뒤집어 확인하는 낱말 카드입니다.</p>',
 aicheck='<p>노션 실습 #3-3(LEFT OUTER JOIN)의 코드 칸에는 <code>INNER JOIN</code>이 적혀 있습니다 — 자료를 옮기다 생긴 오타입니다. 결과 설명은 LEFT JOIN 기준이므로, 코드를 <code>LEFT JOIN</code>으로 바꿔 실행해야 설명과 같은 7줄이 나옵니다. <b>“설명과 코드와 결과가 서로 맞는가”</b>를 확인하는 습관은 AI가 써 준 SQL을 볼 때 더욱 중요합니다.</p>',
 limit='조인으로 “짝이 있는 것”은 찾았습니다. 그렇다면 “<b>모든</b> 과목을 들은 학생”처럼 ‘모두’를 묻는 질문은?', limit_label='“모두”를 만족하는 튜플을 찾지 못함',
 say=('asst','spark','짝 없는 쪽을 NULL로 채워서 남기는 게 외부 조인이군요! 결과 줄 수를 먼저 맞히고 실행하니까 재밌어요.'),
 quiz=[dict(q='a = {2,4,6,8,10,12,14}, b = {4,8,12,16}일 때 a LEFT JOIN b ON a.t1 = b.t2의 결과 행 수는? (계산)',o=['3','4','7','11'],a=2,why='LEFT JOIN은 왼쪽(a)의 7줄을 모두 남깁니다. 짝이 있는 3줄은 값, 나머지 4줄은 오른쪽이 NULL.'),
       dict(q='같은 이름의 속성으로 조인하고, 결과에서 그 속성을 한 번만 남기는 조인은?',o=['세타 조인','동등 조인','자연 조인','외부 조인'],a=2,why='자연 조인은 동등 조인 결과에서 중복된 조인 속성을 하나 제거한 것입니다.')]),
dict(id='lv4', short='디비전', title='디비전 ÷ — “모두”를 만족하는 줄 찾기', concept='디비전', en='division', cid='lab:concept/division',
 tag='현장: 필수 과목을 모두 들은 학생', analogy='스탬프 투어',
 situation='졸업하려면 필수 과목 {DB설계, 통계학}을 <b>모두</b> 들어야 합니다. 수강 표에서 졸업 요건을 채운 학생은 누구일까요?',
 pair=(('현장에서는','스탬프 투어에서 지정된 장소의 도장을 <b>전부</b> 모은 사람만 경품을 받습니다. 한 군데라도 빠지면 탈락입니다.'),
       ('관계 대수에서는','R ÷ S: S의 <b>모든</b> 튜플과 짝을 이루는 R의 튜플(S의 속성은 뺀 부분)을 돌려줍니다. 수강(학번, 과목) ÷ 필수(과목) = 필수 과목을 모두 들은 학번.')),
 panel='''<div class="two"><div id="d7t"></div><div><div class="chips" id="d7req"></div><div id="d7out"></div></div></div><div class="insight" id="d7o"></div>''',
 panel_title='직접 해 보기 — 필수 과목을 바꿔 가며 디비전',
 sim='디비전 계산기',
 explain='<p>디비전은 SQL에 전용 문법이 없습니다. “<b>필수 과목 중에 이 학생이 안 들은 과목이 하나도 없다</b>”로 바꿔 말해 <code>NOT EXISTS</code>를 두 번 씁니다. 오늘은 원리만, SQL은 10주차 하위 질의에서 다시 씁니다.</p>',
 formula_title='SQL로 쓴 디비전 (10주차 미리 보기)',
 formula='<pre>SELECT DISTINCT e.학번 FROM 수강 e\nWHERE NOT EXISTS (\n  SELECT * FROM 필수 r\n  WHERE NOT EXISTS (\n    SELECT * FROM 수강 x\n    WHERE x.학번 = e.학번 AND x.과목 = r.과목));</pre>',
 limit='관계 대수 여덟 가지를 모두 봤습니다. 다음 단계는 이것을 실제 DBMS에서 쓰는 언어, SQL입니다. 그 전에 8주차에서 지금까지를 한 번 정리합니다.', limit_label='관계 대수를 실제 DBMS 언어(SQL)로 옮기지 않음',
 quiz=[dict(q='“필수 과목을 모두 수강한 학생”처럼 ‘모두’를 만족하는 튜플을 구하는 연산은?',o=['카티션 곱','디비전','차집합','셀렉트'],a=1,why='디비전(÷)은 나누는 릴레이션의 모든 튜플과 관련된 튜플을 찾습니다.'),
       dict(q='관계 대수와 관계 해석의 차이로 옳은 것은?',o=['관계 대수는 비절차적, 관계 해석은 절차적','관계 대수는 절차적, 관계 해석은 비절차적','둘 다 절차적','둘 다 표현력이 다르다'],a=1,why='관계 대수는 연산 순서를 적는 절차적 언어, 관계 해석은 원하는 결과만 서술하는 비절차적 언어입니다. 표현력은 같다고 알려져 있습니다.')]),
],
duel=dict(q='고르고 잇기 vs 잇고 고르기 — 중간 표의 크기',
 intro='“gold 고객의 주문 목록”을 구합니다. 초파리는 <b>먼저 gold 고객만 고른 뒤(σ) 주문과 잇고(⋈)</b>, 주판봇은 <b>고객 × 주문을 모두 곱한 뒤(×) 조건으로 고릅니다(σ)</b>. 결과는 같습니다. 중간에 만들어지는 표의 줄 수를 비교합니다.',
 fly_pick='σ 먼저, 그다음 ⋈', fly_line='고를 수 있는 건 먼저 골라. 작은 표끼리 이어야 일이 적어.',
 robo_pick='× 먼저, 그다음 σ', robo_line='전부 곱해 놓으면 빠뜨릴 짝이 없지! 고르는 건 나중에!',
 metric='가장 큰 중간 표의 줄 수 (적을수록 이김)', higher=False, step=2,
 after='<div class="ctrl"><label>고객 수 배율 <input type="range" id="d7k" min="1" max="100" value="1"></label><b id="d7kv">× 1 (고객 7 · 주문 10)</b></div><div id="duel7t"></div>',
 run='return PAGE.duel();',
 announce='return "결과는 똑같이 <b>"+r.res+"줄</b>. 그 과정에서 초파리의 가장 큰 중간 표는 <b>"+r.fly.toLocaleString()+"줄</b>, 주판봇은 <b>"+r.robo.toLocaleString()+"줄</b>이었어요.";',
 verdict='return "같은 답이라도 고르기(σ)를 먼저 하면 중간 표가 작아진다. DBMS의 질의 처리기도 이렇게 순서를 바꾼다. 초파리 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>연산</th><th>결과의 모양</th></tr></thead><tbody>
<tr><td>1</td><td>σ 셀렉트 · π 프로젝트</td><td>σ: 줄이 줄어듦 / π: 칸이 줄고 중복 제거</td></tr>
<tr><td>2</td><td>∪ ∩ − × (합병 가능 조건)</td><td>× : 차수 = 합, 카디널리티 = 곱</td></tr>
<tr><td>3</td><td>⋈ 세타·동등·자연·외부·세미</td><td>외부: 짝 없으면 NULL로 채워 남김</td></tr>
<tr><td>4</td><td>÷ 디비전</td><td>“모두”를 만족하는 튜플</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 짝꿍 찾기</b> 사람은 짝이 한 명이지만, 조인은 한 줄이 여러 줄과 짝이 될 수 있습니다(1:N이면 결과가 늘어남).</div><div><b>대결의 한계</b> 실제 DBMS는 카티션 곱을 그대로 만들지 않고 질의 처리기가 순서를 최적화합니다. 대결은 “최적화가 왜 필요한가”를 보여 주는 사고 실험입니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① σ는 줄, π는 칸 ② ×는 모든 짝, ⋈은 의미 있는 짝 ③ 같은 답이라도 먼저 줄이면 덜 일한다.'),
       ('fly','arms','70줄 대신 6줄. 고를 수 있는 건 먼저 고르는 게 습관이 돼야 해.'),
       ('robo','sigh','고객이 100배로 늘어나니까 곱하기가 7만 줄이 됐어… 다음엔 고르기부터 할게.'),
       ('asst','proud','다음 주는 중간 REVIEW! 1~7주차 퀴즈를 한 번에 풀어 볼 수 있대요.')],
next_note='<p class="recap"><b>다음 회차 — 8주차 「중간 REVIEW」:</b> 1~7주차를 한 장의 지도와 모의 문제로 정리합니다.</p>',
gloss={'셀렉트':('셀렉트 σ','기호','조건을 만족하는 튜플만 고르는 연산(수평 부분집합). SQL의 WHERE.','selection','lv1'),
 '프로젝트':('프로젝트 π','기호','지정한 속성만 남기고 중복 튜플을 없애는 연산(수직 부분집합). SQL의 SELECT 칸 목록.','projection','lv1'),
 '폐쇄 특성':('폐쇄 특성','개념','관계 연산의 결과도 릴레이션이라 다시 연산의 입력이 될 수 있는 성질.','closure-property','lv1'),
 '합병 가능':('합병 가능','개념','속성 수가 같고 대응 속성의 도메인이 같아 합·교·차를 쓸 수 있는 두 릴레이션의 관계.','union-compatible','lv2'),
 '카티션 곱':('카티션 곱 ×','기호','두 릴레이션의 튜플을 모든 경우로 짝지은 결과. 카디널리티 = 곱.','cartesian-product','lv2'),
 '자연 조인':('자연 조인','용어','같은 이름의 속성으로 동등 조인하고 그 속성은 한 번만 남기는 조인.','natural-join','lv3'),
 '외부 조인':('외부 조인','용어','짝이 없는 튜플도 버리지 않고 NULL로 채워 결과에 남기는 조인(LEFT·RIGHT·FULL).','outer-join','lv3'),
 '세미 조인':('세미 조인','용어','짝이 있는 왼쪽 튜플만, 왼쪽 속성만 돌려주는 조인. SQL에서는 EXISTS.','semi-join','lv3'),
 '디비전':('디비전 ÷','기호','나누는 릴레이션의 모든 튜플과 관련 있는 튜플을 찾는 연산.','division','lv4'),
 '관계 해석':('관계 해석','개념','원하는 결과가 무엇인지만 서술하는 비절차적 질의 언어(튜플·도메인 관계 해석).','relational-calculus','lv4')},
facts=[('F01','관계 대수 연산자는 일반 집합 연산(합·교·차·카티션 곱)과 순수 관계 연산(셀렉트·프로젝트·조인·디비전)으로 나뉨','문헌 사실','kim3ed','lv1','6장'),
       ('F02','노션 실습 a = {2,4,6,8,10,12,14}, b = {4,8,12,16}','문헌 사실','ahn2025sqlops','lv2','실습#2-2'),
       ('F03','노션 실습#3-3 LEFT OUTER JOIN 코드 칸에는 INNER JOIN이 적혀 있음 (설명은 LEFT JOIN 기준)','문헌 사실','ahn2025sqlops','lv3','실습#3-3'),
       ('F04','FULL OUTER JOIN은 LEFT JOIN과 RIGHT JOIN 결과를 UNION으로 합쳐 구현','문헌 사실','ahn2025sqlops','lv3','실습#3-9'),
       ('F05','관계 대수와 관계 해석은 표현력이 같다고 알려져 있음','문헌 사실','kim3ed','lv4','6장 (Codd의 정리로 알려짐)')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='출판 연도 미확인'),
      dict(id='ahn2025sqlops',type='webpage',title='SQL 기본 문법 : 연산',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed812fbd9ce0ab3a3b7f1b',role='primary'),
      dict(id='ahn2025w06',type='webpage',title='06주차 : 관계 데이터 연산',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed8109aeb1cafd7b531709',role='background')],
models=['고객·주문 데이터 (노션 실습 예제)','a·b 표 (노션 실습 그대로)','수강·필수 과목 디비전 예 (예시 데이터)','대결의 고객 수 배율 (규모를 바꿔 보는 설명용 시나리오)'],
cover_alt='두 장의 투명 필름 표를 겹쳐 같은 값끼리 빛이 이어지는 모습을 네 캐릭터가 지켜보는 표지 (대체 그림)',
cover_svg='<svg width="300" height="140" viewBox="0 0 300 140"><circle cx="120" cy="70" r="52" fill="#e6eefb" fill-opacity=".8" stroke="#1e55c8"/><circle cx="180" cy="70" r="52" fill="#f6ecfa" fill-opacity=".7" stroke="#9b3fb5"/><text x="95" y="75" font-size="14" fill="#1e55c8">2 6 10</text><text x="140" y="75" font-size="14" fill="#13733a">4 8 12</text><text x="200" y="75" font-size="14" fill="#9b3fb5">16</text><text x="20" y="20" font-size="22" fill="#5b6874">σ π ⋈</text></svg>',
prereq=['06'],
cards={'join7':[['INNER JOIN — 벤 다이어그램에서 칠해지는 곳은?','두 원이 <b>겹치는 부분만</b> (4, 8, 12)'],['LEFT JOIN 은?','<b>왼쪽 원 전체</b> (a의 7개, 짝 없으면 NULL)'],['LEFT JOIN … WHERE b.t2 IS NULL 은?','<b>왼쪽 원에서 겹치는 부분을 뺀 곳</b> (2, 6, 10, 14) = 안티 조인'],['FULL OUTER JOIN 은?','<b>두 원 전체</b> (8개) — MariaDB는 LEFT ∪ RIGHT로'],['FULL … 교집합 제외 는?','<b>두 원에서 겹치는 부분만 뺀 곳</b> (2, 6, 10, 14, 16)'],['SEMI JOIN (EXISTS) 은?','겹치는 부분이지만 <b>왼쪽 칸만</b> (4, 8, 12)']]},
js=r'''
var $=LAB.$,$$=LAB.$$;
var C=['id','name','age','rank','job','credit'],R=[['apple','jane',20,'gold','student',1000],['banana','kim',25,'vip','nurse',2500],['carrot','duke',28,'gold','teacher',4500],['orange','albert',22,'silver','student',0],['melon','dragon',35,'gold','clerk',5000],['peach','jack',31,'silver','doctor',300],['pear','robert',null,'silver','clerk',500]];
var pick={1:1,5:1};var pc=$('#p7c');C.forEach(function(c,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent='π '+c;b.setAttribute('aria-pressed',!!pick[i]);b.onclick=function(){pick[i]=!pick[i];b.setAttribute('aria-pressed',!!pick[i]);s7();};pc.appendChild(b);});
var COND={'':[function(){return true;},'',''],gold:[function(r){return r[3]==='gold';},"rank='gold'","WHERE rank = 'gold'"],age:[function(r){return r[2]!=null&&r[2]>=25;},'age≥25','WHERE age >= 25'],stu:[function(r){return r[4]==='student';},"job='student'","WHERE job = 'student'"],both:[function(r){return r[3]==='gold'&&r[5]>2000;},"rank='gold' ∧ credit>2000","WHERE rank = 'gold' AND credit > 2000"]};
function s7(){var k=$('#s7c').value,cd=COND[k],ix=Object.keys(pick).filter(function(i){return pick[i];}).map(Number).sort();if(!ix.length)ix=[0];
 var rows=R.filter(cd[0]),proj=[],seen={};rows.forEach(function(r){var x=ix.map(function(i){return r[i];}),key=JSON.stringify(x);if(!seen[key]){seen[key]=1;proj.push(x);}});
 var alg='π<sub>'+ix.map(function(i){return C[i];}).join(',')+'</sub>('+(k?'σ<sub>'+cd[1]+'</sub>(customer)':'customer')+')';
 $('#s7eq').innerHTML='관계 대수: '+alg+'<br>SQL: <code>SELECT DISTINCT '+ix.map(function(i){return C[i];}).join(', ')+' FROM customer '+cd[2]+';</code>';
 $('#s7in').innerHTML=LAB.tableHTML(C,R,{cap:'입력 customer (7줄)',cls:function(r){return cd[0](r)?'hl':'dim';}});
 $('#s7out').innerHTML=LAB.tableHTML(ix.map(function(i){return C[i];}),proj,{cap:'결과 ('+proj.length+'줄)'});
 $('#s7o').innerHTML='σ로 남은 줄 <b>'+rows.length+'</b> → π 뒤 <b>'+proj.length+'</b>줄'+(rows.length>proj.length?' (중복 '+(rows.length-proj.length)+'줄이 π에서 사라짐 — SQL은 DISTINCT를 써야 같음)':'');}
$('#s7c').onchange=s7;s7();
/* 디비전 */
var EN=[['S1','DB설계'],['S1','통계학'],['S1','회계원리'],['S2','DB설계'],['S3','통계학'],['S3','DB설계'],['S4','회계원리']],SUB=['DB설계','통계학','회계원리'],req={0:1,1:1};
$('#d7t').innerHTML=LAB.tableHTML(['학번','과목'],EN,{cap:'수강 (7줄)'});
var dr=$('#d7req');SUB.forEach(function(s,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=s;b.setAttribute('aria-pressed',!!req[i]);b.onclick=function(){req[i]=!req[i];b.setAttribute('aria-pressed',!!req[i]);d7();};dr.appendChild(b);});
function d7(){var rq=SUB.filter(function(s,i){return req[i];});var st=['S1','S2','S3','S4'];var ok=st.filter(function(x){return rq.every(function(s){return EN.some(function(e){return e[0]===x&&e[1]===s;});});});
 $('#d7out').innerHTML=LAB.tableHTML(['필수 과목'],rq.map(function(s){return [s];}),{cap:'필수 (나누는 표)'})+LAB.tableHTML(['학번'],ok.map(function(s){return [s];}),{cap:'수강 ÷ 필수 = '+ok.length+'명'});
 $('#d7o').innerHTML=rq.length?('필수 '+rq.length+'과목을 <b>모두</b> 들은 학생: '+(ok.join(', ')||'없음')+'. 하나라도 빠진 학생은 탈락합니다.'):'필수 과목이 하나도 없으면 모든 학생이 조건을 만족합니다(“모두 0개 중 빠진 것 없음”).';}
d7();
/* 대결 */
var ORD=[['q01','apple'],['q02','melon'],['q03','banana'],['q04','carrot'],['q05','melon'],['q06','banana'],['q07','apple'],['q08','pear'],['q09','banana'],['q10','carrot']];
var dk=$('#d7k');dk.oninput=function(){var k=+dk.value;$('#d7kv').textContent='× '+k+' (고객 '+(7*k)+' · 주문 '+(10*k)+')';};
PAGE.duel=function(){var k=+dk.value,cust=7*k,ord=10*k,gold=3*k,goldOrd=ORD.filter(function(o){return ['apple','carrot','melon'].indexOf(o[1])>=0;}).length*k;
 var fly=Math.max(gold,goldOrd),robo=cust*ord;
 document.getElementById('duel7t').innerHTML=LAB.tableHTML(['단계','초파리 (σ → ⋈)','주판봇 (× → σ)'],[['1단계',"σ gold 고객 → "+gold+"줄","고객 × 주문 → "+robo.toLocaleString()+"줄"],['2단계',"⋈ 주문 → "+goldOrd+"줄","σ (id 일치 ∧ gold) → "+goldOrd+"줄"]]);
 return {fly:fly,robo:robo,flyTxt:fly.toLocaleString()+'줄',roboTxt:robo.toLocaleString()+'줄',res:goldOrd};};
''',
labs='''lab7a:{setup:"CREATE DATABASE jointest; USE jointest; CREATE TABLE a (t1 INT); CREATE TABLE b (t2 INT); INSERT INTO a (t1) VALUES (2), (4), (6), (8), (10), (12), (14); INSERT INTO b (t2) VALUES (4), (8), (12), (16);",
presets:[{t:"a, b 보기 (#2-3)",q:"SELECT * FROM a;\\nSELECT * FROM b;"},{t:"UNION ALL (#3-1a)",q:"SELECT * FROM a\\nUNION ALL\\nSELECT * FROM b;"},{t:"UNION 중복 제거",q:"SELECT * FROM a\\nUNION\\nSELECT * FROM b;"},{t:"교집합 a ∩ b",q:"SELECT t1 FROM a\\nWHERE t1 IN (SELECT t2 FROM b);"},{t:"차집합 a − b",q:"SELECT t1 FROM a\\nWHERE t1 NOT IN (SELECT t2 FROM b);"},{t:"카티션 곱 (#3-1b)",q:"SELECT a.t1, b.t2\\nFROM a, b;"},{t:"곱의 행 수 세기",q:"SELECT COUNT(*) AS 행수 FROM a, b;"}],ready:"노션 「SQL 기본 문법 : 연산」의 jointest 데이터베이스 — a(7줄), b(4줄)."},
lab7b:{setup:"CREATE DATABASE jointest; USE jointest; CREATE TABLE a (t1 INT); CREATE TABLE b (t2 INT); INSERT INTO a (t1) VALUES (2), (4), (6), (8), (10), (12), (14); INSERT INTO b (t2) VALUES (4), (8), (12), (16);",
presets:[{t:"INNER (#3-2)",q:"SELECT a.t1, b.t2\\nFROM a\\nINNER JOIN b ON a.t1 = b.t2;"},{t:"LEFT (#3-3 오타 고침)",q:"SELECT a.t1, b.t2\\nFROM a\\nLEFT JOIN b ON a.t1 = b.t2;"},{t:"RIGHT (#3-4)",q:"SELECT a.t1, b.t2\\nFROM a\\nRIGHT OUTER JOIN b ON a.t1 = b.t2;"},{t:"SEMI (#3-5)",q:"SELECT a.t1\\nFROM a\\nWHERE EXISTS (\\n  SELECT 1 FROM b WHERE a.t1 = b.t2\\n);"},{t:"ANTI (#3-6)",q:"SELECT a.t1\\nFROM a\\nLEFT JOIN b ON a.t1 = b.t2\\nWHERE b.t2 IS NULL;"},{t:"RIGHT 제외 (#3-8)",q:"SELECT a.t1, b.t2\\nFROM a\\nRIGHT JOIN b ON a.t1 = b.t2\\nWHERE a.t1 IS NULL;"},{t:"FULL 시도",q:"SELECT a.t1, b.t2\\nFROM a FULL OUTER JOIN b ON a.t1 = b.t2;"},{t:"FULL 흉내 (#3-9)",q:"SELECT a.t1, b.t2 FROM a\\nLEFT JOIN b ON a.t1 = b.t2\\nUNION\\nSELECT a.t1, b.t2 FROM a\\nRIGHT JOIN b ON a.t1 = b.t2\\nWHERE a.t1 IS NULL;"},{t:"FULL − 교집합 (#3-10)",q:"SELECT a.t1, b.t2 FROM a\\nLEFT JOIN b ON a.t1 = b.t2\\nWHERE b.t2 IS NULL\\nUNION\\nSELECT a.t1, b.t2 FROM a\\nRIGHT JOIN b ON a.t1 = b.t2\\nWHERE a.t1 IS NULL;"}],ready:"같은 a·b 표입니다. 버튼을 누르기 전에 결과 행 수를 먼저 짐작해 보세요."}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'셀렉트는 조건에 맞는 튜플을, 프로젝트는 지정한 속성을 골라 새 릴레이션을 만드는 연산.','lv2':'합·교·차(합병 가능한 두 릴레이션)와 모든 짝을 만드는 카티션 곱.','lv3':'공통 속성의 값으로 두 릴레이션의 튜플을 잇는 연산(세타·동등·자연·외부·세미 조인).','lv4':'나누는 릴레이션의 모든 튜플과 관련 있는 튜플을 찾는 연산.'}[s['id']]
