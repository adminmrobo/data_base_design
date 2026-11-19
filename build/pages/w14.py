# 14주차 — 데이터베이스 응용 기술 (비정형 데이터 · NoSQL · 색인 · 분석용 DB)
POSTS = [(1,'김선우','제주 바다',['여행','제주','바다']),(2,'정소화','부산 맛집',['여행','부산','맛집']),(3,'고명석','제주 흑돼지',['제주','맛집']),
         (4,'김선우','강릉 커피',['여행','강릉','커피']),(5,'정소화','집에서 커피',['커피','홈카페']),(6,'고명석','여름 바다',['여행','바다'])]
TAGS = sorted({t for p in POSTS for t in p[3]})
SNS = ("CREATE DATABASE sns; USE sns; CREATE TABLE 게시글 (글번호 INT PRIMARY KEY, 작성자 VARCHAR(10), 제목 VARCHAR(30)); "
 "CREATE TABLE 태그 (태그번호 INT PRIMARY KEY, 태그명 VARCHAR(20) UNIQUE); "
 "CREATE TABLE 글태그 (글번호 INT, 태그번호 INT, PRIMARY KEY (글번호, 태그번호), FOREIGN KEY (글번호) REFERENCES 게시글(글번호), FOREIGN KEY (태그번호) REFERENCES 태그(태그번호)); "
 "INSERT INTO 게시글 VALUES " + ",".join("(%d,'%s','%s')" % (p[0], p[1], p[2]) for p in POSTS) + "; "
 "INSERT INTO 태그 VALUES " + ",".join("(%d,'%s')" % (i + 1, t) for i, t in enumerate(TAGS)) + "; "
 "INSERT INTO 글태그 VALUES " + ",".join("(%d,%d)" % (p[0], TAGS.index(t) + 1) for p in POSTS for t in p[3]) + ";")
