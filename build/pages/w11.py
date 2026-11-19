# 11주차 — 데이터베이스 설계 5단계 (교재 8장)
REQ = [('회원으로 가입하려면 회원아이디, 비밀번호, 이름, 나이, 직업을 입력해야 한다.','회원 개체와 속성'),
 ('가입한 회원에게는 등급과 적립금이 부여된다.','회원 속성 추가'),
 ('회원은 회원아이디로 식별한다.','회원의 키'),
 ('상품에 대한 상품번호, 상품명, 재고량, 단가 정보를 유지해야 한다.','상품 개체와 속성'),
 ('상품은 상품번호로 식별한다.','상품의 키'),
 ('회원은 여러 상품을 주문할 수 있고, 하나의 상품을 여러 회원이 주문할 수 있다.','주문 관계 N:M'),
 ('회원이 상품을 주문하면 주문에 대한 주문번호, 주문수량, 배송지, 주문일자 정보를 유지해야 한다.','주문 관계의 속성'),
 ('각 상품은 한 제조업체가 공급하고, 제조업체 하나는 여러 상품을 공급할 수 있다.','공급 관계 1:N'),
 ('제조업체가 상품을 공급하면 공급일자와 공급량 정보를 유지해야 한다.','공급 관계의 속성'),
 ('제조업체에 대한 제조업체명, 전화번호, 위치, 담당자 정보를 유지해야 한다.','제조업체 개체와 속성'),
 ('제조업체는 제조업체명으로 식별한다.','제조업체의 키'),
 ('회원은 게시글을 여러 개 작성할 수 있고, 게시글 하나는 한 명의 회원만 작성할 수 있다.','작성 관계 1:N'),
 ('게시글에 대한 글번호, 글제목, 글내용, 작성일자 정보를 유지해야 한다.','게시글 개체와 속성'),
 ('게시글은 글번호로 식별한다.','게시글의 키')]
HB = ("CREATE DATABASE hanbit; USE hanbit; "
 "CREATE TABLE 회원 (회원아이디 VARCHAR(20) PRIMARY KEY, 비밀번호 VARCHAR(20) NOT NULL, 이름 VARCHAR(10) NOT NULL, 나이 INT, 직업 VARCHAR(20), 등급 VARCHAR(10) NOT NULL DEFAULT 'silver', 적립금 INT NOT NULL DEFAULT 0); "
 "CREATE TABLE 제조업체 (제조업체명 VARCHAR(20) PRIMARY KEY, 전화번호 VARCHAR(20), 위치 VARCHAR(30), 담당자 VARCHAR(10)); "
 "CREATE TABLE 상품 (상품번호 CHAR(3) PRIMARY KEY, 상품명 VARCHAR(20), 재고량 INT CHECK (재고량 >= 0), 단가 INT, 제조업체명 VARCHAR(20), 공급일자 DATE, 공급량 INT, FOREIGN KEY (제조업체명) REFERENCES 제조업체(제조업체명)); "
 "CREATE TABLE 주문 (주문번호 CHAR(3) PRIMARY KEY, 회원아이디 VARCHAR(20) NOT NULL, 상품번호 CHAR(3) NOT NULL, 주문수량 INT, 배송지 VARCHAR(30), 주문일자 DATE, FOREIGN KEY (회원아이디) REFERENCES 회원(회원아이디), FOREIGN KEY (상품번호) REFERENCES 상품(상품번호)); "
 "CREATE TABLE 게시글 (글번호 INT PRIMARY KEY, 글제목 VARCHAR(50), 글내용 VARCHAR(200), 작성일자 DATE, 회원아이디 VARCHAR(20) NOT NULL, FOREIGN KEY (회원아이디) REFERENCES 회원(회원아이디));")
