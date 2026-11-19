# 5주차 — 데이터 모델링과 E-R 모델 (교재 4장)
PAGE = dict(
num='05', slug='er_modeling', kind='lecture', short='5주', chip='05주차',
title='데이터 모델링과 E-R 모델', title_en='Data modeling and the E-R model',
subtitle='문장에서 개체·속성·관계를 건져 ERD로 그리기',
toc='현실 세계→컴퓨터 세계의 추상화, 요구사항 문장 분석, 개체·속성(단순·복합·다중값·유도·키), 관계와 1:1·1:N·N:M',
kicker='데이터베이스 설계 · 5주차 · 교재 4장',
question='“회원은 최대 5권을 14일 동안 빌릴 수 있다” — 이 한 문장에서 표 몇 개가 나올까?',
desc='데이터베이스 설계 5주차: 데이터 모델링의 개념과 3단계(개념·논리·물리), 요구사항 분석으로 개체·속성·관계 찾기, 속성의 종류와 E-R 다이어그램, 관계의 대응 수(1:1, 1:N, N:M). 도서관 관리 시스템 실습.',
intro='<p>데이터베이스를 만들 때 가장 먼저 쓰는 것은 SQL이 아니라 <b>문장</b>입니다. “회원은 도서를 빌린다”, “도서는 하나의 분류에 속한다” — 이런 업무 문장에서 <b>명사</b>는 개체나 속성이 되고, <b>동사</b>는 관계가 되고, “최대 5권” 같은 숫자는 제약 조건이 됩니다. 이번 회차는 문장을 그림(ERD)으로 옮기는 법을 도서관 관리 시스템으로 연습합니다.</p>',
kpis=[('3단계','개념 → 논리 → 물리 모델링'),('5종','속성: 단순·복합·다중값·유도·키'),('3가지','관계: 1:1 · 1:N · N:M'),('5개','도서관 핵심 개체: 회원·도서·대여·분류·직원')],
hero_talk=[
 ('doc','front','설계도 없이 집을 짓지 않듯, ERD 없이 표를 만들지 않는다. 오늘은 <b>연필로 그리는 날</b>이다.'),
 ('asst','smile','명사는 개체, 동사는 관계… 그러면 문장만 잘 읽으면 ERD가 저절로 나오나요?'),
 ('fly','clip','“대체로” 그래. 명사가 개체일지 속성일지는 그 명사가 <b>스스로 설명할 거리가 있는지</b>로 갈라져.'),
 ('robo','smile','표는 크면 클수록 좋지! 한 표에 다 넣으면 ERD도 네모 하나면 끝이야!')],
crew=[('doc','front','모델링 단계와 표기법 정리'),('asst','smile','문장 분석 진행, 숫자 발표'),('fly','clip','개체/속성 경계를 따짐'),('robo','smile','“한 표에 다”파 (오늘 대결)')],
recap='4주차: 조직 전체 관점의 구조가 <b>개념 스키마</b>였습니다. 오늘 그리는 ERD가 바로 그 개념 스키마의 첫 그림입니다.',
notion=[('04주차 : 데이터모델링 (노션)', NOTION+'1ab17a4520ed81e3bcf4f1adc30c6742', '모델링 강의 영상과 실습 페이지'),
        ('속성의 원자성 예시 (노션)', NOTION+'28217a4520ed804a8e34d6ced8765057', '한 칸에 값 하나 — 5·12주차를 잇는 예시'),
        ('데이터 베이스 설계 : worst case (노션)', NOTION+'1ab17a4520ed810783e8ea080d594176', '열 19개짜리 쇼핑몰 통합 테이블 — 대결의 소재')],
why=[('말과 표 사이의 다리','업무 담당자는 문장으로 말하고 DBMS는 표로 압니다. ERD는 둘이 함께 보는 그림입니다.'),
     ('오류를 일찍 잡는다','표를 다 만든 뒤에 “한 학생이 여러 과목을 듣는다”를 깨달으면 고칠 곳이 많습니다. 그림 단계에서는 선 하나입니다.'),
     ('다음 단계의 재료','6주차 관계 모델, 11주차 ERD→릴레이션 변환, 12주차 정규화가 모두 오늘의 ERD에서 출발합니다.')],
bigpicture='<div class="flow"><span class="chip">현실 세계 (회원, 책, 빌리다)</span><span class="arr">→ 개념적 모델링</span><span class="chip">ERD</span><span class="arr">→ 논리적 모델링</span><span class="chip">릴레이션 스키마</span><span class="arr">→ 물리적 모델링</span><span class="chip">MariaDB의 CREATE TABLE</span></div><p>모델링은 <b>복잡한 현실을 단순화·추상화</b>하는 일입니다. 주요 속성만 뽑고 불필요한 세부는 뺍니다. 그리고 한 번에 끝나지 않는 <b>반복 과정</b>입니다 — 단계마다 검증하고 되돌아갑니다.</p>',
steps=[
dict(id='lv1', short='모델링', title='데이터 모델링 — 현실을 컴퓨터 세계로 옮기는 세 단계', concept='데이터 모델링', en='data modeling', cid='lab:concept/data-modeling',
 tag='현장: 학교를 표로', analogy='지도 만들기',
 situation='학교에는 학생, 교수, 수업이 있습니다. 학생의 키, 좋아하는 음식, 성격도 “사실”입니다. 학사 데이터베이스에는 이 중 무엇을 넣어야 할까요?',
 pair=(('현장에서는','지도는 실제 땅을 그대로 옮기지 않습니다. 길과 건물만 남기고 나무 한 그루 한 그루는 뺍니다. 목적(길 찾기)에 필요한 것만 <b>추상화</b>합니다.'),
       ('모델링에서는','현실의 학생·교수·수업을 <b>개체</b>로, 그 특성 중 업무에 필요한 것(학번, 이름, 학과)만 <b>속성</b>으로, 연관(수강, 담당)을 <b>관계</b>로 옮깁니다. 데이터 모델은 <b>구조 · 연산 · 제약 조건</b>으로 이루어집니다.')),
 flow=dict(id='fl5', title='추상화의 세 단계', h=230, alt='현실 세계 카드가 개념적, 논리적, 물리적 모델링을 거쳐 SQL 문장으로 바뀌는 애니메이션',
   cap='같은 “학생”이 단계마다 다른 모습이 됩니다. 개념 단계는 DBMS와 상관없고, 물리 단계에서 처음으로 MariaDB의 자료형이 나옵니다.',
   js='{stations:["현실 세계","개념적 (ERD)","논리적 (릴레이션)","물리적 (DBMS)"],items:[["학생 김하나","[학생] 개체","학생(학번,이름,학과)","학번 CHAR(8) PK"],["수업을 듣는다","◇수강◇ N:M","수강(학번,과목코드)","FK 2개 + 복합 PK"],["교수 이민수","[교수] 개체","교수(교번,이름,연구실)","교번 INT PK"],["키 172cm","(필요 없음 → 제외)","—","—"]],bad:function(it,i){return /제외|—/.test(it[i]);},stamp:"설명용 모형"}'),
 explain='<div class="tbl"><table><thead><tr><th>단계</th><th>하는 일 (교안)</th><th>결과물</th></tr></thead><tbody><tr><td>요구 분석</td><td>사용자 인터뷰, 업무 문서 분석, 주요 개체·프로세스 식별</td><td>요구사항 명세서</td></tr><tr><td>개념적 모델링</td><td>핵심 개체 정의, 속성 분류, 관계 설정</td><td>ERD</td></tr><tr><td>논리적 모델링</td><td>ERD → 릴레이션 스키마, 키 설정, 정규화</td><td>릴레이션 스키마 (DBMS와 무관)</td></tr><tr><td>물리적 모델링</td><td>자료형, 색인, 저장 공간, 성능</td><td>SQL 스크립트</td></tr></tbody></table></div><p>“키 172cm”가 빠진 것은 틀려서가 아니라 <b>학사 업무에 필요 없어서</b>입니다. 같은 학생이라도 보건실 데이터베이스라면 키가 들어갈 수 있습니다. 무엇을 넣을지는 늘 목적이 정합니다.</p>',
 limit='단계는 알았지만, 실제 업무 문장에서 무엇이 개체이고 무엇이 속성인지 어떻게 골라낼까요?', limit_label='문장에서 개체·속성·관계를 골라내는 방법이 없음',
 say=('fly','point','모델링의 첫 질문은 “무엇을 넣지?”가 아니라 “무엇을 <b>빼도</b> 되지?”야.'),
 quiz=[dict(q='ERD를 그려 핵심 개체와 관계를 정의하는 모델링 단계는?',o=['요구 분석','개념적 모델링','논리적 모델링','물리적 모델링'],a=1,why='개념적 모델링의 결과물이 ERD입니다. 릴레이션 스키마는 논리적, CREATE TABLE은 물리적 모델링 결과입니다.'),
       dict(q='데이터 모델을 이루는 세 요소로 알맞은 것은?',o=['구조·연산·제약 조건','표·그림·문서','입력·처리·출력','개체·뷰·색인'],a=0,why='데이터 모델은 데이터 구조, 연산, 제약 조건으로 구성됩니다.')]),
dict(id='lv2', short='문장 분석', title='요구사항 문장에서 개체·속성·관계·제약 건지기', concept='요구사항 분석', en='requirements analysis', cid='lab:concept/requirements-analysis',
 tag='현장: 도서관 관리 시스템', analogy='문장에 형광펜 칠하기',
 situation='도서관 담당자가 요구사항을 문장으로 보냈습니다. “회원은 회원번호, 이름, 주소, 연락처를 가지며 최대 5권까지 대여할 수 있다. 대여 시 대여일, 반납예정일, 실제반납일, 연체료를 기록한다.” 여기서 표는 몇 개, 칸은 무엇일까요?',
 pair=(('현장에서는','문장에 형광펜 네 색을 칠합니다. <b>명사</b>(회원, 도서)는 개체 후보, <b>동사</b>(대여하다)는 관계 후보, <b>수식어·특성</b>(이름, 대여일)은 속성 후보, <b>숫자 규칙</b>(최대 5권, 14일)은 제약 조건입니다.'),
       ('모델에서는','개체 후보 중 <b>스스로 설명할 속성이 여럿 있는 것</b>은 개체로, 다른 개체를 설명하는 데 그치는 것은 속성으로 둡니다. “주소”는 회원을 설명하므로 속성, “도서”는 제목·저자를 가지므로 개체입니다.')),
 panel='''<p style="margin-top:0">낱말을 눌러 종류를 바꾸세요 (누를 때마다 개체 → 속성 → 관계 → 제약 → 해제). 다 칠했으면 「교안 해설과 비교」.</p>
<div id="req5" style="line-height:2.4;font-size:17px"></div><div class="ctrl"><button type="button" class="bt primary" id="req5c">교안 해설과 비교</button><button type="button" class="bt" id="req5r">지우기</button><span class="pill" style="background:#fcebea">개체</span><span class="pill" style="background:#e6eefb">속성</span><span class="pill" style="background:#f6ecfa">관계</span><span class="pill" style="background:#fdf3e1">제약</span></div><div class="insight" id="req5o"></div>''',
 panel_title='직접 해 보기 — 형광펜 네 색',
 sim='요구사항 문장 형광펜 분석',
 explain='<p>교안의 예: “회원은 최대 3권까지 도서를 대출할 수 있으며 대출 기간은 14일” → 개체: 회원, 도서 / 관계: 대출(회원–도서) / 제약 조건: 최대 3권 / 업무 규칙: 14일. 실세계의 사물·개념은 <b>개체</b>, 그 특성은 <b>속성</b>, 개체 사이의 연관은 <b>관계</b>, 업무 규칙은 <b>제약 조건</b>이 됩니다.</p><p>헷갈리는 경우: “대여”는 동사(빌리다)로 보면 관계, 대여일·반납예정일·연체료라는 <b>자기 속성을 가진 기록</b>으로 보면 개체입니다. 교안의 도서관 ERD는 대여를 개체(Loan)로 두었습니다. 둘 다 틀리지 않고, 기록할 내용이 많을수록 개체 쪽이 편합니다.</p>',
 aicheck='<p>생성 AI에게 같은 요구사항을 주고 “ERD 개체를 뽑아 줘”라고 하면, 흔히 <b>“연체료”를 개체로</b> 뽑거나 <b>“사서”와 “직원”을 서로 다른 개체로</b> 뽑습니다. 확인 질문 두 개: ① 그 개체는 자기만의 속성이 2개 이상 있는가? ② 같은 대상을 다른 이름으로 두 번 뽑지 않았는가?</p>',
 limit='개체를 찾았으니 이제 속성을 그려야 합니다. 그런데 “전화번호가 집·휴대폰 두 개”인 회원은 속성을 어떻게 그릴까요?', limit_label='속성의 여러 모양(복합·다중값·유도)을 표현하지 못함',
 say=('asst','spark','“대여”를 개체로도, 관계로도 볼 수 있다는 게 신기해요. 기록할 게 많으면 개체!'),
 quiz=[dict(q='요구사항 “회원은 최대 5권까지 대여할 수 있다”에서 “최대 5권”은 무엇으로 표현되나요?',o=['개체','속성','관계','제약 조건(업무 규칙)'],a=3,why='수량·기간 같은 업무 규칙은 제약 조건으로 표현합니다.'),
       dict(q='명사 “주소”를 개체가 아니라 속성으로 두는 가장 큰 이유는?',o=['글자 수가 짧아서','다른 개체(회원)를 설명하는 값이고 스스로 설명할 속성을 따로 갖지 않아서','관계가 없어서','숫자가 아니라서'],a=1,why='스스로 여러 속성을 가지며 독립적으로 관리할 대상이면 개체, 다른 개체의 특성이면 속성입니다.')]),
dict(id='lv3', short='속성', title='개체와 속성의 종류 — ERD 기호 읽기', concept='E-R 다이어그램의 속성', en='attributes in the E-R model', cid='lab:concept/er-attribute-types',
 tag='연구실: 회원 개체 그리기', analogy='명함의 칸',
 situation='도서관 회원 김철수는 전화번호가 둘(휴대폰, 집)이고, 주소는 시·구·동·상세로 나뉘며, 나이는 생년월일로 계산됩니다. 이 회원 개체를 ERD로 어떻게 그릴까요?',
 pair=(('연구실에서는','명함에는 칸마다 성격이 다릅니다. 이름 칸에는 하나, 전화 칸에는 여러 개, 주소 칸은 다시 쪼개지고, “경력 연수”는 입사일에서 계산됩니다.'),
       ('E-R 모델에서는','<b>단순 속성</b>(더 쪼갤 수 없음), <b>복합 속성</b>(하위 속성으로 쪼개짐, 주소), <b>다중값 속성</b>(값이 여러 개, 전화번호 — 이중 타원), <b>유도 속성</b>(다른 속성에서 계산, 나이 — 점선 타원), <b>키 속성</b>(개체를 식별, 회원번호 — 밑줄).')),
 panel='''<div class="ctrl" id="attr5b"></div><div style="overflow-x:auto"><svg id="erd5" viewBox="0 0 640 300" style="width:100%;min-width:520px;height:auto;background:#fff;border:1px solid #d5dbe2;border-radius:10px"></svg></div><div class="insight" id="attr5o"></div>''',
 panel_title='직접 해 보기 — 속성 종류별 ERD 기호',
 sim='회원 개체 ERD 기호 보기',
 explain='<div class="tbl"><table><thead><tr><th>종류</th><th>ERD 기호</th><th>도서관 예</th></tr></thead><tbody><tr><td>개체</td><td>사각형 (약한 개체는 이중 사각형)</td><td>회원, 도서 / 약한 개체: 도서 복사본</td></tr><tr><td>속성</td><td>타원</td><td>이름, 가입일</td></tr><tr><td>키 속성</td><td>밑줄 친 이름</td><td>회원번호, ISBN</td></tr><tr><td>다중값 속성</td><td>이중 타원</td><td>전화번호(집·휴대폰·회사)</td></tr><tr><td>유도 속성</td><td>점선 타원</td><td>나이, 대여 중인 도서 수, 연체료(계산값)</td></tr><tr><td>복합 속성</td><td>타원에서 가지가 뻗은 타원들</td><td>주소(시·구·동·상세)</td></tr><tr><td>관계</td><td>마름모</td><td>대여, 소속</td></tr></tbody></table></div><p><b>값 없음(NULL)과 0은 다릅니다.</b> 연체료 0원은 “연체료가 없다는 값”이고, NULL은 “아직 모름·해당 없음”입니다. 교안이 따로 강조한 부분입니다.</p>',
 limit='한 개체는 그렸습니다. 이제 개체끼리 선을 이어야 합니다. 그런데 “한 회원이 여러 권”과 “한 권이 여러 회원”은 선을 어떻게 다르게 그릴까요?', limit_label='개체 사이의 대응 수를 표현하지 못함',
 say=('robo','wow','타원이 두 겹이면 값이 여러 개, 점선이면 계산값! 그림만 봐도 칸의 성격이 보이네!'),
 quiz=[dict(q='생년월일로부터 계산할 수 있는 “나이”는 어떤 속성인가요?',o=['키 속성','다중값 속성','유도 속성','복합 속성'],a=2,why='다른 속성에서 계산되는 속성은 유도 속성이며 점선 타원으로 그립니다.'),
       dict(q='ERD에서 이중 타원으로 표시하는 속성은?',o=['다중값 속성','유도 속성','키 속성','복합 속성'],a=0,why='값을 여러 개 가질 수 있는 다중값 속성은 이중 타원으로 표시합니다.')]),
dict(id='lv4', short='관계', title='관계와 대응 수 — 1:1, 1:N, N:M', concept='관계와 대응 수', en='relationship cardinality', cid='lab:concept/relationship-cardinality',
 tag='현장: 혼인 · 부서와 사원 · 고객과 책', analogy='선 잇기',
 situation='교안의 세 예: 남편과 아내(혼인), 부서와 사원, 고객과 책. 한쪽의 하나가 다른 쪽의 몇 개와 이어질 수 있을까요?',
 pair=(('현장에서는','혼인은 한 사람이 한 사람과(1:1), 부서는 여러 사원을 두지만 사원은 한 부서에만(1:N), 고객은 여러 책을 사고 책도 여러 고객에게 팔립니다(N:M).'),
       ('E-R 모델에서는','관계는 마름모로, 선 위에 <b>1, N, M</b>을 적습니다. 참여 여부도 표시합니다 — 모든 개체가 반드시 관계에 참여하면 <b>필수 참여</b>(이중선), 일부만 참여하면 <b>선택 참여</b>.')),
 panel='''<div class="ctrl"><button type="button" class="bt" data-c="11">1:1 혼인</button><button type="button" class="bt" data-c="1n">1:N 부서–사원</button><button type="button" class="bt" data-c="nm">N:M 고객–책</button></div>
<canvas class="cv" id="card5" style="height:260px" role="img" aria-label="왼쪽 개체 집합과 오른쪽 개체 집합을 잇는 선으로 대응 수를 보여 주는 그림"></canvas>
<div class="ctrl"><button type="button" class="bt" id="card5add">선 하나 더 이어 보기</button><span id="card5msg" style="font-size:14px;color:#5b6874"></span></div>
<div class="insight" id="card5o"></div>''',
 panel_title='직접 해 보기 — 선을 이어 대응 수 확인',
 sim='관계 대응 수 실험',
 body='<h3>도서관 ERD 완성본 (교안)</h3><div style="overflow-x:auto"><svg viewBox="0 0 680 230" style="width:100%;min-width:560px;height:auto;background:#fff;border:1px solid #d5dbe2;border-radius:10px" role="img" aria-label="회원 1대N 대여 N대1 도서, 카테고리 1대N 도서 관계를 그린 ERD"><g font-size="14" text-anchor="middle"><rect x="20" y="40" width="120" height="44" rx="4" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="80" y="67">회원</text><rect x="280" y="40" width="120" height="44" rx="4" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="340" y="67">대여</text><rect x="540" y="40" width="120" height="44" rx="4" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="600" y="67">도서</text><rect x="540" y="170" width="120" height="44" rx="4" fill="#fff" stroke="#16212b" stroke-width="1.5"/><text x="600" y="197">카테고리</text><line x1="140" y1="62" x2="280" y2="62" stroke="#16212b"/><line x1="400" y1="62" x2="540" y2="62" stroke="#16212b"/><line x1="600" y1="84" x2="600" y2="170" stroke="#16212b"/><text x="155" y="56" fill="#c9302c">1</text><text x="268" y="56" fill="#c9302c">N</text><text x="412" y="56" fill="#c9302c">N</text><text x="528" y="56" fill="#c9302c">1</text><text x="612" y="102" fill="#c9302c">N</text><text x="612" y="162" fill="#c9302c">1</text><text x="80" y="110" font-size="12" fill="#5b6874">회원번호(PK), 회원명, 전화번호, 이메일, 주소, 가입일자</text><text x="340" y="110" font-size="12" fill="#5b6874">대여번호(PK), 회원번호(FK), 도서번호(FK)</text><text x="340" y="126" font-size="12" fill="#5b6874">대여일자, 반납예정일, 반납일자, 연체료</text><text x="600" y="24" font-size="12" fill="#5b6874">도서번호(PK), ISBN, 도서명, 저자, 출판사, 카테고리ID(FK)</text><text x="420" y="197" font-size="12" fill="#5b6874">카테고리ID(PK), 카테고리명, 설명</text></g></svg></div><p class="cvcap">회원–도서는 원래 N:M(한 회원이 여러 책, 한 책이 여러 회원)입니다. 교안 완성본은 그 사이에 <b>대여</b> 개체를 두어 1:N 두 개로 풀었습니다. 이렇게 N:M을 풀어 주는 개체를 교차 개체라 합니다.</p>',
 explain='<p><b>손으로 한 번:</b> 회원 3명(김·이·박), 도서 2권(A·B). 김이 A·B를, 이가 A를 빌렸습니다. 회원 쪽에서 보면 김은 2권 → 한 회원이 여러 책(“N”), 도서 쪽에서 보면 A는 2명 → 한 책이 여러 회원(“M”). 그래서 N:M입니다. 박은 아무것도 빌리지 않았으므로 회원의 참여는 <b>선택 참여</b>입니다.</p>',
 limit='ERD는 완성했습니다. 그런데 ERD는 그림일 뿐 DBMS가 이해하지 못합니다. 그림을 “표와 키”로 옮기는 관계 데이터 모델이 6주차입니다.', limit_label='ERD를 DBMS가 이해하는 표로 옮기지 못함',
 quiz=[dict(q='“부서와 사원(사원은 한 부서에만 소속)” 관계의 대응 수는?',o=['1:1','1:N','N:M','0:0'],a=1,why='한 부서는 여러 사원, 한 사원은 한 부서 — 일대다(1:N)입니다.'),
       dict(q='회원–도서의 N:M 대여 관계를 교안 완성본은 어떻게 표현했나요?',o=['회원 표에 도서번호 칸 하나를 추가','중간에 대여 개체를 두고 1:N 관계 두 개로 풀었다','도서 표에 회원번호 칸 하나를 추가','관계를 생략했다'],a=1,why='N:M은 교차 개체(대여)를 두어 회원–대여(1:N), 도서–대여(1:N)로 풉니다. 11주차 변환 규칙 2와 같습니다.')]),
],
duel=dict(q='학생과 과목의 수강 관계 — 어떻게 담을까?',
 intro='학생 3명이 과목을 신청했습니다(총 6건). 주판봇은 “학생 표에 수강과목 칸 하나를 두면 끝”이라고 하고, 초파리는 “수강이라는 연결 개체를 따로 둔다”고 합니다. 6건의 신청 기록을 몇 건이나 빠짐없이 담을 수 있을까요?',
 fly_pick='수강 연결 개체(교차 개체) 따로 두기', fly_line='학생도 여러 과목, 과목도 여러 학생이면 N:M이야. 사이에 표 하나가 필요해.',
 robo_pick='학생 표에 과목코드 칸 하나 추가', robo_line='표를 늘리기 싫어! 학생 줄에 과목 칸 하나면 깔끔하잖아!',
 metric='신청 기록 6건 중 정확히 담긴 건수', step=3,
 after='<div id="duel5t"></div>',
 run='return PAGE.duel();',
 announce='return "신청 6건 중 초파리 방식은 <b>"+r.fly+"건</b>, 주판봇 방식은 <b>"+r.robo+"건</b>을 담았어요. 학생 줄에 과목 칸이 하나뿐이라 두 번째 과목부터는 덮어쓰였어요.";',
 verdict='return "N:M 관계를 외래키 칸 하나로 표현하는 것은 교안의 대표 오답 패턴이다. 연결 개체를 둔 초파리 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>핵심</th><th>그림으로</th></tr></thead><tbody>
<tr><td>1 모델링</td><td>요구 분석 → 개념(ERD) → 논리(릴레이션) → 물리(SQL), 반복</td><td>현실 → 그림 → 표 → 코드</td></tr>
<tr><td>2 문장 분석</td><td>명사=개체·속성, 동사=관계, 규칙=제약</td><td>형광펜 네 색</td></tr>
<tr><td>3 속성</td><td>단순·복합·다중값·유도·키</td><td>타원·가지·이중 타원·점선 타원·밑줄</td></tr>
<tr><td>4 관계</td><td>1:1 · 1:N · N:M, 필수/선택 참여</td><td>마름모 + 1·N·M</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 형광펜</b> 명사가 늘 개체는 아닙니다(“주소”). 형광펜은 후보를 찾는 도구이고, 판단은 “스스로 설명할 속성이 있는가”로 합니다.</div><div><b>표기법 주의</b> ERD 표기는 교재(첸 표기)와 실무 도구(까마귀발 표기)가 다릅니다. 이 페이지는 교재 표기를 따랐습니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 모델링은 목적에 맞게 빼는 일 ② 문장의 명사·동사·숫자가 개체·관계·제약이 된다 ③ N:M은 사이에 개체를 둔다.'),
       ('fly','arms','칸 하나에 과목을 다 담으려다 세 건을 잃었지. 표 하나 더 만드는 게 훨씬 싸.'),
       ('robo','sigh','표가 늘어나는 게 손해인 줄 알았는데… 기록을 잃는 게 더 큰 손해구나.'),
       ('asst','proud','다음 주엔 이 ERD를 진짜 표로 바꿔요. 저는 학사 관리 ERD 실습 과제부터 그려 볼게요!')],
next_note='<p class="recap"><b>다음 회차 — 6주차 「관계 데이터 모델」:</b> 릴레이션·속성·튜플·도메인, 다섯 가지 키, 개체·참조 무결성.</p>',
gloss={'추상화':('추상화','개념','복잡한 현실에서 목적에 필요한 특성만 골라 단순하게 표현하는 일.','abstraction','lv1'),
 '데이터 모델':('데이터 모델','개념','데이터의 구조·연산·제약 조건을 표현하는 틀.','data-model','lv1'),
 '개체':('개체(엔터티)','개념','데이터로 관리할 현실의 대상. 스스로 여러 속성을 가지며 ERD에서 사각형.','entity','lv2'),
 '속성':('속성','개념','개체가 가진 특성. ERD에서 타원.','attribute','lv2'),
 '관계':('관계','개념','개체와 개체 사이의 연관. ERD에서 마름모.','relationship','lv2'),
 '약한 개체':('약한 개체','개념','다른 개체에 의존해야 존재할 수 있는 개체(도서 복사본은 도서에 의존). 이중 사각형.','weak-entity','lv3'),
 '다중값 속성':('다중값 속성','개념','값을 여러 개 가질 수 있는 속성. 이중 타원.','multivalued-attribute','lv3'),
 '유도 속성':('유도 속성','개념','다른 속성에서 계산되는 속성. 점선 타원.','derived-attribute','lv3'),
 '복합 속성':('복합 속성','개념','하위 속성으로 나눌 수 있는 속성(주소 = 시·구·동·상세).','composite-attribute','lv3'),
 '필수 참여':('필수 참여','개념','개체 집합의 모든 개체가 반드시 관계에 참여해야 하는 것. 이중선.','total-participation','lv4'),
 '교차 개체':('교차 개체','개념','N:M 관계를 풀기 위해 사이에 두는 개체(대여, 수강).','intersection-entity','lv4')},
facts=[('F01','데이터 모델링 3단계: 개념적(ERD) → 논리적(관계 스키마, 정규화, DBMS 독립) → 물리적(특정 DBMS 구현)','문헌 사실','ahn2025w04erd','lv1','4주차 심화 교안 「데이터 모델링이란?」'),
       ('F02','요구사항 문장의 명사는 개체 후보, 동사는 관계 후보, 수식어는 속성 후보, 수량·기간은 제약사항','문헌 사실','ahn2025w04erd','lv2','「실세계 요구를 데이터로 추상화」'),
       ('F03','도서관 ERD 완성본: 회원–대여 1:N, 도서–대여 1:N, 카테고리–도서 1:N','문헌 사실','ahn2025w04erd','lv4','「ERD 작성 실습 5단계 완성본 해설」'),
       ('F04','N:M 관계를 외래키로 직접 표현하려는 것은 대표적 오답 패턴, N:M은 별도 릴레이션으로 변환','문헌 사실','ahn2025w04erd','lv4','「변환 실습 해설」 오답 패턴'),
       ('F05','다중값 속성은 이중 타원, 유도 속성은 점선 타원으로 표기','문헌 사실','kim3ed','lv3','4장')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='ahn2025w04erd',type='report',title='데이터베이스 설계 4주차 — ERD 작성, 관계 데이터 모델링, 정규화 과정 및 실무 적용',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025worst',type='webpage',title='데이터 베이스 설계 : worst case',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed810783e8ea080d594176',role='background')],
