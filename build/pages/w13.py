# 13주차 — 트랜잭션 · 회복 · 병행 제어 (교재 10장)
STU = ("CREATE DATABASE school; USE school; CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(50), student_id VARCHAR(10), grade INT, major VARCHAR(50), email VARCHAR(100)); "
 "INSERT INTO students VALUES (1,'김영희','2022001',2,'컴퓨터공학과','younghee.kim@example.com'),(2,'이철수','2021002',3,'전자공학과','chulsu.lee@example.com'),(3,'박민지','2023003',1,'경영학과','minji.park@example.com'),(4,'최지훈','2022004',2,'기계공학과','jihoon.choi@example.com'),(5,'강서연','2021005',3,'화학공학과','seoyeon.kang@example.com'); "
 "CREATE TABLE 계좌 (계좌번호 CHAR(3) PRIMARY KEY, 예금주 VARCHAR(10), 잔액 INT CHECK (잔액 >= 0)); INSERT INTO 계좌 VALUES ('A01','정소화',100000),('B01','김선우',50000);")
PAGE = dict(
num='13', slug='transaction_recovery_concurrency', kind='lecture', short='13주', chip='13주차',
title='트랜잭션 · 회복 · 병행 제어', title_en='Transactions, recovery and concurrency control',
subtitle='반쯤 끝난 송금, 갑자기 꺼진 서버, 동시에 누른 입금 버튼 — DBMS는 어떻게 지키나',
toc='트랜잭션과 ACID, COMMIT·ROLLBACK(노션 TCL·DCL), 로그 기반 회복(REDO·UNDO·검사 시점), 갱신 분실과 로킹·2단계 로킹, 교착 상태',
kicker='데이터베이스 설계 · 13주차 · 교재 10장',
question='송금 도중 서버가 꺼지면, 내 돈은 어디에 있을까?',
desc='데이터베이스 설계 13주차: 트랜잭션의 ACID 특성, COMMIT과 ROLLBACK, 장애 유형과 로그 기반 회복(REDO·UNDO, 검사 시점), 병행 수행 문제(갱신 분실·모순성·연쇄 복귀), 로킹과 2단계 로킹 규약, 교착 상태. 노션 SQL 문법 정리(DCL, TCL) 실습.',
intro='<p>3주차에 은행 송금을 ROLLBACK으로 되돌려 봤습니다. 오늘은 그 장면을 정식으로 다룹니다. 여러 SQL 문을 <b>하나의 작업 단위</b>로 묶는 트랜잭션, 서버가 꺼져도 커밋된 것은 살리고 끝나지 않은 것은 되돌리는 <b>회복</b>, 여러 사람이 같은 데이터를 동시에 고칠 때 값이 사라지지 않게 하는 <b>병행 제어</b>. 노션 「SQL 문법 정리 (DCL, TCL 추가)」의 예제를 실습실에서 그대로 실행합니다.</p>',
kpis=[('ACID','원자성 · 일관성 · 격리성 · 지속성'),('2','TCL 핵심: COMMIT · ROLLBACK'),('REDO · UNDO','로그로 하는 회복'),('2PL','확장 단계 → 축소 단계')],
hero_talk=[
 ('doc','front','트랜잭션은 <b>“전부 아니면 전무”</b>다. 송금의 출금과 입금은 둘 다 되거나 둘 다 안 되어야 한다.'),
 ('asst','smile','동시에 두 명이 같은 계좌에 입금하면요? 둘 다 들어가겠죠?'),
 ('fly','clip','순서가 엉키면 한 사람의 입금이 사라질 수 있어. 오늘 대결에서 직접 세어 보자.'),
 ('robo','smile','잠금(락)은 느려! 나는 잠그지 않고 그냥 빨리 처리할래!'),
 ('doc','front','REDO와 UNDO가 처음에 뒤섞이는 건 정상이다. “커밋이 로그에 있나?” 질문 하나로 정리된다.')],
crew=[('doc','front','ACID·회복·로킹 정리, 판정'),('asst','smile','실습 진행, 숫자 발표'),('fly','clip','로그를 읽고 REDO/UNDO 판정'),('robo','smile','“잠금 없이 빠르게”파 (오늘 대결)')],
recap='3주차: DBMS는 ROLLBACK으로 반쯤 끝난 송금을 되돌린다(파일 시스템은 못 함). 9주차: DDL은 자동 커밋. 10주차: UPDATE·DELETE에는 WHERE를 꼭. — 오늘 이것들의 원리를 봅니다.',
notion=[('노션 일정표 「12주차 : 회복과 병행제어」 (노션 일정의 주차 번호는 이 사이트와 다릅니다)', NOTION+'1ab17a4520ed81b18756d05b5ee83b2a', '회복·병행 제어 회차 페이지'),
        ('SQL 문법 정리 (DCL, TCL 추가) (노션)', NOTION+'1ab17a4520ed8198b223c82808756ddd', 'students 예제 · GRANT/REVOKE · START TRANSACTION/COMMIT/ROLLBACK — 실습실 ①~⑤')],
why=[('돈과 좌석','은행 이체, 공연 예매, 수강 신청 — 동시에 많은 사람이 같은 데이터를 고치는 곳은 모두 트랜잭션 위에 있습니다.'),
     ('장애는 반드시 온다','정전, 디스크 고장, 프로그램 오류. 로그가 있어야 “어디까지 했는지”를 압니다.'),
     ('설계와 연결','11주 RPG 사례의 “레벨업 능력치 계산은 트랜잭션으로”가 바로 오늘 내용입니다.')],
bigpicture='<div class="flow"><span class="chip">활동</span><span class="arr">→ 마지막 연산 끝</span><span class="chip">부분 완료</span><span class="arr">→ COMMIT</span><span class="chip">완료</span></div><div class="flow"><span class="chip">활동 / 부분 완료</span><span class="arr">→ 오류</span><span class="chip">실패</span><span class="arr">→ ROLLBACK</span><span class="chip">철회</span></div><p>트랜잭션의 다섯 상태(교재 10장). <b>부분 완료</b>는 마지막 연산까지 실행했지만 아직 COMMIT 전 — 이때 장애가 나면 철회됩니다.</p>',
steps=[
dict(id='lv1', short='트랜잭션·ACID', title='트랜잭션과 ACID — 송금은 두 개의 UPDATE가 아니라 하나의 작업', concept='트랜잭션과 ACID', en='transaction and acid', cid='lab:concept/transaction-acid',
 tag='현장: 계좌 이체', analogy='반쯤 끝난 송금',
 situation='정소화가 김선우에게 30,000원을 보냅니다. SQL로는 UPDATE 두 번(출금, 입금)입니다. 출금만 되고 서버가 꺼지면 30,000원은 어디로 갈까요?',
 pair=(('현장에서는','은행 창구 직원은 “출금 전표”와 “입금 전표”를 한 묶음으로 처리합니다. 입금 전표를 못 쓰게 되면 출금 전표도 찢습니다.'),
       ('DBMS에서는','<b>트랜잭션</b>: 하나의 논리적 작업 단위. <b>A</b>tomicity 원자성(전부 아니면 전무) · <b>C</b>onsistency 일관성(실행 전후 일관된 상태) · <b>I</b>solation 격리성(실행 중 다른 트랜잭션이 끼어들지 못함) · <b>D</b>urability 지속성(COMMIT된 결과는 영구 보존).')),
 panel='''<p style="margin-top:0">각 장면을 누르면 어느 성질이 지키는지 나옵니다.</p><div class="chips" id="acid13"></div><div class="insight" id="acid13o"></div>''',
 panel_title='ACID 짝 맞추기',
 sim='ACID 장면 연결',
 explain='<p>ACID 중 <b>원자성·지속성은 회복 기능</b>이, <b>격리성은 병행 제어 기능</b>이, <b>일관성은 무결성 제약과 병행 제어</b>가 함께 지킵니다(교재 10장). 그래서 오늘은 회복(2칸)과 병행 제어(3·4칸)를 차례로 봅니다.</p>',
 limit='원자성이 약속은 했지만, 서버가 실제로 꺼진 뒤 “어디까지 했는지”를 어떻게 알까요?', limit_label='장애 후 상태를 판단할 근거가 없음',
 say=('asst','spark','A는 회복, I는 병행 제어, D는 회복, C는 모두 함께! 오늘 페이지 순서가 그대로네요.'),
 quiz=[dict(q='“COMMIT된 결과는 시스템 장애가 나도 사라지지 않는다”는 성질은?',o=['원자성','일관성','격리성','지속성'],a=3,why='지속성(Durability)입니다. 회복 기능이 보장합니다.'),
       dict(q='출금과 입금 중 하나만 반영되는 일을 막는 성질은?',o=['원자성','일관성','격리성','지속성'],a=0,why='전부 아니면 전무 — 원자성(Atomicity)입니다.')]),
dict(id='lv2', short='TCL 실습', title='COMMIT과 ROLLBACK — 노션 TCL·DCL 예제를 직접 실행', concept='트랜잭션 제어어', en='transaction control language', cid='lab:concept/tcl',
 tag='연구실: 노션 students 예제', analogy='전표 확정과 찢기',
 situation='노션 「SQL 문법 정리 (DCL, TCL 추가)」의 students 예제입니다. START TRANSACTION 후 DELETE하고 ROLLBACK하면 정말 돌아올까요? COMMIT 뒤에 ROLLBACK하면요?',
 pair=(('연구실에서는','전표를 쓰는 동안은 연필(START TRANSACTION), 확정하면 도장(COMMIT), 잘못 썼으면 찢기(ROLLBACK). 도장 찍은 전표는 찢을 수 없습니다.'),
       ('SQL에서는','<b>TCL</b>: START TRANSACTION · COMMIT · ROLLBACK. <b>DCL</b>: GRANT(권한 부여) · REVOKE(권한 회수). MariaDB는 기본이 자동 커밋(autocommit)이라 START TRANSACTION 없이 실행한 문장은 바로 확정됩니다.')),
 panel='<div class="sqllab" id="lab13" data-lab="lab13"></div>',
 panel_title='SQL 실습실 — 노션 TCL·DCL + 송금',
 sim='TCL·DCL 실습',
 explain='<p><b>노션 예제와 다른 점 (실습실 기준):</b> ① 노션 #4-1의 제목 “CCOMMIT”은 오타로, 명령은 <code>COMMIT</code>입니다. ② 노션 #3의 GRANT·REVOKE는 실제 MariaDB에서 <code>\'user1\'@\'localhost\'</code> 사용자가 먼저 있어야 합니다(<code>CREATE USER</code>). 실습실은 권한을 흉내만 내고 실제로 막지는 않습니다. ③ <code>CREATE TABLE</code> 같은 DDL은 트랜잭션 중이어도 자동으로 커밋되므로 ROLLBACK으로 되돌아오지 않습니다(9주차).</p>',
 aicheck='<p>AI가 만든 송금 코드에 <code>UPDATE … 출금; UPDATE … 입금;</code>만 있고 트랜잭션 묶음이 없다면, 그 사이 장애에 대비가 없는 것입니다. “두 UPDATE 사이에 오류가 나면?”이라고 되물으세요. 실습실 ⑤처럼 잔액 CHECK 위반으로 두 번째 문장이 실패하면 ROLLBACK해야 합니다.</p>',
 limit='ROLLBACK은 DBMS가 “바꾸기 전 값”을 기억하기 때문에 가능합니다. 그 기억이 로그입니다.', limit_label='되돌리는 원리(로그)를 아직 보지 않음',
 quiz=[dict(q='START TRANSACTION; DELETE FROM students WHERE id=4; ROLLBACK; 후 id=4 학생은?',o=['삭제되어 없다','그대로 있다','id만 남는다','오류로 표가 비었다'],a=1,why='ROLLBACK은 트랜잭션 안의 변경을 모두 취소하므로 그대로 있습니다(노션 #4-2).'),
       dict(q='사용자에게 SELECT 권한을 주는 명령은 어느 언어에 속하나?',o=['DDL','DML','DCL','TCL'],a=2,why='GRANT·REVOKE는 데이터 제어어(DCL)입니다.')]),
dict(id='lv3', short='회복', title='장애와 회복 — 로그를 읽고 REDO와 UNDO 정하기', concept='로그 기반 회복', en='log-based recovery', cid='lab:concept/log-based-recovery',
 tag='연구실: 장애 직후의 로그', analogy='작업 일지로 복구',
 situation='서버가 꺼졌다가 다시 켜졌습니다. 남은 것은 로그(작업 일지)뿐입니다. 트랜잭션 T1~T4 중 다시 실행할 것(REDO)과 되돌릴 것(UNDO)을 골라 보세요.',
 pair=(('연구실에서는','실험 노트에 “시작 / A를 100에서 70으로 / 끝(확정)”을 적어 두면, 정전 뒤에도 확정된 실험은 다시 재현하고 확정 안 된 실험은 원상태로 돌릴 수 있습니다.'),
       ('DBMS에서는','<b>로그</b>: 변경 전 값·변경 후 값을 기록. 장애 후 <b>&lt;COMMIT&gt;이 있는 트랜잭션은 REDO</b>(변경 후 값으로 다시), <b>없는 트랜잭션은 UNDO</b>(변경 전 값으로 되돌림). <b>검사 시점(checkpoint)</b> 이전에 커밋된 것은 이미 디스크에 반영되어 아무것도 안 해도 됩니다.')),
 panel='''<div class="two"><div><pre id="log13" style="font-size:13px;line-height:1.55;background:#f7f9fb;border:1px solid #d5dbe2;border-radius:8px;padding:10px;overflow-x:auto"></pre></div><div><div id="rd13"></div><div class="ctrl"><button type="button" class="bt primary" id="rd13c">채점</button></div><div class="insight" id="rd13o">트랜잭션마다 처리를 고르세요.</div></div></div>''',
 panel_title='직접 해 보기 — REDO · UNDO · 없음',
 sim='로그 기반 회복 판정',
 explain='<p><b>규칙 한 줄:</b> 검사 시점 이전 커밋 → 없음, 검사 시점 이후 커밋 → REDO, 커밋 없음 → UNDO. T4는 검사 시점 이전에 <b>시작</b>했지만 커밋은 이후이므로 REDO입니다(시작 시점이 아니라 커밋 위치로 판단). 교재 10장은 즉시 갱신(커밋 전에도 디스크에 반영 가능 → UNDO 필요)과 지연 갱신(커밋 후에만 반영 → UNDO 불필요)을 구분합니다. 위 판정은 즉시 갱신 기준입니다.</p>',
 limit='한 사람이 일할 때는 이것으로 충분합니다. 그런데 여러 트랜잭션이 <b>동시에</b> 같은 값을 고치면 로그가 있어도 값이 사라질 수 있습니다.', limit_label='동시 실행으로 생기는 문제는 다루지 않음',
 say=('fly','point','시작이 언제였는지가 아니라 커밋이 로그 어디에 있는지를 봐.'),
 quiz=[dict(q='즉시 갱신 회복에서 장애 시점까지 <COMMIT> 기록이 없는 트랜잭션은?',o=['REDO','UNDO','아무것도 안 함','처음부터 다시 실행'],a=1,why='완료되지 않은 트랜잭션은 변경 전 값으로 되돌립니다(UNDO).'),
       dict(q='검사 시점 이전에 커밋된 트랜잭션은 장애 회복 때?',o=['REDO','UNDO','아무 작업도 필요 없음','항상 둘 다'],a=2,why='검사 시점에 이미 디스크에 반영되었으므로 처리할 필요가 없습니다. 검사 시점이 회복 작업을 줄입니다.')]),
dict(id='lv4', short='병행 제어', title='병행 제어 — 갱신 분실과 로킹, 2단계 로킹, 교착 상태', concept='병행 제어와 로킹', en='concurrency control and locking', cid='lab:concept/concurrency-locking',
 tag='연구실: 동시에 누른 입금', analogy='화장실 열쇠',
 situation='계좌 X의 잔액 1,000원. T1은 300원 입금, T2는 500원 입금. 둘이 거의 동시에 실행되면 결과는 1,800원이어야 합니다. 아래 순서를 한 칸씩 진행해 보세요.',
 pair=(('연구실에서는','한 칸짜리 화장실은 열쇠를 가진 사람만 들어갑니다. 열쇠가 없으면 기다립니다. 기다리는 시간은 들지만 두 사람이 부딪히진 않습니다.'),
       ('DBMS에서는','병행 수행 문제: <b>갱신 분실</b>(한 트랜잭션의 쓰기가 다른 쓰기에 덮임), <b>모순성</b>, <b>연쇄 복귀</b>. 해결: <b>로킹</b> — 데이터에 lock을 걸고 쓰고 unlock. <b>2단계 로킹(2PL)</b>: lock만 하는 확장 단계 뒤에 unlock만 하는 축소 단계 — 직렬 가능성을 보장. 단, <b>교착 상태</b>(서로의 lock을 무한히 기다림)가 생길 수 있음.')),
 panel='''<div class="ctrl"><button type="button" class="bt" id="lu13n" aria-pressed="true">잠금 없음</button><button type="button" class="bt" id="lu13l" aria-pressed="false">로킹 사용</button><button type="button" class="bt primary" id="lu13s">한 칸 진행 ▶</button><button type="button" class="bt" id="lu13r">처음으로</button></div><div id="lu13t"></div><div class="insight" id="lu13o">「한 칸 진행」을 눌러 보세요.</div>''',
 panel_title='직접 해 보기 — 갱신 분실 재현',
 sim='갱신 분실과 로킹 시뮬레이터',
 explain='<p><b>손으로 따라가기 (잠금 없음):</b> T1 read 1,000 → T2 read 1,000 → T1 write 1,300 → T2 write 1,500. T2는 T1이 쓰기 전에 읽은 1,000에 500을 더했으므로 T1의 300원이 <b>사라졌습니다</b>. 로킹을 쓰면 T2의 read가 T1의 unlock까지 기다리므로 1,300을 읽고 1,800을 씁니다.</p><p><b>교착 상태 예:</b> T1이 X를 lock하고 Y를 기다리는 동안 T2가 Y를 lock하고 X를 기다리면 둘 다 영원히 기다립니다. DBMS는 한쪽을 철회(ROLLBACK)해 풀고, MariaDB(InnoDB)는 이때 오류 1213 Deadlock을 돌려줍니다.</p>',
 aicheck='<p>“동시에 재고를 차감하는 코드”를 AI에게 받으면, <code>SELECT 재고 → (프로그램에서 계산) → UPDATE 재고 = 계산값</code> 구조인지 확인하세요. 이것이 바로 갱신 분실 구조입니다. <code>UPDATE 상품 SET 재고 = 재고 - 1 WHERE …</code>처럼 DBMS 안에서 한 번에 고치거나, <code>SELECT … FOR UPDATE</code>로 잠그는지 물어보세요.</p>',
 limit='지금까지는 관계형 DBMS 한 대 안의 이야기였습니다. 사진·영상·SNS 글처럼 표에 잘 안 맞는 데이터, 여러 서버에 퍼진 데이터는? 데이터베이스 응용 기술 — 14주차.', limit_label='관계형으로 다루기 어려운 데이터·분산 환경은 아직',
 quiz=[dict(q='잔액 1,000에서 T1(+300)과 T2(+500)가 잠금 없이 “T1 read, T2 read, T1 write, T2 write” 순으로 실행되면 최종 잔액은? (계산)',o=['1,300','1,500','1,800','800'],a=1,why='T2가 처음 읽은 1,000에 500을 더해 마지막에 1,500을 씁니다. T1의 +300이 사라진 갱신 분실입니다.'),
       dict(q='2단계 로킹 규약의 내용으로 옳은 것은?',o=['unlock 후에도 새 lock을 할 수 있다','lock만 하는 확장 단계 후 unlock만 하는 축소 단계','교착 상태가 절대 생기지 않는다','읽기에는 lock이 필요 없다'],a=1,why='확장 단계 → 축소 단계. 직렬 가능성은 보장하지만 교착 상태는 생길 수 있습니다.')]),
],
duel=dict(q='잠금 없이 빠르게 vs 로킹 — 입금 20건 동시 처리',
 intro='계좌 잔액 0원에서 창구 두 곳이 각각 10,000원 입금을 10번씩(총 20건) 동시에 처리합니다. 정답은 200,000원. 초파리는 <b>로킹</b>(read 전에 lock, write 후 unlock), 주판봇은 <b>잠금 없이</b> 처리합니다. 두 창구의 연산 순서는 같은 무작위 순서(seed 고정)로 섞습니다.',
 fly_pick='로킹 — 기다렸다가 처리', fly_line='열쇠 없으면 기다려. 조금 늦어도 돈은 안 사라져.',
 robo_pick='잠금 없이 바로 처리', robo_line='기다리는 시간이 아깝지! 그냥 동시에 쓰자!',
 metric='최종 잔액 (정답 200,000원에 가까울수록 이김)', higher=True, step=3,
 after='<div id="duel13t"></div>',
 run='return PAGE.duel();',
 announce='return "최종 잔액: 초파리 <b>"+r.fly.toLocaleString()+"원</b>, 주판봇 <b>"+r.robo.toLocaleString()+"원</b> — 주판봇 쪽에서 입금 <b>"+r.lost+"건</b>이 사라졌어요. 대신 로킹은 기다림이 <b>"+r.wait+"번</b> 있었어요.";',
 verdict='return "잠금이 없으면 빨라도 입금이 사라진다. 기다림의 비용보다 돈이 사라지는 비용이 크다. 초파리 승.";'),
summary='''<div class="tbl"><table><thead><tr><th>주제</th><th>핵심</th><th>지키는 ACID</th></tr></thead><tbody>
<tr><td>트랜잭션</td><td>논리적 작업 단위, 활동·부분 완료·완료·실패·철회</td><td>—</td></tr>
<tr><td>TCL · DCL</td><td>START TRANSACTION · COMMIT · ROLLBACK / GRANT · REVOKE</td><td>원자성</td></tr>
<tr><td>회복</td><td>로그(변경 전·후 값), 커밋 있음 → REDO, 없음 → UNDO, 검사 시점</td><td>원자성 · 지속성</td></tr>
<tr><td>병행 제어</td><td>갱신 분실·모순성·연쇄 복귀 → 로킹, 2PL, 교착 상태</td><td>격리성 · 일관성</td></tr></tbody></table></div>
<div class="cards"><div><b>비유의 한계 — 화장실 열쇠</b> 실제 DBMS는 읽기용(공유)·쓰기용(전용) 잠금을 나눠 여러 사람이 동시에 읽는 것은 허용합니다. 열쇠 하나 비유는 전용 잠금만 보여 줍니다.</div><div><b>대결의 한계</b> 시뮬레이션은 창구 두 곳, 연산 순서 하나(seed 고정)만 봅니다. 순서가 달라지면 사라지는 건수도 달라집니다. 운 좋게 0건이 나오는 순서도 있지만, 그것은 우연이지 보장이 아닙니다.</div></div>''',
outro=[('doc','front','오늘의 세 줄: ① 트랜잭션은 전부 아니면 전무, ACID ② 장애 후 커밋 있으면 REDO, 없으면 UNDO ③ 동시 수정은 로킹(2PL)으로, 대신 교착 상태를 조심.'),
       ('asst','report','잠금 없는 쪽에서 입금이 사라졌어요. 정답은 20만 원인데 말이에요.'),
       ('robo','sigh','빨리 끝낸 게 아니라 틀리게 끝낸 거였구나…'),
       ('fly','coffee','기다림은 성능 문제고, 사라진 돈은 신뢰 문제야. 둘은 무게가 달라.')],
next_note='<p class="recap"><b>다음 회차 — 14주차 「데이터베이스 응용 기술」:</b> 비정형 데이터와 NoSQL(MongoDB), 빅데이터, 데이터 웨어하우스 — 노션 13주차 링크와 이미지 검색 사례.</p>',
gloss={'트랜잭션':('트랜잭션','개념','하나의 논리적 작업 단위를 이루는 연산들의 묶음. 전부 실행되거나 전혀 실행되지 않는다.','transaction-unit','lv1'),
 '원자성':('원자성','개념','트랜잭션의 연산이 모두 반영되거나 전혀 반영되지 않아야 하는 성질.','atomicity','lv1'),
 '격리성':('격리성','개념','실행 중인 트랜잭션의 중간 결과에 다른 트랜잭션이 접근할 수 없는 성질.','isolation','lv1'),
 '지속성':('지속성','개념','완료된 트랜잭션의 결과는 장애가 나도 영구히 유지되는 성질.','durability','lv1'),
 '로그':('로그','용어','변경 전 값과 변경 후 값을 기록한 작업 일지. 회복의 근거.','log','lv3'),
 '검사 시점':('검사 시점(checkpoint)','용어','일정 간격으로 로그와 버퍼 내용을 디스크에 반영해 두는 시점. 회복 작업을 줄인다.','checkpoint','lv3'),
 '갱신 분실':('갱신 분실','개념','한 트랜잭션이 쓴 값을 다른 트랜잭션이 덮어써 첫 변경이 사라지는 문제.','lost-update','lv4'),
 '교착 상태':('교착 상태','개념','트랜잭션들이 서로의 잠금 해제를 무한히 기다리는 상태.','deadlock','lv4'),
 '2단계 로킹':('2단계 로킹 규약','개념','lock만 하는 확장 단계 후 unlock만 하는 축소 단계로 나누는 로킹 규약. 직렬 가능성 보장.','two-phase-locking','lv4')},
facts=[('F01','트랜잭션의 특성 ACID: 원자성·일관성·격리성·지속성','문헌 사실','kim3ed','lv1','10장 1절'),
       ('F02','노션 TCL 예제: START TRANSACTION 후 DELETE를 ROLLBACK하면 변경이 취소된다','문헌 사실','ahn2025sqltcl','lv2','#4-2 ROLLBACK'),
       ('F03','즉시 갱신 회복: 장애 시 커밋된 트랜잭션은 REDO, 미완료 트랜잭션은 UNDO, 검사 시점으로 회복 범위를 줄임','문헌 사실','kim3ed','lv3','10장 회복 기법'),
       ('F04','병행 수행 문제: 갱신 분실, 모순성, 연쇄 복귀 — 로킹과 2단계 로킹 규약으로 해결, 교착 상태 가능','문헌 사실','kim3ed','lv4','10장 병행 제어')],
refs=[dict(id='kim3ed',type='book',title='데이터베이스 개론 (3판)',author=[{'family':'김연희','given':''}],publisher='한빛아카데미',role='primary',verified={'title':True,'authors':True,'year':False},note='3판 출판 연도 미확인 — 4판(2026년 7월)이 나왔으나 강의는 3판 기준'),
      dict(id='ahn2025sqltcl',type='webpage',title='SQL 문법 정리 (DCL, TCL 추가)',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},URL=NOTION+'1ab17a4520ed8198b223c82808756ddd',role='primary'),
      dict(id='ahn2025rpg',type='report',title='RPG 용사의 전설 — 데이터베이스 설계자의 실무 프로젝트 가이드',author=[{'family':'안상선','given':''}],issued={'date-parts':[[2025]]},role='background')],
