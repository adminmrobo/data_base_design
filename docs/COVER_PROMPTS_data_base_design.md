# 표지 지시문 모음 — 데이터베이스 설계 (data_base_design)

SKILL v1.15 18-14 규칙 — **그림체는 16비트 RPG풍 픽셀아트 필수(고정)**. 매끈한 일러스트·벡터·3D로 받으면 다시 생성한다(18-15). 목차 1장 + 회차 15장(키 `cover_index`, `cover_01`~`cover_15`). 모든 표지는 넷 모두 등장, 16:9, 글자 없음. 생물 앵커가 아니므로 현미경·초파리 해부 소품을 넣지 않는다(18-13).

**참고 이미지 (함께 올리기):** 네 캐릭터 기본 그림 4장 (기준: GitHub `adminmrobo/fruitfly-lab-expressions`).

그림을 받으면 `assets/img/cover_{N}.webp`(1600×900, 220 KB 이하)로 바꿔 넣고, 각 페이지 맨 위 `<!-- lab-cover -->` 픽셀 대체 표지(픽셀 소품 + 픽셀 캐릭터 넷)를 18-15 절차로 교체한다. 받은 그림이 픽셀아트가 아니면 쓰지 않는다. `cover_manifest.json`의 해당 항목 `status`도 바꾼다.

<a id="cover_index"></a>

## 00 데이터베이스 설계 (목차)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_index · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `index.html` |
| 장소 (앵커) | B 연구실 · 방이 줄지은 복도 |
| 주제 은유 | 15개의 방문이 줄지은 밝은 복도, 8번과 15번 방문만 초록색 |
| 네 캐릭터 포즈 | 박사가 가운데 뒤에서 벽의 큰 지도를 가리킴 / 조수가 빈 점수판을 들고 옆에 섬 / 초파리가 왼쪽에서 첫 문을 바라봄 / 주판봇이 오른쪽에서 마지막 문을 바라봄 |
| 대체 글 (alt) | 밝은 연구실 복도에 열다섯 개의 문이 줄지어 있고 네 캐릭터가 벽의 지도를 올려다보는 표지 |
| 앞 표지와 다른 점 | 시리즈 첫 표지 — 복도 전경 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a long bright corridor of the lab with fifteen identical doors in a row, two of the doors painted mint green, a big blank map of circles and lines on the wall, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a long bright corridor of the lab with fifteen identical doors in a row, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the blank wall map.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_01"></a>

## 01 과목 사용 설명서

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_01 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w01_course_guide.html` |
| 장소 (앵커) | D 쇼핑몰 화면 뒤편 |
| 주제 은유 | 투명한 쇼핑 앱 화면 뒤로 보이는 정리된 서랍장 |
| 네 캐릭터 포즈 | 박사가 화면 뒤를 가리킴 / 조수가 장바구니를 듦 / 초파리가 왼쪽에서 서랍장을 봄 / 주판봇이 오른쪽에서 흩어진 종이 더미를 봄 |
| 대체 글 (alt) | 투명한 쇼핑 화면 뒤에 정리된 서랍장이 보이고 네 캐릭터가 그 뒤편을 들여다보는 표지 |
| 앞 표지와 다른 점 | 화면 뒤 서랍장 — 복도·지도 없음 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a giant transparent shopping app screen standing in the lab, behind it a neat cabinet of labeled-less drawers glowing softly, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a giant transparent shopping app screen standing in the lab, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the drawer cabinet.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_02"></a>

## 02 데이터와 데이터베이스

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_02 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w02_data_and_database.html` |
| 장소 (앵커) | B 연구실 창고 |
| 주제 은유 | 원재료 상자와 정리된 선반 사이의 저울 |
| 네 캐릭터 포즈 | 박사가 저울 뒤에 섬 / 조수가 선반에 상자를 올림 / 초파리가 왼쪽에서 원재료 상자를 봄 / 주판봇이 오른쪽에서 선반을 봄 |
| 대체 글 (alt) | 원재료 상자와 정리된 선반 사이에 저울이 놓인 창고 장면 |
| 앞 표지와 다른 점 | 창고와 저울 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a storage room with raw unlabeled crates on one side and tidy shelves on the other, a brass scale between them, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a storage room with raw unlabeled crates on one side and tidy shelves on the other, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the brass scale.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_03"></a>

