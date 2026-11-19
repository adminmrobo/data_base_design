# 12주차 — 정규화 (교재 9장)
RAW = [['L001','B101','데이터베이스 개론','M201','김철수','010-1234-5678, 02-123-4567','2023-09-10'],
       ['L002','B102','자바 프로그래밍','M201','김철수','010-1234-5678, 02-123-4567','2023-09-15'],
       ['L003','B101','데이터베이스 개론','M202','이영희','010-9876-5432','2023-09-20']]
PAGE = dict(
num='12', slug='normalization', kind='lecture', short='12주', chip='12주차',
title='정규화', title_en='Normalization',
subtitle='나쁜 표를 알아보고 쪼개기 — 이상 현상, 함수 종속, 1NF에서 BCNF까지',
toc='삽입·갱신·삭제 이상, 함수 종속(완전·부분·이행), 1NF·2NF·3NF·BCNF와 4·5NF 개요, 무손실 분해, 반정규화와 실무 판단',
kicker='데이터베이스 설계 · 12주차 · 교재 9장',
question='표 하나에 다 넣으면 편한데, 왜 굳이 쪼개야 할까?',
desc='데이터베이스 설계 12주차: 이상 현상(삽입·갱신·삭제), 함수 종속성(완전·부분·이행), 정규형(1NF·2NF·3NF·BCNF, 4NF·5NF 개요), 무손실 분해, 반정규화와 성능의 균형. 도서 대여 예제와 노션 worst case.',
intro='<p>5주차 대결에서 주판봇은 “한 표에 다 넣자”다가 기록을 잃었고, 1주차에 본 노션 “worst case” 쇼핑몰 표는 칸이 19개였습니다. 그런 표가 왜 위험한지 오늘은 <b>이름을 붙여</b> 설명합니다(이상 현상). 그리고 “어느 칸이 어느 칸을 결정하는가”(함수 종속)를 기준으로 표를 <b>단계적으로 쪼갭니다</b>(정규화). 마지막에는 반대로, 일부러 합쳐 두는 반정규화가 언제 필요한지도 봅니다.</p>',
kpis=[('3가지','이상 현상: 삽입 · 갱신 · 삭제'),('3종','함수 종속: 완전 · 부분 · 이행'),('1→2→3→BC','정규형 단계'),('0줄','무손실 분해로 잃는 정보')],
hero_talk=[
 ('doc','front','정규화는 “쪼개기”가 아니라 <b>“한 사실은 한 곳에”</b>를 지키는 기술이다. 쪼개는 건 그 결과일 뿐.'),
 ('asst','smile','쪼개면 나중에 JOIN을 해야 하잖아요. 그건 귀찮지 않아요?'),
 ('fly','clip','귀찮지. 그래서 무조건이 아니야. 오늘 대결이 그 이야기야 — 조건에 따라 답이 달라.'),
 ('robo','smile','나는 다시 합치는 쪽! 표가 하나면 조회가 한 번에 끝나잖아!'),
 ('doc','front','부분 종속과 이행 종속은 처음엔 누구나 헷갈린다. 막히면 2칸 판정기에서 직접 눌러 보면 구별된다.')],
crew=[('doc','front','종속과 정규형 정리, 판정'),('asst','smile','이상 현상 실험 진행, 숫자 발표'),('fly','clip','부분·이행 종속을 찾아냄'),('robo','smile','반정규화파 (조건부로 맞음)')],
recap='6주차: 속성의 원자성(한 칸에 값 하나), 후보키 = 유일 + 최소. 11주차: 변환 규칙 5(다중값 속성은 별도 릴레이션). 정규화는 이 규칙들을 “함수 종속”이라는 하나의 잣대로 다시 정리한 것입니다.',
notion=[('노션 일정표 「10주차 : 정규화」 (노션 일정의 주차 번호는 이 사이트와 다릅니다)', NOTION+'1ab17a4520ed81d8a67ec7b5a8b5df74', '정규화 회차 페이지 (SQL 실습 페이지 묶음 포함)'),
        ('데이터 베이스 설계 : worst case (노션)', NOTION+'1ab17a4520ed810783e8ea080d594176', '열 19개짜리 쇼핑몰 통합 테이블 — 2칸 실습 재료'),
        ('속성의 원자성 예시 (노션)', NOTION+'28217a4520ed804a8e34d6ced8765057', '제1정규형의 출발점')],
why=[('이상 현상은 매일 일어난다','고객 전화번호를 주문 줄마다 저장하면, 번호가 바뀔 때마다 여러 줄을 고쳐야 하고 하나만 놓쳐도 불일치입니다.'),
     ('정규형은 체크리스트','“1NF인가? 2NF인가?”를 차례로 물으면, 감이 아니라 규칙으로 나쁜 구조를 찾습니다.'),
     ('균형이 필요하다','교안: 과도한 정규화는 조인 증가로 성능이 떨어질 수 있습니다. 실무에서는 접근 패턴을 보고 판단합니다.')],
bigpicture='<div class="flow"><span class="chip">비정규 (다중값)</span><span class="arr">→ 원자값</span><span class="chip">1NF</span><span class="arr">→ 부분 종속 제거</span><span class="chip">2NF</span><span class="arr">→ 이행 종속 제거</span><span class="chip">3NF</span><span class="arr">→ 결정자는 모두 후보키</span><span class="chip">BCNF</span><span class="arr">→ 다치·조인 종속</span><span class="chip">4NF · 5NF</span></div><p>정규화는 <b>함수 종속에 기반해 표를 단계적으로 분해</b>하는 과정이고(교안), 목표는 중복 최소화와 무결성 보장입니다. 실무 설계는 보통 3NF 또는 BCNF까지 갑니다.</p>',
steps=[
dict(id='lv1', short='이상 현상', title='이상 현상 — 한 표에 다 넣었을 때 생기는 세 가지 사고', concept='이상 현상', en='anomalies', cid='lab:concept/anomalies',
 tag='현장: 도서 대여 통합 표', analogy='한 장짜리 만능 장부',
 situation='도서관이 대여 기록을 표 하나(대여번호·도서ID·도서명·회원ID·회원명·연락처·대여일)에 모두 적습니다. 새 책이 들어왔는데 아직 아무도 안 빌렸다면, 이 표 어디에 적을까요?',
 pair=(('현장에서는','만능 장부 한 장에 책 정보, 회원 정보, 대여 기록을 다 적으면 처음엔 편합니다. 그런데 “빌린 적 없는 책”은 적을 줄이 없고, 회원 전화번호는 빌린 횟수만큼 반복됩니다.'),
       ('관계 모델에서는','<b>삽입 이상</b>: 필요한 정보를 넣으려는데 불필요한 정보까지 있어야 함(대여 없이 책만 등록 불가). <b>갱신 이상</b>: 중복된 값 중 일부만 바뀌어 불일치. <b>삭제 이상</b>: 지우려는 정보와 함께 다른 정보까지 사라짐.')),
 panel='''<div id="an12"></div><div class="ctrl"><button type="button" class="bt" id="an12i">새 책 B103 등록 (대여 없음)</button><button type="button" class="bt" id="an12u">김철수 번호 바꾸기 (첫 줄만)</button><button type="button" class="bt" id="an12d">L003 대여 기록 삭제</button><button type="button" class="bt" id="an12r">처음으로</button></div><div class="insight" id="an12o">버튼을 눌러 세 가지 사고를 일으켜 보세요.</div>''',
 panel_title='직접 해 보기 — 이상 현상 세 가지',
 sim='이상 현상 시뮬레이터',
 explain='<p>세 사고의 공통 원인은 <b>한 표에 서로 다른 사실이 섞여 있다</b>는 것입니다: “책의 사실(도서ID→도서명)”, “회원의 사실(회원ID→회원명·연락처)”, “대여의 사실(대여번호→누가·무엇을·언제)”. 사실마다 표를 하나씩 주면 세 사고가 모두 사라집니다. 그 “사실”을 정확히 말하는 도구가 다음 칸의 함수 종속입니다.</p>',
 aicheck='<p>노션 worst case 쇼핑몰 표(열 19개)를 AI에게 보여 주며 “이 표 괜찮아?”라고 물으면 “조회가 편해서 좋다”는 답이 나오기도 합니다. 이렇게 되물어 보세요: “판매자 전화번호가 바뀌면 몇 줄을 고쳐야 하나?”, “아직 주문이 없는 신상품은 어디에 넣나?”, “마지막 주문을 지우면 그 고객 정보는?” — 세 질문이 각각 갱신·삽입·삭제 이상입니다.</p>',
 limit='사고는 봤습니다. 그런데 “서로 다른 사실이 섞였다”를 어떻게 정확히 판정할까요?', limit_label='섞인 사실을 판정하는 기준이 없음',
 say=('asst','shock','L003을 지웠더니 이영희 회원이 통째로 사라졌어요! 대여 기록만 지운 건데…'),
 quiz=[dict(q='대여 기록이 하나도 없는 새 책을 통합 표에 등록할 수 없는 문제는?',o=['삽입 이상','갱신 이상','삭제 이상','참조 무결성'],a=0,why='필요한 정보(책)를 넣으려는데 불필요한 정보(대여)가 있어야만 넣을 수 있는 삽입 이상입니다.'),
       dict(q='김철수의 연락처가 2줄에 저장되어 있는데 1줄만 고쳤을 때 생기는 문제는?',o=['삽입 이상','갱신 이상','삭제 이상','개체 무결성'],a=1,why='중복된 값의 일부만 바뀌어 불일치가 생기는 갱신 이상입니다.')]),
dict(id='lv2', short='함수 종속', title='함수 종속 — 어느 칸이 어느 칸을 결정하는가', concept='함수 종속', en='functional dependency', cid='lab:concept/functional-dependency',
 tag='연구실: 종속 판정기', analogy='학번을 알면 이름을 안다',
 situation='학번을 알면 이름이 하나로 정해집니다. 이름을 알면 학번이 정해질까요? 동명이인이 있다면? 이 “정해진다”를 기호로 쓰면 학번 → 이름입니다.',
 pair=(('연구실에서는','학번표를 보고 학번 하나에 이름이 둘 나오는 일은 없습니다. 반대로 “김철수”를 찾으면 학번이 여럿 나올 수 있습니다.'),
       ('관계 모델에서는','X의 값 하나에 Y의 값이 하나만 대응하면 <b>Y는 X에 함수적으로 종속</b>, X → Y, X는 <b>결정자</b>. <b>완전</b> 종속: 기본키 전체에 종속. <b>부분</b> 종속: 기본키의 일부에만 종속. <b>이행</b> 종속: X → Y, Y → Z이면 X → Z.')),
 panel='''<p style="margin-top:0">왼쪽(결정자)과 오른쪽(종속자) 칸을 골라 「검사」를 누르세요. 아래 1NF 표의 데이터에서 반례가 있는지 찾습니다.</p>
<div class="ctrl"><label>X <select id="fdX"></select></label><span>→</span><label>Y <select id="fdY"></select></label><button type="button" class="bt primary" id="fdgo">검사</button></div><div id="fd12t"></div><div class="insight" id="fd12o"></div>''',
 panel_title='직접 해 보기 — 함수 종속 판정기',
 sim='함수 종속 판정기',
 explain='<p><b>1NF 표의 기본키는 {대여번호, 연락처}</b>입니다(연락처를 쪼갠 뒤 대여번호만으로는 줄이 구별되지 않음). 이때 대여번호 → 도서ID·회원ID·대여일, 도서ID → 도서명, 회원ID → 회원명. 도서명은 기본키의 <b>일부</b>(대여번호)를 거쳐 정해지므로 부분 종속, 그리고 대여번호 → 도서ID → 도서명은 <b>이행</b> 종속입니다.</p><p><b>주의:</b> 데이터 몇 줄로는 종속을 <b>증명</b>할 수 없고 <b>반례</b>만 찾을 수 있습니다. 종속은 업무 규칙(“도서ID가 같으면 책 제목이 같다”)에서 정합니다. 판정기가 “반례 없음”이라고 해도 그것은 “이 데이터에서는”입니다.</p>',
 limit='기준은 생겼습니다. 이제 이 기준으로 표를 한 단계씩 쪼개 봅니다.', limit_label='종속을 찾았지만 아직 분해하지 않음',
 say=('fly','point','데이터 세 줄이 X → Y를 증명해 주진 않아. 반례 하나는 반증해 주지만.'),
 quiz=[dict(q='기본키 {학번, 과목번호}인 수강 표에서 “학번 → 이름”이 성립한다. 이름은 기본키에 어떻게 종속되는가?',o=['완전 함수 종속','부분 함수 종속','이행 함수 종속','종속 없음'],a=1,why='기본키의 일부(학번)에만 종속되므로 부분 함수 종속입니다. 2NF에서 제거합니다.'),
       dict(q='X → Y, Y → Z가 성립해 X → Z가 되는 종속은?',o=['완전 종속','부분 종속','이행 종속','다치 종속'],a=2,why='이행 함수 종속입니다. 3NF에서 제거합니다.'),
       dict(q='판정기가 데이터 5줄에서 “도서명 → 도서ID 반례 없음”이라고 했다. 옳은 해석은?',o=['도서명 → 도서ID가 증명되었다','이 데이터에서는 반례가 없을 뿐, 업무 규칙(같은 제목의 다른 책이 있나)으로 따로 확인해야 한다','도서ID가 기본키가 아니다','1NF가 아니다'],a=1,why='데이터 몇 줄은 반례로 종속을 깨뜨릴 수만 있고 증명은 못 합니다. 같은 제목의 다른 판이 들어오면 깨집니다.')]),
dict(id='lv3', short='1NF·2NF', title='제1정규형과 제2정규형 — 원자값, 그리고 부분 종속 제거', concept='제1·제2정규형', en='first and second normal form', cid='lab:concept/1nf-2nf',
 tag='연구실: 교안 정규화 실습 1', analogy='장부를 칸마다 하나씩',
 situation='교안의 정규화 실습 1: 비정규화 표 “도서_대여_회원”을 1NF로, 다시 2NF로 바꿉니다. 단계마다 표가 몇 개, 줄이 몇 개가 되는지 보세요.',
 pair=(('연구실에서는','한 칸에 전화번호 두 개를 적은 장부는 칸마다 하나씩 다시 씁니다(1NF). 그다음 “책 이름은 대여 기록이 아니라 책에 딸린 정보”이니 책 목록을 따로 뺍니다(2NF).'),
       ('정규형으로는','<b>1NF</b>: 모든 속성이 원자값. <b>2NF</b>: 1NF + 기본키가 아닌 모든 속성이 기본키에 <b>완전</b> 함수 종속(부분 종속 제거). 기본키가 단일 속성이면 1NF는 자동으로 2NF입니다.')),
 panel='''<div class="ctrl"><button type="button" class="bt" data-nf="0">비정규</button><button type="button" class="bt" data-nf="1">1NF</button><button type="button" class="bt" data-nf="2">2NF</button></div><div id="nf12"></div><div class="insight" id="nf12o"></div>''',
 panel_title='단계별 보기 — 비정규 → 1NF → 2NF',
 sim='정규화 단계 보기 (1NF·2NF)',
 explain='<p><b>손으로 세기:</b> 비정규 3줄 → 1NF는 김철수의 연락처 두 개가 두 줄로 펼쳐져 <b>5줄</b>(L001×2, L002×2, L003×1). 중복은 오히려 늘었습니다! 1NF는 원자성만 해결하고 중복은 그대로라는 뜻입니다. 2NF에서 도서(도서ID→도서명), 회원(회원ID→회원명), 회원연락처(회원ID, 연락처), 대여(대여번호→도서ID·회원ID·대여일)로 나누면 “데이터베이스 개론”은 한 번, 김철수의 번호도 한 번씩만 저장됩니다.</p>',
 limit='2NF가 되어도 기본키가 아닌 칸끼리의 종속(회원ID → 회원등급 같은)이 남아 있을 수 있습니다.', limit_label='기본키가 아닌 속성 사이의 종속(이행 종속)이 남음',
 quiz=[dict(q='제1정규형의 조건은?',o=['부분 종속이 없다','모든 속성 값이 원자값이다','이행 종속이 없다','모든 결정자가 후보키다'],a=1,why='1NF는 모든 속성이 더 쪼갤 수 없는 원자값만 갖는 것입니다.'),
       dict(q='비정규 표 3줄 중 한 줄의 연락처 칸에 번호가 2개, 다른 한 줄에도 2개, 나머지는 1개다. 1NF로 펼치면 몇 줄? (계산)',o=['3','4','5','6'],a=2,why='2 + 2 + 1 = 5줄. 1NF는 중복을 줄이지 않고 오히려 늘릴 수 있습니다.')]),
dict(id='lv4', short='3NF·BCNF', title='제3정규형·BCNF, 그리고 반정규화 — 어디까지 쪼갤까', concept='제3정규형과 BCNF', en='third normal form and bcnf', cid='lab:concept/3nf-bcnf',
 tag='연구실: 교안 정규화 실습 2', analogy='등급표는 회원 명부에',
 situation='교안 실습 2의 2NF 표 “도서대출정보(대출번호, 회원ID, 회원이름, 회원등급, 도서ID)”. 대출번호가 기본키인데, 회원이름·회원등급은 사실 회원ID가 정합니다. 김철수의 등급이 실버로 바뀌면?',
 pair=(('연구실에서는','회원 등급은 대출 기록마다 적을 일이 아니라 회원 명부에 한 번 적을 일입니다. 대출 기록에는 “누가”(회원ID)만 남기면 됩니다.'),
       ('정규형으로는','<b>3NF</b>: 2NF + 기본키가 아닌 속성이 기본키에 <b>이행적</b>으로 종속하지 않음(비주요 속성끼리의 종속 제거). <b>BCNF</b>: 모든 결정자가 후보키. 4NF는 다치 종속, 5NF는 조인 종속을 제거합니다(개요만).')),
 panel='<div class="sqllab" id="lab12" data-lab="lab12"></div>',
 panel_title='SQL 실습실 — 3NF로 쪼개고 JOIN으로 되돌리기',
 sim='3NF 분해와 무손실 조인 실습',
 explain='<p><b>무손실 분해:</b> 쪼갠 표를 다시 JOIN했을 때 원래 표와 <b>똑같은 줄</b>이 나와야 합니다(더 생기지도, 사라지지도 않음). 실습실 ③에서 원래 2줄이 그대로 나오는지 확인하세요. 공통 속성(회원ID)이 한쪽 표의 키이기 때문에 무손실이 보장됩니다.</p><p><b>BCNF 예(교재 유형):</b> 수강(학번, 과목, 교수)에서 “교수 → 과목”(교수는 한 과목만 담당)이면, 교수는 결정자지만 후보키가 아니므로 3NF여도 BCNF가 아닙니다. (학번, 교수)와 (교수, 과목)으로 나눕니다.</p><p><b>반정규화(교안):</b> 모든 표를 3NF로 바꾸면 조인이 늘어 성능이 떨어질 수 있습니다. 조회가 아주 잦은 데이터는 일부러 합쳐 두는 것을 검토하되, 그 대가로 생기는 중복은 트리거나 일괄 갱신으로 관리해야 합니다.</p>',
 aicheck='<p>“3NF가 무조건 정답인가요?”라고 물으면 AI는 “네, 정규화가 좋습니다”라고 하기도 하고 “실무에선 반정규화합니다”라고 하기도 합니다. 둘 다 반쪽 답입니다. 판단 질문은 이것입니다: <b>이 데이터는 읽기가 많은가, 쓰기가 많은가? 중복된 값이 바뀌면 누가 다 고치는가?</b> — 오늘의 대결.</p>',
 limit='구조는 튼튼해졌습니다. 그런데 이 표들을 여러 사람이 <b>동시에</b> 고치거나, 고치는 도중에 서버가 멈추면? 트랜잭션·회복·병행 제어 — 13주차.', limit_label='동시 수정·장애 상황의 데이터 보호는 아직',
 quiz=[dict(q='2NF 표에서 기본키가 아닌 속성 사이의 종속(이행 종속)을 제거한 정규형은?',o=['1NF','2NF','3NF','4NF'],a=2,why='3NF는 기본키에 대한 이행적 함수 종속을 제거한 정규형입니다.'),
       dict(q='“모든 결정자가 후보키”인 정규형은?',o=['2NF','3NF','BCNF','5NF'],a=2,why='보이스-코드 정규형(BCNF)의 정의입니다. 3NF보다 엄격합니다.')]),
],
duel=dict(q='3NF로 쪼갤까, 반정규화로 합쳐 둘까?',
 intro='회원 1,000명, 대출 기록 20,000건. 초파리는 3NF(대출 표 + 회원 표, 조회 때 JOIN), 주판봇은 반정규화(대출 표에 회원이름·등급을 함께 저장). 한 달 동안의 작업 비용을 <b>설명용 비용 모형</b>(건드리는 행 수)으로 비교합니다. 가정을 바꿔 보세요.',
 fly_pick='3NF — 회원 정보는 회원 표에 한 번', fly_line='한 사실은 한 곳에. 등급이 바뀌면 한 줄만 고치면 돼.',
 robo_pick='반정규화 — 대출 표에 회원 정보도 저장', robo_line='조회할 때 JOIN이 없으니 빠르지! 표 하나면 한 번에 끝!',
 metric='한 달 작업 비용 (건드리는 행 수, 설명용 모형 · 적을수록 이김)', higher=False, step=3,
 after='<div class="ctrl"><button type="button" class="bt" id="asR" aria-pressed="true">가정 A — 조회 위주 (조회 5만 번 · 등급 변경 10번)</button><button type="button" class="bt" id="asW" aria-pressed="false">가정 B — 변경 위주 (조회 500번 · 등급 변경 300번)</button></div><div id="duel12t"></div><p class="cvcap">모형: 조회 1번 = 3NF는 대출 1줄 + JOIN한 회원 1줄(2행), 반정규화는 1행. 등급 변경 1번 = 3NF는 회원 1행, 반정규화는 그 회원의 대출 기록 평균 20행 + 회원 1행. 실제 성능은 색인·캐시에 따라 다릅니다.</p>',
 run='return PAGE.duel();',
 announce='return "[설명용 모형 기준] 가정 A(조회 위주): 초파리 <b>"+r.a[0].toLocaleString()+"</b> vs 주판봇 <b>"+r.a[1].toLocaleString()+"</b> · 가정 B(변경 위주): 초파리 <b>"+r.b[0].toLocaleString()+"</b> vs 주판봇 <b>"+r.b[1].toLocaleString()+"</b> (행)";',
 verdict='return "조회가 압도적이면 반정규화가, 변경이 잦으면 3NF가 덜 일한다. 어느 쪽이 맞는지는 접근 패턴이 정한다. 조건부 판정.";'),
summary='''<div class="tbl"><table><thead><tr><th>정규형</th><th>조건 (앞 단계 +)</th><th>없애는 것</th><th>도서 대여 예</th></tr></thead><tbody>
<tr><td>1NF</td><td>모든 값이 원자값</td><td>다중값·반복 그룹</td><td>연락처 “010…, 02…” → 두 줄</td></tr>
<tr><td>2NF</td><td>기본키에 완전 종속</td><td>부분 종속</td><td>도서(도서ID, 도서명) 분리</td></tr>
<tr><td>3NF</td><td>이행 종속 없음</td><td>비주요 속성끼리의 종속</td><td>회원(회원ID, 이름, 등급) 분리</td></tr>
<tr><td>BCNF</td><td>모든 결정자가 후보키</td><td>후보키 아닌 결정자</td><td>교수 → 과목 분리</td></tr>
<tr><td>4NF · 5NF</td><td>다치 종속 · 조인 종속 제거</td><td>(개요)</td><td>—</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 만능 장부</b> 종이 장부는 사람이 알아서 맞춰 읽지만, DBMS는 중복된 값이 서로 다르면 어느 것이 맞는지 모릅니다. 그래서 구조로 막아야 합니다.</div><div><b>대결의 한계</b> 비용 모형은 행 수만 셉니다. 실제로는 색인, 메모리 캐시, 잠금 경합(13주차)이 결과를 크게 바꿉니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 이상 현상 셋 — 삽입·갱신·삭제 ② 함수 종속으로 판정, 1NF→2NF(부분)→3NF(이행)→BCNF ③ 어디까지 쪼갤지는 접근 패턴이 정한다.'),
       ('asst','report','대결은 조건부였어요. 조회 위주면 반정규화, 변경 위주면 3NF가 덜 일했어요.'),
       ('fly','coffee','반정규화를 고르더라도, 그 중복을 누가 맞춰 줄지는 꼭 정해 둬.'),
       ('robo','calc','합쳐 두는 게 늘 이기는 건 아니구나. 등급 변경이 잦으면 20줄씩 고쳐야 하니까…')],
next_note='<p class="recap"><b>다음 회차 — 13주차 「트랜잭션 · 회복 · 병행 제어」:</b> ACID, COMMIT·ROLLBACK, 로그와 회복, 갱신 분실과 로킹 — 노션 DCL·TCL 실습.</p>',
gloss={'삽입 이상':('삽입 이상','개념','데이터를 넣을 때 원하지 않는 다른 데이터까지 함께 넣어야 하는 문제.','insertion-anomaly','lv1'),
 '갱신 이상':('갱신 이상','개념','중복된 데이터 중 일부만 수정되어 불일치가 생기는 문제.','update-anomaly','lv1'),
 '삭제 이상':('삭제 이상','개념','데이터를 지울 때 지우면 안 되는 다른 데이터까지 함께 사라지는 문제.','deletion-anomaly','lv1'),
 '결정자':('결정자','용어','함수 종속 X → Y에서 X. 값 하나가 Y의 값 하나를 결정한다.','determinant','lv2'),
 '부분 함수 종속':('부분 함수 종속','개념','기본키의 일부에만 종속되는 것. 2NF에서 제거.','partial-dependency','lv2'),
 '이행 함수 종속':('이행 함수 종속','개념','X → Y, Y → Z일 때 X → Z. 3NF에서 제거.','transitive-dependency','lv2'),
 '제1정규형':('제1정규형(1NF)','용어','모든 속성 값이 원자값인 정규형.','first-normal-form','lv3'),
 '제2정규형':('제2정규형(2NF)','용어','1NF이면서 부분 함수 종속이 없는 정규형.','second-normal-form','lv3'),
 'BCNF':('BCNF','용어','모든 결정자가 후보키인 정규형(보이스-코드 정규형).','bcnf','lv4'),
 '무손실 분해':('무손실 분해','개념','분해한 표들을 다시 조인하면 원래 표와 정확히 같아지는 분해.','lossless-decomposition','lv4'),
 '반정규화':('반정규화','개념','성능을 위해 정규화한 표를 일부러 합치거나 중복을 허용하는 것.','denormalization','lv4')},
facts=[('F01','정규화는 함수적 종속성에 기반해 테이블을 단계적으로 분해하는 과정이며, 중복 최소화와 무결성 보장이 목적','문헌 사실','ahn2025w04erd','lv2','「정규화의 개념과 필요성」'),
       ('F02','이상 현상: 삽입 이상(불필요한 정보도 입력 필요), 갱신 이상(일부만 변경되어 불일치), 삭제 이상(다른 정보까지 삭제)','문헌 사실','ahn2025w04erd','lv1','「정규화의 개념과 필요성」'),
       ('F03','과도한 정규화는 조인 연산 증가로 성능 저하 — 성능과 균형 고려, 조회 빈번 데이터는 반정규화 검토','문헌 사실','ahn2025w04erd','lv4','「정규화와 실무적 데이터베이스 설계 고려사항」'),
       ('F04','정규화 실습 1: 도서_대여_회원 비정규 표의 다중값 연락처를 원자값으로 분해(1NF) 후 부분 종속 제거(2NF)','문헌 사실','ahn2025w04erd','lv3','「정규화 실습 1」'),
       ('F05','정규화 실습 2: 도서대출정보(대출번호, 회원ID, 회원이름, 회원등급, 도서ID)의 이행 종속을 제거해 도서대출·회원으로 분리(3NF)','문헌 사실','ahn2025w04erd','lv4','「정규화 실습 2」')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='ahn2025w04erd',type='report',title='데이터베이스 설계 4주차 — ERD 작성, 관계 데이터 모델링, 정규화 과정 및 실무 적용',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025worst',type='webpage',title='데이터 베이스 설계 : worst case',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed810783e8ea080d594176',role='background')],
models=['도서 대여 비정규 표 (교안 정규화 실습 1의 예)','함수 종속 판정기의 데이터 (1NF 표 5줄)','3NF 실습 데이터 (교안 실습 2의 예)','대결 비용 모형 (설명용 예시값)'],
cover_alt='커다란 장부 한 장을 가위로 네 장의 깔끔한 표로 나누고, 실선으로 다시 이어 보이는 장면을 네 캐릭터가 지켜보는 표지 (대체 그림)',
prereq=['11'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var H=['대여번호','도서ID','도서명','회원ID','회원명','연락처','대여일'],RAW=__RAW__,T;
function rA(){T=JSON.parse(JSON.stringify(RAW));dA('비정규 통합 표 3줄. 버튼을 눌러 보세요.');}
function dA(m,cls){$('#an12').innerHTML=LAB.tableHTML(H,T,{cap:'도서_대여_회원 (한 표에 모두)',cls:cls});$('#an12o').innerHTML=m;}
$('#an12i').onclick=function(){dA('<b style="color:#c9302c">삽입 이상</b> — 새 책 B103 「SQL 첫걸음」을 넣으려면 대여번호가 있어야 합니다(대여번호는 키). 아직 아무도 빌리지 않았으니 넣을 줄이 없습니다. 억지로 넣으면 대여번호를 가짜로 만들어야 합니다.');};
$('#an12u').onclick=function(){T[0][5]='010-5555-0000, 02-123-4567';dA('<b style="color:#c9302c">갱신 이상</b> — 김철수의 번호를 첫 줄(L001)만 고쳤습니다. 이제 L002 줄과 번호가 다릅니다. 김철수의 진짜 번호는 무엇일까요?',function(r){return r[3]==='M201'?'bad':'';});};
$('#an12d').onclick=function(){T=T.filter(function(r){return r[0]!=='L003';});dA('<b style="color:#c9302c">삭제 이상</b> — L003 대여 기록을 지웠더니 이영희 회원(M202)의 정보가 표에서 완전히 사라졌습니다. 이영희는 탈퇴하지 않았는데도요.');};
$('#an12r').onclick=rA;rA();
/* 1NF 데이터 & FD */
var N1=[];RAW.forEach(function(r){r[5].split(', ').forEach(function(p){var x=r.slice();x[5]=p;N1.push(x);});});
['fdX','fdY'].forEach(function(id,k){$('#'+id).innerHTML=H.map(function(h,i){return '<option value="'+i+'"'+((k===0&&i===1)||(k===1&&i===2)?' selected':'')+'>'+h+'</option>';}).join('');});
$('#fd12t').innerHTML=LAB.tableHTML(H,N1,{cap:'1NF 표 (5줄) — 기본키 {대여번호, 연락처}'});
$('#fdgo').onclick=function(){var x=+$('#fdX').value,y=+$('#fdY').value,m={},bad=null;if(x===y){$('#fd12o').textContent='서로 다른 칸을 고르세요.';return;}
 N1.forEach(function(r){if(bad)return;var k=r[x];if(k in m&&m[k]!==r[y])bad=[k,m[k],r[y]];m[k]=r[y];});
 $('#fd12o').innerHTML=bad?('<b>'+H[x]+' → '+H[y]+' 아님</b> — 반례: '+H[x]+'가 같은 “'+bad[0]+'”인데 '+H[y]+'가 “'+bad[1]+'”와 “'+bad[2]+'”로 다릅니다.'):('<b>'+H[x]+' → '+H[y]+'</b> — 이 데이터에는 반례가 없습니다. (업무 규칙으로도 성립하는지는 따로 확인)'+({'1-2':' ✓ 업무 규칙: 같은 도서ID는 같은 책.','3-4':' ✓ 같은 회원ID는 같은 회원.','0-1':' ✓ 대여 한 건은 책 한 권.'}[x+'-'+y]||''));};
$('#fdgo').click();
/* 정규형 단계 */
var NF=[function(){return LAB.tableHTML(H,RAW,{cap:'비정규 — 연락처 칸에 값 여러 개',cls:function(r){return /,/.test(r[5])?'bad':'';}});},
 function(){return LAB.tableHTML(H,N1,{cap:'1NF — 원자값 (5줄, 중복은 그대로)'});},
 function(){var bk={},mb={};RAW.forEach(function(r){bk[r[1]]=r[2];mb[r[3]]=r[4];});
  return LAB.tableHTML(['도서ID','도서명'],Object.keys(bk).map(function(k){return [k,bk[k]];}),{cap:'도서',pk:[0]})+LAB.tableHTML(['회원ID','회원명'],Object.keys(mb).map(function(k){return [k,mb[k]];}),{cap:'회원',pk:[0]})+
   LAB.tableHTML(['회원ID','연락처'],[['M201','010-1234-5678'],['M201','02-123-4567'],['M202','010-9876-5432']],{cap:'회원연락처',pk:[0,1]})+LAB.tableHTML(['대여번호','도서ID','회원ID','대여일'],RAW.map(function(r){return [r[0],r[1],r[3],r[6]];}),{cap:'대여',pk:[0]});}];
var NFM=['한 칸에 번호가 둘 — 원자성 위반. “02로 시작하는 번호를 가진 회원”을 찾기 어렵습니다.','원자값이 되었지만 5줄로 늘었고 “데이터베이스 개론”·“김철수”가 여러 번 반복됩니다. 기본키 {대여번호, 연락처}의 일부(대여번호)에만 종속된 칸이 많습니다 — 부분 종속.','부분 종속을 없애 4개 표로 나눴습니다. 책 제목·회원 이름·번호가 각각 한 번씩만 저장됩니다. (밑줄 = 기본키)'];
$$('#lv3 [data-nf]').forEach(function(b){b.onclick=function(){var i=+b.dataset.nf;$$('#lv3 [data-nf]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});$('#nf12').innerHTML=NF[i]();$('#nf12o').innerHTML=NFM[i];};});
$$('#lv3 [data-nf]')[0].click();
/* 대결 */
var asm='A';
function cost(s){var q=s==='A'?50000:500,u=s==='A'?10:300;return [q*2+u*1,q*1+u*(20+1)];}
function t12(){var a=cost('A'),b=cost('B');$('#duel12t').innerHTML=LAB.tableHTML(['가정','3NF (초파리)','반정규화 (주판봇)'],[['A 조회 위주',a[0].toLocaleString(),a[1].toLocaleString()],['B 변경 위주',b[0].toLocaleString(),b[1].toLocaleString()]],{cls:function(r){return r[0][0]===asm?'hl':'dim';}});}
$('#asR').onclick=function(){asm='A';$('#asR').setAttribute('aria-pressed','true');$('#asW').setAttribute('aria-pressed','false');t12();};
$('#asW').onclick=function(){asm='B';$('#asW').setAttribute('aria-pressed','true');$('#asR').setAttribute('aria-pressed','false');t12();};t12();
PAGE.duel=function(){var a=cost('A'),b=cost('B'),c=asm==='A'?a:b;return {fly:c[0],robo:c[1],flyTxt:c[0].toLocaleString(),roboTxt:c[1].toLocaleString(),cond:true,a:a,b:b};};
'''.replace('__RAW__', str(RAW).replace("'", '"')),
labs='''lab12:{setup:"CREATE DATABASE lib; USE lib; CREATE TABLE 도서대출정보 (대출번호 VARCHAR(4) PRIMARY KEY, 회원ID VARCHAR(4), 회원이름 VARCHAR(10), 회원등급 VARCHAR(10), 도서ID VARCHAR(4)); INSERT INTO 도서대출정보 VALUES ('L001','M100','김철수','골드','B001'),('L002','M100','김철수','골드','B002');",
presets:[{t:"① 2NF 표 보기",q:"SELECT * FROM 도서대출정보;"},{t:"② 갱신 이상 — 한 줄만 실버로",q:"UPDATE 도서대출정보 SET 회원등급 = '실버' WHERE 대출번호 = 'L001';\\nSELECT 회원ID, 회원이름, 회원등급 FROM 도서대출정보;"},{t:"③ 3NF로 분해",q:"CREATE TABLE 회원 (회원ID VARCHAR(4) PRIMARY KEY, 회원이름 VARCHAR(10), 회원등급 VARCHAR(10));\\nINSERT INTO 회원 VALUES ('M100','김철수','골드'), ('M200','이영희','실버');\\nCREATE TABLE 도서대출 (대출번호 VARCHAR(4) PRIMARY KEY, 회원ID VARCHAR(4), 도서ID VARCHAR(4), FOREIGN KEY (회원ID) REFERENCES 회원(회원ID));\\nINSERT INTO 도서대출 VALUES ('L001','M100','B001'), ('L002','M100','B002');\\nSELECT * FROM 회원;\\nSELECT * FROM 도서대출;"},{t:"④ 무손실 확인 (JOIN)",q:"SELECT d.대출번호, d.회원ID, m.회원이름, m.회원등급, d.도서ID\\nFROM 도서대출 d JOIN 회원 m ON d.회원ID = m.회원ID;"},{t:"⑤ 등급 변경은 한 줄",q:"UPDATE 회원 SET 회원등급 = '실버' WHERE 회원ID = 'M100';\\nSELECT d.대출번호, m.회원이름, m.회원등급\\nFROM 도서대출 d JOIN 회원 m ON d.회원ID = m.회원ID;"},{t:"⑥ 대출 없는 회원도 저장됨",q:"SELECT * FROM 회원 WHERE 회원ID NOT IN (SELECT 회원ID FROM 도서대출);"}],
ready:"교안 정규화 실습 2의 2NF 표(도서대출정보 2줄)가 준비되어 있습니다. ①→②로 갱신 이상을 보고, 「처음 상태로」 후 ③부터."}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'불필요한 중복 때문에 삽입·갱신·삭제할 때 생기는 문제.','lv2':'속성 X의 값이 속성 Y의 값을 하나로 결정하는 관계(X → Y). 완전·부분·이행 종속.','lv3':'원자값만 갖는 1NF와, 부분 함수 종속을 제거한 2NF.','lv4':'이행 종속을 제거한 3NF와 모든 결정자가 후보키인 BCNF, 그리고 성능을 위한 반정규화.'}[s['id']]