models=['계좌 송금 데이터 (설명용 예시값)','회복 판정용 로그 (교재 10장 유형으로 만든 예)','갱신 분실 시뮬레이터의 순서 (교재 유형)','대결 시뮬레이션 (창구 2곳 × 입금 10건, 고정 seed 무작위 순서)'],
cover_alt='은행 창구 두 곳 앞에 같은 금고가 놓이고, 한쪽은 열쇠를 기다리는 줄, 다른 쪽은 동전이 새어 나가는 장면 (대체 그림)',
prereq=['12'],
js=r'''
var $=LAB.$,$$=LAB.$$;
var AC=[['출금 성공 후 입금에서 오류 → 출금도 취소','원자성(A) — 전부 아니면 전무. 회복 기능이 지킵니다.'],['잔액은 0원 이상이어야 한다는 CHECK가 실행 후에도 지켜짐','일관성(C) — 실행 전후 모두 일관된 상태.'],['내 송금이 끝나기 전엔 다른 사람이 중간 잔액을 볼 수 없음','격리성(I) — 병행 제어가 지킵니다.'],['COMMIT 직후 정전이 나도 송금 결과가 남아 있음','지속성(D) — 회복 기능(로그·REDO)이 지킵니다.']];
var ac=$('#acid13');AC.forEach(function(a){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=a[0];b.style.textAlign='left';b.onclick=function(){[].forEach.call(ac.children,function(x){x.setAttribute('aria-pressed',x===b);});$('#acid13o').innerHTML=a[1];};ac.appendChild(b);});
var LOG=['<T1, start>','<T1, X, 100, 70>','<T1, commit>','<T4, start>','<T4, Y, 50, 80>','─── <checkpoint> ───','<T2, start>','<T2, Z, 10, 40>','<T3, start>','<T2, commit>','<T3, W, 5, 9>','<T4, commit>','<T5, start>','<T5, X, 70, 60>','✖ 장애 발생'];
$('#log13').textContent=LOG.join('\n');
var ANS={T1:'없음',T2:'REDO',T3:'UNDO',T4:'REDO',T5:'UNDO'},WHY={T1:'검사 시점 이전에 커밋 — 이미 디스크에 반영.',T2:'검사 시점 이후 커밋 — 변경 후 값(Z=40)으로 REDO.',T3:'커밋 없음 — 변경 전 값(W=5)으로 UNDO.',T4:'시작은 검사 시점 전이지만 커밋은 이후 — REDO(Y=80).',T5:'커밋 없음 — UNDO(X=70으로).'},pick={};
$('#rd13').innerHTML=Object.keys(ANS).map(function(t){return '<div class="ctrl"><b style="min-width:30px;display:inline-block">'+t+'</b>'+['REDO','UNDO','없음'].map(function(c){return '<button type="button" class="bt" data-t="'+t+'" data-c="'+c+'">'+c+'</button>';}).join('')+'</div>';}).join('');
$$('#rd13 button').forEach(function(b){b.onclick=function(){pick[b.dataset.t]=b.dataset.c;$$('#rd13 button[data-t="'+b.dataset.t+'"]').forEach(function(x){x.setAttribute('aria-pressed',x===b);});};});
$('#rd13c').onclick=function(){var ok=0,h='';Object.keys(ANS).forEach(function(t){var g=pick[t]===ANS[t];if(g)ok++;h+='<br>'+(g?'✓ ':'✗ ')+t+' → <b>'+ANS[t]+'</b>: '+WHY[t];});$('#rd13o').innerHTML='맞힘 <b>'+ok+'/5</b>'+h;};
/* 갱신 분실 */
var mode='n',k=0;
var SN=[['T1','read(X) → 1,000',1000,null],['T2','read(X) → 1,000',null,1000],['T1','X = 1,000 + 300; write(X)',1300,null],['T2','X = 1,000 + 500; write(X)',1500,null]];
var SL=[['T1','lock(X)'],['T1','read(X) → 1,000'],['T2','lock(X) 요청 → 대기'],['T1','write(X) = 1,300'],['T1','unlock(X)'],['T2','lock(X) 획득, read(X) → 1,300'],['T2','write(X) = 1,800; unlock(X)']];
var XV={n:[1000,1000,1300,1500],l:[1000,1000,1000,1300,1300,1300,1800]};
function lu(){var S=mode==='n'?SN:SL,rows=S.slice(0,k).map(function(s,i){return [i+1,s[0]==='T1'?s[1]:'',s[0]==='T2'?s[1]:'',XV[mode][i].toLocaleString()];});
 $('#lu13t').innerHTML=LAB.tableHTML(['시각','T1 (+300)','T2 (+500)','디스크의 X'],rows,{cls:function(r){return /대기/.test(r[2])?'dim':'';}});
 $('#lu13o').innerHTML=k<S.length?('진행 '+k+'/'+S.length):(mode==='n'?'<b style="color:#c9302c">최종 1,500원 — T1의 300원이 사라졌습니다(갱신 분실).</b>':'<b style="color:#13733a">최종 1,800원 — T2가 기다린 덕에 정확합니다.</b> 대가: T2는 한 번 기다렸습니다.');}
$('#lu13s').onclick=function(){var S=mode==='n'?SN:SL;if(k<S.length)k++;lu();};
$('#lu13r').onclick=function(){k=0;lu();};
$('#lu13n').onclick=function(){mode='n';k=0;$('#lu13n').setAttribute('aria-pressed','true');$('#lu13l').setAttribute('aria-pressed','false');lu();};
$('#lu13l').onclick=function(){mode='l';k=0;$('#lu13l').setAttribute('aria-pressed','true');$('#lu13n').setAttribute('aria-pressed','false');lu();};lu();
/* 대결: seed 고정 순서 */
function sim(lock){var s=13013;function r(){s=(s*1103515245+12345)%2147483648;return s/2147483648;}
 var bal=0,done={A:0,B:0},st={A:null,B:null},local={A:0,B:0},holder=null,wait=0,lost=0,commits=0;
 while(done.A<10||done.B<10){var w=r()<0.5?'A':'B';if(done[w]>=10)w=w==='A'?'B':'A';
  if(st[w]===null){if(lock){if(holder&&holder!==w){wait++;continue;}holder=w;}local[w]=bal;st[w]='r';}
  else{bal=local[w]+10000;st[w]=null;done[w]++;commits++;if(lock)holder=null;}}
 lost=(200000-bal)/10000;return {bal:bal,wait:wait,lost:lost};}
PAGE.duel=function(){var L=sim(true),N=sim(false);
 $('#duel13t').innerHTML=LAB.tableHTML(['방식','최종 잔액','사라진 입금','기다림'],[['로킹 (초파리)',L.bal.toLocaleString()+'원',L.lost+'건',L.wait+'번'],['잠금 없음 (주판봇)',N.bal.toLocaleString()+'원',N.lost+'건','0번']],{cap:'정답 200,000원 (10,000원 × 20건)'});
 return {fly:L.bal,robo:N.bal,flyTxt:L.bal.toLocaleString()+'원',roboTxt:N.bal.toLocaleString()+'원',lost:N.lost,wait:L.wait};};
''',
labs=('lab13:{setup:%s,presets:[{t:"① 노션 #4-1 COMMIT",q:"START TRANSACTION;\\nUPDATE students SET grade = 2 WHERE id = 3;\\nCOMMIT;\\nSELECT id, name, grade FROM students WHERE id = 3;"},{t:"② 노션 #4-2 ROLLBACK",q:"START TRANSACTION;\\nDELETE FROM students WHERE id = 4;\\nSELECT COUNT(*) AS 삭제직후 FROM students;\\nROLLBACK;\\nSELECT COUNT(*) AS 롤백후 FROM students;"},{t:"③ 노션 복습 예제",q:"START TRANSACTION;\\nINSERT INTO students (id, name, student_id, grade, major, email)\\nVALUES (9, \'박성호\', \'2023009\', 1, \'물리학과\', \'sungho.park@example.com\');\\nCOMMIT;\\nSTART TRANSACTION;\\nDELETE FROM students WHERE id = 9;\\nROLLBACK;\\nSELECT id, name FROM students WHERE id = 9;"},{t:"④ 노션 #3 DCL",q:"GRANT SELECT, INSERT ON students TO \'user1\'@\'localhost\';\\nREVOKE DELETE ON students FROM \'user1\'@\'localhost\';"},{t:"⑤ 송금 실패 → ROLLBACK",q:"-- 김선우(B01, 잔액 50,000)가 정소화에게 80,000원 송금 시도\\nSTART TRANSACTION;\\nUPDATE 계좌 SET 잔액 = 잔액 + 80000 WHERE 계좌번호 = \'A01\';\\nUPDATE 계좌 SET 잔액 = 잔액 - 80000 WHERE 계좌번호 = \'B01\';"},{t:"⑥ 오류 뒤 정리",q:"-- ⑤에서 두 번째 UPDATE가 CHECK(잔액 >= 0) 위반. 첫 번째는 반영된 상태!\\nSELECT * FROM 계좌;\\nROLLBACK;\\nSELECT * FROM 계좌;"}],ready:"노션 students(5명)와 계좌 2개가 준비되어 있습니다. ⑤→⑥은 이어서 실행하세요."}') % ('"' + STU.replace('"', '\\"') + '"'),
)
for s in PAGE['steps']:
    s['def'] = {'lv1':'하나의 논리적 작업 단위. 원자성·일관성·격리성·지속성(ACID)을 가져야 한다.','lv2':'트랜잭션을 확정(COMMIT)하거나 취소(ROLLBACK)하는 SQL 명령, 그리고 권한을 다루는 GRANT·REVOKE(DCL).','lv3':'로그에 남긴 변경 전·후 값으로, 장애 후 커밋된 트랜잭션은 REDO, 미완료 트랜잭션은 UNDO하는 회복 방법.','lv4':'동시에 실행되는 트랜잭션이 서로 간섭하지 않도록 잠금(로킹)으로 순서를 제어하는 기법. 2단계 로킹 규약.'}[s['id']]