## 03 DBMS

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_03 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w03_dbms.html` |
| 장소 (앵커) | C 금고실 |
| 주제 은유 | 두 개의 금고 문 — 하나는 낡은 서류함, 하나는 관리인이 지키는 금고 |
| 네 캐릭터 포즈 | 박사가 금고 문 옆 / 조수가 서류 한 장을 듦 / 초파리가 왼쪽에서 금고를 봄 / 주판봇이 오른쪽에서 서류함을 봄 |
| 대체 글 (alt) | 낡은 서류함과 관리되는 금고 문이 나란한 금고실 장면 |
| 앞 표지와 다른 점 | 금고실 — 창고 장면과 다름 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a vault room with an old filing cabinet overflowing with copies on the left and a round vault door with a small control panel on the right, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a vault room with an old filing cabinet overflowing with copies on the left and a round vault door with a small control panel on the right, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the round vault door.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_04"></a>

## 04 데이터베이스 시스템

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_04 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w04_database_system.html` |
| 장소 (앵커) | B 세 층 건물 모형 |
| 주제 은유 | 세 층으로 나뉜 투명 건물 모형과 층 사이 계단 |
| 네 캐릭터 포즈 | 박사가 모형의 가운데 층을 가리킴 / 조수가 위층 창을 들여다봄 / 초파리가 왼쪽에서 아래층을 봄 / 주판봇이 오른쪽에서 맨 아래 상자를 엶 |
| 대체 글 (alt) | 세 층 투명 건물 모형을 네 캐릭터가 층별로 들여다보는 장면 |
| 앞 표지와 다른 점 | 세 층 모형 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a transparent three-story building model on a lab table, each floor a different pastel color, small staircases linking the floors, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a transparent three-story building model on a lab table, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the middle floor of the model.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_05"></a>

## 05 데이터 모델링 (E-R)

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_05 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w05_er_modeling.html` |
| 장소 (앵커) | D 도서관 설계실 |
| 주제 은유 | 네모·동그라미·마름모 나무 블록과 연결 끈 |
| 네 캐릭터 포즈 | 박사가 마름모 블록을 듦 / 조수가 끈을 연결함 / 초파리가 왼쪽에서 네모 블록을 봄 / 주판봇이 오른쪽에서 큰 상자 하나에 모두 넣으려 함 |
| 대체 글 (alt) | 네모·동그라미·마름모 블록을 끈으로 잇는 설계 탁자 장면 |
| 앞 표지와 다른 점 | 블록과 끈 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a library design room, wooden blocks shaped as rectangles, ovals and diamonds on a big table connected by colored strings, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a library design room, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the diamond block.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_06"></a>

## 06 관계 데이터 모델

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_06 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w06_relational_model.html` |
| 장소 (앵커) | B 열쇠 보관함 |
| 주제 은유 | 열쇠가 꽂힌 표 모양 보관함, 열쇠마다 다른 모양 |
| 네 캐릭터 포즈 | 박사가 열쇠 하나를 듦 / 조수가 리본을 따라감 / 초파리가 왼쪽에서 보관함을 봄 / 주판봇이 오른쪽에서 열쇠 꾸러미를 셈 |
| 대체 글 (alt) | 격자 모양 열쇠 보관함과 리본으로 이어진 열쇠들을 보는 장면 |
| 앞 표지와 다른 점 | 열쇠 보관함 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a wall key cabinet shaped like a grid table, each slot holding a differently shaped key, a few keys connected by thin ribbons to another cabinet, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a wall key cabinet shaped like a grid table, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the glowing key.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_07"></a>

## 07 관계 데이터 연산

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_07 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w07_relational_operations.html` |
| 장소 (앵커) | B 체 거르기 실험대 |
| 주제 은유 | 카드 더미를 거르는 체와 카드를 맞물리는 톱니 |
| 네 캐릭터 포즈 | 박사가 톱니 기계 옆 / 조수가 체를 흔듦 / 초파리가 왼쪽에서 걸러진 카드를 봄 / 주판봇이 오른쪽에서 거대한 카드 더미를 봄 |
| 대체 글 (alt) | 체로 카드를 거르고 톱니로 카드 더미를 맞물리는 실험대 장면 |
| 앞 표지와 다른 점 | 체와 톱니 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a lab bench with a sieve sorting colored cards, two stacks of cards being zipped together by a small gear machine, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a lab bench with a sieve sorting colored cards, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the sieve.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_08"></a>

## 08 중간 REVIEW

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_08 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w08_midterm_review.html` |
| 장소 (앵커) | B 복도 중간의 초록 문 |
| 주제 은유 | 열린 초록 문 안 벽에 붙은 일곱 장의 지도 |
| 네 캐릭터 포즈 | 박사가 지도를 가리킴 / 조수가 카드 묶음을 듦 / 초파리가 왼쪽에서 짧은 메모를 듦 / 주판봇이 오른쪽에서 두꺼운 노트를 듦 |
| 대체 글 (alt) | 복도 중간 초록 문 안에 일곱 장의 지도가 걸린 복습 방 장면 |
| 앞 표지와 다른 점 | 중간 쉼터 방 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a mint green door wide open in the middle of the corridor, inside a small room with seven framed blank maps on the wall, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a mint green door wide open in the middle of the corridor, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the seven maps.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_09"></a>

