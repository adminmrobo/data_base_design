# 2주차 — 데이터와 데이터베이스 (교재 1장)
PAGE = dict(
num='02', slug='data_and_database', kind='lecture', short='2주', chip='02주차',
title='데이터와 데이터베이스', title_en='Data, information and the database',
subtitle='측정값이 판단이 되기까지, 그리고 데이터베이스의 네 조건',
toc='데이터와 정보의 차이, 데이터베이스의 정의(공유·통합·저장·운영)와 특징, 데이터의 분류',
kicker='데이터베이스 설계 · 2주차 · 교재 1장',
question='창고에 쌓을 것은 “데이터”일까, “정보”일까?',
desc='데이터베이스 설계 2주차: 데이터와 정보, 정보시스템, 데이터베이스의 정의와 네 가지 특징, 정형·반정형·비정형 데이터와 변수의 유형.',
intro='<p>편의점 점주는 “삼각김밥 12, 9, 15, 30…”이라는 숫자를 보고 “금요일엔 두 배로 들여놓자”고 결정합니다. 앞의 숫자는 <b>데이터</b>, 뒤의 판단 근거는 <b>정보</b>입니다. 이번 회차는 이 둘을 구분하고, 그 데이터를 담는 그릇이 “데이터베이스”라고 불리려면 무엇을 갖춰야 하는지 정합니다.</p>',
kpis=[('4조건','공유 · 통합 · 저장 · 운영'),('4특징','실시간 · 계속 변화 · 동시 공유 · 내용 참조'),('3형태','정형 · 반정형 · 비정형'),('4척도','명목 · 서열 · 등간 · 비율')],
hero_talk=[
 ('doc','front','데이터는 <b>재료</b>, 정보는 <b>요리</b>다. 오늘은 재료를 어떤 창고에 넣어야 하는지 정한다.'),
 ('asst','smile','그럼 창고에는 요리(정보)를 넣어 두면 더 편하지 않아요? 바로 꺼내 먹게요.'),
 ('fly','clip','오늘 대결이 바로 그 질문이야. 미리 요리해 두면 편하지만, 손님이 다른 메뉴를 시키면?'),
 ('robo','smile','나는 재료든 요리든 전부 다 쌓아 두는 쪽! 많을수록 든든하니까!')],
crew=[('doc','front','정의를 정리하고 판정'),('asst','smile','실제 예로 바꿔 묻기, 숫자 발표'),('fly','clip','정의의 빈틈 짚기'),('robo','smile','“다 저장하자”파')],
recap='1주차에서 데이터베이스를 “여러 사람이 함께 쓰려고 한 곳에 정리해 둔 데이터 모음”이라고 했습니다. 오늘은 이 문장을 <b>네 개의 조건</b>으로 쪼개 정확히 만듭니다.',
notion=[('02주차 : 데이터베이스 기본 개념', NOTION+'1ab17a4520ed81f181b5eb26af692a6a', '강의 영상과 자료 (노션 Schedule)'),
        ('실습 · 파이썬의 데이터 구조 (Colab)', 'https://colab.research.google.com/drive/1l6Aczs6mP6kRSdWzReN2-WMqnTll6iYt?usp=sharing', '리스트 · 배열 · 데이터프레임 — 교안 실습 링크'),
        ('실습 · 데이터프레임 사례 (Colab)', 'https://colab.research.google.com/drive/1Hseo56ZgstcHK8aUBIq06ssMAtGn4xGe?usp=sharing', '교안의 두 번째 파이썬 실습')],
why=[('설계의 첫 질문','무엇을 저장할지(데이터)와 무엇을 보여 줄지(정보)를 섞으면 표가 금세 꼬입니다.'),
     ('정의가 기준이 된다','공유·통합·저장·운영 네 조건은 3주차의 “파일 시스템은 왜 실패했나”를 판정하는 잣대입니다.'),
     ('분류가 도구를 고른다','표로 딱 떨어지는 데이터와 사진·글 같은 데이터는 담는 방법(관계형 DB, NoSQL)이 다릅니다 — 14주차.')],
bigpicture='<div class="flow"><span class="chip">관찰·측정</span><span class="arr">→</span><span class="chip">데이터</span><span class="arr">→</span><span class="chip">정보 처리</span><span class="arr">→</span><span class="chip">정보</span><span class="arr">→</span><span class="chip">의사 결정</span></div><p>교재(1장)의 정의: <b>데이터</b>는 현실에서 관찰하거나 측정해 수집한 값, <b>정보</b>는 데이터를 의사 결정에 유용하게 쓸 수 있도록 처리해 체계적으로 조직한 결과물, <b>정보 처리</b>는 데이터에서 정보를 추출하는 과정 또는 방법입니다.</p>',
steps=[
dict(id='lv1', short='데이터·정보', title='데이터와 정보 — 같은 숫자가 판단이 되는 순간', concept='데이터와 정보', en='data and information', cid='lab:concept/data-and-information',
 tag='현장: 편의점 발주', analogy='편의점 발주',
 situation='편의점 점주가 4주 동안의 삼각김밥 판매 개수를 받았습니다. 숫자 28개만으로는 아무것도 결정할 수 없습니다. 무엇을 해야 “내일 몇 개 주문할까”에 답이 될까요?',
 pair=(('현장에서는','하루하루의 판매 개수(28개 숫자)가 <b>데이터</b>입니다. 요일별로 묶어 평균을 내면 “금요일이 다른 날의 두 배”라는 <b>정보</b>가 됩니다. 점주는 그 정보로 발주량을 정합니다.'),
       ('데이터베이스에서는','데이터베이스는 원래의 판매 기록(데이터)을 저장하고, 질의로 그때그때 요일별 평균 같은 정보를 만들어 냅니다. 저장되는 것은 재료, 화면에 나오는 것은 요리입니다.')),
 panel='''<p style="margin-top:0">4주치 판매 데이터를 어떻게 처리하느냐에 따라 다른 정보가 나옵니다. 처리 방법을 골라 보세요.</p>
<div id="raw2"></div><div class="ctrl"><button type="button" class="bt" data-p="sum">총합</button><button type="button" class="bt" data-p="dow">요일별 평균</button><button type="button" class="bt" data-p="max">가장 많이 팔린 날</button><button type="button" class="bt" data-p="trend">주별 합계</button></div>
<div class="insight" id="info2">처리 버튼을 누르면 정보가 만들어집니다.</div>''',
 panel_title='직접 해 보기 — 같은 데이터, 다른 정보',
 sim='판매 데이터 처리기',
 flow=dict(id='fl2', title='측정값이 결정이 되기까지', h=230, alt='측정값 카드가 데이터, 정보 처리, 정보, 의사 결정 칸을 지나가며 바뀌는 애니메이션',
   cap='같은 카드가 칸을 지날 때마다 이름이 바뀝니다. 마지막 칸의 “결정”은 데이터베이스가 아니라 사람이 내립니다.',
   js='{stations:["측정","데이터","정보 처리","정보","의사 결정"],items:[["체온계 36.9","36.9","최근 3일 평균","평열 범위","등교 OK"],["판매 30개","금 30","금요일 평균","금=평일×2","금 발주 2배"],["강수 12mm","12","주간 누적","이번 주 많음","우산 진열"],["출석 27/30","27","결석률","10%","공지 발송"]],stamp:"설명용 모형"}'),
 explain='<p>① <b>데이터</b>는 해석하기 전의 값입니다(“30”). ② <b>정보 처리</b>는 묶고, 세고, 평균 내고, 비교하는 일입니다. ③ <b>정보</b>는 결정에 쓸 수 있는 형태입니다(“금요일은 평일의 두 배”). 같은 데이터에서도 질문이 바뀌면 다른 정보가 나옵니다.</p><p><b>손으로 한 번:</b> 금요일 판매가 30, 28, 32, 30이면 금요일 평균은 (30+28+32+30)÷4 = 30입니다. 위 실험의 「요일별 평균」과 같은 값이 나오는지 확인해 보세요.</p>',
 limit='데이터를 정보로 바꿔 주는 장치가 회사 안에 따로 있다면 그것은 무엇이고, 데이터베이스는 그 안에서 어떤 자리일까요?', limit_label='데이터·정보를 다루는 조직의 장치가 아직 없음',
 say=('asst','spark','처리 방법만 바꿨는데 정보가 네 개나 나왔어요. 그러니까 원래 숫자는 버리면 안 되겠네요!'),
 quiz=[dict(q='교재의 정의에 따를 때 “데이터”에 해당하는 것은?',o=['이번 주는 매출이 늘었다','어제 삼각김밥 판매량 30개','금요일에 발주를 늘리자','고객 만족도가 높다'],a=1,why='관찰·측정해 수집한 값 그 자체가 데이터입니다. “늘었다”, “높다”는 처리·해석을 거친 정보, “늘리자”는 결정입니다.'),
       dict(q='금요일 판매량이 30, 28, 32, 30개일 때 금요일 평균 판매량은? (계산)',o=['28','29','30','32'],a=2,why='(30+28+32+30)÷4 = 120÷4 = 30. 이렇게 데이터를 묶어 평균을 내는 것이 정보 처리입니다.')]),
dict(id='lv2', short='DB 정의', title='데이터베이스의 네 조건 — 공유 · 통합 · 저장 · 운영', concept='데이터베이스의 정의', en='definition of a database', cid='lab:concept/database-definition',
 tag='현장: 무엇이 DB인가', analogy='우리 주변의 데이터 모음',
 situation='휴대폰 사진첩, 학과 단톡방의 공지 모음, 학교 수강신청 시스템 — 셋 다 데이터를 모아 둔 곳입니다. 셋 다 “데이터베이스”라고 불러도 될까요?',
 pair=(('현장에서는','정보 시스템은 조직 운영에 필요한 데이터를 모아 두었다가 결정이 필요할 때 처리해 정보를 만드는 수단이고, 데이터베이스는 그 안에서 <b>데이터를 저장해 두는 자리</b>입니다(경영정보시스템·재고관리시스템 모두 같은 구조).'),
       ('정의로는','교재는 데이터베이스를 <b>특정 조직의 여러 사용자가 공유해 사용할 수 있도록 통합해서 저장한 운영 데이터의 집합</b>으로 봅니다. 공유·통합·저장·운영 네 조건을 모두 갖춰야 합니다.')),
 panel='''<p style="margin-top:0">사례를 고르고, 네 조건 중 갖춘 것을 눌러 보세요. 네 개를 모두 갖추면 데이터베이스입니다.</p>
<div class="chips" id="caseChips"></div>
<div class="chips" id="condChips"></div><div class="insight" id="condOut"></div>''',
 panel_title='직접 해 보기 — 네 조건 판정기',
 sim='데이터베이스 네 조건 판정',
 explain='<div class="tbl"><table><thead><tr><th>조건</th><th>뜻 (교안)</th><th>지키지 못하면</th></tr></thead><tbody><tr><td>공유 데이터</td><td>여러 사용자가 함께 소유하고 이용</td><td>개인 메모장 — 남이 못 씀</td></tr><tr><td>통합 데이터</td><td>중복을 최소화, 허용하더라도 통제 가능</td><td>부서별 엑셀 복사본 — 값이 갈라짐</td></tr><tr><td>저장 데이터</td><td>컴퓨터가 접근할 수 있는 매체에 저장</td><td>종이 장부 — 검색 불가</td></tr><tr><td>운영 데이터</td><td>조직의 업무에 쓰이며 지속적으로 유지·관리</td><td>한 번 쓰고 버린 설문 결과 파일</td></tr></tbody></table></div><p>“통합”은 중복을 <b>0으로</b> 만든다는 뜻이 아니라, 꼭 필요한 중복만 남기고 <b>통제할 수 있게</b> 한다는 뜻입니다. 이 차이는 12주차 정규화에서 다시 중요해집니다.</p>',
 aicheck='<p>“휴대폰 사진첩도 데이터베이스인가요?”를 AI에게 물으면 “예, 사진 데이터를 저장하니까요”라고 답하기도 합니다. 네 조건으로 따져 보세요. <b>공유(여러 사용자)와 운영(조직 업무)</b> 조건이 빠져 있다면, 교재 정의의 데이터베이스는 아닙니다. 다만 사진첩 앱 내부에는 사진 목록을 관리하는 작은 DB가 쓰일 수 있습니다 — 무엇을 “그 데이터베이스”로 보는지 범위를 먼저 정하는 것이 판단의 출발입니다.</p>',
 limit='무엇이 데이터베이스인지는 정했습니다. 그런데 데이터베이스는 실제로 “어떻게 굴러가는” 물건일까요? 특징을 직접 실행해 봅니다.', limit_label='정의만 있고 작동 방식(특징)은 아직 모름',
 say=('fly','point','통합은 “중복 0”이 아니라 “중복을 통제할 수 있다”야. 시험에 잘 나오는 함정이지.'),
 quiz=[dict(q='데이터베이스의 정의를 이루는 네 조건이 아닌 것은?',o=['공유 데이터','통합 데이터','암호화 데이터','운영 데이터'],a=2,why='교재의 네 조건은 공유·통합·저장·운영입니다. 암호화는 보안 기법이지 정의의 조건이 아닙니다.'),
       dict(q='“통합 데이터”의 뜻으로 가장 알맞은 것은?',o=['중복이 하나도 없는 데이터','중복을 최소화하고, 허용하는 중복은 통제할 수 있는 데이터','여러 파일을 하나로 압축한 데이터','모든 부서가 따로 가진 데이터'],a=1,why='중복을 최소화하되, 성능 등의 이유로 남긴 중복은 통제 가능해야 한다는 뜻입니다.')]),
dict(id='lv3', short='DB 특징', title='데이터베이스의 네 특징 — 직접 실행해 확인하기', concept='데이터베이스의 특징', en='characteristics of a database', cid='lab:concept/database-characteristics',
 tag='연구실: 실습실', analogy='도서관 대출 창구',
 situation='도서관 대출 시스템에서는 지금도 누군가 책을 빌리고(변화), 여러 창구가 동시에 같은 목록을 보며(공유), “제목에 ‘설계’가 들어간 책”을 즉시 찾습니다(내용 참조, 실시간). 이 네 가지를 SQL로 직접 해 봅니다.',
 pair=(('연구실에서는','실습실의 <code>book</code> 표는 위치(몇 번째 줄)를 몰라도 <b>내용</b>(제목, 저자)으로 찾을 수 있고, 줄을 넣고 빼도 표는 그대로 살아 있습니다.'),
       ('데이터베이스에서는','교재의 네 특징: <b>실시간 접근</b>(질의에 바로 응답), <b>계속 변화</b>(삽입·삭제·수정으로 늘 최신), <b>동시 공유</b>(여러 사용자가 동시에), <b>내용으로 참조</b>(주소가 아니라 값으로 찾기).')),
 panel='<div class="sqllab" id="lab2" data-lab="lab2"></div>',
 panel_title='SQL 실습실 — 네 특징 확인하기',
 sim='도서관 대출 테이블 실습',
 explain='<p><b>내용으로 참조</b>가 왜 중요할까요? 파일에서는 “3번째 줄”처럼 위치로 찾다가, 누가 한 줄을 지우면 3번째 줄이 다른 책이 됩니다. 데이터베이스는 <code>WHERE title LIKE \'%설계%\'</code>처럼 <b>값</b>으로 찾으므로 줄 순서가 바뀌어도 같은 책을 찾습니다. 「③ 계속 변화」를 실행한 뒤 「② 내용으로 찾기」를 다시 눌러 결과가 어떻게 바뀌는지 보세요.</p>',
 limit='이 표의 칸(제목, 저자, 대출 여부)은 모두 깔끔하게 정해져 있었습니다. 하지만 세상의 데이터가 모두 이렇게 칸에 딱 들어갈까요?', limit_label='표로 딱 떨어지는 데이터만 다룸',
 say=('robo','wow','줄을 지웠는데도 “설계” 책을 정확히 찾았어! 위치가 아니라 내용으로 찾으니까 안 헷갈리는구나.'),
 quiz=[dict(q='“데이터를 저장된 위치나 주소가 아니라 값(내용)으로 찾는다”는 데이터베이스의 어떤 특징인가요?',o=['실시간 접근','계속 변화','동시 공유','내용으로 참조'],a=3,why='내용에 의한 참조(content reference)입니다. SQL의 WHERE 조건이 그 예입니다.'),
       dict(q='대출·반납이 일어날 때마다 데이터가 삽입·삭제·수정되어 늘 최신 상태를 유지하는 특징은?',o=['계속 변화','동시 공유','실시간 접근','통합'],a=0,why='데이터베이스는 정적인 파일이 아니라 계속 변화(continuous evolution)하는 데이터 모음입니다.')]),
dict(id='lv4', short='데이터 분류', title='데이터의 분류 — 형태로 나누고, 특성으로 나누기', concept='데이터의 분류', en='classification of data', cid='lab:concept/data-classification',
 tag='현장: 결혼정보회사 회원 카드', analogy='회원 카드 정리',
 situation='결혼정보회사(교안 실습)의 회원 자료에는 나이·키 같은 숫자, 학력 같은 등급, 자기소개 글, 프로필 사진이 섞여 있습니다. 이걸 한 표에 다 넣을 수 있을까요? 평균을 낼 수 있는 칸은 어느 것일까요?',
 pair=(('현장에서는','숫자 칸(나이, 키)은 표에 바로 넣고 평균도 냅니다. 학력은 순서는 있지만 “간격”이 일정하지 않고, 자기소개 글과 사진은 칸에 넣기 어렵습니다.'),
       ('데이터 분류로는','형태에 따라 <b>정형</b>(정해진 구조) · <b>반정형</b>(구조 설명이 데이터 안에, 예: JSON·XML) · <b>비정형</b>(구조 없음, 예: 글·사진). 특성에 따라 <b>범주형</b>(명목·서열)과 <b>수치형</b>(등간·비율, 이산·연속)으로 나눕니다.')),
 panel='''<p style="margin-top:0">카드를 눌러 맞는 칸으로 보내 보세요. 한 번 더 누르면 다음 칸으로 갑니다.</p>
<div class="ctrl"><button type="button" class="bt" id="clsF" aria-pressed="true">형태로 나누기</button><button type="button" class="bt" id="clsS" aria-pressed="false">척도로 나누기</button><button type="button" class="bt primary" id="clsChk">채점</button></div>
<div class="chips" id="clsCards"></div><div class="bucket" id="clsB"></div><div class="insight" id="clsOut">카드를 칸에 모두 넣고 「채점」을 누르세요.</div>''',
 panel_title='직접 해 보기 — 데이터 분류 카드',
 sim='데이터 분류 카드 맞히기',
 explain='<div class="tbl"><table><thead><tr><th>척도</th><th>할 수 있는 일</th><th>예 (교안)</th></tr></thead><tbody><tr><td>명목</td><td>같다/다르다 구분만</td><td>성별, 혈액형</td></tr><tr><td>서열</td><td>순서 비교 (간격은 모름)</td><td>학력, 만족도, 선호도</td></tr><tr><td>등간</td><td>순서 + 간격이 같음, 절대 0 없음</td><td>섭씨온도 (100도가 50도의 “2배 뜨겁다”고 말할 수 없음)</td></tr><tr><td>비율</td><td>순서 + 간격 + 비율 계산 가능</td><td>나이, 무게, 거리, 시간</td></tr></tbody></table></div><p>수치형은 다시 <b>이산형</b>(점수, 빈도처럼 셀 수 있는 값)과 <b>연속형</b>(키, 몸무게, 수익률처럼 사이 값이 무수히 있는 값)으로 나눕니다. 이 구분은 테이블의 열 자료형(INT, DECIMAL, VARCHAR)을 고를 때 그대로 쓰입니다.</p>',
 aicheck='<p>AI가 만든 분석표에 “평균 만족도 3.7”이 나왔다면 한 번 멈추세요. 만족도(1~5점)는 서열 척도라 간격이 같다는 보장이 없어, 평균은 <b>참고값</b>일 뿐입니다. 서열 자료에서는 중앙값이나 “4점 이상 비율”을 함께 보는 것이 안전합니다.</p>',
 limit='데이터를 담을 그릇의 조건(네 조건)과 데이터의 종류는 알았습니다. 그렇다면 데이터베이스가 나오기 전, 사람들은 이 데이터를 무엇에 담았고 왜 실패했을까요? — 3주차.', limit_label='데이터베이스 이전의 관리 방식(파일 시스템)을 아직 모름',
 quiz=[dict(q='JSON처럼 데이터 안에 구조(키 이름)에 대한 설명이 함께 들어 있는 데이터는?',o=['정형 데이터','반정형 데이터','비정형 데이터','메타 데이터만 있는 데이터'],a=1,why='반정형 데이터는 정해진 표 구조는 아니지만, 데이터 안에 구조를 설명하는 정보(키·태그)가 들어 있습니다.'),
       dict(q='섭씨온도가 “등간 척도”인 이유로 알맞은 것은?',o=['순서가 없어서','0도가 “온도가 없음”을 뜻하지 않아 비율 비교가 의미 없어서','셀 수 있는 값이라서','글자로 된 값이라서'],a=1,why='섭씨 0도는 임의로 정한 기준점이라 절대 영점이 아닙니다. 그래서 100도가 50도의 2배 뜨겁다고 말할 수 없습니다.')]),
],
duel=dict(q='창고에 무엇을 넣을까 — 요리(정보) vs 재료(데이터)',
 intro='4주 판매 기록을 저장할 공간이 있습니다. 초파리는 “매달 평균 하나만 저장하면 깔끔하다”, 주판봇은 “28일치 원자료를 전부 저장하자”고 합니다. 다음 달 점주가 던진 다섯 질문에 몇 개나 답할 수 있을까요?',
 fly_pick='월평균 하나만 저장 (요리만)', fly_line='평균 하나면 충분해. 저장 공간도 아끼고 깔끔하잖아.',
 robo_pick='28일치 원자료를 모두 저장 (재료 전부)', robo_line='나중에 무슨 질문이 올지 모르잖아? 다 넣어 두면 다 대답할 수 있어!',
 metric='다섯 질문 중 답할 수 있는 질문 수', step=0,
 after='<div class="tbl" id="duelQ"></div>',
 run='return PAGE.duel();',
 announce='return "다섯 질문 중 초파리 창고는 <b>"+r.fly+"개</b>, 주판봇 창고는 <b>"+r.robo+"개</b>에 답했어요. 평균만 남긴 창고는 「요일별」 「최고 판매일」 같은 새 질문에 답할 재료가 없었어요.";',
 verdict='return "정보는 질문마다 다시 만들어진다. 그래서 창고에는 <b>원자료(데이터)</b>를 넣는다. 주판봇 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>칸</th><th>핵심</th><th>시험에 나오는 형태</th></tr></thead><tbody>
<tr><td>1 데이터·정보</td><td>데이터 = 측정값, 정보 = 결정에 쓰게 처리한 결과, 정보 처리 = 그 과정</td><td>사례를 주고 데이터/정보 고르기</td></tr>
<tr><td>2 정의</td><td>공유 · 통합 · 저장 · 운영 데이터의 집합</td><td>네 조건이 아닌 것 고르기, “통합”의 뜻</td></tr>
<tr><td>3 특징</td><td>실시간 접근 · 계속 변화 · 동시 공유 · 내용으로 참조</td><td>설명에 맞는 특징 이름</td></tr>
<tr><td>4 분류</td><td>정형·반정형·비정형 / 명목·서열·등간·비율 / 이산·연속</td><td>예시 데이터 분류하기</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 재료와 요리</b> 정보가 늘 “완성된 요리”는 아닙니다. 어떤 사람에게는 정보인 것이 다른 처리의 입력(데이터)이 되기도 합니다.</div><div><b>대결의 한계</b> 원자료를 전부 저장하는 데에도 비용(공간·개인정보 보호)이 듭니다. “무엇을 얼마나 오래 보관할지”도 설계의 일부입니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 창고에는 데이터, 화면에는 정보 ② 데이터베이스 = 공유·통합·저장·운영 ③ 데이터 종류가 담는 방법을 정한다.'),
       ('robo','happy','재료를 다 넣어 두길 잘했지! 다섯 질문에 다 대답했어!'),
       ('fly','coffee','인정. 다만 “다 넣자”가 “아무렇게나 넣자”는 아니야. 그건 다음 주에 파일 시스템이 보여 줄 거야.'),
       ('asst','proud','저는 결혼정보회사 표를 척도별로 다시 정리해 볼게요. 평균 내면 안 되는 칸에 표시하면서요!')],
next_note='<p class="recap"><b>다음 회차 — 3주차 「데이터베이스 관리 시스템」:</b> 파일로 관리하던 시절의 다섯 가지 문제와 DBMS의 등장.</p>',
gloss={'정보 처리':('정보 처리','개념','데이터에서 정보를 추출하는 과정 또는 방법.','information-processing','lv1'),
 '정보 시스템':('정보 시스템','개념','조직 운영에 필요한 데이터를 모아 두었다가 결정이 필요할 때 처리해 유용한 정보를 만들어 주는 수단.','information-system','lv2'),
 '통합 데이터':('통합 데이터','개념','중복을 최소화하고, 허용한 중복은 통제할 수 있게 저장한 데이터.','integrated-data','lv2'),
 '운영 데이터':('운영 데이터','개념','조직의 업무를 위해 지속적으로 유지·관리되는 데이터.','operational-data','lv2'),
 '내용으로 참조':('내용에 의한 참조','개념','주소나 위치가 아니라 데이터의 값으로 찾는 데이터베이스의 특징.','content-reference','lv3'),
 '반정형':('반정형 데이터','개념','구조에 따라 저장되지만 구조 설명이 데이터 안에 함께 있는 데이터(JSON, XML).','semi-structured-data','lv4'),
 '비정형':('비정형 데이터','개념','정해진 구조 없이 저장된 데이터(글, 사진, 음성).','unstructured-data','lv4'),
 '서열':('서열 척도','용어','순서는 있지만 간격이 같다고 볼 수 없는 범주형 척도(학력, 만족도).','ordinal-scale','lv4'),
 '등간':('등간 척도','용어','순서와 같은 간격은 있지만 절대 영점이 없는 수치형 척도(섭씨온도).','interval-scale','lv4'),
 '연속형':('연속형 변수','용어','키·몸무게처럼 두 값 사이에 무수히 많은 값이 있을 수 있는 변수.','continuous-variable','lv4')},
facts=[('F01','데이터는 현실에서 관찰·측정해 수집한 값, 정보는 의사 결정에 유용하게 처리해 조직한 결과물','문헌 사실','kim3ed','lv1','1장 (교안 20쪽 인용)'),
       ('F02','정보 처리는 데이터에서 정보를 추출하는 과정 또는 방법','문헌 사실','kim3ed','lv1','1장 (교안 21쪽 인용)'),
       ('F03','데이터베이스는 공유·통합·저장·운영 데이터의 성격을 가진다','문헌 사실','kim3ed','lv2','1장 (교안 23쪽 인용)'),
       ('F04','데이터베이스의 특징: 실시간 접근, 계속 변화, 동시 공유, 내용으로 참조','문헌 사실','kim3ed','lv3','1장 (교안 24쪽 인용)'),
       ('F05','형태에 따라 정형·반정형·비정형으로 분류','문헌 사실','ahn2025w02','lv4','2주차 교안')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='출판 연도 미확인'),
      dict(id='ahn2025w02',type='report',title='데이터베이스설계 2주차 강의 교안: 데이터와 데이터베이스',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='primary'),
      dict(id='ahn2025syllabus',type='webpage',title='데이터베이스설계 (2025년 2학기) 강의 개요',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'2025-2-1ab17a4520ed81cd9040dbae826a48ad',role='background')],