# ── 5칸: 실제 실습 + 사례 분석 (2026-11 보강) ─────────────────
PAGE['steps'][3]['limit'] = '원리는 손에 익었습니다. 이제 실제 게임 거래 사례를 두 개의 창(세션)으로 재현하고, 진짜 MariaDB에서도 해 봅니다.'
PAGE['steps'][3]['limit_label'] = '실제 두 세션에서 재현해 보지 않음'
PAGE['steps'].append(dict(id='lv5', short='거래 실습', title='실습 · 사례 분석 — RPG 거래소를 두 세션으로 재현하기', concept='트랜잭션 실습과 사례 분석', en='transaction lab and case analysis', cid='lab:concept/transaction-lab-case',
 tag='사례: 용사의 전설 거래소', analogy='계산대 두 개, 물건은 하나',
 situation='RPG 「용사의 전설」 사례 문서에는 “트랜잭션: 거래/교환 시 데이터 일관성 유지”, “퀘스트 완료 시 보상 지급과 상태 업데이트를 단일 트랜잭션으로 처리”라는 설계 결정이 있습니다. 거래소에 하나뿐인 <b>전설의 검(매물 7번, 1,000골드)</b>을 레온과 미라가 거의 동시에 사려 합니다. 두 사람의 접속을 <b>세션 A·B</b>로 나눠 한 줄씩 실행해 보세요.',
 pair=(('현장에서는','계산대 두 곳에서 마지막 한 개 남은 물건을 동시에 팔면, 둘 다 “재고 있음”을 보고 계산해 버립니다. 한 직원이 물건을 손에 쥐고(잠금) 계산을 끝낼 때까지 다른 직원은 기다려야 합니다.'),
       ('MariaDB에서는','두 접속(세션)이 각자 <code>START TRANSACTION</code>을 엽니다. 읽고 나서 고칠 행은 <code>SELECT … FOR UPDATE</code>로 미리 잠급니다. 다른 세션은 그 행을 고치거나 잠그려 하면 기다리고, 서로 기다리면 InnoDB가 한쪽을 <b>ERROR 1213 (Deadlock)</b>으로 철회합니다.')),
 panel='''<div class="ctrl" id="ts13s"></div><div class="ctrl"><button type="button" class="bt primary" id="ts13n">다음 줄 실행 ▶</button><button type="button" class="bt" id="ts13r">처음으로</button><span id="ts13p" class="cvcap"></span></div>
<div class="two"><div><p class="ptitle" style="color:#1e55c8">세션 A (레온)</p><div id="ts13a" style="font-size:13px;min-height:120px"></div></div><div><p class="ptitle" style="color:#c42a6e">세션 B (미라)</p><div id="ts13b" style="font-size:13px;min-height:120px"></div></div></div>
<div class="two"><div id="ts13d"></div><div id="ts13l"></div></div><div class="insight" id="ts13o"></div>''',
 panel_title='두 세션 재현기 — 시나리오를 고르고 한 줄씩',
 sim='두 세션 거래 재현기',
 body='''<h3>진짜 MariaDB에서 해 보기 (두 창 실습)</h3>
<ol><li>HeidiSQL에서 같은 서버에 <b>쿼리 탭을 두 개</b> 열거나, 명령 프롬프트 두 개에서 <code>mariadb -u root -p</code>로 접속합니다(설치는 1주차 안내). 두 창 모두 <code>SET autocommit = 0;</code></li>
<li>한쪽 창에서 준비 SQL을 실행합니다.<pre style="font-size:13px;background:#f7f9fb;border:1px solid #d5dbe2;border-radius:8px;padding:8px;overflow-x:auto">CREATE DATABASE rpg; USE rpg;
CREATE TABLE 캐릭터 (이름 VARCHAR(10) PRIMARY KEY, 골드 INT CHECK (골드 &gt;= 0)) ENGINE=InnoDB;
CREATE TABLE 매물 (매물번호 INT PRIMARY KEY, 아이템 VARCHAR(20), 가격 INT, 판매자 VARCHAR(10), 상태 VARCHAR(10)) ENGINE=InnoDB;
INSERT INTO 캐릭터 VALUES ('레온', 5000), ('미라', 3000), ('보리', 0);
INSERT INTO 매물 VALUES (7, '전설의 검', 1000, '보리', '판매중');
COMMIT;</pre></li>
<li>두 창 모두 <code>USE rpg; START TRANSACTION;</code> → A 창: <code>SELECT 상태 FROM 매물 WHERE 매물번호 = 7 FOR UPDATE;</code> → B 창: 같은 문장. <b>B 창이 멈춰 있는지</b> 확인합니다.</li>
<li>A 창: <code>UPDATE 매물 SET 상태='판매완료' WHERE 매물번호=7; UPDATE 캐릭터 SET 골드=골드-1000 WHERE 이름='레온'; UPDATE 캐릭터 SET 골드=골드+1000 WHERE 이름='보리'; COMMIT;</code> → B 창의 SELECT가 풀리며 <b>‘판매완료’</b>를 돌려주는지 봅니다. B는 <code>ROLLBACK;</code></li>
<li>교착 실험: A는 <code>UPDATE 캐릭터 … WHERE 이름='레온'</code> 다음 <code>… '미라'</code>, B는 반대 순서로 실행합니다. 한쪽에 <code>ERROR 1213 (40001): Deadlock found</code>가 나오면 성공입니다. 마지막에 <code>SHOW ENGINE INNODB STATUS;</code>의 LATEST DETECTED DEADLOCK 부분을 읽어 보세요.</li></ol>
<p class="cvcap">기다림이 너무 길면 <code>innodb_lock_wait_timeout</code>(기본 50초) 뒤에 ERROR 1205가 납니다. 실습 결과(시각·오류 번호)를 과제 메모에 적어 두세요.</p>
<h3>사례 분석 — 사례 문서의 문장을 오늘 개념으로 번역하기</h3>
<div class="tbl"><table><thead><tr><th>사례 문서의 문장</th><th>오늘 개념</th><th>설계 결정으로 바꾸면</th></tr></thead><tbody>
<tr><td>트랜잭션: 거래/교환 시 데이터 일관성 유지</td><td>원자성 · 격리성</td><td>골드 차감·지급·아이템 이동·매물 상태를 한 트랜잭션으로, 매물 행은 FOR UPDATE로 잠금</td></tr>
<tr><td>퀘스트 완료 시 보상 지급과 상태 업데이트를 단일 트랜잭션으로 처리</td><td>원자성</td><td>보상만 들어가고 퀘스트가 미완료로 남는 반쪽 상태 금지 — 실패 시 ROLLBACK</td></tr>
<tr><td>레벨업 시 스탯 계산 트랜잭션 필요</td><td>일관성</td><td>레벨·경험치·능력치를 함께 갱신, CHECK로 음수 방지</td></tr>
<tr><td>시스템 복구 — 서버 장애 발생 시 데이터 롤백 가능</td><td>회복 (로그, UNDO)</td><td>로그 보관·검사 시점, 장애 훈련</td></tr>
<tr><td>DB 장애 시 전체 게임 서비스 중단 가능성 / 백업 및 복구 프로세스 구축</td><td>지속성 · 회복의 한계</td><td>정기 백업 + 복제 서버, 복구 시간 목표 정하기</td></tr></tbody></table></div>
<div class="sqllab" id="lab13b" data-lab="lab13b"></div>''',
 explain='<p><b>세 시나리오에서 배우는 것:</b> ① 잠금 없음 — 둘 다 “판매중”을 읽고 사서 <b>검이 두 자루</b>가 되고 판매자는 2,000골드를 받습니다(아이템 복사). ② FOR UPDATE — B가 기다렸다가 “판매완료”를 읽고 포기합니다. ③ 반대 순서로 잠그면 교착 — 한쪽이 1213으로 철회됩니다. 해결책은 <b>항상 같은 순서로 잠그기</b>(예: 이름 가나다순, 계좌 번호 순)입니다. 아래 실습실은 같은 거래를 한 세션에서 트랜잭션으로 묶는 연습입니다.</p>',
 aicheck='<p>AI가 만든 거래 코드에서 <code>SELECT 상태 …</code>로 확인한 뒤 프로그램에서 판단하고 <code>UPDATE</code>하는 구조라면, 확인과 수정 사이에 다른 세션이 끼어들 수 있습니다. “확인하는 SELECT에 FOR UPDATE가 있는가?”, “두 행 이상을 잠글 때 순서가 정해져 있는가?” 두 가지를 물어보세요.</p>',
 limit='지금까지는 관계형 DBMS 한 대 안의 이야기였습니다. 사진·영상·SNS 글처럼 표에 잘 안 맞는 데이터, 여러 서버에 퍼진 데이터는? 데이터베이스 응용 기술 — 14주차.', limit_label='관계형으로 다루기 어려운 데이터·분산 환경은 아직',
 say=('fly','point','검이 두 자루가 되는 건 버그가 아니라 설계 누락이야. FOR UPDATE 한 단어면 막혀.'),
 quiz=[dict(q='두 세션이 같은 매물을 동시에 사는 것을 막으려면, 상태를 확인하는 SELECT에 무엇을 붙이나?',o=['ORDER BY','FOR UPDATE','LIMIT 1','DISTINCT'],a=1,why='SELECT … FOR UPDATE는 읽은 행에 쓰기 잠금을 걸어, 다른 세션이 그 행을 잠그거나 고치려면 기다리게 합니다.'),
       dict(q='세션 A는 레온→미라, 세션 B는 미라→레온 순서로 행을 잠그다 서로 기다렸다. 가장 근본적인 예방책은?',o=['잠금을 쓰지 않는다','모든 세션이 같은 순서(예: 이름순)로 잠근다','COMMIT을 두 번 한다','CHECK 제약을 추가한다'],a=1,why='교착 상태는 서로 반대 순서로 잠글 때 생깁니다. 잠금 순서를 하나로 정하면 순환 대기가 생기지 않습니다.')],
 **{'def': '두 세션에서 트랜잭션·잠금·교착을 직접 재현하고, 사례 문서의 설계 결정을 ACID와 회복·병행 제어 개념으로 해석하는 실습.'}))