## 09 SQL ① 데이터 정의

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_09 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w09_sql_ddl.html` |
| 장소 (앵커) | B 틀 만들기 공방 |
| 주제 은유 | 빈 진열장 틀과 규칙 도장, 틀에 새겨지는 홈 |
| 네 캐릭터 포즈 | 박사가 도장을 듦 / 조수가 틀을 받침 / 초파리가 왼쪽에서 홈이 새겨진 틀을 봄 / 주판봇이 오른쪽에서 체크리스트 판을 봄 |
| 대체 글 (alt) | 빈 진열장 틀에 규칙 홈을 새기는 공방 장면 |
| 앞 표지와 다른 점 | 공방 — 진열장 틀 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a workshop corner where empty display shelves are being built, small stamping tools carving grooves into the shelf frames, a blank rulebook stand, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a workshop corner where empty display shelves are being built, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the carved shelf frame.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_10"></a>

## 10 SQL ② 데이터 조작

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_10 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w10_sql_dml.html` |
| 장소 (앵커) | D 마트 창고 |
| 주제 은유 | 선반에서 꺼내지는 상자, 상자를 묶는 끈과 바구니 |
| 네 캐릭터 포즈 | 박사가 바구니를 듦 / 조수가 상자를 묶음 / 초파리가 왼쪽에서 선반을 봄 / 주판봇이 오른쪽에서 바구니 두 개를 비교함 |
| 대체 글 (alt) | 마트 창고 선반에서 상자를 골라 바구니에 묶는 장면 |
| 앞 표지와 다른 점 | 마트 창고 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a bright market storeroom, labeled-less boxes being picked from shelves into baskets, some boxes grouped with ribbons, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a bright market storeroom, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the ribbon-grouped boxes.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_11"></a>

## 11 데이터베이스 설계 5단계

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_11 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w11_database_design_process.html` |
| 장소 (앵커) | D 설계실 |
| 주제 은유 | 메모 종이 더미 → 설계도 → 도면 → 모형으로 이어지는 다섯 탁자 |
| 네 캐릭터 포즈 | 박사가 가운데 탁자 뒤 / 조수가 메모를 읽음 / 초파리가 왼쪽에서 첫 탁자를 봄 / 주판봇이 오른쪽에서 끝 모형에 바로 손을 뻗음 |
| 대체 글 (alt) | 메모에서 모형까지 다섯 탁자가 이어진 설계실 장면 |
| 앞 표지와 다른 점 | 다섯 탁자의 흐름 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a design studio with five tables in a row: a pile of sticky notes, a sketch of boxes and diamonds, a blueprint, a material sample board, a finished small cabinet model, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a design studio with five tables in a row: a pile of sticky notes, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the row of five tables.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_12"></a>

## 12 정규화

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_12 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w12_normalization.html` |
| 장소 (앵커) | B 재단 탁자 |
| 주제 은유 | 큰 장부 한 장을 가위로 네 장의 깔끔한 카드로 나누기 |
| 네 캐릭터 포즈 | 박사가 가위를 듦 / 조수가 카드를 정리 / 초파리가 왼쪽에서 점선을 봄 / 주판봇이 오른쪽에서 큰 장부를 붙잡음 |
| 대체 글 (alt) | 커다란 장부를 네 장으로 자르는 재단 탁자 장면 |
| 앞 표지와 다른 점 | 재단 탁자 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a cutting table with one huge messy ledger sheet being cut by big scissors into four neat cards, a dotted line showing they still fit back together, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a cutting table with one huge messy ledger sheet being cut by big scissors into four neat cards, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the scissors and dotted line.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_13"></a>

