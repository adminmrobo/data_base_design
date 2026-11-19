# 8주차 — 중간 REVIEW (1~7주)
MOCK = [
 ('def', dict(q='관찰·측정해 수집한 값으로, 아직 처리되지 않은 것은?',o=['정보','데이터','지식','메타데이터'],a=1,why='데이터입니다. 의사 결정에 쓰도록 처리한 결과가 정보입니다. (2주차)')),
 ('case', dict(q='3개 부서가 같은 고객 엑셀을 복사해 각자 고친다. 데이터베이스 정의의 네 조건 중 가장 먼저 깨지는 것은?',o=['저장 데이터','통합 데이터','운영 데이터','공유 데이터'],a=1,why='같은 사실이 여러 곳에 따로 있어 중복이 통제되지 않습니다 — 통합 데이터 조건. (2주차)')),
 ('def', dict(q='JSON·XML처럼 구조 설명이 데이터 안에 들어 있는 데이터는?',o=['정형','반정형','비정형','범주형'],a=1,why='반정형 데이터입니다. (2주차)')),
 ('case', dict(q='만족도(1~5점) 평균을 내려는 보고서가 있다. 가장 적절한 지적은?',o=['비율 척도라 문제없다','서열 척도라 평균은 참고값이며 중앙값·비율을 함께 봐야 한다','명목 척도라 셀 수도 없다','등간 척도라 비율 계산이 된다'],a=1,why='만족도는 서열 척도 — 간격이 같다는 보장이 없습니다. (2주차)')),
 ('def', dict(q='응용 프로그램이 파일 구조에 맞춰 작성되어, 구조가 바뀌면 프로그램도 고쳐야 하는 성질은?',o=['데이터 독립성','데이터 종속성','데이터 무결성','동시 공유'],a=1,why='데이터 종속성. DBMS는 이를 데이터 독립성으로 해결합니다. (3주차)')),
 ('case', dict(q='A→B 이체 중 B 쪽 갱신이 실패했다. DBMS가 이전 상태로 되돌리는 동작은?',o=['커밋','롤백','조인','인덱싱'],a=1,why='롤백(후진 복귀) — 저널(로그)로 되돌립니다. (3주차)')),
 ('def', dict(q='DBMS의 단점이 아닌 것은?',o=['비용','백업·회복의 복잡성','중앙 관리 취약점','데이터 중복 통제'],a=3,why='중복 통제는 장점입니다. (3주차)')),
 ('def', dict(q='데이터베이스 하나에 여러 개 있을 수 있는 스키마는?',o=['외부 스키마','개념 스키마','내부 스키마','없다'],a=0,why='외부 스키마(서브 스키마)는 사용자마다 있을 수 있습니다. (4주차)')),
 ('case', dict(q='개념 스키마의 칸 이름 “연락처”를 “전화번호”로 바꿨다. 학생 앱을 고치지 않으려면 무엇을 고치나?',o=['내부 스키마','외부/개념 사상','개념/내부 사상','데이터 사전을 직접'],a=1,why='논리적 데이터 독립성 — 외부/개념 사상(뷰 정의)만 고칩니다. 사전 직접 수정은 금지. (4주차)')),
 ('def', dict(q='데이터 사전에 대한 설명으로 옳은 것은?',o=['사용자가 자유롭게 수정한다','데이터를 위한 데이터(메타데이터)이며 사용자는 조회만 한다','실제 업무 데이터를 저장한다','외부 스키마의 다른 이름이다'],a=1,why='시스템 카탈로그 — DBMS가 관리하고 사용자는 조회만. (4주차)')),
 ('case', dict(q='“회원은 최대 5권을 14일 동안 대여한다”에서 “14일”은 ERD에서 무엇인가?',o=['개체','속성','관계','제약 조건(업무 규칙)'],a=3,why='기간·수량 규칙은 제약 조건입니다. (5주차)')),
 ('def', dict(q='ERD에서 점선 타원으로 표시하는 속성은?',o=['키 속성','다중값 속성','유도 속성','복합 속성'],a=2,why='유도 속성(나이 등 계산값). 이중 타원은 다중값. (5주차)')),
 ('case', dict(q='학생은 여러 과목을, 과목은 여러 학생을 가진다. 올바른 표현은?',o=['학생 표에 과목코드 칸 하나','과목 표에 학번 칸 하나','수강이라는 연결(교차) 개체를 둔다','관계를 생략한다'],a=2,why='N:M은 교차 개체(수강)로 풉니다. 칸 하나로는 기록이 덮어써집니다. (5주차 대결)')),
 ('def', dict(q='릴레이션의 튜플 개수를 무엇이라 하나?',o=['차수','카디널리티','도메인','스키마'],a=1,why='카디널리티. 속성 개수는 차수. (6주차)')),
 ('case', dict(q='{아이디}와 {아이디, 이름}이 모두 유일하다. {아이디, 이름}은 무엇인가?',o=['후보키','슈퍼키(후보키 아님)','외래키','대체키'],a=1,why='이름을 빼도 유일하므로 최소성을 만족하지 못합니다 → 슈퍼키. (6주차)')),
 ('case', dict(q='주문 표에 고객 표에 없는 고객 아이디를 넣으려 하자 거부되었다. 어떤 제약 때문인가?',o=['개체 무결성','참조 무결성','도메인 무결성','튜플 무순서'],a=1,why='외래키는 참조되는 표에 있는 값(또는 NULL)만 가질 수 있습니다. (6주차)')),
 ('def', dict(q='기본키 선택 기준으로 옳지 않은 것은?',o=['NULL이 될 수 있는 속성은 피한다','자주 바뀌는 속성은 피한다','가능하면 속성이 많은 후보키를 고른다','단순한 후보키를 고른다'],a=2,why='단순한(속성이 적은) 후보키를 고릅니다. (6주차)')),
 ('case', dict(q='R(4튜플, 3속성) × S(5튜플, 2속성)의 차수와 카디널리티는?',o=['차수 5, 카디널리티 20','차수 6, 카디널리티 9','차수 5, 카디널리티 9','차수 6, 카디널리티 20'],a=0,why='카티션 곱: 차수 = 3+2 = 5, 카디널리티 = 4×5 = 20. (7주차)')),
 ('def', dict(q='짝이 없는 튜플도 NULL로 채워 결과에 남기는 조인은?',o=['동등 조인','자연 조인','외부 조인','세미 조인'],a=2,why='외부 조인(LEFT·RIGHT·FULL). (7주차)')),
 ('case', dict(q='“필수 과목을 모두 들은 학생”을 구하는 관계 대수 연산은?',o=['셀렉트','카티션 곱','디비전','차집합'],a=2,why='‘모두’는 디비전 ÷. (7주차)')),
]
PAGE = dict(
num='08', slug='midterm_review', kind='review', short='8주', chip='08주차 · REVIEW',
title='중간 REVIEW', title_en='Midterm review (weeks 1-7)',
subtitle='1~7주차를 한 장의 지도와 모의 문제 20개로',
toc='데이터·DBMS·3단계 스키마·E-R 모델·관계 모델·관계 연산을 지도·낱말 카드·SQL 종합 실습·모의 문제 20개로 복습',
toc_faces=[('doc','front'),('asst','proud'),('moa','cheer')],
kicker='데이터베이스 설계 · 8주차 · 시험 대비 REVIEW',
question='7주 동안 배운 것을 “한 줄의 흐름”으로 말할 수 있을까?',
desc='데이터베이스 설계 8주차 중간 REVIEW: 1~7주차(데이터와 데이터베이스, DBMS, 3단계 스키마, E-R 모델, 관계 데이터 모델, 관계 연산) 핵심 정리, 낱말 카드, SQL 종합 실습, 모의 문제 20개.',
intro='<p>중간고사는 강의에서 다룬 개념과 사례의 <b>객관식·단답식</b>입니다. 이 페이지는 새 내용을 배우지 않습니다. 대신 7주를 <b>네 묶음</b>으로 다시 걷고, 묶음마다 “헷갈리는 짝”을 정리한 뒤, 맨 아래 <b>모의 문제 20개</b>로 스스로 점검합니다. 틀린 문항의 해설 끝에 몇 주차인지 적어 두었으니 그 페이지로 돌아가면 됩니다.</p>',
kpis=[('7주','범위: 1~7주차 (교재 1~6장)'),('4묶음','데이터 · 시스템 · 모델링 · 관계'),('20문항','모의 문제 (정의형 10 · 상황형 10)'),('16장','낱말 카드')],
kpi_note='시험 날짜·장소는 학사 일정과 강의 공지를 따릅니다. 이 페이지는 범위 복습용입니다.',
hero_talk=[
 ('doc','front','오늘은 <b>지도를 다시 펴는 날</b>이다. 새 길은 없다. 지나온 길에서 헷갈렸던 갈림길만 다시 본다.'),
 ('asst','smile','저는 키 다섯 개랑 스키마 세 개가 아직 섞여요… 그것부터 정리하고 싶어요.'),
 ('fly','clip','정의만 외우면 상황형 문제에서 막혀. 정의 하나에 <b>예시 하나, 반례 하나</b>를 붙여.'),
 ('robo','smile','나는 노트를 두껍게 만들 거야! 예시랑 반례까지 전부!')],
crew=[('doc','front','묶음별 핵심과 헷갈리는 짝 정리'),('asst','smile','모의 문제 진행, 점수 발표'),('fly','clip','정의만 외우는 습관을 경계'),('robo','smile','두꺼운 노트파 (오늘은 쓸모가 있음)'),('moa','cheer','인턴 모아 — 응원 담당 (판정·숫자 발표는 하지 않음)')],
recap='1~7주 한 줄 흐름: <b>데이터</b>를 함께 쓰려면 <b>데이터베이스</b>가 필요하고 → 파일로는 무너지니 <b>DBMS</b>가 관리하며 → 세 겹 <b>스키마</b>로 독립성을 얻고 → 현실을 <b>ERD</b>로 그린 뒤 → <b>릴레이션·키·무결성</b>으로 표를 만들고 → <b>관계 연산</b>으로 원하는 결과를 꺼낸다.',
notion=[('08주차 : 시험대비 Review (노션)', NOTION+'1ab17a4520ed81a5808df3129b624862', '강의 계획 대비 부족한 부분 보충 — 자료·출결 과제는 사이버캠퍼스'),
        ('데이터베이스설계 강의 개요 — 시험 방식', NOTION+'2025-2-1ab17a4520ed81cd9040dbae826a48ad', '객관식·단답식, 대면 원칙, 시험 후 답안 배포')],
why_title='이 REVIEW를 쓰는 법',
why=[('지도 먼저','아래 표의 한 줄 요약을 소리 내어 읽어 보세요. 막히는 줄이 복습할 주차입니다.'),
     ('묶음별로','1~4칸은 묶음마다 “핵심 → 헷갈리는 짝 → 확인 퀴즈” 순서입니다. 각 칸 3분이면 됩니다.'),
     ('모의 문제로 확인','맨 아래 20문항. 틀린 문항의 해설에 적힌 주차로 돌아가세요.')],
bigpicture='''<div class="tbl"><table><thead><tr><th>주차</th><th>교재</th><th>한 줄 요약</th><th>대결 결과 (교훈)</th><th>페이지</th></tr></thead><tbody>
<tr><td>1</td><td>—</td><td>화면 뒤에는 DB, “여러 사람·오래·같은 사실”이면 한 곳에</td><td>초파리 승 (미리 정리해 두면 빨리 찾는다)</td><td><a href="w01_course_guide.html">열기</a></td></tr>
<tr><td>2</td><td>1장</td><td>데이터 vs 정보, DB = 공유·통합·저장·운영, 정형·반정형·비정형</td><td>주판봇 승 (창고에는 원자료)</td><td><a href="w02_data_and_database.html">열기</a></td></tr>
<tr><td>3</td><td>2장</td><td>파일 시스템의 중복·종속 → DBMS(정의·조작·제어), 장점 8 · 단점 3</td><td>조건부 (작으면 파일, 크면 DBMS)</td><td><a href="w03_dbms.html">열기</a></td></tr>
<tr><td>4</td><td>3장</td><td>외부·개념·내부 스키마, 사상으로 논리적·물리적 독립성, 데이터 사전</td><td>주판봇 실격 (사전은 조회만)</td><td><a href="w04_database_system.html">열기</a></td></tr>
<tr><td>5</td><td>4장</td><td>문장 → 개체·속성·관계, 속성 5종, 1:1·1:N·N:M</td><td>초파리 승 (N:M은 연결 개체)</td><td><a href="w05_er_modeling.html">열기</a></td></tr>
<tr><td>6</td><td>5장</td><td>릴레이션 특징 4, 키 5종, 개체·참조 무결성</td><td>무승부 (대리키는 UNIQUE와 함께)</td><td><a href="w06_relational_model.html">열기</a></td></tr>
<tr><td>7</td><td>6장</td><td>σ π ∪ ∩ − × ⋈ ÷, 외부 조인</td><td>초파리 승 (먼저 고르면 덜 일한다)</td><td><a href="w07_relational_operations.html">열기</a></td></tr></tbody></table></div>''',
why_say=('moa','cheer','오늘은 제가 응원 담당이에요! 틀려도 괜찮아요, 틀린 곳이 바로 복습 지도예요!'),
steps=[
dict(id='lv1', short='데이터', title='묶음 ① 데이터와 데이터베이스 (1~2주)', concept='데이터와 데이터베이스 복습', en='review of data and databases', cid='lab:concept/review-data-database',
 tag='복습: 1~2주차', analogy='재료와 창고',
 situation='시험 문제는 이렇게 나옵니다: “다음 중 ‘정보’에 해당하는 것은?”, “데이터베이스의 특징이 아닌 것은?”. 정의를 말할 수 있는지, 예를 고를 수 있는지 둘 다 봅니다.',
 pair=(('핵심','데이터 = 측정값 / 정보 = 결정에 쓰도록 처리한 결과 / 데이터베이스 = <b>공유·통합·저장·운영</b> 데이터 / 특징 = <b>실시간 접근·계속 변화·동시 공유·내용으로 참조</b>'),
       ('헷갈리는 짝','<b>통합</b> ≠ 중복 0 (중복을 통제할 수 있음) · <b>반정형</b>(JSON) vs <b>비정형</b>(사진·글) · <b>서열</b>(만족도) vs <b>등간</b>(섭씨) vs <b>비율</b>(나이)')),
 panel='<div class="flash" data-cards="c1"></div>', panel_title='낱말 카드 — 눌러서 뒤집기',
 sim='1~2주 낱말 카드',
 explain='<p><b>네 조건 vs 네 특징</b>을 섞지 마세요. 조건(공유·통합·저장·운영)은 “무엇이 데이터베이스인가”, 특징(실시간·변화·동시 공유·내용 참조)은 “데이터베이스가 어떻게 동작하는가”입니다. “동시 공유”는 특징, “공유 데이터”는 조건 — 비슷한 말이 양쪽에 다 있다는 점이 함정입니다.</p>',
 limit='데이터베이스가 무엇인지는 정리했습니다. 다음 묶음은 그것을 관리하는 시스템입니다.', limit_label='관리 시스템 쪽 복습이 남음',
 quiz=[dict(q='데이터베이스의 “특징”에 해당하는 것은?',o=['통합 데이터','운영 데이터','내용으로 참조','저장 데이터'],a=2,why='나머지 셋은 정의의 “조건”입니다. 특징은 실시간 접근·계속 변화·동시 공유·내용으로 참조.'),
       dict(q='“평균 기온이 작년보다 2도 높다”는 데이터와 정보 중 무엇에 가까운가?',o=['데이터','정보','메타데이터','스키마'],a=1,why='측정값들을 처리(평균·비교)해 판단에 쓸 수 있게 만든 결과이므로 정보입니다.')]),
dict(id='lv2', short='시스템', title='묶음 ② DBMS와 데이터베이스 시스템 (3~4주)', concept='DBMS와 3단계 구조 복습', en='review of dbms and three-schema architecture', cid='lab:concept/review-dbms-schema',
 tag='복습: 3~4주차', analogy='관리인과 세 층 건물',
 situation='“파일 시스템의 문제 → DBMS의 답” 짝 맞추기와 “어느 스키마/어느 독립성” 고르기가 단골입니다.',
 pair=(('핵심','파일 시스템: 중복·종속·동시 공유·보안·회복 부족·개발 어려움 → DBMS: 정의(DDL)·조작(DML)·제어(DCL). 3단계: 외부(여러 개)·개념(1)·내부(1), 사상 2개.'),
       ('헷갈리는 짝','<b>논리적</b> 독립성 = 개념 변경에도 외부 그대로 (외부/개념 사상) · <b>물리적</b> 독립성 = 내부 변경에도 개념 그대로 (개념/내부 사상) · <b>질의 처리기</b>(해석) vs <b>저장 데이터 관리자</b>(디스크)')),
 panel='''<p style="margin-top:0">왼쪽 문제를 고르고, 오른쪽에서 그 문제를 푸는 DBMS의 답을 고르세요.</p><div class="two"><div class="chips" id="m8a"></div><div class="chips" id="m8b"></div></div><div class="insight" id="m8o">짝을 맞춰 보세요.</div>''',
 panel_title='짝 맞추기 — 문제와 답',
 sim='파일 시스템 문제–DBMS 해법 짝 맞추기',
 explain='<p>독립성 문제는 “<b>무엇이 바뀌었나</b>”부터 보세요. 칸 이름·표 구조가 바뀌었으면 개념 스키마 → 논리적 독립성. 디스크·색인·저장 방식이 바뀌었으면 내부 스키마 → 물리적 독립성.</p>',
 limit='시스템 구조까지 정리했습니다. 다음은 그 안에 들어갈 표를 설계하는 모델링입니다.', limit_label='모델링 쪽 복습이 남음',
 quiz=[dict(q='색인(인덱스)을 새로 만들었는데 개념 스키마는 그대로였다. 어떤 독립성인가?',o=['논리적 데이터 독립성','물리적 데이터 독립성','참조 무결성','데이터 종속성'],a=1,why='저장 구조(내부) 변경을 개념/내부 사상이 흡수 — 물리적 독립성.'),
       dict(q='DBMS의 세 기능 중 무결성·보안·동시성·회복을 담당하는 것은?',o=['정의','조작','제어','저장'],a=2,why='제어 기능(DCL)입니다.')]),
dict(id='lv3', short='모델링', title='묶음 ③ 데이터 모델링과 E-R 모델 (5주)', concept='E-R 모델 복습', en='review of e-r modeling', cid='lab:concept/review-er-model',
 tag='복습: 5주차', analogy='문장 → 그림',
 situation='시험에는 짧은 업무 문장을 주고 “개체·관계·대응 수”를 묻거나, ERD 기호의 뜻을 묻는 문제가 나옵니다.',
 pair=(('핵심','명사 → 개체·속성, 동사 → 관계, 숫자 규칙 → 제약 조건 · 사각형(개체)·타원(속성)·마름모(관계) · 1:1 / 1:N / N:M'),
       ('헷갈리는 짝','<b>이중 타원</b>(다중값) vs <b>점선 타원</b>(유도) · <b>이중 사각형</b>(약한 개체) · <b>이중선</b>(필수 참여) · N:M은 <b>교차 개체</b>로 풂')),
 panel='''<p style="margin-top:0">교안의 학사 관리 실습 과제입니다. 각 관계의 대응 수를 고르세요.</p><div id="er8"></div><div class="ctrl"><button type="button" class="bt primary" id="er8c">채점</button></div><div class="insight" id="er8o"></div>''',
 panel_title='실습 — 학사 관리 ERD의 대응 수',
 sim='학사 관리 ERD 대응 수 맞히기',
 explain='<p>교안 조건: 학생은 한 학과에만 소속, 교수는 한 학과에만 소속, 학생–과목은 다대다, 교수–과목은 일대다. 설계 힌트: <b>다대다는 중간 연결 표로</b>, <b>일대다는 ‘다’ 쪽에 외래키</b>. 이 힌트는 11주차 변환 규칙 2·3과 같습니다.</p>',
 limit='그림까지 복습했습니다. 마지막 묶음은 그 그림을 표·키·연산으로 다루는 관계 모델입니다.', limit_label='관계 모델·연산 복습이 남음',
 quiz=[dict(q='“교수는 한 학과에만 소속, 학과에는 여러 교수”의 대응 수(학과:교수)는?',o=['1:1','1:N','N:M','N:1만 가능'],a=1,why='학과 하나에 교수 여럿, 교수는 학과 하나 → 학과:교수 = 1:N.'),
       dict(q='개체 사각형이 이중선(이중 사각형)이면?',o=['다중값 개체','약한 개체','필수 참여','유도 개체'],a=1,why='다른 개체에 의존하는 약한 개체입니다. 필수 참여는 관계선이 이중선입니다.')]),
dict(id='lv4', short='관계', title='묶음 ④ 관계 모델과 관계 연산 (6~7주)', concept='관계 모델과 연산 복습', en='review of relational model and algebra', cid='lab:concept/review-relational',
 tag='복습: 6~7주차 · SQL 종합', analogy='표의 규칙과 표의 산수',
 situation='키 판정(유일성·최소성), 무결성 위반 고르기, 관계 대수 결과의 차수·카디널리티 계산이 나옵니다. SQL은 9주차부터지만, 관계 연산을 SQL로 확인해 두면 기억이 오래갑니다.',
 pair=(('핵심','슈퍼키(유일) ⊃ 후보키(유일+최소) ⊃ 기본키 / 대체키 / 외래키 · 개체 무결성(PK에 NULL 금지) · 참조 무결성(FK는 있는 값) · σ 줄, π 칸(중복 제거), × 곱, ⋈ 짝, ÷ 모두'),
       ('헷갈리는 짝','<b>차수</b>(열 수) vs <b>카디널리티</b>(행 수) · ×의 결과 차수는 <b>합</b>, 카디널리티는 <b>곱</b> · <b>π</b>는 중복 제거, SQL SELECT는 DISTINCT가 있어야 제거')),
 panel='<div class="sqllab" id="lab8" data-lab="lab8"></div>', panel_title='SQL 종합 실습 — 관계 연산을 SQL로 확인',
 sim='관계 연산 종합 SQL 실습',
 explain='<p>실습실의 다섯 버튼은 각각 σ, π, ⋈, 외부 조인, ÷를 SQL로 쓴 것입니다. 실행하기 전에 <b>결과 행 수를 먼저 적어 보고</b> 맞혀 보세요. 맞히면 그 연산은 이해한 것입니다.</p>',
 limit='여기까지가 중간고사 범위입니다. 9주차부터는 SQL로 직접 표를 만들고 고칩니다.', limit_label='SQL로 직접 정의·조작하는 단계가 남음',
 quiz=[dict(q='후보키 {학번}, {이메일} 중 {학번}을 기본키로 했다. 주문 표가 학번을 참조하면 주문 표의 학번은?',o=['대체키','외래키','슈퍼키','후보키'],a=1,why='다른 릴레이션의 기본키를 참조하는 속성은 외래키입니다.'),
       dict(q='R(차수 3, 카디널리티 4)에 σ를 적용했다. 결과의 차수는?',o=['3','4','줄어든다','알 수 없다'],a=0,why='셀렉트는 줄만 고르므로 차수(열 수)는 그대로 3. 카디널리티는 4 이하.')]),
],
nav_extra=[('mock','모의 20')],
extra_sections=['''<section class="level" id="mock"><div class="wrap"><h2>모의 문제 20 — 객관식</h2>
<p>정의형 10문항, 상황·계산형 10문항이 섞여 있습니다. 해설 끝의 (n주차)가 돌아갈 페이지입니다. 다 풀면 맨 위 사용법 칸의 퀴즈 진행 표시로 점수를 확인하세요.</p>
<div class="quiz" data-quiz="mock"></div>
<div class="say"><img data-who="moa" data-mood="cheer" width="56" height="56" alt="" aria-hidden="true"><div class="bub"><span class="who w-moa">인턴 모아</span><p>상황형에서 많이 틀렸다면, 정의에 예시 하나씩만 붙여 보세요. 대결이 그 이야기예요!</p></div></div>
</div></section>'''],
extra_quiz={'mock':[m[1] for m in MOCK]},
duel=dict(q='요약 노트 — 한 줄 정의 vs 정의 + 예시 + 반례',
 intro='시험 전날, 초파리는 “개념마다 정의 한 줄” 노트를, 주판봇은 “정의 + 예시 + 반례 세 줄” 노트를 만들었습니다. 위 모의 문제 20개 중 각 노트만 보고 답할 수 있는 문항 수를 셉니다. (정의형 문항은 둘 다, 상황형 문항은 예시·반례가 있어야 답할 수 있다고 가정합니다.)',
 fly_pick='개념마다 정의 한 줄', fly_line='시험 전날엔 짧은 게 최고야. 정의만 정확하면 돼.',
 robo_pick='정의 + 예시 + 반례 세 줄', robo_line='많이 써 두면 든든하지! 예시랑 반례까지 다 적었어!',
 metric='노트로 답할 수 있는 모의 문항 수 (20개 중)', step=3,
 run='return PAGE.duel();',
 announce='return "모의 20문항 중 정의형 "+r.d+"개, 상황형 "+r.c+"개. 초파리 노트는 <b>"+r.fly+"개</b>, 주판봇 노트는 <b>"+r.robo+"개</b>에 답할 수 있었어요.";',
 verdict='return "시험은 정의만이 아니라 상황으로 묻는다. 예시와 반례를 붙인 노트가 이긴다. 주판봇 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>헷갈리는 짝</th><th>구별하는 한마디</th></tr></thead><tbody>
<tr><td>데이터 / 정보</td><td>처리 전 값 / 결정에 쓰는 결과</td></tr>
<tr><td>DB 조건 / DB 특징</td><td>무엇이 DB인가(공유·통합·저장·운영) / 어떻게 동작하나(실시간·변화·동시 공유·내용 참조)</td></tr>
<tr><td>논리적 / 물리적 독립성</td><td>개념이 바뀌어도 외부 그대로 / 내부가 바뀌어도 개념 그대로</td></tr>
<tr><td>스키마 / 인스턴스</td><td>구조(잘 안 바뀜) / 그 순간의 값(계속 바뀜)</td></tr>
<tr><td>다중값 / 유도 속성</td><td>이중 타원(값 여러 개) / 점선 타원(계산값)</td></tr>
<tr><td>슈퍼키 / 후보키</td><td>유일 / 유일 + 최소</td></tr>
<tr><td>개체 / 참조 무결성</td><td>PK에 NULL 금지 / FK는 있는 값만</td></tr>
<tr><td>σ / π</td><td>줄 고르기 / 칸 고르기(중복 제거)</td></tr></tbody></table></div>
<div class="cards"><div><b>대결의 한계</b> “상황형은 예시가 있어야 풀린다”는 이 페이지의 가정입니다. 실제로는 정의를 정확히 이해하면 처음 보는 상황도 풀 수 있습니다 — 예시는 그 이해를 돕는 도구입니다.</div></div>''',
outro=[('doc','front','중간까지의 세 줄: ① 함께 쓰려면 DB, 관리하려면 DBMS ② 세 겹 스키마와 사상이 변경을 막는다 ③ ERD → 릴레이션·키 → 관계 연산.'),
       ('robo','happy','두꺼운 노트가 이겼어! 예시랑 반례를 적어 두길 잘했지!'),
       ('fly','coffee','인정. 다만 노트가 두꺼워도 읽지 않으면 0줄이야. 오늘 모의 20문항부터 풀어.'),
       ('asst','proud','저는 상황형에서 세 개 틀렸어요. 4주차랑 6주차 페이지로 돌아가 볼게요. 시험 잘 봐요, 모두!')],
next_note='<p class="recap"><b>시험 뒤 — 9주차 「SQL ① 데이터 정의」:</b> CREATE · ALTER · DROP과 제약 조건, 노션 「SQL 기본 문법」 실습.</p>',
gloss={'카디널리티':('카디널리티','용어','릴레이션의 튜플(행) 개수.','cardinality','lv4'),
 '차수':('차수','용어','릴레이션의 속성(열) 개수.','degree','lv4'),
 '사상':('사상','개념','두 스키마 단계 사이의 대응 관계.','mapping','lv2'),
 '교차 개체':('교차 개체','개념','N:M 관계를 풀기 위해 사이에 두는 개체.','intersection-entity','lv3'),
 '후보키':('후보키','용어','유일성과 최소성을 만족하는 키.','candidate-key','lv4'),
 '통합':('통합 데이터','개념','중복을 최소화하고 허용한 중복은 통제하는 데이터.','integrated-data','lv1')},
facts=[('F01','8주차는 시험 대비 Review로 강의 계획 대비 부족한 부분을 보충','문헌 사실','ahn2025w08','lv1','노션 08주차 페이지'),
       ('F02','시험은 강의에서 다룬 주요 개념·사례의 객관식·단답식','문헌 사실','ahn2025syllabus','lv1','강의 개요 「시험 방식」'),
       ('F03','학사 관리 ERD 실습 조건: 학생·교수는 한 학과에만 소속, 학생–과목 다대다, 교수–과목 일대다','문헌 사실','ahn2025w04erd','lv3','「ERD 작성 실습 4단계」')],
refs=[dict(id='ahn2025w08',type='webpage',title='08주차 : 시험대비 Review',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed81a5808df3129b624862',role='primary'),
      dict(id='ahn2025syllabus',type='webpage',title='데이터베이스설계 (2025년 2학기) 강의 개요',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'2025-2-1ab17a4520ed81cd9040dbae826a48ad',role='primary'),
      dict(id='ahn2025w04erd',type='report',title='데이터베이스 설계 4주차 — ERD 작성, 관계 데이터 모델링, 정규화 과정 및 실무 적용',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='background',verified={'title':True,'authors':True,'year':False},note='출판 연도 미확인')],
models=['모의 문제 20개 (이 페이지가 만든 연습 문제 — 실제 시험 문제 아님)','대결의 “상황형은 예시·반례가 있어야 답할 수 있다” (설명용 가정)','SQL 종합 실습 데이터 (예시)'],
cover_alt='연구실 복도 한가운데 초록 문이 열려 있고, 그 안에 지나온 일곱 방의 지도가 벽에 붙어 있는 표지 (대체 그림)',
cover_svg='<svg width="320" height="130" viewBox="0 0 320 130">'+''.join('<rect x="%d" y="30" width="34" height="70" rx="4" fill="#fff" stroke="#9aa5b1"/><text x="%d" y="70" font-size="14" fill="#5b6874">%d</text>'%(8+i*40,21+i*40,i+1) for i in range(7))+'<rect x="288" y="20" width="28" height="90" rx="4" fill="#e7f5ec" stroke="#13733a" stroke-width="2"/><text x="293" y="70" font-size="13" fill="#13733a">8</text></svg>',
prereq=['07'],
cards={'c1':[['데이터','관찰·측정해 수집한 값 (예: 판매량 30개)'],['정보','데이터를 결정에 쓰도록 처리한 결과 (예: 금요일이 평일의 2배)'],['공유 데이터','여러 사용자가 함께 소유·이용'],['통합 데이터','중복 최소화, 허용한 중복은 통제 가능 — “중복 0”이 아님!'],['저장 데이터','컴퓨터가 접근할 수 있는 매체에 저장'],['운영 데이터','조직 업무에 쓰이며 지속적으로 유지·관리'],['내용으로 참조','위치가 아니라 값으로 찾기 (WHERE)'],['반정형','구조 설명이 데이터 안에 (JSON, XML)'],['비정형','구조가 없음 (글, 사진, 음성)'],['서열 척도','순서만 있음, 간격 모름 (학력, 만족도)'],['등간 척도','같은 간격, 절대 0 없음 (섭씨)'],['비율 척도','비율 계산 가능 (나이, 무게)'],['실시간 접근','질의에 바로 응답'],['계속 변화','삽입·삭제·수정으로 늘 최신'],['동시 공유','여러 사용자가 동시에 사용 (특징)'],['이산형 vs 연속형','셀 수 있는 값 (점수) vs 사이 값이 무수 (키)']]},
js=r'''
var $=LAB.$,$$=LAB.$$;
var PR=[['같은 값이 여러 파일에','통합 저장 + 제약 조건'],['프로그램이 파일 구조에 묶임','데이터 독립성 (3단계 스키마)'],['갱신 도중 실패','트랜잭션 · 롤백'],['동시 수정 충돌·권한 부족','동시성 제어 · 권한 관리(DCL)'],['조회·삽입 코드를 매번 작성','표준 질의 언어 SQL']];
var shuf=[3,0,4,1,2],pa=null,done={};
function m8(){$('#m8a').innerHTML=PR.map(function(p,i){return '<button type="button" class="bt" data-i="'+i+'" aria-pressed="'+(pa===i)+'"'+(done[i]?' disabled':'')+'>'+p[0]+'</button>';}).join('');
 $('#m8b').innerHTML=shuf.map(function(j){return '<button type="button" class="bt" data-j="'+j+'"'+(done[j]?' disabled':'')+'>'+PR[j][1]+'</button>';}).join('');
 $$('#m8a button').forEach(function(b){b.onclick=function(){pa=+b.dataset.i;m8();};});
 $$('#m8b button').forEach(function(b){b.onclick=function(){if(pa==null){$('#m8o').textContent='왼쪽 문제부터 고르세요.';return;}var j=+b.dataset.j;
  if(j===pa){done[j]=1;$('#m8o').innerHTML='<b>맞아요.</b> '+PR[j][0]+' → '+PR[j][1]+' ('+Object.keys(done).length+'/5)';pa=null;}else $('#m8o').innerHTML='다시 볼까요. 이 답은 “'+PR[j][0]+'”의 해법입니다.';m8();};});}
m8();
var REL=[['학과 – 학생','1n'],['학과 – 교수','1n'],['학생 – 과목 (수강)','nm'],['교수 – 과목 (담당)','1n']],ans={};
$('#er8').innerHTML=REL.map(function(r,i){return '<div class="ctrl"><b style="min-width:150px;display:inline-block">'+r[0]+'</b>'+['11','1n','nm'].map(function(c){return '<button type="button" class="bt" data-r="'+i+'" data-c="'+c+'">'+{'11':'1:1','1n':'1:N','nm':'N:M'}[c]+'</button>';}).join('')+'</div>';}).join('');
$$('#er8 button').forEach(function(b){b.onclick=function(){ans[b.dataset.r]=b.dataset.c;$$('#er8 button[data-r="'+b.dataset.r+'"]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});};});
$('#er8c').onclick=function(){var ok=REL.filter(function(r,i){return ans[i]===r[1];}).length;$('#er8o').innerHTML='맞힘 <b>'+ok+'/4</b>. 정답: 학과–학생 1:N, 학과–교수 1:N, 학생–과목 N:M(→ 수강 연결 표), 교수–과목 1:N(→ 과목 표에 교수번호 외래키).';};
var TYPES=__TYPES__;
PAGE.duel=function(){var d=TYPES.filter(function(t){return t==='def';}).length,c=TYPES.length-d;return {fly:d,robo:d+c,flyTxt:d+'/20',roboTxt:(d+c)+'/20',d:d,c:c};};
'''.replace('__TYPES__', str([m[0] for m in MOCK]).replace("'", '"')),
labs='''lab8:{setup:"CREATE DATABASE review; USE review; CREATE TABLE student (학번 VARCHAR(4) PRIMARY KEY, 이름 VARCHAR(10), 학과 VARCHAR(10)); CREATE TABLE enroll (학번 VARCHAR(4), 과목 VARCHAR(10), PRIMARY KEY (학번, 과목), FOREIGN KEY (학번) REFERENCES student(학번)); CREATE TABLE required (과목 VARCHAR(10) PRIMARY KEY); INSERT INTO student VALUES ('S1','김하나','컴공'),('S2','이두리','경영'),('S3','박세나','컴공'),('S4','최유나','통계'); INSERT INTO enroll VALUES ('S1','DB설계'),('S1','통계학'),('S2','DB설계'),('S3','DB설계'),('S3','통계학'); INSERT INTO required VALUES ('DB설계'),('통계학');",
presets:[{t:"σ 컴공 학생",q:"SELECT * FROM student WHERE 학과 = '컴공';"},{t:"π 학과 (중복 제거)",q:"SELECT DISTINCT 학과 FROM student;"},{t:"⋈ 학생–수강",q:"SELECT s.이름, e.과목\\nFROM student s JOIN enroll e ON s.학번 = e.학번;"},{t:"외부 조인 (수강 0과목 포함)",q:"SELECT s.이름, e.과목\\nFROM student s LEFT JOIN enroll e ON s.학번 = e.학번;"},{t:"÷ 필수 과목 모두",q:"SELECT s.이름 FROM student s\\nWHERE NOT EXISTS (\\n  SELECT * FROM required r\\n  WHERE NOT EXISTS (\\n    SELECT * FROM enroll e\\n    WHERE e.학번 = s.학번 AND e.과목 = r.과목));"}],
ready:"review 데이터베이스: student 4명, enroll 5건, required 2과목. 버튼을 누르기 전에 결과 행 수를 먼저 적어 보세요."}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'1~2주차 — 데이터와 정보, 데이터베이스의 네 조건과 네 특징, 데이터 분류.','lv2':'3~4주차 — 파일 시스템의 문제와 DBMS의 기능, 3단계 스키마와 데이터 독립성.','lv3':'5주차 — 데이터 모델링 단계, 개체·속성·관계, 대응 수.','lv4':'6~7주차 — 릴레이션의 특징, 키와 무결성, 관계 대수.'}[s['id']]