PAGE['gloss']['FOR UPDATE'] = ('SELECT … FOR UPDATE', '용어', '읽은 행에 쓰기 잠금을 걸어 트랜잭션이 끝날 때까지 다른 세션이 고치지 못하게 하는 문장.', 'select-for-update', 'lv5')
PAGE['facts'].append(('F05', 'RPG 사례: 거래/교환 시 트랜잭션으로 데이터 일관성 유지, 퀘스트 완료 시 보상 지급과 상태 업데이트를 단일 트랜잭션으로 처리', '사례 기록', 'ahn2025rpg', 'lv5', '「아이템 시스템」·「퀘스트 시스템」'))
PAGE['js'] += r'''
var TS={none:{t:'① 잠금 없음 — 같은 검을 동시에',steps:[
 ['A','START TRANSACTION;','',{}],['B','START TRANSACTION;','',{}],
 ['A',"SELECT 상태 FROM 매물 WHERE 매물번호 = 7;",'→ 판매중',{}],['B',"SELECT 상태 FROM 매물 WHERE 매물번호 = 7;",'→ 판매중 (A가 아직 안 바꿈)',{}],
 ['A',"UPDATE 캐릭터 SET 골드 = 골드 - 1000 WHERE 이름 = '레온';\nUPDATE 캐릭터 SET 골드 = 골드 + 1000 WHERE 이름 = '보리';\nINSERT INTO 인벤토리 VALUES ('레온', '전설의 검');\nUPDATE 매물 SET 상태 = '판매완료' WHERE 매물번호 = 7;",'',{leon:4000,bori:1000,inv:['레온'],st:'판매완료(미확정)'}],
 ['B',"UPDATE 캐릭터 SET 골드 = 골드 - 1000 WHERE 이름 = '미라';\nUPDATE 캐릭터 SET 골드 = 골드 + 1000 WHERE 이름 = '보리';\nINSERT INTO 인벤토리 VALUES ('미라', '전설의 검');\nUPDATE 매물 SET 상태 = '판매완료' WHERE 매물번호 = 7;",'(설명을 위해 행 잠금이 없는 엔진을 가정)',{mira:2000,bori:2000,inv:['레온','미라']}],
 ['A','COMMIT;','',{st:'판매완료'}],['B','COMMIT;','',{}]],end:'<b style="color:#c9302c">검이 두 자루, 판매자 보리는 2,000골드.</b> 하나뿐인 매물이 두 번 팔렸습니다(아이템 복사). 실제 InnoDB는 UPDATE에 행 잠금을 걸지만, 확인(SELECT)과 수정 사이에 끼어드는 문제는 그대로 남습니다 — 그래서 ②가 필요합니다.'},
 lock:{t:'② SELECT … FOR UPDATE',steps:[
 ['A','START TRANSACTION;','',{}],['B','START TRANSACTION;','',{}],
 ['A',"SELECT 상태 FROM 매물 WHERE 매물번호 = 7 FOR UPDATE;",'→ 판매중 · 매물 7 잠금(A)',{lock:'매물 7 ← A'}],
 ['B',"SELECT 상태 FROM 매물 WHERE 매물번호 = 7 FOR UPDATE;",'⏳ 대기 — A의 잠금',{wait:'B가 매물 7을 기다림'}],
 ['A',"UPDATE 캐릭터 SET 골드 = 골드 - 1000 WHERE 이름 = '레온';\nUPDATE 캐릭터 SET 골드 = 골드 + 1000 WHERE 이름 = '보리';\nINSERT INTO 인벤토리 VALUES ('레온', '전설의 검');\nUPDATE 매물 SET 상태 = '판매완료' WHERE 매물번호 = 7;",'',{leon:4000,bori:1000,inv:['레온'],st:'판매완료(미확정)'}],
 ['A','COMMIT;','잠금 해제',{st:'판매완료',lock:'매물 7 ← B',wait:''}],
 ['B','(대기하던 SELECT가 풀림)','→ 판매완료',{}],['B','ROLLBACK;','구매 포기 — 아무것도 바뀌지 않음',{lock:''}]],end:'<b style="color:#13733a">검은 한 자루, 골드 총량 그대로.</b> B는 기다린 대가로 정확한 상태를 읽었습니다.'},
 dead:{t:'③ 맞교환 — 반대 순서로 잠그면',steps:[
 ['A','START TRANSACTION;','레온이 미라에게 500골드 보내고 물약을 받는 교환',{}],['B','START TRANSACTION;','미라가 레온에게 물약을 보내고 500골드를 받는 같은 교환',{}],
 ['A',"UPDATE 캐릭터 SET 골드 = 골드 - 500 WHERE 이름 = '레온';",'레온 행 잠금(A)',{leon:4500,lock:'레온 ← A'}],
 ['B',"UPDATE 캐릭터 SET 골드 = 골드 + 500 WHERE 이름 = '미라';",'미라 행 잠금(B)',{mira:3500,lock:'레온 ← A, 미라 ← B'}],
 ['A',"UPDATE 캐릭터 SET 골드 = 골드 + 500 WHERE 이름 = '미라';",'⏳ 대기 — 미라 행은 B가 잠금',{wait:'A가 미라를 기다림'}],
 ['B',"UPDATE 캐릭터 SET 골드 = 골드 - 500 WHERE 이름 = '레온';",'ERROR 1213 (40001): Deadlock found — B 철회',{mira:3000,lock:'레온 ← A, 미라 ← A',wait:''}],
 ['A','(대기가 풀려 실행됨) COMMIT;','',{mira:3500,lock:''}]],end:'<b style="color:#a35c00">교착 → B만 철회.</b> 응용 프로그램은 1213을 받으면 다시 시도해야 합니다. 두 세션이 모두 “이름 가나다순”(레온 → 미라)으로 잠갔다면 B는 처음부터 A를 기다렸을 뿐 교착은 생기지 않습니다.'}};
var sc='none',k=0;
var tsc=LAB.$('#ts13s');Object.keys(TS).forEach(function(key){var b=document.createElement('button');b.type='button';b.className='bt';b.textContent=TS[key].t;b.onclick=function(){sc=key;k=0;[].forEach.call(tsc.children,function(x){x.setAttribute('aria-pressed',x===b);});tsr();};tsc.appendChild(b);});
function tsr(){var S=TS[sc].steps,st={leon:5000,mira:3000,bori:0,inv:[],st:'판매중',lock:'',wait:''},la=[],lb=[];
 for(var i=0;i<k;i++){var s=S[i];for(var key in s[3])st[key]=s[3][key];var line='<div style="margin:3px 0"><code style="white-space:pre-wrap">'+LAB.esc(s[1])+'</code>'+(s[2]?'<br><small style="color:'+(/ERROR|대기/.test(s[2])?'#c9302c':'#5b6874')+'">'+s[2]+'</small>':'')+'</div>';
  (s[0]==='A'?la:lb).push('<b>'+(i+1)+'.</b> '+line);(s[0]==='A'?lb:la).push('<div style="height:4px"></div>');}
 LAB.$('#ts13a').innerHTML=la.join('');LAB.$('#ts13b').innerHTML=lb.join('');
 LAB.$('#ts13d').innerHTML=LAB.tableHTML(['캐릭터','골드'],[['레온',st.leon.toLocaleString()],['미라',st.mira.toLocaleString()],['보리(판매자)',st.bori.toLocaleString()]],{cap:'캐릭터 표'})+LAB.tableHTML(['매물 7','상태','검을 가진 사람'],[['전설의 검',st.st,st.inv.join(', ')||'—']],{cap:'매물 · 인벤토리'});
 LAB.$('#ts13l').innerHTML=LAB.tableHTML(['잠금 표',''],[['잠긴 행',st.lock||'없음'],['기다리는 세션',st.wait||'없음']],{cap:'InnoDB 행 잠금 (설명용)'});
 LAB.$('#ts13p').textContent=k+'/'+S.length;LAB.$('#ts13o').innerHTML=k>=S.length?TS[sc].end:'다음 줄을 실행하세요. 어느 세션 차례인지 번호를 보세요.';}
LAB.$('#ts13n').onclick=function(){if(k<TS[sc].steps.length)k++;tsr();};LAB.$('#ts13r').onclick=function(){k=0;tsr();};tsc.children[0].click();
'''
PAGE['labs'] += ',lab13b:{setup:"CREATE DATABASE rpg; USE rpg; CREATE TABLE 캐릭터 (이름 VARCHAR(10) PRIMARY KEY, 골드 INT CHECK (골드 >= 0)); CREATE TABLE 매물 (매물번호 INT PRIMARY KEY, 아이템 VARCHAR(20), 가격 INT, 판매자 VARCHAR(10), 상태 VARCHAR(10)); CREATE TABLE 인벤토리 (이름 VARCHAR(10), 아이템 VARCHAR(20), FOREIGN KEY (이름) REFERENCES 캐릭터(이름)); CREATE TABLE 퀘스트진행 (이름 VARCHAR(10), 퀘스트 VARCHAR(20), 상태 VARCHAR(10)); INSERT INTO 캐릭터 VALUES (\'레온\',5000),(\'미라\',300),(\'보리\',0); INSERT INTO 매물 VALUES (7,\'전설의 검\',1000,\'보리\',\'판매중\'),(8,\'용의 방패\',800,\'보리\',\'판매중\'); INSERT INTO 퀘스트진행 VALUES (\'레온\',\'슬라임 사냥\',\'진행중\');",presets:[{t:"① 정상 거래 (레온이 검 구매)",q:"START TRANSACTION;\\nUPDATE 캐릭터 SET 골드 = 골드 - 1000 WHERE 이름 = \'레온\';\\nUPDATE 캐릭터 SET 골드 = 골드 + 1000 WHERE 이름 = \'보리\';\\nINSERT INTO 인벤토리 VALUES (\'레온\', \'전설의 검\');\\nUPDATE 매물 SET 상태 = \'판매완료\' WHERE 매물번호 = 7;\\nCOMMIT;\\nSELECT * FROM 캐릭터;"},{t:"② 잔액 부족 (미라가 방패 구매)",q:"-- 미라는 300골드뿐. 두 번째 문장에서 CHECK(골드 >= 0) 위반\\nSTART TRANSACTION;\\nUPDATE 캐릭터 SET 골드 = 골드 + 800 WHERE 이름 = \'보리\';\\nUPDATE 캐릭터 SET 골드 = 골드 - 800 WHERE 이름 = \'미라\';"},{t:"③ 반쪽 상태 확인 후 ROLLBACK",q:"-- ②의 첫 문장(보리 +800)만 반영된 반쪽 상태\\nSELECT * FROM 캐릭터;\\nROLLBACK;\\nSELECT * FROM 캐릭터;"},{t:"④ 퀘스트 보상 — 한 트랜잭션",q:"START TRANSACTION;\\nUPDATE 퀘스트진행 SET 상태 = \'완료\' WHERE 이름 = \'레온\' AND 퀘스트 = \'슬라임 사냥\';\\nUPDATE 캐릭터 SET 골드 = 골드 + 200 WHERE 이름 = \'레온\';\\nINSERT INTO 인벤토리 VALUES (\'레온\', \'슬라임 젤리\');\\nCOMMIT;\\nSELECT * FROM 퀘스트진행;\\nSELECT * FROM 인벤토리;"}],ready:"RPG 거래소: 캐릭터 3명(레온 5,000 · 미라 300 · 보리 0골드), 매물 2개. ②→③은 이어서 실행하세요."}'
