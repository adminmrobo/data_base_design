# 데이터베이스 설계 연구실 — 15회차 해설

강남대학교 「데이터베이스 설계」(2025년 2학기) 강의를 회차별 **연구실 해설 페이지**로 만든 사이트입니다.
박사·조수 하루·초파리 연구원·주판봇이 회차마다 개념을 4칸 사다리로 풀고, 초파리와 주판봇의 대결로 판단 기준을 보여 줍니다.
SQL 실습은 노션 실습 페이지의 예제를 **설치 없이 브라우저 안 실습실(MariaDB 흉내 엔진)**에서 바로 실행합니다.

- **저자** 안상선 ((주)M-Robo 대표)
- **교재** 김연희, 『데이터베이스 개론』(3판), 한빛아카데미 — 출판 연도 확인 필요
- **노션 강의 페이지** https://mrobo2016.notion.site/2025-2-1ab17a4520ed81cd9040dbae826a48ad
- **라이선스** CC BY-NC 4.0 (비상업적 이용, 출처 표기)

## 보기

- 첫 화면 — https://adminmrobo.github.io/data_base_design/ (GitHub Pages를 켠 뒤)
- 파일을 내려받았다면 `index.html`을 브라우저로 열면 됩니다. 페이지마다 CSS·JS·그림이 한 파일에 들어 있습니다.

## 15회차

| 회차 | 페이지 | 교재 | 대결 |
|---|---|---|---|
| 1 | [과목 사용 설명서](weeks/w01_course_guide.html) | — | 초파리 승 |
| 2 | [데이터와 데이터베이스](weeks/w02_data_and_database.html) | 1장 | 주판봇 승 |
| 3 | [DBMS](weeks/w03_dbms.html) | 2장 | 조건부 |
| 4 | [데이터베이스 시스템](weeks/w04_database_system.html) | 3장 | 주판봇 실격 |
| 5 | [데이터 모델링 (E-R)](weeks/w05_er_modeling.html) | 4장 | 초파리 승 |
| 6 | [관계 데이터 모델](weeks/w06_relational_model.html) | 5장 | 무승부 |
| 7 | [관계 데이터 연산](weeks/w07_relational_operations.html) | 6장 | 초파리 승 |
| 8 | [**중간 REVIEW**](weeks/w08_midterm_review.html) | 1~6장 | 주판봇 승 |
| 9 | [SQL ① 데이터 정의](weeks/w09_sql_ddl.html) | 7장 | 주판봇 승 |
| 10 | [SQL ② 데이터 조작](weeks/w10_sql_dml.html) | 7장 | 무승부 |
| 11 | [데이터베이스 설계 5단계](weeks/w11_database_design_process.html) | 8장 | 초파리 승 |
| 12 | [정규화](weeks/w12_normalization.html) | 9장 | 조건부 |
| 13 | [트랜잭션 · 회복 · 병행 제어](weeks/w13_transaction_recovery_concurrency.html) | 10장 | 초파리 승 |
| 14 | [데이터베이스 응용 기술](weeks/w14_database_applications.html) | — | 주판봇 승 |
| 15 | [**기말 REVIEW**](weeks/w15_final_review.html) | 7~10장 | 무승부 |

노션 일정표의 주차 번호(예: 10주차 정규화)는 이 사이트와 다릅니다. 각 회차의 N 상자가 해당 노션 페이지를 가리킵니다.

## 구성

```
index.html                  첫 화면 (15회차 목차, 도구 안내, 보관함)
weeks/w01~w15_*.html        회차 페이지 (단일 파일)
data/KG_00_registry.json    시리즈 지식 그래프 등록부
cover_manifest.json         표지 그림 현황 (16장 모두 반영, 2026-11-22)
assets/img/                 표지 WebP (1600·960) · src/ 원본 PNG
docs/
  COVER_PROMPTS_data_base_design.md   표지 16장 생성 지시문
  REVIEW_supoja_persona.md            수포자 기준(P1~P7)·페르소나 감사 보고서
build/
  build.py                  빌드 (python3 build/build.py)
  pages/index.py, w01~w15.py  회차별 원고
  lab.css, lab.js, kgx.js   공통 스타일·위젯·지식 색인
  minisql.js                SQL 실습실 엔진 (MariaDB 문법 일부를 흉내 냄)
  sprites/                  캐릭터 표정 (96px)
archive/database_01of04/    이전 판 (보관, 더 이상 고치지 않음)
```

## 빌드

```bash
python3 build/build.py
```

`build/pages/wNN.py`를 고친 뒤 실행하면 `weeks/`와 `index.html`, `data/`, `cover_manifest.json`이 다시 만들어집니다.

## SQL 실습실에 대해

실습실은 실제 MariaDB가 아니라 이 강의에 필요한 문법(CREATE·ALTER·DROP, 제약 조건, SELECT·JOIN·GROUP BY·부속 질의, 뷰, 트랜잭션)을 흉내 낸 작은 엔진입니다.
오류 메시지는 MariaDB의 오류 번호를 따르지만, 색인(`CREATE INDEX`, `EXPLAIN`)과 실제 권한(GRANT·REVOKE)은 지원하지 않습니다.
과제·시험 전에는 실제 MariaDB에서 한 번 더 실행해 보세요(설치: 1주차 안내).

## 이전 저장소

이 저장소는 [adminmrobo/database_01of04](https://github.com/adminmrobo/database_01of04)(「데이터베이스 설계 — 야간 연구실」, 1~4주)를 흡수했습니다.
이전 판의 파일과 커밋 기록은 `archive/database_01of04/`에 보관하며 더 이상 고치지 않습니다.