## 13 트랜잭션 · 회복 · 병행 제어

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_13 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w13_transaction_recovery_concurrency.html` |
| 장소 (앵커) | C 은행 창구 |
| 주제 은유 | 두 창구가 한 금고를 공유, 한쪽에는 열쇠 걸이, 바닥의 일지책 |
| 네 캐릭터 포즈 | 박사가 일지책 옆 / 조수가 열쇠를 듦 / 초파리가 왼쪽에서 열쇠 걸이를 봄 / 주판봇이 오른쪽에서 동전을 바로 넣으려 함 |
| 대체 글 (alt) | 두 창구가 한 금고를 함께 쓰는 은행 창구 장면 |
| 앞 표지와 다른 점 | 은행 창구 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a small bank counter with two windows sharing one round vault, a key hook beside one window, an open logbook on a stand, a few coins on the counter, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a small bank counter with two windows sharing one round vault, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the shared vault.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_14"></a>

## 14 데이터베이스 응용 기술

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_14 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w14_database_applications.html` |
| 장소 (앵커) | D 우편물 분류실 |
| 주제 은유 | 서류철 책장, 스티커가 붙은 봉투 더미, 사진 상자, 찾아보기 카드함 |
| 네 캐릭터 포즈 | 박사가 카드함 옆 / 조수가 사진 상자를 듦 / 초파리가 왼쪽에서 서류철 책장을 봄 / 주판봇이 오른쪽에서 봉투 더미를 봄 |
| 대체 글 (alt) | 서류철·봉투·사진 상자를 어디에 담을지 고르는 분류실 장면 |
| 앞 표지와 다른 점 | 분류실 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: a mail sorting room with a bookcase of binders, a pile of envelopes with blank colorful stickers, boxes of photos, a small index card drawer, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: a mail sorting room with a bookcase of binders, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the envelope pile.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`

<a id="cover_15"></a>

## 15 기말 REVIEW

| 항목 | 내용 |
|---|---|
| 키 · 판 | cover_15 · L (16:9, 1920 이상) |
| 그림체 | 16비트 RPG풍 픽셀아트 (필수, 고정) |
| 페이지 | `weeks/w15_final_review.html` |
| 장소 (앵커) | B 복도 끝 초록 문 |
| 주제 은유 | 복도 끝 두 번째 초록 문, 안에 여섯 장의 지도와 졸업 모자 |
| 네 캐릭터 포즈 | 박사가 저울을 듦 / 조수가 카드 묶음을 듦 / 초파리가 왼쪽에서 지도를 봄 / 주판봇이 오른쪽에서 지도를 봄 (같은 높이) |
| 대체 글 (alt) | 복도 끝 초록 문 안에 여섯 장의 지도와 졸업 모자가 놓인 복습 방 장면 |
| 앞 표지와 다른 점 | 기말 방 — 중간 방과 다른 졸업 모자 |

**Genspark에 붙여 넣기 ↓**
```
웹페이지 맨 위에 거는 표지 그림 1장을 만들어 줘.
- 비율 16:9, 가로 1920px 이상
- 그림체는 반드시 16비트 RPG풍 픽셀아트 (네모 픽셀이 보이게, 매끈한 일러스트·벡터·수채화·3D 금지)
- 첨부한 참고 이미지의 네 캐릭터(박사, 조수, 초파리 연구원, 주판봇)를 같은 외형으로, 넷 모두 픽셀아트로 등장
- 그림 안에 글자·숫자·로고를 넣지 말 것
- 얼굴과 손은 가장자리에서 떨어진 가운데 영역에, 왼쪽 아래 구석은 밝고 단순하게
아래 영어 프롬프트를 그대로 써 줘.

Website top cover illustration, wide 16:9.
Art style (required, always): 16-bit RPG style pixel art with clearly visible square pixels, limited palette, bold dark outline,
  2–3 tone shading, small highlights; no smooth gradients, no painterly, vector, watercolor or 3D look.
Match the characters' proportions and colors of the attached reference images exactly, drawn in this same pixel-art style.
bright daytime laboratory mood, soft natural sunlight through large windows, clean white walls, light lavender, mint and pink accents.
Scene: the second mint green door at the end of the corridor, inside a room with six framed blank maps and a graduation cap on a stand, rendered as part of the same bright daytime lab world, a few lavender lab items on one side.
All four characters together:
  the chibi scientist, thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back, white lab coat over black vest and tie, at the back center;
  the girl researcher, long pink hair with two round buns and a navy streak, blue eyes, white lab coat over lavender hoodie, jeans, at one side;
  the anthropomorphic fruit fly researcher, black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables, white lab coat over a black vest, black gloves, transparent wings, on the left facing right;
  the boxy beige retro CRT-monitor robot, dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads, on the right facing left.
Visual metaphor of the topic: the second mint green door at the end of the corridor, no writing anywhere.
Composition: keep every face and hand inside the central safe area (12% margin left and right, 10% top, 18% bottom);
  keep the bottom-left corner plain, bright and simple; the light falls on the six maps.
Mood: curious, friendly rivalry, the moment before the result.
No text, no letters, no numbers, no logos, no weapons, no cigarettes, no alcohol, no blood, no real brands.
```

**고칠 때 (같은 대화에서):** `Same four characters, same 16-bit pixel-art style and composition. Change only: {고칠 점}. Still pixel art, still no text.`