models=['4주 판매 데이터 (설명용 예시값, 고정 값)','네 조건 판정 사례의 정답 (교재 정의에 따른 해석)','도서관 book 테이블 (예시 데이터)','결혼정보회사 회원 카드 분류 예 (교안 실습 주제를 바탕으로 만든 예시)'],
cover_alt='연구실 탁자 위 숫자 카드 더미가 그래프와 결정 메모로 바뀌어 가는 장면을 네 캐릭터가 지켜보는 표지 (대체 그림)',
cover_svg='<svg width="300" height="140" viewBox="0 0 300 140"><g font-family="monospace" font-size="13" fill="#5b6874">'+''.join('<rect x="%d" y="%d" width="34" height="22" rx="4" fill="#fff" stroke="#9aa5b1"/><text x="%d" y="%d">%s</text>'%(10+(i%4)*38,20+(i//4)*28,16+(i%4)*38,35+(i//4)*28,v) for i,v in enumerate(['12','9','15','30','11','10','14','28','13','8','16','32']))+'</g><path d="M170 70 h30" stroke="#9aa5b1" stroke-width="2" marker-end="url(#a)"/><defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8z" fill="#9aa5b1"/></marker></defs><g fill="#13733a">'+''.join('<rect x="%d" y="%d" width="12" height="%d"/>'%(210+i*14,110-h,h) for i,h in enumerate([30,22,34,70,28]))+'</g></svg>',
prereq=['01'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var DAYS=['월','화','수','목','금','토','일'];
var S=[12,9,15,11,30,22,8, 11,10,14,12,28,20,9, 13,8,16,10,32,24,7, 12,11,15,13,30,21,10];
$('#raw2').innerHTML=LAB.tableHTML(['주'].concat(DAYS),[0,1,2,3].map(function(w){return [(w+1)+'주'].concat(S.slice(w*7,w*7+7));}),{cap:'삼각김밥 판매 개수 (예시값, 4주 × 7일)'});
$$('#lv1 [data-p]').forEach(function(b){b.onclick=function(){$$('#lv1 [data-p]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});var p=b.dataset.p,t;
 if(p==='sum'){t='4주 총 판매량은 <b>'+S.reduce(function(a,b){return a+b;},0)+'개</b> → “한 달에 약 420개 팔린다”';}
 if(p==='dow'){t=DAYS.map(function(d,i){var v=(S[i]+S[i+7]+S[i+14]+S[i+21])/4;return d+' '+v.toFixed(1);}).join(' · ')+' → <b>금요일이 평일의 약 2.5배</b>';}
 if(p==='max'){var m=Math.max.apply(0,S),i=S.indexOf(m);t='가장 많이 팔린 날: <b>'+(Math.floor(i/7)+1)+'주 '+DAYS[i%7]+'요일 '+m+'개</b> → “3주 금요일에 무슨 일이 있었나?”라는 새 질문';}
 if(p==='trend'){t=[0,1,2,3].map(function(w){return (w+1)+'주 '+S.slice(w*7,w*7+7).reduce(function(a,b){return a+b;},0);}).join(' · ')+' → <b>주마다 거의 같다</b> (큰 추세 없음)';}
 $('#info2').innerHTML=t;};});
/* 네 조건 판정 */
var CASES=[['학교 수강신청 시스템',[1,1,1,1],'여러 학생·교직원이 함께, 중복 없이, 서버에, 매 학기 운영 — 네 조건을 모두 갖춥니다.'],['내 휴대폰 사진첩',[0,0,1,0],'나 혼자 쓰고(공유×), 조직 업무용이 아니므로(운영×) 교재 정의의 데이터베이스는 아닙니다.'],['부서별로 따로 쓰는 고객 엑셀',[1,0,1,1],'함께 쓰고 업무에도 쓰지만, 같은 고객이 부서마다 따로 있어 통합 조건이 깨집니다.'],['동아리 종이 출석부',[1,1,0,1],'컴퓨터가 접근할 수 없는 종이라 저장 데이터 조건이 빠집니다.'],['한 번 쓰고 버린 설문 결과 파일',[1,1,1,0],'지속적으로 유지·관리되는 운영 데이터가 아닙니다.']];
var CN=['공유','통합','저장','운영'],cur=0,pick=[0,0,0,0];
var cc=$('#caseChips'),cd=$('#condChips');
CASES.forEach(function(c,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=c[0];b.onclick=function(){cur=i;pick=[0,0,0,0];[].forEach.call(cc.children,function(x){x.setAttribute('aria-pressed',x===b);});drawC();};cc.appendChild(b);});
CN.forEach(function(n,i){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=n+' 데이터';b.onclick=function(){pick[i]=1-pick[i];drawC();};cd.appendChild(b);});
function drawC(){[].forEach.call(cd.children,function(b,i){b.setAttribute('aria-pressed',!!pick[i]);});var c=CASES[cur],ok=c[1].every(function(v,i){return v===pick[i];});
 $('#condOut').innerHTML='<b>'+c[0]+'</b> — 내가 고른 조건 '+pick.reduce(function(a,b){return a+b;},0)+'개 · '+(ok?'<span class="pill ok">교재 해석과 같음</span> '+c[2]:'<span class="pill">아직 다름</span> 네 조건을 하나씩 따져 보세요.');}
cc.children[0].click();
/* 분류 카드 */
var CARDS2=[['나이 (34)','정형','비율'],['키 (172.5cm)','정형','비율'],['학력 (학사·석사·박사)','정형','서열'],['혈액형','정형','명목'],['선호 지역 (서울·부산…)','정형','명목'],['만족도 (1~5점)','정형','서열'],['섭씨 체온','정형','등간'],['자기소개 글','비정형','명목'],['프로필 사진','비정형','명목'],['앱이 보낸 JSON {"취미":["등산"]}','반정형','명목']];
var mode='F',where={};
function bins(){return mode==='F'?['정형','반정형','비정형']:['명목','서열','등간','비율'];}
function drawB(){var bs=bins();$('#clsB').innerHTML=bs.map(function(b){return '<div><b>'+b+'</b>'+CARDS2.map(function(c,i){return where[i]===b?'<span class="pill" data-i="'+i+'">'+c[0]+'</span>':'';}).join('')+'</div>';}).join('');
 $('#clsCards').innerHTML=CARDS2.map(function(c,i){return where[i]?'':'<button type="button" class="bt" data-i="'+i+'">'+c[0]+'</button>';}).join('');
 $$('#clsCards button,#clsB .pill').forEach(function(e){e.style.cursor='pointer';e.onclick=function(){var i=+e.dataset.i,bs=bins(),k=bs.indexOf(where[i]);where[i]=k<0?bs[0]:(k+1<bs.length?bs[k+1]:undefined);drawB();};});
 if(mode==='S')$('#clsB').insertAdjacentHTML('afterend','');}
$('#clsF').onclick=function(){mode='F';where={};$('#clsF').setAttribute('aria-pressed','true');$('#clsS').setAttribute('aria-pressed','false');drawB();};
$('#clsS').onclick=function(){mode='S';where={};$('#clsS').setAttribute('aria-pressed','true');$('#clsF').setAttribute('aria-pressed','false');drawB();};
$('#clsChk').onclick=function(){var k=mode==='F'?1:2,ok=0,n=0,wrong=[];CARDS2.forEach(function(c,i){if(where[i]){n++;if(where[i]===c[k])ok++;else wrong.push(c[0]+' → '+c[k]);}});
 $('#clsOut').innerHTML='넣은 카드 '+n+'/'+CARDS2.length+' · 맞힘 <b>'+ok+'</b>'+(wrong.length?'<br>다시 볼 것: '+wrong.join(' · '):(n===CARDS2.length?' — 모두 맞았습니다!':''))+(mode==='S'?'<br><span style="font-size:13px">자기소개 글·사진처럼 수치가 아닌 자료는 여기서 “명목”으로 두었습니다(범주를 구분할 뿐).</span>':'');};
drawB();
/* 대결 */
var QS=[['지난달 하루 평균 판매량은?','avg'],['요일별 평균은?','raw'],['가장 많이 팔린 날은?','raw'],['3주차 합계는?','raw'],['판매가 0인 날이 있었나?','raw']];
PAGE.duel=function(){var f=QS.filter(function(q){return q[1]==='avg';}).length,r=QS.length;
 document.getElementById('duelQ').innerHTML=LAB.tableHTML(['점주의 질문','월평균만 저장','원자료 저장'],QS.map(function(q){return [q[0],q[1]==='avg'?'답함 ('+(S.reduce(function(a,b){return a+b;},0)/28).toFixed(1)+'개)':'답 못 함','답함'];}));
 return {fly:f,robo:r,flyTxt:f+'/5',roboTxt:r+'/5'};};
''',
labs='''lab2:{setup:"CREATE DATABASE library; USE library; CREATE TABLE book (book_id INT PRIMARY KEY, title VARCHAR(60), author VARCHAR(30), on_loan VARCHAR(3)); INSERT INTO book VALUES (1,'데이터베이스 설계 입문','김연희','no'),(2,'파이썬 첫걸음','이수진','yes'),(3,'관계형 모델 이야기','박정훈','no'),(4,'SQL 설계 패턴','최민아','yes'),(5,'통계와 데이터','정다은','no');",
presets:[{t:"① 실시간 접근 — 전부 보기",q:"SELECT * FROM book;"},{t:"② 내용으로 찾기",q:"SELECT book_id, title FROM book\\nWHERE title LIKE '%설계%';"},{t:"③ 계속 변화 — 대출·반납·새 책",q:"UPDATE book SET on_loan = 'yes' WHERE book_id = 1;\\nDELETE FROM book WHERE book_id = 3;\\nINSERT INTO book VALUES (6, '설계 실무 노트', '한서윤', 'no');\\nSELECT * FROM book;"},{t:"④ 동시 공유 — 창구별 질문",q:"-- 대출 창구: 빌릴 수 있는 책\\nSELECT title FROM book WHERE on_loan = 'no';\\n-- 사서 창구: 대출 중인 권수\\nSELECT COUNT(*) AS 대출중 FROM book WHERE on_loan = 'yes';"}],ready:"도서관 library 데이터베이스와 book 테이블(5권)이 준비되어 있습니다. ①부터 눌러 보세요."}''',
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'데이터는 관찰·측정한 값, 정보는 그 데이터를 결정에 쓰도록 처리해 조직한 결과.','lv2':'특정 조직의 여러 사용자가 공유하도록 통합해 저장한 운영 데이터의 집합.','lv3':'실시간 접근, 계속 변화, 동시 공유, 내용으로 참조라는 데이터베이스의 네 가지 성질.','lv4':'형태(정형·반정형·비정형)와 특성(명목·서열·등간·비율, 이산·연속)에 따른 데이터 구분.'}[s['id']]
