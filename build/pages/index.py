# 목차(첫 화면)
IDX['desc'] = '데이터베이스 설계 15회차 연구실 해설 — 1~7주 이론, 8주 중간 REVIEW, 9~14주 SQL·설계·정규화·트랜잭션·응용, 15주 기말 REVIEW. SQL 실습은 노션 실습 페이지와 페이지 안 SQL 실습실로.'
IDX['cover_alt'] = '하얀 연구실 복도에 열다섯 개의 문이 줄지어 있고, 네 캐릭터가 첫 문 앞에 모인 표지 (대체 그림)'
IDX['body'] = '''
<header class="hero"><div class="wrap">
<div class="kicker">강남대학교 · 데이터베이스 설계 · 2025-2학기 강의안을 연구실 해설로</div>
<h1>데이터베이스 설계 연구실<br><span style="font-size:.5em;color:#5b6874">15회차 — 데이터 한 줄에서 설계·SQL·트랜잭션까지</span></h1>
<p class="question">“표를 어떻게 나눠 담아야, 틀리지 않고 빨리 꺼낼 수 있을까?”</p>
<p>교안(PDF)과 노션 강의 페이지를 바탕으로, 박사·조수 하루·초파리 연구원·주판봇이 한 회차씩 진행하는 해설 페이지입니다. 회차마다 <b>직접 눌러 보는 실험</b>, <b>페이지 안에서 바로 실행되는 SQL 실습실</b>, 확인 퀴즈, 대결, 그리고 회차 마지막의 <b>실전 연습장</b>(배운 것을 직접 돌려 보는 동작 대시보드)과 지식 색인이 들어 있습니다. SQL 실습은 강의 노션의 실습 페이지를 그대로 따라가고, 같은 예제를 이 페이지에서도 실행해 볼 수 있습니다.</p>
<section class="kpis"><div><b>15</b><span>회차 (본강의 13 + 리뷰 2)</span></div><div><b>11장</b><span>교재 『데이터베이스 개론』 3판 범위</span></div><div><b>7</b><span>노션 SQL 실습 페이지 연결</span></div><div><b>0줄</b><span>설치 없이 시작 (실습실 내장)</span></div></section>
<div class="talk">''' + say('doc', 'front', '한 주에 한 문, 열다섯 개의 문을 지난다. 8번과 15번 문은 <b>복습실</b>이다.') + say('asst', 'smile', '저는 1번 문부터 차례로 갈게요. 각 페이지 끝의 퀴즈로 제가 어디까지 왔는지 확인할 수 있어요.') + '''</div>
</div></header>
<section class="level" id="course"><div class="wrap"><h2>강좌 안내</h2>
<p>데이터베이스의 개념을 이해하고 구조·설계 등 다양한 특징을 배웁니다. 이를 근거로 설계에 필요한 모델을 익히고, 데이터베이스 도구(MariaDB 등)를 직접 실습합니다.</p>
<div class="steps"><div><span class="n">1</span><b>개념과 구조</b>데이터베이스의 개념과 특징, 데이터베이스 구조를 배웁니다.</div><div><span class="n">2</span><b>설계</b>데이터베이스 설계를 배우고, 실습으로 체계적으로 익힙니다.</div><div><span class="n">3</span><b>명령어 활용</b>데이터베이스 활용을 위한 명령어(SQL)를 씁니다.</div></div>
<div class="tbl"><table><thead><tr><th>항목</th><th>내용 (2025-2학기 강의 개요 기준)</th></tr></thead><tbody>
<tr><td>담당</td><td>안상선 (외래강사, (주)M-Robo 대표) · logix44@hanmail.net / sangsun.ahn@gmail.com</td></tr>
<tr><td>선수 과목 · 과제</td><td>선수 과목 없음 · 모든 과제는 개인 과제(팀 과제 없음)</td></tr>
<tr><td>교재</td><td>김연희, 『데이터베이스 개론』(3판), 한빛아카데미</td></tr>
<tr><td>평가</td><td>출석 10% · 중간고사 40% · 기말고사 40% · 과제 10%, 상대평가 (장기 결석 시 F 있음)</td></tr>
<tr><td>시험</td><td>강의에서 다룬 주요 개념·사례의 객관식·단답식, 대면 원칙 · 시험일은 학사 일정에 따라 바뀔 수 있음</td></tr></tbody></table></div>
<div class="notion"><span class="nb">N</span><a href="''' + NOTION + '''2025-2-1ab17a4520ed81cd9040dbae826a48ad" target="_blank" rel="noopener">데이터베이스설계 (2025년 2학기) — 노션 강의 개요 ↗</a><span>주차별 진도(Schedule), 학습교재, 성적평가 원본</span></div>
<p style="font-size:14px;color:#5b6874">주차 번호 안내: 노션 일정표는 “10주차 정규화 · 12주차 회복과 병행제어 · 13주차 응용기술”처럼 번호가 이 사이트와 다릅니다. 이 사이트는 교재 순서대로 9·10주 SQL → 11주 설계 → 12주 정규화 → 13주 트랜잭션 → 14주 응용 → 15주 기말 REVIEW로 다시 배열했고, 각 회차의 N 상자에 해당 노션 페이지를 이어 두었습니다. 시험 날짜와 범위는 강의 공지를 따릅니다.</p>
</div></section>
<section class="level" id="toc"><div class="wrap"><h2>15회차</h2><p>초록 카드는 리뷰 회차입니다. 각 회차는 따로 읽어도 되도록 만들었고, 페이지 맨 위 “30초 복습”이 앞 회차를 이어 줍니다.</p>
{{TOC}}</div></section>
<section class="level" id="how"><div class="wrap"><h2>공부하는 법</h2>
<div class="steps"><div><span class="n">1</span><b>상황부터</b>칸마다 “상황” 한 문단이 먼저 나옵니다. 정의보다 장면을 먼저 떠올리세요.</div><div><span class="n">2</span><b>손으로 한 번</b>작은 표로 결과를 먼저 짐작한 뒤 실습실에서 실행해 확인합니다.</div><div><span class="n">3</span><b>AI 결과 의심하기</b>“AI·도구 결과 판단 코너”에서 그럴듯하지만 틀린 답을 골라내는 연습을 합니다.</div><div><span class="n">4</span><b>퀴즈와 대결</b>퀴즈는 시험 형식(객관식·단답식)과 같은 결로 만들었습니다.</div><div><span class="n">5</span><b>실전 연습장</b>회차 맨 끝의 대시보드에서 값을 바꿔 돌려 보고, 미션 체크리스트를 채웁니다. 13~15주에는 두 세션 거래 재현기, 문서 질의 실습, SQL 자동 채점이 더해졌습니다.</div></div>
''' + say('fly', 'point', '막히면 그 칸의 “풀어서 보면” 상자부터 다시 읽어. 막히는 건 실력이 아니라 순서 문제인 경우가 많아.') + '''
</div></section>
<section class="level" id="tools"><div class="wrap"><h2>실습 도구</h2>
<div class="tbl"><table><thead><tr><th>도구</th><th>쓰는 곳</th><th>준비</th></tr></thead><tbody>
<tr><td>페이지 안 SQL 실습실</td><td>모든 SQL 예제 (설치 없이)</td><td>없음 — 브라우저만</td></tr>
<tr><td>MariaDB (3306)</td><td>9·10·12·13주 실습을 실제 서버에서</td><td><a href="https://adminmrobo.github.io/how_to_start_db/" target="_blank" rel="noopener">DB 환경 설치 해설</a></td></tr>
<tr><td>PostgreSQL (5432) · Orange</td><td>비교 실습, 데이터 분류·응용</td><td>같은 설치 해설의 미션 2·3</td></tr>
<tr><td>노션 실습 페이지</td><td>SQL 기본 문법 · 교재 예제 수정 · 연산(JOIN) · DCL/TCL</td><td>각 회차 페이지의 N 표시 링크</td></tr></tbody></table></div>
</div></section>
<section class="level" id="archive"><div class="wrap"><h2>보관함 — 이전 판</h2>
<p>이 저장소는 이전의 「데이터베이스 설계 — 야간 연구실」(1~4주, 저장소 database_01of04)을 흡수했습니다. 이전 판은 더 이상 고치지 않으며, 기록용으로 <a href="archive/database_01of04/index.html">archive/database_01of04/</a>에 그대로 보관합니다. 새 판의 1~5주차가 그 내용을 이어받아 다시 썼습니다.</p>
</div></section>
<footer><div class="wrap"><p>글 · 안상선 ((주)M-Robo 대표) · 시리즈 「데이터베이스 설계 연구실」 · 라이선스 CC BY-NC 4.0 · <a href="https://github.com/adminmrobo/data_base_design">저장소</a></p>
<p>교재 참고: 김연희, 『데이터베이스 개론』(3판). 캐릭터 그림: 연구실 캐릭터 팩(fruitfly-lab-expressions).</p></div></footer>'''