PAGE = dict(
num='14', slug='database_applications', kind='lecture', short='14주', chip='14주차',
title='데이터베이스 응용 기술', title_en='Database application technologies',
subtitle='표에 잘 안 맞는 데이터 — 해시태그·사진·로그, 그리고 NoSQL과 색인',
toc='비정형 데이터와 빅데이터 3V, 4세대 이후 DBMS(NoSQL·NewSQL), 문서형 데이터베이스(MongoDB)와 해시태그 사례, 색인으로 빨라지는 조회(RPG 사례), 운영용 DB와 분석용 DB',
kicker='데이터베이스 설계 · 14주차 · 응용 기술',
question='해시태그 사이의 관계는 표로 담는 게 좋을까, 문서로 담는 게 좋을까?',
desc='데이터베이스 설계 14주차: 비정형 데이터와 빅데이터(3V), 4세대 이후 DBMS(NoSQL, NewSQL), 관계형 표와 문서형(MongoDB) 모델 비교, 해시태그 사례 SQL 실습, 색인(인덱스)과 조회 성능(RPG 사례), 운영용(OLTP)과 분석용(OLAP·데이터 웨어하우스) 데이터베이스.',
intro='<p>지금까지 다룬 데이터는 모두 <b>칸이 정해진 표</b>였습니다. 그런데 SNS 글에는 해시태그가 몇 개 붙을지 모르고, 사진에는 칸이 없고, 게임 전투 로그는 1초에 수천 줄씩 쌓입니다. 1주차 교안의 질문 — “비정형 데이터, 빅데이터(3V): 안정성과 일관성 유지가 가능?” — 에 오늘 답해 봅니다. 해시태그 사례를 <b>관계형 표</b>와 <b>문서형(MongoDB 방식)</b>으로 각각 담아 보고, 11주 RPG 사례의 “조회 3초 → 0.1초”를 만든 <b>색인</b>을 손으로 세어 봅니다.</p>',
kpis=[('3V','Volume · Velocity · Variety'),('4가지','NoSQL: 키-값 · 문서 · 열 · 그래프'),('3초 → 0.1초','RPG 사례 — 색인 추가 후 응답 시간'),('OLTP · OLAP','운영용 vs 분석용')],
hero_talk=[
 ('doc','front','오늘은 “관계형이 늘 정답인가?”를 묻는 날이다. 답은 <b>데이터 모양과 쓰는 방식</b>에 달려 있다.'),
 ('asst','smile','12주 내내 쪼개라고 하셨는데, 오늘은 합쳐도 된다고요?'),
 ('fly','clip','쪼개는 이유가 “한 사실은 한 곳에”였지. 그런데 읽을 때마다 다시 합쳐야 한다면 비용이 생겨. 오늘 대결이 그거야.'),
 ('robo','smile','이번엔 내가 자신 있어! 글 하나에 태그까지 통째로 넣는 문서형이 빠를걸!')],
crew=[('doc','front','모델 비교 정리, 판정'),('asst','smile','실습 진행, 숫자 발표'),('fly','clip','정규화된 표 쪽 (오늘 대결)'),('robo','smile','문서형 쪽 (오늘 대결)')],
recap='2주차: 정형·반정형·비정형 데이터. 11주차: 물리적 설계에서 색인 결정. 12주차: 반정규화는 조회 위주일 때 검토. — 오늘은 이것들이 실제 기술(NoSQL, 색인)로 어떻게 나타나는지 봅니다.',
notion=[('노션 일정표 「13주차 : 데이터 베이스 응용기술」 (노션 일정의 주차 번호는 이 사이트와 다릅니다)', NOTION+'1ab17a4520ed8182bd55ffb2a052dbed', '비정형 데이터 읽을거리 · 사례: 이미지 검색 (첨부 발표 자료·영상)'),
        ('MongoDB 공식 사이트', 'https://www.mongodb.com/', '노션 13주차 첫 링크 — 문서형 데이터베이스'),
        ('MongoDB Full-Text Search (sy34.net)', 'https://sy34.net/mongodb-full-text-search/', '노션 13주차 링크 — 문서 안의 글자 검색'),
        ('FLO 테크 — MongoDB 도입기 (드림어스 블로그)', 'https://www.blog-dreamus.com/post/flo-tech-mongodb-도입기', '노션 13주차 링크 — 실제 서비스의 도입 사례')],
why=[('데이터가 달라졌다','SNS 글, 사진, 센서·게임 로그처럼 칸이 정해지지 않았거나 매우 빠르게 쌓이는 데이터가 늘었습니다(교안: 비정형 데이터, 빅데이터 3V).'),
     ('도구가 늘었다','교안의 DBMS 발전 과정: 4세대 이후 NoSQL, NewSQL DBMS. 관계형을 대체한다기보다 함께 씁니다(RPG 사례: “전투 중 실시간 데이터는 NoSQL 병행 검토”).'),
     ('설계자의 판단','어느 데이터를 어디에 담을지 정하는 것이 설계자의 일입니다. 기말 이후 실무에서 가장 먼저 만나는 질문입니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th></th><th>관계형 (SQL)</th><th>NoSQL (예: 문서형 MongoDB)</th></tr></thead><tbody>
<tr><td>데이터 모양</td><td>칸이 정해진 표 (스키마 먼저)</td><td>JSON 같은 문서, 문서마다 칸이 달라도 됨</td></tr>
<tr><td>관계</td><td>외래키 + JOIN</td><td>문서 안에 넣기(내장) 또는 참조</td></tr>
<tr><td>강점</td><td>일관성, 트랜잭션(13주), 복잡한 질의·집계</td><td>스키마 유연성, 여러 서버로 늘리기(수평 확장)</td></tr>
<tr><td>주의</td><td>칸 구조 변경이 무거움(11주 대결)</td><td>중복 관리 책임이 응용 프로그램으로 넘어감(12주 반정규화)</td></tr></tbody></table></div><p>NewSQL은 관계형의 SQL·트랜잭션을 유지하면서 NoSQL처럼 여러 서버로 늘리는 것을 목표로 하는 DBMS 묶음을 가리킵니다.</p>''',
steps=[
dict(id='lv1', short='비정형·3V', title='비정형 데이터와 빅데이터 3V — 어떤 데이터가 표에 안 맞나', concept='비정형 데이터와 빅데이터', en='unstructured data and big data', cid='lab:concept/unstructured-big-data',
 tag='현장: SNS·사진·로그', analogy='서류철과 상자',
 situation='아래 다섯 가지 데이터를 담아야 합니다. 어느 것이 관계형 표에 잘 맞고, 어느 것이 어색할까요? 왜 어색할까요?',
 pair=(('현장에서는','양식이 정해진 서류는 서류철(칸이 있는 표)에 꽂으면 되지만, 모양이 제각각인 물건은 이름표를 붙인 상자에 담는 편이 낫습니다.'),
       ('데이터베이스에서는','<b>빅데이터 3V</b>: Volume(양) · Velocity(속도) · Variety(다양성). 교안의 질문은 이런 데이터에서도 “안정성과 일관성 유지가 가능한가?”입니다. 관계형은 일관성이 강점이지만, 다양성(칸이 매번 다름)과 속도(초당 수천 건)에서 부담이 생깁니다.')),
 panel='''<div class="chips" id="dt14"></div><div class="insight" id="dt14o">데이터를 골라 보세요.</div>''',
 panel_title='직접 해 보기 — 이 데이터, 어디에 담을까',
 sim='데이터 유형별 저장 방식 고르기',
 explain='<p>정답은 하나가 아닙니다. 주문표처럼 칸이 정해지고 돈이 오가는 데이터는 관계형이 기본입니다. 칸이 글마다 다른 SNS 글은 문서형, 초당 수천 건의 로그는 키-값·열 지향, “누가 누구를 팔로우”처럼 관계 자체가 주인공인 데이터는 그래프형이 잘 맞는 경우가 많습니다. 실제 서비스는 이들을 <b>함께</b> 씁니다.</p>',
 limit='“문서형이 잘 맞는다”는 말이 정말인지, 같은 데이터를 두 방식으로 담아 비교해 봐야 합니다.', limit_label='같은 데이터를 두 모델로 비교하지 않음',
 say=('asst','spark','사진은 칸이 없고, 해시태그는 개수가 매번 달라요. 표가 싫어하는 두 가지네요!'),
 quiz=[dict(q='빅데이터 3V에 해당하지 않는 것은?',o=['Volume(양)','Velocity(속도)','Variety(다양성)','Validity(유효성)'],a=3,why='교안의 3V는 Volume·Velocity·Variety입니다.'),
       dict(q='교안의 DBMS 발전 과정에서 4세대 이후 DBMS로 제시된 것은?',o=['계층·망형','관계형만','NoSQL, NewSQL','파일 시스템'],a=2,why='교안: “4세대 이후 데이터베이스 관리 시스템: NoSQL, NewSQL DBMS”.')]),
dict(id='lv2', short='표 vs 문서', title='해시태그 사례 — 관계형 표 3개 vs 문서 하나', concept='관계형 모델과 문서형 모델', en='relational vs document model', cid='lab:concept/relational-vs-document',
 tag='연구실: 해시태그 간의 관계는?', analogy='카드 세 장 vs 봉투 하나',
 situation='교안의 질문 “해시태그 사이의 관계는?”. 글 6개에 해시태그가 붙어 있습니다. #제주와 함께 가장 많이 쓰인 태그는? 관계형 표로 SQL을 짜 보고, 같은 데이터를 문서로 담으면 어떻게 생겼는지 비교합니다.',
 pair=(('연구실에서는','관계형은 게시글 카드, 태그 카드, “어느 글에 어느 태그” 연결 카드로 나눠 보관합니다. 문서형은 글 하나를 봉투에 넣고 그 안에 태그 목록을 함께 넣습니다.'),
       ('데이터베이스에서는','관계형: 게시글 N : M 태그 → 규칙 2로 <b>글태그</b> 릴레이션(11주). 문서형(MongoDB): <code>{ "글번호": 1, "작성자": "김선우", "태그": ["여행","제주","바다"] }</code> — 다중값을 문서 안의 배열로 둡니다. 1NF(12주)를 일부러 따르지 않는 셈입니다.')),
 panel='<div class="sqllab" id="lab14" data-lab="lab14"></div><p class="ptitle" style="margin-top:14px">같은 데이터를 문서로 (MongoDB 방식 · 설명용)</p><pre id="doc14" style="font-size:13px;background:#f7f9fb;border:1px solid #d5dbe2;border-radius:8px;padding:10px;overflow-x:auto;max-height:260px"></pre><div class="ctrl"><label>태그 <select id="tg14"></select></label><button type="button" class="bt primary" id="tg14b">문서에서 찾기 (find)</button></div><div class="insight" id="tg14o"></div>',
 panel_title='SQL 실습실 + 문서 보기 — 해시태그',
 sim='해시태그 관계형·문서형 비교 실습',
 explain='<p><b>관계형 질의(실습실 ④)</b>는 글태그 표를 자기 자신과 JOIN해 “같은 글에 함께 붙은 태그 쌍”을 셉니다. 정확하고 강력하지만 JOIN이 세 번입니다. <b>문서형</b>에서는 <code>db.게시글.find({ "태그": "제주" })</code> 한 번으로 해당 글과 태그 목록이 함께 나옵니다. 대신 “#여행을 #여행기로 바꾸기” 같은 일은 태그가 들어 있는 모든 문서를 고쳐야 합니다(12주 갱신 이상과 같은 구조).</p><p style="font-size:14px;color:#5b6874">아래 문서 보기는 MongoDB를 흉내 낸 설명용 화면입니다. 실제 MongoDB는 노션 13주차 링크의 공식 사이트에서 무료 클라우드로 체험할 수 있습니다.</p>',
 aicheck='<p>AI에게 “SNS 서비스 DB 설계해 줘”라고 하면 무조건 MongoDB, 혹은 무조건 MySQL을 권하는 답이 나오기도 합니다. 되물을 질문: <b>가장 자주 하는 조회는 무엇인가? 태그 이름이 바뀌는 일이 있는가? 결제처럼 트랜잭션이 필요한 부분이 있는가?</b> — 답에 따라 둘을 섞는 설계가 나와야 정상입니다.</p>',
 limit='모델을 바꾸지 않아도 같은 표에서 조회를 수십 배 빠르게 하는 방법이 있습니다. 11주 물리적 설계의 색인입니다.', limit_label='같은 모델 안에서의 조회 성능 개선은 아직',
 quiz=[dict(q='게시글과 태그의 N:M 관계를 관계형으로 담을 때 필요한 것은? (11주 규칙 2)',o=['게시글 표에 태그 칸 하나','글태그처럼 양쪽 기본키를 가진 별도 릴레이션','태그 표에 글번호 칸 하나','관계를 생략'],a=1,why='N:M 관계는 별도 릴레이션이 되고 양쪽 기본키를 외래키로 가집니다.'),
       dict(q='문서형에서 글 문서 안에 태그 배열을 넣었다. 태그 이름 “여행”을 “여행기”로 바꾸려면?',o=['태그 표 한 줄만 수정','“여행”이 들어 있는 모든 글 문서를 수정','바꿀 수 없다','자동으로 바뀐다'],a=1,why='중복 저장된 값이므로 모든 문서를 고쳐야 합니다. 12주의 갱신 이상과 같은 구조입니다.')]),
dict(id='lv3', short='색인', title='색인(인덱스) — 조회 3초를 0.1초로 만든 것', concept='색인과 조회 성능', en='index and query performance', cid='lab:concept/index-performance',
 tag='현장: RPG 서버 오픈 날', analogy='책 뒤의 찾아보기',
 situation='RPG 「용사의 전설」 사례: 신규 서버 오픈 날 동시 접속 5만 명, 인벤토리 조회가 느려 서비스가 멈췄습니다. 색인을 추가하고 조회 로직을 고쳐 응답 시간이 3초에서 0.1초로 줄었습니다(사례 기록). 색인은 왜 빠를까요?',
 pair=(('현장에서는','두꺼운 책에서 “정규화”를 찾을 때 첫 쪽부터 넘기지 않고 책 뒤의 <b>찾아보기</b>(가나다순)에서 쪽 번호를 찾습니다.'),
       ('DBMS에서는','<b>색인</b>: 특정 칸의 값을 정렬해 두고 그 행의 위치를 가리키는 구조(대표적으로 B-트리). 색인이 없으면 <b>전체 스캔</b>(모든 행 확인), 있으면 정렬된 구조를 반씩 좁혀 찾습니다. 대가: 저장 공간과 INSERT·UPDATE 때 색인도 고쳐야 하는 비용.')),
 panel='''<div class="ctrl"><label>행 수 N <input type="range" id="ix14n" min="3" max="7" step="1" value="5"></label><b id="ix14v"></b></div><div id="ix14t"></div><p class="cvcap">비교 횟수는 최악의 경우입니다. 정렬된 색인을 반씩 좁혀 찾는 횟수는 약 log₂N + 1 (설명용 단순화 — 실제 B-트리는 한 번에 여러 갈래로 나뉘어 더 적습니다).</p>''',
 panel_title='직접 해 보기 — 전체 스캔 vs 색인',
 sim='전체 스캔과 색인 비교 횟수',
 explain='<p><b>손으로 세기:</b> 1,000명 중 한 명을 찾을 때 전체 스캔은 최악 1,000번, 반씩 좁히면 1,000 → 500 → 250 → … → 1로 약 10번입니다. N이 10배가 될 때 스캔은 10배, 반씩 좁히기는 약 3~4번만 늘어납니다.</p><p><b>MariaDB에서:</b> <code>CREATE INDEX idx_inv_char ON inventories(character_id);</code> 그리고 <code>EXPLAIN SELECT …</code>로 색인을 쓰는지 확인합니다. (실습실 엔진은 색인을 흉내 내지 않습니다.) 색인은 WHERE·JOIN에 자주 쓰는 칸에 걸고, 값 종류가 둘뿐인 칸(성별 등)이나 자주 바뀌는 칸에는 효과가 작습니다.</p>',
 limit='여기까지는 주문·인벤토리처럼 “지금 일어나는 일”을 처리하는 데이터베이스였습니다. 몇 년치 데이터를 모아 분석하는 데이터베이스는 다르게 설계합니다.', limit_label='분석 목적의 데이터베이스 설계는 아직',
 say=('fly','point','색인은 공짜가 아니야. 찾기는 빨라지지만 넣고 고칠 때마다 찾아보기도 같이 고쳐야 해.'),
 quiz=[dict(q='정렬된 색인에서 반씩 좁혀 찾을 때, 행 1,000,000개에서 필요한 비교 횟수에 가장 가까운 것은? (계산)',o=['약 20번','약 1,000번','약 500,000번','약 1,000,000번'],a=0,why='2²⁰ ≈ 1,048,576이므로 약 20번입니다.'),
       dict(q='색인의 단점으로 옳은 것은?',o=['조회가 느려진다','INSERT·UPDATE 때 색인도 갱신해야 해 쓰기 비용이 늘어난다','기본키를 쓸 수 없다','JOIN을 할 수 없다'],a=1,why='저장 공간과 쓰기 비용이 늘어나는 것이 대가입니다.')]),
dict(id='lv4', short='운영 vs 분석', title='운영용 DB와 분석용 DB — OLTP, OLAP, 데이터 웨어하우스', concept='OLTP와 OLAP', en='oltp and olap', cid='lab:concept/oltp-olap',
 tag='연구실: 한빛 마트의 두 질문', analogy='계산대와 결산실',
 situation='한빛 마트(11주)에서 두 가지 질문이 옵니다. ① “apple 회원의 주문 o01 배송지를 바꿔 주세요.” ② “지난 3년간 지역·월·상품별 매출 추세를 보여 주세요.” 같은 데이터베이스로 둘 다 처리하면 어떤 일이 생길까요?',
 pair=(('현장에서는','마트 계산대는 한 번에 손님 한 명을 빠르게 처리하고, 본사 결산실은 몇 년치 영수증을 한꺼번에 모아 분석합니다. 결산실이 계산대를 막고 영수증을 뒤지면 손님 줄이 길어집니다.'),
       ('데이터베이스에서는','<b>OLTP</b>(온라인 트랜잭션 처리): 짧은 읽기·쓰기가 아주 많음, 정규화된 표, 13주의 트랜잭션. <b>OLAP</b>(온라인 분석 처리): 대량 읽기·집계, 운영 DB에서 데이터를 모아 둔 <b>데이터 웨어하우스</b>에서 수행. 분석 쪽은 조회 위주라 반정규화(12주)를 흔히 씁니다.')),
 panel='''<div class="tbl"><table><thead><tr><th></th><th>OLTP (운영용)</th><th>OLAP (분석용)</th></tr></thead><tbody>
<tr><td>대표 질문</td><td>주문 o01 배송지 변경</td><td>3년간 지역·월·상품별 매출</td></tr>
<tr><td>한 번에 다루는 행</td><td>몇 행</td><td>수백만 행 이상</td></tr>
<tr><td>주된 연산</td><td>INSERT · UPDATE · 짧은 SELECT</td><td>GROUP BY · 집계 SELECT</td></tr>
<tr><td>설계</td><td>정규화(3NF), 트랜잭션</td><td>반정규화, 데이터 웨어하우스</td></tr>
<tr><td>오늘 강의와 연결</td><td>9·10·13주</td><td>10주 GROUP BY, 12주 반정규화</td></tr></tbody></table></div>
<div class="chips" id="op14"></div><div class="insight" id="op14o">질문을 골라 OLTP / OLAP로 나눠 보세요.</div>''',
 panel_title='직접 해 보기 — 이 질문은 운영인가 분석인가',
 sim='OLTP·OLAP 분류',
 explain='<p>데이터 웨어하우스는 여러 운영 DB(주문, 회원, 재고 …)의 데이터를 주기적으로 추출·변환·적재(ETL)해 분석용으로 모아 둔 데이터베이스입니다. 이렇게 나누면 분석이 운영을 느리게 하지 않고, 분석에 맞는 구조(반정규화·사실 표와 차원 표)를 따로 설계할 수 있습니다.</p>',
 limit='다음 주는 기말 리뷰입니다. 9~14주의 SQL·설계·정규화·트랜잭션·응용을 한 번에 다시 엮습니다.', limit_label='후반부 전체를 엮어 보는 정리는 아직',
 quiz=[dict(q='“3년간 지역별 월 매출 추세”를 구하는 작업은?',o=['OLTP','OLAP','DCL','TCL'],a=1,why='대량 데이터를 집계·분석하는 OLAP 작업입니다.'),
       dict(q='데이터 웨어하우스의 설명으로 옳은 것은?',o=['주문 접수용 운영 DB','여러 운영 DB의 데이터를 분석용으로 모아 둔 DB','권한 관리 도구','로그 파일'],a=1,why='여러 원천의 데이터를 통합해 분석용으로 쌓아 둔 데이터베이스입니다.')]),
],
duel=dict(q='SNS 피드 화면 — 정규화된 표 vs 문서형',
 intro='피드 화면은 글 6개를 <b>태그와 함께</b> 보여 줍니다(이 서비스에서 가장 자주 하는 조회). 초파리는 <b>정규화된 표 3개</b>(게시글·태그·글태그, 매번 JOIN), 주판봇은 <b>문서형</b>(글 문서 안에 태그 배열). 피드를 한 번 그릴 때 읽는 행·문서 수를 셉니다.',
 fly_pick='정규화된 표 3개 + JOIN', fly_line='태그는 태그 표에 한 번만. 피드는 JOIN으로 다시 합치면 돼.',
 robo_pick='문서형 — 글 안에 태그 배열', robo_line='피드는 글이랑 태그를 늘 같이 보여 주잖아! 처음부터 같이 담아 두자!',
 metric='피드 1회에 읽는 행·문서 수 (예시 데이터 6개 기준 · 적을수록 이김)', higher=False, step=3,
 after='<div id="duel14t"></div>',
 run='return PAGE.duel();',
 announce='return "[예시 데이터 기준] 피드 한 번에 초파리는 <b>"+r.fly+"행</b>(게시글 "+r.p+" + 글태그 "+r.pt+" + 태그 "+r.pt+"), 주판봇은 문서 <b>"+r.robo+"개</b>를 읽었어요.";',
 verdict='return "이 서비스의 주된 조회(글과 태그를 함께 보기)에서는 문서형이 덜 읽는다. 주판봇 승. 단, 태그 이름 변경이나 태그별 통계가 주된 일이라면 결과는 달라진다.";'),
summary='''<div class="tbl"><table><thead><tr><th>주제</th><th>한 줄</th></tr></thead><tbody>
<tr><td>비정형 · 3V</td><td>양·속도·다양성 — 관계형만으로는 부담이 생기는 데이터</td></tr>
<tr><td>NoSQL · NewSQL</td><td>4세대 이후 DBMS. 키-값·문서·열·그래프 / SQL 유지하며 확장</td></tr>
<tr><td>문서형</td><td>다중값을 문서 안 배열로 — 읽기 쉬움, 중복 관리는 응용의 몫</td></tr>
<tr><td>색인</td><td>찾아보기 — 조회 빠름, 쓰기·공간 비용 (RPG 3초 → 0.1초)</td></tr>
<tr><td>OLTP · OLAP</td><td>운영은 정규화·트랜잭션, 분석은 웨어하우스·반정규화</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 봉투 하나</b> 문서형도 문서끼리 참조(관계)를 둘 수 있고, MongoDB도 여러 문서에 걸친 트랜잭션 기능을 제공합니다. “문서형 = 관계 없음”은 지나친 단순화입니다.</div><div><b>대결의 한계</b> 읽은 행 수만 셌습니다. 실제 속도는 색인·캐시·네트워크에 따라 다르고, 쓰기·변경 비용은 이 대결에 들어 있지 않습니다(12주 대결처럼 조건이 바뀌면 결과도 바뀝니다).</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 3V 데이터는 관계형만으로는 부담 — NoSQL을 함께 쓴다 ② 문서형은 읽기 패턴에 맞춰 담고, 중복 관리 책임을 진다 ③ 색인은 같은 표를 빠르게, 분석은 웨어하우스로 분리.'),
       ('robo','proud','이번엔 내가 이겼어! 피드처럼 늘 같이 읽는 데이터는 같이 담는 게 답이었지!'),
       ('fly','coffee','인정. 대신 태그 이름 바꾸는 날엔 네가 문서를 전부 고쳐야 해.'),
       ('asst','report','다음 주는 기말 리뷰예요! 9주차 SQL부터 오늘까지 모의고사로 정리한대요.')],
next_note='<p class="recap"><b>다음 회차 — 15주차 「기말 REVIEW」:</b> SQL(DDL·DML), 설계 5단계·변환 규칙, 정규화, 트랜잭션·회복·병행 제어, 응용 기술 — 모의고사와 플래시 카드.</p>',
gloss={'빅데이터':('빅데이터','개념','양(Volume)·속도(Velocity)·다양성(Variety)이 커서 기존 방식으로 다루기 어려운 데이터.','big-data','lv1'),
 'NoSQL':('NoSQL','용어','관계형 표·SQL에 얽매이지 않는 데이터베이스들의 묶음. 키-값·문서·열·그래프형.','nosql','lv1'),
 'NewSQL':('NewSQL','용어','관계형의 SQL과 트랜잭션을 유지하면서 여러 서버로 확장하는 것을 목표로 한 DBMS.','newsql','lv1'),
 '문서형 데이터베이스':('문서형 데이터베이스','개념','JSON 같은 문서 단위로 저장하는 NoSQL. 예: MongoDB.','document-database','lv2'),
 '전체 스캔':('전체 스캔','용어','색인 없이 테이블의 모든 행을 처음부터 끝까지 확인하는 조회 방식.','full-scan','lv3'),
 'OLTP':('OLTP','용어','온라인 트랜잭션 처리 — 짧은 읽기·쓰기가 많은 운영 업무.','oltp','lv4'),
 'OLAP':('OLAP','용어','온라인 분석 처리 — 대량 데이터를 집계·분석하는 업무.','olap','lv4'),
 '데이터 웨어하우스':('데이터 웨어하우스','개념','여러 운영 데이터베이스의 데이터를 분석용으로 통합해 쌓아 둔 데이터베이스.','data-warehouse','lv4')},
facts=[('F01','교안: 4세대 이후 데이터베이스 관리 시스템은 NoSQL, NewSQL DBMS — 비정형 데이터·빅데이터(3V)에서 안정성과 일관성 유지가 과제','문헌 사실','ahn2025w0104','lv1','「데이터베이스 관리시스템」 4세대 이후'),
       ('F02','교안 해시태그 사례: 트위터·페이스북·인스타그램 검색과 해시태그 간의 관계','문헌 사실','ahn2025w0104','lv2','「해쉬태그 사례」'),
       ('F03','RPG 사례: 서버 오픈 당일 동시접속 5만 명에서 인벤토리 조회 지연 — 색인 추가와 조회 로직 개선으로 응답 3초 → 0.1초','사례 기록','ahn2025rpg','lv3','「실제 장애 사례」'),
       ('F04','RPG 사례의 교훈: 전투 중 실시간 데이터는 NoSQL 병행 검토, 비정형 데이터에 MongoDB 검토','사례 기록','ahn2025rpg','lv2','「프로젝트 회고」'),
       ('F05','노션 13주차: 비정형 데이터 읽을거리(MongoDB, Full-Text Search, FLO MongoDB 도입기)와 이미지 검색 사례','문헌 사실','ahn2025notion13','lv1','13주차 페이지')],
refs=[dict(id='ahn2025w0104',type='report',title='데이터베이스 설계 1~4주차 강의 교안 (데이터베이스 관리시스템 발전 과정)',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025rpg',type='report',title='RPG 용사의 전설 — 데이터베이스 설계자의 실무 프로젝트 가이드',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025notion13',type='webpage',title='13주차 : 데이터 베이스 응용기술',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed8182bd55ffb2a052dbed',role='primary'),
      dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='background',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준')],
models=['SNS 게시글 6개와 해시태그 (설명용 예시 데이터)','문서 보기 화면 (MongoDB를 흉내 낸 설명용)','색인 비교 횟수 (log₂N + 1 단순화)','대결의 읽은 행 수 (예시 데이터로 계산)'],
cover_alt='서류철이 꽂힌 책장 옆에 해시태그 스티커가 붙은 봉투 더미와 사진 상자가 놓이고, 캐릭터들이 무엇을 어디에 담을지 고르는 장면 (대체 그림)',
prereq=['13'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var POSTS=__POSTS__;
var DT=[['온라인 주문표 (주문번호·회원·상품·수량·금액)','관계형','칸이 정해져 있고 돈이 오갑니다. 트랜잭션(13주)과 정규화가 그대로 필요 — 관계형이 기본.'],
 ['SNS 글 + 해시태그 (태그 0~30개)','문서형','글마다 태그 수가 다르고, 글과 태그를 늘 함께 읽습니다 — 문서 안 배열이 자연스럽습니다(②칸).'],
 ['상품 사진 · 동영상 파일','파일 저장소 + 메타데이터','사진 자체는 객체 저장소에 두고, DB에는 파일 위치·촬영일·태그 같은 메타데이터를 저장합니다(노션: 이미지 검색 사례).'],
 ['게임 전투 로그 (초당 수천 줄)','키-값 · 열 지향','쓰기 속도가 핵심(Velocity). RPG 사례: “전투 중 실시간 데이터는 NoSQL 병행 검토”.'],
 ['팔로우 관계 (누가 누구를)','그래프형','“친구의 친구” 같은 관계 탐색이 주된 질의 — 관계형에서는 JOIN이 깊어집니다.']];
var dt=$('#dt14');DT.forEach(function(d){var b=document.createElement('button');b.type='button';b.className='bt';b.style.textAlign='left';b.textContent=d[0];b.onclick=function(){[].forEach.call(dt.children,function(x){x.setAttribute('aria-pressed',x===b);});$('#dt14o').innerHTML='<b>'+d[1]+'</b> — '+d[2];};dt.appendChild(b);});
var docs=POSTS.map(function(p){return {'글번호':p[0],'작성자':p[1],'제목':p[2],'태그':p[3]};});
$('#doc14').textContent='db.게시글 = [\n'+docs.map(function(d){return '  '+JSON.stringify(d);}).join(',\n')+'\n]';
var tags=[];POSTS.forEach(function(p){p[3].forEach(function(t){if(tags.indexOf(t)<0)tags.push(t);});});tags.sort();
$('#tg14').innerHTML=tags.map(function(t){return '<option'+(t==='제주'?' selected':'')+'>'+t+'</option>';}).join('');
$('#tg14b').onclick=function(){var t=$('#tg14').value,hit=docs.filter(function(d){return d['태그'].indexOf(t)>=0;}),co={};
 hit.forEach(function(d){d['태그'].forEach(function(x){if(x!==t)co[x]=(co[x]||0)+1;});});
 var top=Object.keys(co).sort(function(a,b){return co[b]-co[a]||(a<b?-1:1);});
 $('#tg14o').innerHTML='<code>db.게시글.find({ "태그": "'+t+'" })</code> → 문서 <b>'+hit.length+'개</b> ('+hit.map(function(d){return d['제목'];}).join(', ')+')<br>함께 쓰인 태그: '+(top.length?top.map(function(x){return '#'+x+' '+co[x]+'번';}).join(', '):'없음');};
$('#tg14b').click();
function ix(){var e=+$('#ix14n').value,rows=[];for(var k=3;k<=7;k++){var n=Math.pow(10,k);rows.push([n.toLocaleString(),n.toLocaleString(),Math.floor(Math.log2(n))+1]);}
 $('#ix14v').textContent='10^'+e+' = '+Math.pow(10,e).toLocaleString()+'행';
 $('#ix14t').innerHTML=LAB.tableHTML(['행 수 N','전체 스캔 (최악)','색인 반씩 좁히기 (최악)'],rows,{cls:function(r){return r[0]===Math.pow(10,e).toLocaleString()?'hl':'dim';}});}
$('#ix14n').oninput=ix;ix();
var OP=[['회원 apple의 비밀번호 변경','OLTP'],['지난해 분기별 매출 합계','OLAP'],['주문 o04 접수','OLTP'],['연령대별 인기 상품 상위 10개 (3년치)','OLAP'],['상품 p01 재고 1개 차감','OLTP']];
var op=$('#op14');OP.forEach(function(o){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=o[0];b.onclick=function(){[].forEach.call(op.children,function(x){x.setAttribute('aria-pressed',x===b);});$('#op14o').innerHTML='<b>'+o[1]+'</b> — '+(o[1]==='OLTP'?'몇 행을 바로 읽고 쓰는 운영 업무입니다.':'많은 행을 모아 집계하는 분석 업무입니다. 데이터 웨어하우스에서.');};op.appendChild(b);});
PAGE.duel=function(){var p=POSTS.length,pt=POSTS.reduce(function(a,x){return a+x[3].length;},0);
 $('#duel14t').innerHTML=LAB.tableHTML(['방식','읽는 것','합계'],[['정규화 (초파리)','게시글 '+p+'행 + 글태그 '+pt+'행 + 태그 '+pt+'행 (JOIN)',p+2*pt+'행'],['문서형 (주판봇)','게시글 문서 '+p+'개 (태그 포함)',p+'개']],{cap:'피드 한 번 그리기'});
 return {fly:p+2*pt,robo:p,flyTxt:(p+2*pt)+'행',roboTxt:p+'개',p:p,pt:pt};};
'''.replace('__POSTS__', str([[a, b, c, d] for a, b, c, d in POSTS]).replace("'", '"')),
labs=('lab14:{setup:%s,presets:[{t:"① 표 3개 보기",q:"SELECT * FROM 게시글;\\nSELECT * FROM 태그;\\nSELECT * FROM 글태그 LIMIT 6;"},{t:"② 글과 태그 합치기 (JOIN)",q:"SELECT g.글번호, g.제목, t.태그명\\nFROM 게시글 g\\nJOIN 글태그 gt ON g.글번호 = gt.글번호\\nJOIN 태그 t ON gt.태그번호 = t.태그번호\\nORDER BY g.글번호;"},{t:"③ #제주가 붙은 글",q:"SELECT g.제목 FROM 게시글 g\\nWHERE g.글번호 IN (SELECT gt.글번호 FROM 글태그 gt JOIN 태그 t ON gt.태그번호 = t.태그번호 WHERE t.태그명 = \'제주\');"},{t:"④ #제주와 함께 쓰인 태그",q:"SELECT t2.태그명, COUNT(*) AS 함께쓴횟수\\nFROM 글태그 a\\nJOIN 태그 t1 ON a.태그번호 = t1.태그번호\\nJOIN 글태그 b ON a.글번호 = b.글번호 AND a.태그번호 <> b.태그번호\\nJOIN 태그 t2 ON b.태그번호 = t2.태그번호\\nWHERE t1.태그명 = \'제주\'\\nGROUP BY t2.태그명\\nORDER BY 함께쓴횟수 DESC, t2.태그명;"},{t:"⑤ 태그 이름 바꾸기 (한 줄)",q:"UPDATE 태그 SET 태그명 = \'여행기\' WHERE 태그명 = \'여행\';\\nSELECT g.제목, t.태그명 FROM 게시글 g JOIN 글태그 gt ON g.글번호 = gt.글번호 JOIN 태그 t ON gt.태그번호 = t.태그번호 WHERE t.태그명 = \'여행기\';"}],ready:"게시글 6개 · 태그 · 글태그(N:M 연결) 표가 준비되어 있습니다."}') % ('"' + SNS.replace('"', '\\"') + '"'),
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'칸이 정해지지 않은 데이터(비정형)와 양·속도·다양성(3V)이 큰 빅데이터. 관계형만으로는 부담이 생기는 데이터.','lv2':'관계형은 표와 외래키·JOIN으로, 문서형은 JSON 같은 문서 안에 관련 값을 함께 담아 표현하는 데이터 모델.','lv3':'특정 칸의 값을 정렬해 행의 위치를 가리키는 구조. 전체 스캔 대신 빠르게 찾게 해 준다.','lv4':'짧은 거래를 처리하는 운영용 OLTP와, 대량 데이터를 집계·분석하는 OLAP(데이터 웨어하우스).'}[s['id']]

# ── 5칸: 사례 분석 + 문서 질의 실습 (2026-11 보강) ─────────────────
PAGE['steps'][3]['limit'] = '네 가지 도구(관계형·문서형·색인·분석용 DB)를 봤습니다. 실제 서비스는 이것들을 어떻게 섞어 쓸까요? RPG 사례의 운영 설계를 분석하고, 전투 로그를 문서 질의로 직접 다뤄 봅니다.'
PAGE['steps'][3]['limit_label'] = '실제 서비스에서 도구를 섞는 판단은 아직'
PAGE['steps'].append(dict(id='lv5', short='사례·실습', title='사례 분석 · 실습 — 용사의 전설 운영 설계와 전투 로그 문서 질의', concept='운영 설계 사례 분석', en='operational design case analysis', cid='lab:concept/operational-design-case',
 tag='사례: 서버 오픈 날 5만 명', analogy='창고와 매장 진열대',
 situation='RPG 「용사의 전설」 사례 문서의 “성능 최적화 및 인덱싱 전략” 장에는 데이터 종류마다 다른 결정이 적혀 있습니다: 캐릭터–장비는 정규화, 전투 로그는 비정규화, 레벨 정보·아이템 속성은 메모리 캐싱, 월드/서버별 데이터는 샤딩, 전투 중 실시간 데이터는 NoSQL 병행 검토. 왜 데이터마다 답이 다를까요? 먼저 직접 골라 보고 사례와 비교하세요.',
 pair=(('현장에서는','마트는 모든 물건을 같은 방식으로 두지 않습니다. 비싼 물건은 잠금 진열장(트랜잭션), 자주 팔리는 물건은 계산대 옆(캐시), 대량 재고는 창고를 지역별로 나눠(샤딩) 둡니다.'),
       ('데이터베이스에서는','설계자는 데이터마다 <b>얼마나 자주 읽나 · 얼마나 자주 바뀌나 · 틀리면 얼마나 큰일인가</b>를 묻고 저장 방식을 고릅니다. 사례의 인덱스 우선순위 표는 “자주 검색되는 칸”에 색인을 먼저 건 결과입니다.')),
 panel='''<div id="cs14"></div><div class="ctrl"><button type="button" class="bt primary" id="cs14c">사례와 비교</button></div><div class="insight" id="cs14o">데이터마다 저장 방식을 고른 뒤 「사례와 비교」를 누르세요.</div>''',
 panel_title='직접 해 보기 — 데이터마다 저장 방식 고르기',
 sim='운영 설계 결정 맞히기',
 body='''<h3>사례의 숫자 읽기 — 인덱스 적용 우선순위 (사례 문서의 표)</h3>
<div class="tbl"><table><thead><tr><th>테이블</th><th>색인 칸</th><th>사례가 적은 효과</th><th>읽는 법</th></tr></thead><tbody>
<tr><td>Characters</td><td>player_id, level</td><td>캐릭터 검색 300% 향상</td><td rowspan="3">“향상”의 기준(응답 시간인지 처리량인지)과 측정 조건이 적혀 있지 않습니다. 사례의 숫자는 <b>방향</b>을 보여 줄 뿐, 다른 서비스에 그대로 옮길 수 있는 값이 아닙니다.</td></tr>
<tr><td>Items</td><td>type, rarity</td><td>아이템 필터링 250% 향상</td></tr>
<tr><td>Quest_Progress</td><td>character_id, status</td><td>퀘스트 로딩 500% 향상</td></tr></tbody></table></div>
<p>장애 사례: “신규 서버 오픈 당일, 동시접속자 5만명 상황에서 인벤토리 조회 쿼리 지연으로 전체 서비스 마비 → 인덱스 추가 및 조회 로직 개선으로 응답시간 3초 → 0.1초”. 3초 → 0.1초는 <b>30배</b> 빨라진 것입니다(3 ÷ 0.1). 색인만의 효과인지, 조회 로직 개선의 효과인지는 사례에서 나뉘지 않습니다.</p>
<h3>실습 — 전투 로그를 문서로 다루기 (MongoDB 방식 질의)</h3>
<p>전투 로그는 전투마다 모양이 다릅니다(드롭 아이템이 없기도, 여럿이기도, 스킬 기록이 있기도). 아래는 MongoDB의 <code>find</code>·<code>aggregate</code> 문법 일부를 흉내 낸 실습 창입니다. 예제 버튼을 누르고, 직접 고쳐 실행해 보세요.</p>
<div class="ctrl" id="mg14p"></div><textarea class="dq" id="mg14q" spellcheck="false" style="width:100%;min-height:90px;font:13px/1.5 ui-monospace,Consolas,monospace;border:1px solid #d5dbe2;border-radius:8px;padding:8px"></textarea>
<div class="ctrl"><button type="button" class="bt primary" id="mg14r">실행 ▶</button><span class="cvcap">지원: find(조건, 투영) · countDocuments · aggregate($match · $unwind · $group($sum · $avg · $max) · $sort · $limit) · 조건 $gt $gte $lt $lte $ne $in</span></div>
<pre id="mg14o" style="font-size:13px;background:#f7f9fb;border:1px solid #d5dbe2;border-radius:8px;padding:10px;max-height:300px;overflow:auto"></pre>
<p class="cvcap">전투 로그 12건은 설명용 예시 데이터입니다. 실제 MongoDB는 노션 13주차 링크의 공식 사이트에서 무료 클라우드(Atlas)로 같은 질의를 해 볼 수 있습니다.</p>''',
 explain='<p><b>같은 질문, 두 가지 답:</b> “드롭 아이템별 횟수”를 관계형으로 하면 전투 표와 드롭 표(1:N)를 JOIN하고 GROUP BY 합니다. 문서형은 <code>$unwind</code>로 배열을 펼친 뒤 <code>$group</code>합니다 — 펼치기가 JOIN 역할을 합니다. 반대로 “레온의 골드를 깎고 미라에게 주기”처럼 여러 문서를 함께 바꾸는 일은 관계형 트랜잭션(13주)이 자연스럽습니다. 사례가 “전투 로그는 비정규화·NoSQL 검토, 캐릭터–장비는 정규화”로 나눈 이유가 여기 있습니다.</p>',
 aicheck='<p>AI가 “성능 300% 향상” 같은 숫자를 근거로 설계를 권하면 세 가지를 물어보세요: <b>무엇을 쟀나(응답 시간·처리량)?</b> <b>어떤 조건(데이터 양·동시 접속)에서?</b> <b>무엇과 비교했나?</b> — 이 세 가지가 없는 숫자는 사례의 방향일 뿐 근거가 아닙니다.</p>',
 limit='다음 주는 기말 리뷰입니다. 9~14주의 SQL·설계·정규화·트랜잭션·응용을 한 번에 다시 엮습니다.', limit_label='후반부 전체를 엮어 보는 정리는 아직',
 say=('asst','report','3초에서 0.1초면 30배예요! 그런데 색인 덕인지 로직 덕인지는 사례에 안 나뉘어 있네요.'),
 quiz=[dict(q='RPG 사례에서 전투 로그를 비정규화하고 NoSQL 병행을 검토한 가장 알맞은 이유는?',o=['돈이 오가므로 트랜잭션이 중요해서','쓰기가 매우 많고 모양이 전투마다 달라, 조인 없이 통째로 쓰고 읽는 편이 유리해서','정규화가 불가능해서','색인을 걸 수 없어서'],a=1,why='전투 로그는 쓰기가 많고 형태가 다양하며, 한 전투를 통째로 읽는 일이 많습니다. 돈·장비처럼 일관성이 핵심인 데이터는 정규화·트랜잭션 쪽에 둡니다.'),
       dict(q='MongoDB 질의 db.전투로그.aggregate([{ $unwind: "$드롭" }, { $group: { _id: "$드롭", n: { $sum: 1 } } }])가 하는 일과 가장 가까운 SQL은?',o=['SELECT 드롭 FROM 전투로그;','전투–드롭 표를 JOIN한 뒤 GROUP BY 드롭, COUNT(*)','DELETE FROM 드롭;','CREATE INDEX ON 드롭;'],a=1,why='$unwind는 배열을 행으로 펼치고(JOIN과 비슷한 효과), $group은 GROUP BY와 같습니다.')],
 **{'def': '실제 서비스 사례에서 데이터 종류별로 정규화·비정규화·색인·캐싱·샤딩·NoSQL을 고른 이유를 분석하고, 문서형 질의로 같은 질문을 풀어 보는 실습.'}))
PAGE['facts'].append(('F06', 'RPG 사례 인덱스 우선순위: Characters(player_id, level) 캐릭터 검색 300% 향상, Items(type, rarity) 250%, Quest_Progress(character_id, status) 500% (사례 기록, 측정 조건 미기재)', '사례 기록', 'ahn2025rpg', 'lv5', '「성능 최적화 및 인덱싱 전략」'))
PAGE['facts'].append(('F07', 'RPG 사례: 캐릭터-장비 관계는 정규화, 전투 로그는 비정규화, 레벨·아이템 속성은 메모리 캐싱, 월드/서버별 샤딩', '사례 기록', 'ahn2025rpg', 'lv5', '「성능 최적화 핵심 전략」'))
PAGE['gloss']['샤딩'] = ('샤딩', '용어', '데이터를 기준(월드·지역 등)에 따라 여러 서버로 나눠 저장하는 방법.', 'sharding', 'lv5')
PAGE['gloss']['캐싱'] = ('캐싱', '용어', '자주 읽는 데이터를 메모리에 복사해 두고 데이터베이스까지 가지 않고 돌려주는 방법.', 'caching', 'lv5')
PAGE['js'] += r'''
var CS=[['캐릭터–장비 (누가 어떤 장비를 차고 있나)','정규화 + 트랜잭션','장비 교환은 돈·아이템이 오가는 일 — 사례: “캐릭터-장비 관계는 정규화”'],
 ['전투 로그 (초당 수천 건, 전투마다 모양이 다름)','비정규화 · NoSQL 검토','쓰기 폭주 + 다양한 모양 — 사례: “전투 로그는 비정규화”, “전투 중 실시간 데이터는 NoSQL 병행 검토”'],
 ['레벨별 필요 경험치 표 (거의 안 바뀜, 매우 자주 읽음)','메모리 캐싱','읽기만 많고 거의 안 바뀜 — 사례: “레벨 정보, 아이템 속성 등 자주 조회되는 데이터는 메모리 캐싱”'],
 ['월드(서버)별 캐릭터 데이터 (동시 접속 5만 명)','샤딩','한 서버로 감당하기 어려운 양을 월드별로 나눔 — 사례: “월드/서버별 데이터 분리로 대규모 동시접속 처리”'],
 ['인벤토리 조회 (오픈 날 지연으로 서비스 마비)','색인','자주 검색되는 칸에 색인 — 사례: 색인 추가와 조회 로직 개선으로 3초 → 0.1초']];
var OPT=['정규화 + 트랜잭션','비정규화 · NoSQL 검토','메모리 캐싱','샤딩','색인'],cp={};
LAB.$('#cs14').innerHTML=CS.map(function(c,i){return '<div class="ctrl" style="margin:4px 0"><b style="min-width:240px;display:inline-block">'+c[0]+'</b><select data-i="'+i+'"><option value="">— 고르기 —</option>'+OPT.map(function(o){return '<option>'+o+'</option>';}).join('')+'</select></div>';}).join('');
LAB.$$('#cs14 select').forEach(function(s){s.onchange=function(){cp[s.dataset.i]=s.value;};});
LAB.$('#cs14c').onclick=function(){var ok=0;LAB.$('#cs14o').innerHTML=CS.map(function(c,i){var g=cp[i]===c[1];if(g)ok++;return (g?'<span style="color:#13733a">✓</span> ':'<span style="color:#c9302c">✗</span> ')+'<b>'+c[1]+'</b> — '+c[2];}).join('<br>')+'<br><b>'+ok+'/5</b> — 같은 서비스 안에서도 데이터마다 답이 다릅니다.';};
var LOGS=[{"전투번호":1,"캐릭터":"레온","몬스터":"슬라임","피해":120,"드롭":["슬라임 젤리"],"초":14},{"전투번호":2,"캐릭터":"미라","몬스터":"고블린","피해":340,"드롭":["녹슨 단검","동전 주머니"],"초":31,"스킬":["화염구"]},{"전투번호":3,"캐릭터":"레온","몬스터":"고블린","피해":290,"드롭":[],"초":27},{"전투번호":4,"캐릭터":"보리","몬스터":"슬라임","피해":80,"드롭":["슬라임 젤리"],"초":12},{"전투번호":5,"캐릭터":"미라","몬스터":"늑대","피해":510,"드롭":["늑대 가죽"],"초":44,"스킬":["화염구","얼음벽"]},{"전투번호":6,"캐릭터":"레온","몬스터":"늑대","피해":470,"드롭":["늑대 가죽","늑대 이빨"],"초":40},{"전투번호":7,"캐릭터":"레온","몬스터":"드래곤","피해":2600,"드롭":["전설의 검"],"초":180,"파티":["미라","보리"]},{"전투번호":8,"캐릭터":"보리","몬스터":"고블린","피해":260,"드롭":["동전 주머니"],"초":35},{"전투번호":9,"캐릭터":"미라","몬스터":"슬라임","피해":95,"드롭":["슬라임 젤리","슬라임 젤리"],"초":10},{"전투번호":10,"캐릭터":"레온","몬스터":"슬라임","피해":110,"드롭":[],"초":13},{"전투번호":11,"캐릭터":"보리","몬스터":"늑대","피해":430,"드롭":["늑대 이빨"],"초":52},{"전투번호":12,"캐릭터":"미라","몬스터":"드래곤","피해":2400,"드롭":["용의 비늘"],"초":200,"스킬":["얼음벽"],"파티":["레온"]}];
var MP=[['① 레온의 전투','db.전투로그.find({ "캐릭터": "레온" }, { "몬스터": 1, "피해": 1 })'],['② 피해 400 이상','db.전투로그.find({ "피해": { "$gte": 400 } })'],['③ 스킬을 쓴 전투 수','db.전투로그.countDocuments({ "스킬": { "$ne": null } })'],['④ 드롭 아이템별 횟수','db.전투로그.aggregate([\n  { "$unwind": "$드롭" },\n  { "$group": { "_id": "$드롭", "n": { "$sum": 1 } } },\n  { "$sort": { "n": -1 } }\n])'],['⑤ 캐릭터별 평균 피해','db.전투로그.aggregate([\n  { "$group": { "_id": "$캐릭터", "평균피해": { "$avg": "$피해" }, "전투": { "$sum": 1 } } },\n  { "$sort": { "평균피해": -1 } }\n])'],['⑥ 드래곤 전투의 파티원','db.전투로그.find({ "몬스터": { "$in": ["드래곤"] } }, { "캐릭터": 1, "파티": 1 })']];
var mp=LAB.$('#mg14p');MP.forEach(function(m){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=m[0];b.onclick=function(){LAB.$('#mg14q').value=m[1];mrun();};mp.appendChild(b);});
function J(s){return JSON.parse(s.replace(/([{,]\s*)([$\w가-힣]+)\s*:/g,'$1"$2":').replace(/'/g,'"'));}
function get(d,k){return k.charAt(0)==='$'?d[k.slice(1)]:k;}
function match(d,f){return Object.keys(f||{}).every(function(k){var c=f[k],v=d[k];
 if(c&&typeof c==='object'&&!Array.isArray(c))return Object.keys(c).every(function(op){var x=c[op];switch(op){case '$gt':return v>x;case '$gte':return v>=x;case '$lt':return v<x;case '$lte':return v<=x;case '$ne':return x===null?(v!==undefined&&v!==null):v!==x;case '$in':return x.some(function(y){return Array.isArray(v)?v.indexOf(y)>=0:v===y;});default:throw new Error('지원하지 않는 연산자 '+op);}});
 return Array.isArray(v)?v.indexOf(c)>=0:v===c;});}
function proj(d,p){if(!p||!Object.keys(p).length)return d;var o={};Object.keys(p).forEach(function(k){if(p[k]&&d[k]!==undefined)o[k]=d[k];});return o;}
function agg(st){var a=LOGS.slice();st.forEach(function(s){var op=Object.keys(s)[0],x=s[op];
 if(op==='$match')a=a.filter(function(d){return match(d,x);});
 else if(op==='$unwind'){var f=x.slice(1),b=[];a.forEach(function(d){(d[f]||[]).forEach(function(v){var c=JSON.parse(JSON.stringify(d));c[f]=v;b.push(c);});});a=b;}
 else if(op==='$group'){var g={},order=[];a.forEach(function(d){var key=JSON.stringify(get(d,x._id));if(!g[key]){g[key]={_id:get(d,x._id),_c:{}};order.push(key);}var r=g[key];
  Object.keys(x).forEach(function(k){if(k==='_id')return;var e=x[k],fn=Object.keys(e)[0],arg=e[fn],val=typeof arg==='string'?get(d,arg):arg;r._c[k]=r._c[k]||{s:0,n:0,m:-Infinity};r._c[k].s+=val;r._c[k].n++;r._c[k].m=Math.max(r._c[k].m,val);r._c[k].fn=fn;});});
  a=order.map(function(key){var r=g[key],o={_id:r._id};Object.keys(r._c).forEach(function(k){var c=r._c[k];o[k]=c.fn==='$sum'?c.s:c.fn==='$avg'?Math.round(c.s/c.n*10)/10:c.m;});return o;});}
 else if(op==='$sort'){var ks=Object.keys(x);a.sort(function(p,q){for(var i=0;i<ks.length;i++){var k=ks[i];if(p[k]!==q[k])return (p[k]<q[k]?-1:1)*x[k];}return 0;});}
 else if(op==='$limit')a=a.slice(0,x);else throw new Error('지원하지 않는 단계 '+op);});return a;}
function mrun(){var q=LAB.$('#mg14q').value.trim(),o=LAB.$('#mg14o');try{var m=q.match(/^db\.전투로그\.(find|countDocuments|aggregate)\(([\s\S]*)\)\s*;?$/);if(!m)throw new Error('db.전투로그.find(...) / countDocuments(...) / aggregate([...]) 형식으로 써 주세요.');
 var r;if(m[1]==='aggregate'){r=agg(J(m[2]));}else{var args=J('['+(m[2]||'')+']');var hit=LOGS.filter(function(d){return match(d,args[0]);});r=m[1]==='countDocuments'?hit.length:hit.map(function(d){return proj(d,args[1]);});}
 o.textContent=(typeof r==='number'?r:(r.length+'건\n'+r.map(function(d){return JSON.stringify(d);}).join('\n')));}catch(e){o.textContent='오류: '+e.message;}}
LAB.$('#mg14r').onclick=mrun;mp.children[3].click();
'''