models=['추상화 단계 애니메이션 (설명용 모형)','요구사항 문장 형광펜 정답 (교안 해설에 따른 한 가지 해석)','관계 대응 수 그림의 개체·선 (예시)','대결의 수강 신청 6건 (예시 데이터)'],
cover_alt='큰 화이트보드에 사각형·타원·마름모가 선으로 이어진 ERD가 그려져 있고, 네 캐릭터가 마커를 들고 모여 있는 표지 (대체 그림)',
prereq=['04'],
js=r'''
var $=LAB.$,$$=LAB.$$;
/* 칸2 형광펜 */
var W=[['회원','e'],['은 ',0],['회원번호','a'],[', ',0],['이름','a'],[', ',0],['주소','a'],[', ',0],['연락처','a'],['를 가지며 ',0],['최대 5권','c'],['까지 ',0],['도서','e'],['를 ',0],['대여','r'],['할 수 있다. ',0],['도서','e'],['는 ',0],['ISBN','a'],[', ',0],['제목','a'],[', ',0],['저자','a'],[', ',0],['장르','a'],[' 정보를 가진다. ',0],['대여','r'],[' 시 ',0],['대여일','a'],[', ',0],['반납예정일','a'],[', ',0],['연체료','a'],['를 기록한다. 대출 기간은 ',0],['14일','c'],['이다.',0]];
var CL=['e','a','r','c',''],COL={e:'#fcebea',a:'#e6eefb',r:'#f6ecfa',c:'#fdf3e1','':'transparent'},NM={e:'개체',a:'속성',r:'관계',c:'제약'},st={};
function dr(){$('#req5').innerHTML=W.map(function(w,i){if(!w[1])return '<span>'+w[0]+'</span>';var k=st[i]||'';return '<button type="button" class="bt" data-i="'+i+'" style="min-height:30px;padding:1px 7px;background:'+COL[k]+'">'+w[0]+'</button>';}).join('');
 $$('#req5 button').forEach(function(b){b.onclick=function(){var i=+b.dataset.i,k=st[i]||'';st[i]=CL[(CL.indexOf(k)+1)%CL.length];dr();};});}
$('#req5c').onclick=function(){var ok=0,n=0,bad=[];W.forEach(function(w,i){if(!w[1])return;n++;if((st[i]||'')===w[1])ok++;else bad.push(w[0]+'→'+NM[w[1]]);});
 $('#req5o').innerHTML='맞힌 낱말 <b>'+ok+'/'+n+'</b>'+(bad.length?'<br>교안 해설과 다른 것: '+bad.join(' · '):' — 교안 해설과 모두 같습니다.')+'<br><span style="font-size:13px">“대여”는 여기서 동사(관계)로 칠했지만, 기록할 속성이 많아 ERD 완성본에서는 개체로 둡니다. 둘 다 근거가 있으면 정답입니다.</span>';};
$('#req5r').onclick=function(){st={};dr();$('#req5o').textContent='';};dr();
/* 칸3 ERD 속성 */
var AT=[['all','전체'],['key','키'],['multi','다중값'],['derived','유도'],['comp','복합']];
var bx=$('#attr5b');AT.forEach(function(a){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=a[1];b.onclick=function(){[].forEach.call(bx.children,function(x){x.setAttribute('aria-pressed',x===b);});svg(a[0]);};bx.appendChild(b);});
function svg(f){var o='<g font-size="13" text-anchor="middle" font-family="inherit">';
 function el(x,y,t,k,ex){var on=f==='all'||f===k,c=on?'#1e55c8':'#c9d1da',sw=on?1.6:1;var s='<line x1="320" y1="150" x2="'+x+'" y2="'+y+'" stroke="'+c+'"/>';
  s+='<ellipse cx="'+x+'" cy="'+y+'" rx="58" ry="20" fill="#fff" stroke="'+c+'" stroke-width="'+sw+'"'+(k==='derived'?' stroke-dasharray="5 4"':'')+'/>';
  if(k==='multi')s+='<ellipse cx="'+x+'" cy="'+y+'" rx="52" ry="15" fill="none" stroke="'+c+'" stroke-width="'+sw+'"/>';
  s+='<text x="'+x+'" y="'+(y+4)+'" fill="'+(on?'#16212b':'#a4adb6')+'"'+(k==='key'?' text-decoration="underline"':'')+'>'+t+'</text>';return s+(ex||'');}
 o+=el(110,50,'회원번호','key')+el(320,40,'이름','simple')+el(530,50,'전화번호','multi')+el(560,170,'나이','derived')+el(110,250,'주소','comp')+el(90,150,'가입일','simple');
 var on=f==='all'||f==='comp',c=on?'#1e55c8':'#c9d1da';[['시',230,285],['구',320,285],['동',410,285]].forEach(function(s){o+='<line x1="160" y1="256" x2="'+s[1]+'" y2="'+s[2]+'" stroke="'+c+'"/><ellipse cx="'+s[1]+'" cy="'+s[2]+'" rx="30" ry="12" fill="#fff" stroke="'+c+'"/><text x="'+s[1]+'" y="'+(s[2]+4)+'" fill="'+(on?'#16212b':'#a4adb6')+'">'+s[0]+'</text>';});
 o+='<rect x="270" y="128" width="100" height="44" rx="3" fill="#fff" stroke="#16212b" stroke-width="2"/><text x="320" y="155" font-weight="700">회원</text></g>';
 $('#erd5').innerHTML=o;
 $('#attr5o').innerHTML={all:'회원 개체와 다섯 종류의 속성. 버튼을 눌러 종류별로 보세요.',key:'<b>키 속성</b> — 회원을 하나로 식별. 이름에 밑줄.',multi:'<b>다중값 속성</b> — 전화번호가 집·휴대폰처럼 여러 개. 이중 타원. (11주차: 별도 릴레이션으로 분리)',derived:'<b>유도 속성</b> — 나이는 생년월일로 계산. 점선 타원. 저장하지 않고 계산하는 경우가 많음.',comp:'<b>복합 속성</b> — 주소를 시·구·동으로 쪼갬. “구별로 회원 수 세기”가 필요하면 쪼개 둡니다.'}[f];}
bx.children[0].click();
/* 칸4 대응 수 캔버스 */
var cv=$('#card5'),mode='11',links=[],L={'11':[['남편','아내'],[['김','이','박'],['정','최','한']],[[0,0],[1,1]]],'1n':[['부서','사원'],[['영업','인사'],['가','나','다','라']],[[0,0],[0,1],[1,2]]],'nm':[['고객','책'],[['김','이','박'],['A','B','C']],[[0,0],[0,1],[1,0],[2,2]]]};
function drawC(){var F=LAB.fit(cv),c=F.c,Wd=F.W,H=F.H,d=L[mode];c.clearRect(0,0,Wd,H);var fam=getComputedStyle(document.body).fontFamily;
 function pos(side,i,n){return [side?Wd-120:120,56+i*((H-80)/Math.max(1,n-1||1))+(n===1?(H-80)/2:0)];}
 c.font='700 14px '+fam;c.fillStyle='#5b6874';c.textAlign='center';c.fillText(d[0][0],120,20);c.fillText(d[0][1],Wd-120,20);
 links.forEach(function(l){var a=pos(0,l[0],d[1][0].length),b=pos(1,l[1],d[1][1].length);c.strokeStyle='#9b3fb5';c.lineWidth=2;c.beginPath();c.moveTo(a[0]+22,a[1]);c.lineTo(b[0]-22,b[1]);c.stroke();});
 [0,1].forEach(function(s){d[1][s].forEach(function(n,i){var p=pos(s,i,d[1][s].length);c.fillStyle='#fff';c.strokeStyle='#16212b';c.lineWidth=1.5;c.beginPath();c.arc(p[0],p[1],20,0,7);c.fill();c.stroke();c.fillStyle='#16212b';c.font='14px '+fam;c.fillText(n,p[0],p[1]+5);});});
 LAB.stamp(c,Wd,'설명용 예시');}
LAB.addMod(cv,function(){drawC();});
function setM(m){mode=m;links=L[m][2].slice();$$('#lv4 [data-c]').forEach(function(x){x.setAttribute('aria-pressed',x.dataset.c===m);});
 $('#card5o').innerHTML={'11':'<b>1:1</b> — 남편 한 명은 아내 한 명과만, 아내 한 명도 남편 한 명과만.','1n':'<b>1:N</b> — 한 부서에 여러 사원, 한 사원은 한 부서에만. “라” 사원은 아직 어느 부서와도 이어지지 않았습니다(그렇다면 사원의 참여는 선택 참여).','nm':'<b>N:M</b> — 김 고객은 A·B를, A 책은 김·이에게 팔렸습니다. 양쪽 모두 “여러 개”와 이어집니다.'}[m];$('#card5msg').textContent='';drawC();}
$$('#lv4 [data-c]').forEach(function(b){b.onclick=function(){setM(b.dataset.c);};});
$('#card5add').onclick=function(){var d=L[mode],R=LAB.rng(links.length*7+3),tries=0,ok=false,msg='';
 while(tries++<40&&!ok){var a=Math.floor(R()*d[1][0].length),b=Math.floor(R()*d[1][1].length);if(links.some(function(l){return l[0]===a&&l[1]===b;}))continue;
  var la=links.filter(function(l){return l[0]===a;}).length,lb=links.filter(function(l){return l[1]===b;}).length;
  if(mode==='11'&&(la||lb)){msg=d[1][0][a]+'–'+d[1][1][b]+' 연결 거부: 1:1에서는 이미 짝이 있는 쪽을 또 이을 수 없어요.';break;}
  if(mode==='1n'&&lb){msg=d[1][1][b]+' 사원은 이미 부서가 있어 다른 부서와 이을 수 없어요 (1:N의 N쪽은 하나만).';continue;}
  links.push([a,b]);ok=true;msg=d[1][0][a]+'–'+d[1][1][b]+' 연결 — 규칙 안에서 허용.';}
 $('#card5msg').textContent=msg||'더 이을 수 있는 선이 없습니다.';drawC();};
setM('11');
/* 대결 */
var REQ=[['김하나','DB설계'],['김하나','통계학'],['이두리','DB설계'],['이두리','회계원리'],['박세나','통계학'],['박세나','DB설계']];
PAGE.duel=function(){var robo={};REQ.forEach(function(r){robo[r[0]]=r[1];});var keep=Object.keys(robo).length;
 document.getElementById('duel5t').innerHTML=LAB.tableHTML(['학생','수강과목 (칸 하나)'],Object.keys(robo).map(function(k){return [k,robo[k]];}),{cap:'주판봇의 학생 표 — 마지막에 신청한 과목만 남음'})+LAB.tableHTML(['학생','과목'],REQ,{cap:'초파리의 수강 표 — 6건 모두'});
 return {fly:REQ.length,robo:keep,flyTxt:REQ.length+'/6',roboTxt:keep+'/6'};};
''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'현실 세계의 정보를 목적에 맞게 추상화해 컴퓨터 세계의 데이터베이스로 옮기는 과정(개념·논리·물리).','lv2':'업무 문장에서 개체·속성·관계·제약 조건 후보를 찾아내는 일.','lv3':'단순·복합·다중값·유도·키 속성과 그 ERD 기호.','lv4':'한 개체가 다른 개체 몇 개와 이어질 수 있는지(1:1, 1:N, N:M)와 참여의 필수·선택.'}[s['id']]