PAGE = dict(
num='11', slug='database_design_process', kind='lecture', short='11주', chip='11주차',
title='데이터베이스 설계 5단계', title_en='The database design process',
subtitle='요구 사항 문장 14개에서 MariaDB 테이블 5개까지 — 한빛 마트',
toc='요구 사항 분석 → 개념적 설계(E-R) → 논리적 설계(변환 규칙 5) → 물리적 설계 → 구현, 한빛 마트 사례와 RPG 실무 사례',
kicker='데이터베이스 설계 · 11주차 · 교재 8장',
question='요구 사항 문장 14개를 받았다. 테이블은 몇 개, 외래키는 어디에?',
desc='데이터베이스 설계 11주차: 설계 5단계(요구 사항 분석, 개념적 설계, 논리적 설계, 물리적 설계, 구현), 한빛 마트 요구 사항 명세와 E-R 다이어그램, E-R 다이어그램을 릴레이션 스키마로 변환하는 규칙 5가지, RPG 실무 사례.',
intro='<p>5주차에 ERD를 그렸고, 6주차에 키를, 9·10주차에 SQL을 배웠습니다. 오늘은 그 조각을 <b>한 줄로 꿰는 날</b>입니다. 교재 8장의 한빛 마트 요구 사항 14문장에서 출발해, 개체와 관계를 뽑고(개념적 설계), <b>변환 규칙 5가지</b>로 릴레이션을 만들고(논리적 설계), 자료형과 색인을 정해(물리적 설계), MariaDB에 실제로 만듭니다(구현). 마지막 칸은 같은 과정을 게임 회사 프로젝트(RPG 용사의 전설)에 적용한 실무 사례입니다.</p>',
kpis=[('5단계','요구 분석 · 개념 · 논리 · 물리 · 구현'),('14문장','한빛 마트 요구 사항 명세'),('4 · 3','개체 4개 · 관계 3개 (주문·공급·작성)'),('5규칙','E-R → 릴레이션 변환')],
hero_talk=[
 ('doc','front','오늘은 <b>처음부터 끝까지 한 번</b> 간다. 문장 14개가 테이블 5개가 되는 길이다.'),
 ('asst','smile','14문장이면 테이블도 14개쯤 나오는 거 아니에요?'),
 ('fly','clip','아니야. 문장 여러 개가 한 개체를 설명하기도 하고, 관계는 테이블이 되기도 안 되기도 해. 규칙을 보자.'),
 ('robo','smile','문장 읽는 건 지루해! 나는 바로 CREATE TABLE부터 칠래!')],
crew=[('doc','front','단계와 변환 규칙 정리, 판정'),('asst','smile','요구 사항 따라가기, 숫자 발표'),('fly','clip','규칙을 하나씩 대조'),('robo','smile','“바로 코딩”파 (오늘 대결)')],
recap='5주차: 명사→개체·속성, 동사→관계, N:M은 교차 개체. 6주차: 외래키는 다른 표의 기본키를 참조. 9주차: CREATE TABLE에 PK·FK·CHECK. — 오늘 이 셋이 한 흐름이 됩니다.',
notion=[('04주차 : 데이터모델링 — 실습 (노션)', NOTION+'1ab17a4520ed81e3bcf4f1adc30c6742', 'ERD 실습과 「ERD에서 릴레이션 변환」 실습 과제'),
        ('데이터베이스 설계사례 (업종별)', NOTION+'1ab17a4520ed81cc9c8ad60616c2e1de', '1주차에 본 업종별 주요 개체 — 오늘 과정을 다른 업종에 적용해 보기'),
        ('SQL 기본 문법 (교재 예제 코드 수정)', NOTION+'1ab17a4520ed815294ccd69faa520526', '구현 단계의 CREATE TABLE·FK 실습')],
why=[('순서가 품질이다','요구 분석 없이 만든 표는 나중에 ALTER·DROP을 반복하게 됩니다(오늘의 대결).'),
     ('규칙이 있다','ERD를 릴레이션으로 바꾸는 일은 감이 아니라 다섯 가지 규칙입니다. 규칙을 알면 누가 해도 같은 결과가 나옵니다.'),
     ('기말의 중심','설계 단계와 변환 규칙, 12주 정규화는 기말고사 범위의 뼈대입니다.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>단계</th><th>하는 일</th><th>결과물</th><th>DBMS를 고려?</th></tr></thead><tbody>
<tr><td>1 요구 사항 분석</td><td>데이터베이스의 용도 파악, 사용자·업무 조사</td><td>요구 사항 명세서</td><td>아니오</td></tr>
<tr><td>2 개념적 설계</td><td>DBMS에 독립적인 개념적 구조 설계</td><td>E-R 다이어그램 (개념적 스키마)</td><td>아니오</td></tr>
<tr><td>3 논리적 설계</td><td>DBMS에 적합한 논리적 구조 설계</td><td>릴레이션 스키마 (논리적 스키마)</td><td>DBMS 종류(관계형)만</td></tr>
<tr><td>4 물리적 설계</td><td>DBMS로 구현 가능한 물리적 구조 설계</td><td>물리적 스키마 (자료형·색인·저장)</td><td>예 (MariaDB 등)</td></tr>
<tr><td>5 구현</td><td>SQL로 DBMS에 실제 데이터베이스 생성</td><td>데이터베이스</td><td>예</td></tr></tbody></table></div>''',
steps=[
dict(id='lv1', short='요구 분석', title='1단계 요구 사항 분석 — 한빛 마트의 14문장', concept='요구 사항 명세', en='requirements specification', cid='lab:concept/requirements-specification',
 tag='현장: 한빛 마트', analogy='주문서 받아 적기',
 situation='온라인 쇼핑몰 “한빛 마트”를 만들려 합니다. 담당자와 인터뷰해 정리한 요구 사항 명세가 14문장입니다. 문장을 하나씩 열어 무엇이 들어 있는지 보세요.',
 pair=(('현장에서는','인테리어 업자는 공사 전에 “방 몇 개, 콘센트 몇 구, 수납장 어디”를 받아 적습니다. 빠진 요구는 공사 중에 벽을 다시 뜯게 만듭니다.'),
       ('설계에서는','요구 사항 분석의 결과물은 <b>요구 사항 명세서</b>입니다. 누가 쓰는지, 어떤 데이터를 유지해야 하는지, 데이터 사이에 어떤 규칙이 있는지를 <b>문장으로</b> 정리합니다. 이 문장들이 2단계의 재료입니다.')),
 panel='''<p style="margin-top:0">문장을 누르면 그 문장이 설계에서 무엇이 되는지 나옵니다.</p><ol id="req11" style="padding-left:22px"></ol><div class="insight" id="req11o">문장을 눌러 보세요.</div>''',
 panel_title='한빛 마트 요구 사항 명세 (교재 8장)',
 sim='한빛 마트 요구 사항 읽기',
 explain='<p>14문장을 묶어 보면 <b>개체 4개</b>(회원·상품·제조업체·게시글)와 <b>관계 3개</b>(주문·공급·작성)입니다. “식별한다”는 문장은 키, “유지해야 한다”는 문장은 속성, “여러 … 할 수 있다”는 문장은 관계의 대응 수를 알려 줍니다. 이 세 가지 말버릇을 찾으면 명세서가 빨리 읽힙니다.</p>',
 limit='문장을 읽었으니 이제 그림으로 옮길 차례입니다.', limit_label='요구 사항이 아직 문장 상태',
 say=('asst','spark','“식별한다”는 키, “유지해야 한다”는 속성, “여러 … 할 수 있다”는 대응 수! 말버릇만 찾아도 반은 끝났어요.'),
 quiz=[dict(q='요구 사항 분석 단계의 결과물은?',o=['E-R 다이어그램','요구 사항 명세서','릴레이션 스키마','SQL 스크립트'],a=1,why='요구 사항 분석의 결과물은 요구 사항 명세서입니다.'),
       dict(q='“상품은 상품번호로 식별한다”라는 요구 사항은 설계에서 무엇이 되나요?',o=['관계','상품 개체의 키 속성','외래키','제약 없음'],a=1,why='“식별한다”는 문장은 키 속성을 알려 줍니다.')]),
dict(id='lv2', short='개념적 설계', title='2단계 개념적 설계 — 개체·관계 추출과 E-R 다이어그램', concept='개념적 설계', en='conceptual design', cid='lab:concept/conceptual-design',
 tag='연구실: 한빛 마트 ERD', analogy='설계도 초안',
 situation='명세서의 명사와 동사에서 개체와 관계를 뽑습니다. 주문은 몇 대 몇일까요? 주문수량·배송지는 누구의 속성일까요?',
 pair=(('연구실에서는','STEP 1 개체·속성 추출 → STEP 2 관계 추출 → STEP 3 E-R 다이어그램. 관계에도 속성이 있을 수 있습니다(주문수량은 회원의 것도 상품의 것도 아니라 “주문”의 것).'),
       ('E-R 모델에서는','주문: 회원 N : M 상품, 속성 주문번호·주문수량·배송지·주문일자. 공급: 제조업체 1 : N 상품, 속성 공급일자·공급량. 작성: 회원 1 : N 게시글. 상품·게시글은 관계에 <b>필수 참여</b>(제조업체·작성자가 반드시 있음).')),
 panel='''<p style="margin-top:0">세 관계의 대응 수를 골라 보세요.</p><div id="rel11"></div><div class="ctrl"><button type="button" class="bt primary" id="rel11c">교재와 비교</button></div><div class="insight" id="rel11o">고른 뒤 「교재와 비교」를 누르세요. 아래 그림에 답이 있으니, 먼저 고르고 나서 보세요.</div>
<div style="overflow-x:auto;margin-top:8px"><svg viewBox="0 0 700 250" style="width:100%;min-width:600px;height:auto;background:#fff;border:1px solid #d5dbe2;border-radius:10px" role="img" aria-label="회원 N대M 상품 주문 관계, 제조업체 1대N 상품 공급 관계, 회원 1대N 게시글 작성 관계를 그린 한빛 마트 E-R 다이어그램"><g font-size="14" text-anchor="middle">
<rect x="40" y="40" width="110" height="40" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="95" y="65">회원</text>
<rect x="540" y="40" width="110" height="40" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="595" y="65">상품</text>
<rect x="540" y="180" width="110" height="40" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="595" y="205">제조업체</text>
<rect x="40" y="180" width="110" height="40" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="95" y="205">게시글</text>
<polygon points="345,35 390,60 345,85 300,60" fill="#f6ecfa" stroke="#9b3fb5"/><text x="345" y="65">주문</text>
<polygon points="595,105 635,130 595,155 555,130" fill="#f6ecfa" stroke="#9b3fb5"/><text x="595" y="135">공급</text>
<polygon points="95,105 135,130 95,155 55,130" fill="#f6ecfa" stroke="#9b3fb5"/><text x="95" y="135">작성</text>
<line x1="150" y1="60" x2="300" y2="60" stroke="#16212b"/><line x1="390" y1="60" x2="540" y2="60" stroke="#16212b"/><line x1="595" y1="80" x2="595" y2="105" stroke="#16212b" stroke-width="3"/><line x1="595" y1="155" x2="595" y2="180" stroke="#16212b"/><line x1="95" y1="80" x2="95" y2="105" stroke="#16212b"/><line x1="95" y1="155" x2="95" y2="180" stroke="#16212b" stroke-width="3"/>
<text x="165" y="52" fill="#c9302c">N</text><text x="528" y="52" fill="#c9302c">M</text><text x="610" y="98" fill="#c9302c">N</text><text x="610" y="175" fill="#c9302c">1</text><text x="110" y="98" fill="#c9302c">1</text><text x="110" y="175" fill="#c9302c">N</text>
<text x="345" y="110" font-size="12" fill="#5b6874">주문번호 · 주문수량 · 배송지 · 주문일자</text><text x="470" y="130" font-size="12" fill="#5b6874">공급일자 · 공급량</text></g></svg></div><p class="cvcap">굵은 선 = 필수 참여(상품은 반드시 공급되고, 게시글은 반드시 작성자가 있음). 개체의 속성 타원은 생략했습니다.</p>''',
 panel_title='한빛 마트 E-R 다이어그램',
 sim='한빛 마트 관계 대응 수 맞히기',
 explain='<p>관계에 속성이 붙는 경우를 놓치기 쉽습니다. “주문수량”을 회원 개체에 붙이면 “어느 상품을 몇 개”인지 알 수 없고, 상품 개체에 붙이면 “누가 몇 개”인지 알 수 없습니다. 두 개체가 <b>만났을 때 생기는 값</b>이므로 관계(주문)의 속성입니다.</p>',
 limit='그림은 완성됐지만 DBMS는 그림을 모릅니다. 관계형 DBMS가 이해하는 릴레이션으로 바꾸는 규칙이 필요합니다.', limit_label='E-R 다이어그램을 릴레이션으로 바꾸지 않음',
 quiz=[dict(q='한빛 마트에서 “주문수량”은 무엇의 속성인가?',o=['회원 개체','상품 개체','주문 관계','제조업체 개체'],a=2,why='회원과 상품이 만나는 주문에서 생기는 값이므로 관계의 속성입니다.'),
       dict(q='“각 상품은 한 제조업체가 공급하고, 제조업체는 여러 상품을 공급”의 대응 수(제조업체:상품)는?',o=['1:1','1:N','N:M','N:1만 있음'],a=1,why='제조업체 하나가 여러 상품 — 1:N 공급 관계입니다.')]),
dict(id='lv3', short='변환 규칙', title='3단계 논리적 설계 — E-R 다이어그램을 릴레이션으로 바꾸는 규칙 5', concept='E-R 다이어그램의 릴레이션 변환', en='er to relational mapping', cid='lab:concept/er-to-relational-mapping',
 tag='연구실: 규칙 하나씩 적용', analogy='설계도를 시공 도면으로',
 situation='한빛 마트 ERD의 개체 4개, 관계 3개를 릴레이션으로 바꿉니다. 관계는 모두 테이블이 될까요? 외래키는 어느 쪽에 둘까요?',
 pair=(('연구실에서는','건축 설계도의 “방”은 시공 도면에서 벽·문·배관으로 바뀝니다. 바꾸는 방법은 정해진 규칙을 따릅니다.'),
       ('논리적 설계에서는','<b>규칙 1</b> 모든 개체 → 릴레이션 (복합 속성은 단순 속성으로 풀어서). <b>규칙 2</b> N:M 관계 → 릴레이션 (양쪽 기본키를 외래키로, 둘을 묶어 기본키). <b>규칙 3</b> 1:N 관계 → N쪽에 1쪽 기본키를 외래키로 (관계 속성도 N쪽에). <b>규칙 4</b> 1:1 관계 → 한쪽에 외래키 (필수 참여 쪽에). <b>규칙 5</b> 다중값 속성 → 별도 릴레이션.')),
 panel='''<div class="chips" id="rule11"></div><div class="two"><div id="rule11a"></div><div id="rule11b"></div></div><div class="insight" id="rule11o"></div>''',
 panel_title='직접 해 보기 — 규칙별 변환',
 sim='E-R → 릴레이션 변환 규칙 적용',
 explain='<p><b>한빛 마트 결과 (손으로 먼저):</b> 규칙 1 → 회원·상품·제조업체·게시글 4개. 규칙 2 → 주문(N:M)은 새 릴레이션 1개. 규칙 3 → 공급(1:N)은 상품에 제조업체명·공급일자·공급량 추가, 작성(1:N)은 게시글에 회원아이디 추가 — 새 테이블 없음. 그래서 <b>테이블 5개</b>입니다. 14문장에서 테이블 14개가 나오지 않는 이유가 이것입니다.</p><p style="font-size:14px;color:#5b6874">교재의 규칙 3에는 약한 개체가 참여하는 1:N(3-2: 외래키를 기본키에 포함), 규칙 4에는 필수 참여(4-2)·모두 필수(4-3, 한 릴레이션으로 합침)의 세부 경우가 있습니다. 위 버튼의 “세부”에서 확인하세요.</p>',
 aicheck='<p>교안이 꼽은 대표 오답 세 가지는 AI가 만든 스키마에서도 자주 보입니다. ① N:M 관계를 외래키 칸 하나로 표현 ② 다중값 속성(연락처 여러 개)을 한 칸에 쉼표로 ③ 상위·하위 타입에서 같은 칸을 중복해 생성. AI에게 스키마를 받으면 이 세 가지부터 확인하세요.</p>',
 limit='릴레이션 스키마가 나왔습니다. 이제 MariaDB에서 칸마다 자료형을 정하고, 자주 찾는 칸에 색인을 걸어 실제로 만들 차례입니다.', limit_label='자료형·색인·실제 생성(물리 설계·구현)이 남음',
 say=('fly','arms','관계 3개 중 테이블이 된 건 주문 하나뿐이야. 1:N은 외래키 한 칸이면 충분하니까.'),
 quiz=[dict(q='N:M 관계를 릴레이션으로 변환하는 규칙은?',o=['N쪽에 외래키 추가','관계를 독립된 릴레이션으로 만들고 양쪽 기본키를 외래키로 포함','관계를 생략','한쪽 개체에 합침'],a=1,why='규칙 2: N:M 관계는 별도 릴레이션이 되고, 양쪽 기본키가 외래키(보통 함께 기본키)가 됩니다.'),
       dict(q='한빛 마트(개체 4개, N:M 관계 1개, 1:N 관계 2개)를 규칙대로 변환하면 릴레이션은 몇 개? (계산)',o=['4개','5개','7개','14개'],a=1,why='개체 4개 + N:M 관계 1개 = 5개. 1:N 관계 2개는 외래키로 처리되어 테이블이 생기지 않습니다.')]),
dict(id='lv4', short='물리·구현', title='4·5단계 물리적 설계와 구현 — 그리고 RPG 실무 사례', concept='물리적 설계와 구현', en='physical design and implementation', cid='lab:concept/physical-design-implementation',
 tag='연구실: MariaDB에 한빛 마트 만들기', analogy='자재 고르기와 시공',
 situation='릴레이션 5개를 MariaDB에 만듭니다. 회원아이디는 VARCHAR 몇 자? 단가는 INT? 주문을 날짜로 자주 찾는다면 무엇을 준비해 둘까요?',
 pair=(('연구실에서는','시공 도면이 나오면 자재(타일 크기, 배관 굵기)를 고르고 실제로 짓습니다. 자주 다니는 길에는 미리 넓은 통로(색인)를 냅니다.'),
       ('물리적 설계·구현에서는','<b>물리적 설계</b>: 칸마다 자료형·길이, 기본값, 색인(인덱스), 저장 공간 추정, 응답 시간·처리량 같은 성능 고려. <b>구현</b>: SQL(DDL)로 데이터베이스와 테이블을 만들고 초기 데이터를 넣습니다.')),
 panel='<div class="sqllab" id="lab11" data-lab="lab11"></div>',
 panel_title='SQL 실습실 — 한빛 마트 구현 (테이블 5개)',
 sim='한빛 마트 구현 실습',
 body='''<h3>실무 사례 — RPG 「용사의 전설」 데이터베이스 설계 (강의 사례)</h3>
<div class="tbl"><table><thead><tr><th>단계</th><th>용사의 전설 프로젝트에서</th></tr></thead><tbody>
<tr><td>요구 분석</td><td>캐릭터·아이템·전투·NPC·퀘스트 데이터를 파일로 관리하다 중복·종속·동시 작업 충돌·확장성 부족을 겪음 → DBMS 도입 결정</td></tr>
<tr><td>개념적 설계</td><td>캐릭터 1:1 능력치, 캐릭터 1:N 인벤토리 N:1 아이템, 캐릭터 N:M 스킬, 캐릭터 1:N 퀘스트 진행</td></tr>
<tr><td>논리적 설계</td><td>characters(character_id PK, name, job_id FK, level, exp), character_stats(character_id PK·FK, strength, intelligence, dexterity, vitality), inventories(캐릭터 FK, 아이템 FK) …</td></tr>
<tr><td>물리적 설계</td><td>캐릭터와 능력치 테이블 분리로 성능 고려, 레벨업 시 능력치 계산은 트랜잭션으로, 캐릭터ID+능력치 복합 색인</td></tr>
<tr><td>운영 과제</td><td>DB 장애 시 전체 서비스 중단 가능(중앙 관리 취약점), 라이브 서비스 후에는 스키마 변경이 어려워 초기 설계가 중요</td></tr></tbody></table></div>
<p class="cvcap">출처: 안상선, 「RPG 용사의 전설 — 데이터베이스 설계자의 실무 프로젝트 가이드」(2025 강의 자료). 강의용으로 재구성한 사례입니다.</p>''',
 explain='<p><b>구현 후 확인:</b> 실습실 ⑤ 「설계 검증 질의」는 요구 사항 문장을 그대로 SQL 질문으로 바꾼 것입니다(“회원이 여러 상품을 주문할 수 있다” → 회원별 주문 상품 수). 설계가 요구를 담았는지는 <b>요구 문장을 질의로 바꿔 실행해 보는 것</b>으로 검증합니다.</p><p>물리적 설계의 “색인”은 14주차 응용 기술에서 다시 다룹니다. 실습실 엔진은 색인을 흉내 내지 않으므로, 실제 MariaDB에서 <code>CREATE INDEX idx_주문일자 ON 주문(주문일자);</code>로 해 보세요.</p>',
 limit='5단계를 지나 테이블을 만들었습니다. 그런데 처음 만든 표가 이미 “나쁜 구조”라면 어떻게 알아보고 고칠까요? 이상 현상과 정규화 — 12주차.', limit_label='이미 만든 표의 구조를 평가·개선하는 방법이 없음',
 quiz=[dict(q='물리적 설계 단계에서 하는 일이 아닌 것은?',o=['속성의 자료형과 길이 결정','색인(인덱스) 설계','요구 사항 인터뷰','저장 공간과 성능 고려'],a=2,why='인터뷰는 1단계 요구 사항 분석에서 합니다.'),
       dict(q='RPG 사례에서 캐릭터와 능력치(character_stats)는 1:1 관계다. character_stats의 character_id는?',o=['기본키이자 외래키','외래키가 아님','다중값 속성','대체키만'],a=0,why='1:1 관계에서 의존하는 쪽(능력치)이 캐릭터의 기본키를 외래키로 갖고, 그것이 곧 자신의 기본키가 됩니다.')]),
],
duel=dict(q='설계 먼저 vs 코딩 먼저 — 고쳐야 할 구조 변경 횟수',
 intro='한빛 마트 요구 사항 14문장이 차례로 들어옵니다. 초파리는 <b>14문장을 다 읽고 5단계를 거친 뒤</b> 테이블을 만들고, 주판봇은 <b>첫 문장부터 바로 CREATE TABLE</b>을 치고 새 문장이 올 때마다 고칩니다. 완성될 때까지 필요한 구조 변경(ALTER·DROP·새 테이블로 옮기기) 횟수를 셉니다.',
 fly_pick='5단계를 거친 뒤 한 번에 생성', fly_line='문장을 다 읽고 그림부터 그려. 그래야 고칠 일이 없어.',
 robo_pick='문장마다 바로 CREATE · ALTER', robo_line='읽으면서 바로 치는 게 빠르지! 고치면 되잖아!',
 metric='완성까지의 구조 변경 횟수 (적을수록 이김)', higher=False, step=3,
 after='<div id="duel11t"></div>',
 run='return PAGE.duel();',
 announce='return "완성까지 초파리는 구조 변경 <b>"+r.fly+"번</b>, 주판봇은 <b>"+r.robo+"번</b>이었어요. 특히 6·7번째 문장(N:M 주문)에서 회원 표에 넣었던 주문 칸을 새 테이블로 옮겨야 했어요.";',
 verdict='return "요구 사항을 끝까지 읽고 설계한 쪽이 고칠 일이 없었다. 운영 중인 표를 고치는 비용은 훨씬 크다. 초파리 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>단계</th><th>한빛 마트에서 나온 것</th></tr></thead><tbody>
<tr><td>1 요구 분석</td><td>요구 사항 14문장</td></tr>
<tr><td>2 개념적</td><td>개체 4(회원·상품·제조업체·게시글) + 관계 3(주문 N:M, 공급 1:N, 작성 1:N)</td></tr>
<tr><td>3 논리적</td><td>릴레이션 5: 회원, 상품(+제조업체명 FK·공급일자·공급량), 제조업체, 게시글(+회원아이디 FK), 주문(회원아이디 FK, 상품번호 FK)</td></tr>
<tr><td>4 물리적</td><td>자료형·길이, NOT NULL·DEFAULT·CHECK, 색인(주문일자 등)</td></tr>
<tr><td>5 구현</td><td>CREATE DATABASE hanbit … 테이블 5개, 요구 문장 → 검증 질의</td></tr></tbody></table></div>
<div class="tbl"><table><thead><tr><th>규칙</th><th>한 줄</th></tr></thead><tbody><tr><td>1</td><td>개체 → 릴레이션 (복합 속성은 풀어서)</td></tr><tr><td>2</td><td>N:M → 새 릴레이션 (양쪽 PK가 FK)</td></tr><tr><td>3</td><td>1:N → N쪽에 FK (약한 개체면 FK가 PK에 포함)</td></tr><tr><td>4</td><td>1:1 → 한쪽에 FK (필수 참여 쪽, 모두 필수면 합침)</td></tr><tr><td>5</td><td>다중값 속성 → 별도 릴레이션</td></tr></tbody></table></div>
<div class="cards"><div><b>대결의 한계</b> 실제 개발은 요구가 한꺼번에 오지 않아 반복(애자일)도 흔합니다. 다만 반복하더라도 각 반복 안에서는 분석→설계→구현 순서를 지킵니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 요구 → 개념 → 논리 → 물리 → 구현 ② 변환 규칙 5: 개체·N:M·1:N·1:1·다중값 ③ 요구 문장을 질의로 바꿔 검증.'),
       ('fly','arms','설계부터 한 쪽은 구조 변경 0번. 문장 14개 읽는 시간이 가장 싼 투자였지.'),
       ('robo','sigh','주문상품 칸을 회원 표에서 꺼내 옮기느라 고생했어… 다음엔 문장부터 끝까지 읽을게.'),
       ('asst','proud','한빛 마트 테이블 5개를 직접 만들었어요! 다음 주엔 “나쁜 표”를 고치는 정규화래요.')],
next_note='<p class="recap"><b>다음 회차 — 12주차 「정규화」:</b> 이상 현상(삽입·갱신·삭제), 함수 종속, 1NF·2NF·3NF·BCNF — 노션 “worst case” 표를 직접 쪼개기.</p>',
gloss={'요구 사항 명세서':('요구 사항 명세서','용어','요구 사항 분석의 결과물. 데이터베이스가 유지해야 할 데이터와 규칙을 문장으로 정리한 문서.','requirements-document','lv1'),
 '개념적 설계':('개념적 설계','개념','DBMS와 무관하게 E-R 다이어그램으로 개념적 스키마를 만드는 단계.','conceptual-design-phase','lv2'),
 '논리적 설계':('논리적 설계','개념','개념적 스키마를 DBMS에 맞는 논리적 스키마(릴레이션 스키마)로 바꾸는 단계.','logical-design-phase','lv3'),
 '물리적 설계':('물리적 설계','개념','자료형·색인·저장 구조 등 실제 DBMS에서 구현할 물리적 구조를 정하는 단계.','physical-design-phase','lv4'),
 '변환 규칙':('E-R → 릴레이션 변환 규칙','개념','개체, N:M, 1:N, 1:1, 다중값 속성을 릴레이션으로 바꾸는 다섯 규칙.','mapping-rules','lv3'),
 '필수 참여':('필수 참여','개념','개체가 반드시 관계에 참여해야 함. 1:1 변환 때 외래키를 둘 쪽을 정하는 기준.','total-participation','lv2'),
 '색인':('색인(인덱스)','용어','특정 칸으로 빨리 찾도록 따로 만들어 두는 정렬된 구조. 물리적 설계에서 결정.','index','lv4')},
facts=[('F01','데이터베이스 설계 5단계: 요구 사항 분석, 개념적 설계, 논리적 설계, 물리적 설계, 구현','문헌 사실','kim3ed','lv1','8장 그림 8-1'),
       ('F02','한빛 마트 요구 사항 명세는 회원·상품·제조업체·게시글과 주문·공급·작성 관계를 기술','문헌 사실','kim3ed','lv1','8장 그림 8-4'),
       ('F03','주문은 N:M 관계로 주문번호·주문수량·배송지·주문일자 속성을, 공급은 1:N 관계로 공급일자·공급량 속성을 가짐','문헌 사실','kim3ed','lv2','8장 그림 8-22'),
       ('F04','E-R 다이어그램의 릴레이션 변환 규칙 5가지(개체, N:M, 1:N, 1:1, 다중값 속성)','문헌 사실','kim3ed','lv3','8장 4절'),
       ('F05','RPG 사례: 캐릭터–능력치 1:1, 캐릭터–아이템은 인벤토리를 통한 N:M, 캐릭터–스킬 N:M','문헌 사실','ahn2025rpg','lv4','RPG 캐릭터·아이템 시스템 설계')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='ahn2025w12design',type='report',title='데이터베이스설계 12주차 강의 교안: 데이터베이스 설계',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025rpg',type='report',title='RPG 용사의 전설 — 데이터베이스 설계자의 실무 프로젝트 가이드',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025w04erd',type='report',title='데이터베이스 설계 4주차 — ERD 작성, 관계 데이터 모델링, 정규화 과정 및 실무 적용',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='background')],
models=['한빛 마트 요구 사항 14문장 (교재 8장을 따라 정리)','한빛 마트 테이블의 자료형·길이·예시 데이터 (물리 설계 예시)','RPG 사례 (강의용으로 재구성한 사례)','대결의 구조 변경 횟수 (요구 순서에 따라 센 설명용 시나리오)'],
cover_alt='책상 위에 요구 사항 메모 14장이 놓이고, 그 옆으로 설계도·도면·완성된 테이블 모형이 차례로 늘어선 장면 (대체 그림)',
prereq=['10'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var REQ=__REQ__;
$('#req11').innerHTML=REQ.map(function(r,i){return '<li><button type="button" class="bt" data-i="'+i+'" style="text-align:left;min-height:30px">'+r[0]+'</button></li>';}).join('');
$$('#req11 button').forEach(function(b){b.onclick=function(){var r=REQ[+b.dataset.i];$('#req11o').innerHTML='<b>'+(+b.dataset.i+1)+'번</b> → '+r[1];};});
var RL=[['주문 (회원 – 상품)','nm'],['공급 (제조업체 – 상품)','1n'],['작성 (회원 – 게시글)','1n']],an={};
$('#rel11').innerHTML=RL.map(function(r,i){return '<div class="ctrl"><b style="min-width:170px;display:inline-block">'+r[0]+'</b>'+['11','1n','nm'].map(function(c){return '<button type="button" class="bt" data-r="'+i+'" data-c="'+c+'">'+{'11':'1:1','1n':'1:N','nm':'N:M'}[c]+'</button>';}).join('')+'</div>';}).join('');
$$('#rel11 button').forEach(function(b){b.onclick=function(){an[b.dataset.r]=b.dataset.c;$$('#rel11 button[data-r="'+b.dataset.r+'"]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});};});
$('#rel11c').onclick=function(){var ok=RL.filter(function(r,i){return an[i]===r[1];}).length;$('#rel11o').innerHTML='맞힘 <b>'+ok+'/3</b> — 교재: 주문 N:M(요구 6), 공급 1:N(요구 8), 작성 1:N(요구 12).';};
var RU=[['규칙 1','개체 → 릴레이션','[회원] 회원아이디(키), 비밀번호, 이름, 나이, 직업, 등급, 적립금',['회원(<u>회원아이디</u>, 비밀번호, 이름, 나이, 직업, 등급, 적립금)'],'개체 하나가 릴레이션 하나. 키 속성이 기본키. 세부(1-1): 복합 속성 “주소(우편번호·기본주소·상세주소)”는 하위 속성 세 칸으로 풀어 넣습니다.'],
 ['규칙 2','N:M 관계 → 새 릴레이션','[회원] N —◇주문◇— M [상품], 주문 속성: 주문번호, 주문수량, 배송지, 주문일자',['주문(<u>주문번호</u>, 회원아이디(FK), 상품번호(FK), 주문수량, 배송지, 주문일자)'],'양쪽 기본키를 외래키로 가져옵니다. 교재처럼 주문번호를 기본키로 쓰거나, (회원아이디, 상품번호)를 묶어 기본키로 쓸 수 있습니다(같은 회원이 같은 상품을 두 번 주문할 수 있다면 주문번호 쪽).'],
 ['규칙 3','1:N 관계 → N쪽에 외래키','[제조업체] 1 —◇공급◇— N [상품], 공급 속성: 공급일자, 공급량',['상품(<u>상품번호</u>, 상품명, 재고량, 단가, 제조업체명(FK), 공급일자, 공급량)','제조업체(<u>제조업체명</u>, 전화번호, 위치, 담당자)'],'새 테이블 없이 N쪽(상품)에 1쪽 기본키(제조업체명)와 관계 속성을 넣습니다. 세부(3-2): 약한 개체가 참여하면 외래키를 기본키에 포함합니다 — 예: 부양가족(<u>사원번호(FK), 이름</u>, …).'],
 ['규칙 4','1:1 관계 → 한쪽에 외래키','[남자] 1 —◇혼인◇— 1 [여자] (교재 예)',['남자(<u>남자번호</u>, 이름, 나이, 여자번호(FK), 결혼날짜)','여자(<u>여자번호</u>, 이름, 나이)'],'어느 쪽이든 상대 기본키를 외래키로 넣으면 됩니다. 세부(4-2): 한쪽만 필수 참여면 필수 쪽에 외래키(NULL이 생기지 않게). 세부(4-3): 양쪽 모두 필수면 두 개체를 하나의 릴레이션으로 합칩니다.'],
 ['규칙 5','다중값 속성 → 별도 릴레이션','[회원] 연락처{집, 휴대폰} (이중 타원)',['회원(<u>회원아이디</u>, 이름, …)','회원연락처(<u>회원아이디(FK), 연락처</u>)'],'한 칸에 여러 값을 넣지 않고(원자성), 원래 개체의 기본키와 값을 짝지어 따로 저장합니다. 12주차 제1정규형과 같은 생각입니다.']];
var rc=$('#rule11');RU.forEach(function(r){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=r[0];b.onclick=function(){[].forEach.call(rc.children,function(x){x.setAttribute('aria-pressed',x===b);});
 $('#rule11a').innerHTML='<p class="ptitle" style="color:#9b3fb5">E-R 다이어그램에서</p><p>'+r[2]+'</p>';$('#rule11b').innerHTML='<p class="ptitle" style="color:#13733a">릴레이션 스키마로 ('+r[1]+')</p>'+r[3].map(function(s){return '<p><code>'+s+'</code></p>';}).join('');$('#rule11o').innerHTML=r[4];};rc.appendChild(b);});
rc.children[0].click();
var STEPS=[[1,'CREATE 회원(아이디·비밀번호·이름·나이·직업)',0],[2,'ALTER 회원 ADD 등급, 적립금',1],[3,'ALTER 회원 ADD PRIMARY KEY',1],[4,'CREATE 상품',0],[5,'ALTER 상품 ADD PRIMARY KEY',1],[6,'ALTER 회원 ADD 주문상품 칸 → 여러 상품을 못 담음',1],[7,'CREATE 주문 + 회원의 주문상품 칸 데이터 옮기기 + DROP COLUMN',2],[8,'ALTER 상품 ADD 제조업체 칸',1],[9,'ALTER 상품 ADD 공급일자, 공급량',1],[10,'CREATE 제조업체 + 상품의 제조업체 칸을 FK로 바꾸기',1],[11,'ALTER 제조업체 ADD PRIMARY KEY',1],[12,'CREATE 게시글',0],[13,'ALTER 게시글 ADD 작성일자 등',1],[14,'ALTER 게시글 ADD PRIMARY KEY',1]];
PAGE.duel=function(){var robo=STEPS.reduce(function(a,s){return a+s[2];},0),fly=0;
 document.getElementById('duel11t').innerHTML=LAB.tableHTML(['요구 문장','주판봇이 한 일','변경 횟수'],STEPS.map(function(s){return [s[0]+'번',s[1],s[2]?s[2]:'0 (새로 만듦)'];}),{cap:'주판봇 — 문장마다 바로 코딩 (새 테이블을 만드는 것 자체는 변경에서 제외)'})+'<p class="cvcap">초파리는 14문장을 다 읽고 5단계를 거쳐 테이블 5개를 한 번에 만들었으므로 구조 변경 0번.</p>';
 return {fly:fly,robo:robo,flyTxt:fly+'번',roboTxt:robo+'번'};};
'''.replace('__REQ__', str([[a, b] for a, b in REQ]).replace("'", '"')),
labs=('lab11:{presets:[{t:"① 5단계 구현: 테이블 5개",q:%s},{t:"② 테이블 확인",q:"SHOW TABLES;\\nDESCRIBE 주문;"},{t:"③ 초기 데이터",q:"INSERT INTO 회원 (회원아이디, 비밀번호, 이름, 나이, 직업) VALUES (\'apple\',\'1234\',\'정소화\',20,\'학생\'),(\'banana\',\'0000\',\'김선우\',25,\'간호사\'),(\'carrot\',\'1111\',\'고명석\',28,\'교사\');\\nINSERT INTO 제조업체 VALUES (\'대한식품\',\'02-123-4567\',\'서울\',\'홍길동\'),(\'한빛제과\',\'031-111-2222\',\'경기\',\'박민수\');\\nINSERT INTO 상품 VALUES (\'p01\',\'그냥만두\',5000,4500,\'대한식품\',\'2022-01-02\',100),(\'p03\',\'쿵떡파이\',3600,2600,\'한빛제과\',\'2022-01-05\',80);\\nINSERT INTO 주문 VALUES (\'o01\',\'apple\',\'p03\',10,\'서울시 마포구\',\'2022-01-01\'),(\'o02\',\'banana\',\'p01\',5,\'인천시 계양구\',\'2022-01-10\'),(\'o03\',\'apple\',\'p01\',2,\'서울시 마포구\',\'2022-01-11\');\\nINSERT INTO 게시글 VALUES (1,\'배송 문의\',\'언제 오나요?\',\'2022-01-12\',\'apple\');\\nSELECT COUNT(*) AS 주문수 FROM 주문;"},{t:"④ 요구 위반 시도",q:"-- 요구 12: 게시글은 한 명의 회원이 작성 → 작성자 없는 글 금지\\nINSERT INTO 게시글 VALUES (2,\'익명 글\',\'...\',\'2022-01-13\',NULL);"},{t:"⑤ 설계 검증 질의",q:"-- 요구 6: 회원은 여러 상품을 주문할 수 있다\\nSELECT 회원아이디, COUNT(DISTINCT 상품번호) AS 주문한상품수\\nFROM 주문 GROUP BY 회원아이디;\\n-- 요구 8: 상품마다 제조업체가 하나\\nSELECT 상품명, 제조업체명 FROM 상품;"}],ready:"빈 실습실입니다. ①로 한빛 마트의 테이블 5개를 만들고 차례로 진행하세요."}') % ('"' + HB.replace('"', '\\"').replace('; ', ';\\n') + '"'),
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'데이터베이스의 용도와 사용자 요구를 분석해 유지할 데이터와 규칙을 문장으로 정리한 문서.','lv2':'요구 사항 명세에서 개체·속성·관계를 추출해 DBMS와 무관한 E-R 다이어그램(개념적 스키마)을 만드는 단계.','lv3':'개체, N:M·1:N·1:1 관계, 다중값 속성을 릴레이션 스키마로 바꾸는 다섯 가지 규칙.','lv4':'자료형·제약·색인 등 물리적 구조를 정하고(물리적 설계) SQL로 실제 데이터베이스를 만드는 것(구현).'}[s['id']]
