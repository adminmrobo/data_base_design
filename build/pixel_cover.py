# 픽셀 대체 표지 (SKILL v1.15 · 18-14-5)
# 장면 48×27 칸 SVG — 창문·바닥 타일·주제 소품을 모두 네모 칸으로 그린다 (shape-rendering="crispEdges").
# 소품은 페이지마다 24×16 칸 안에 주제 은유를 그린다.
W, H = 48, 22
K = '#2a2f3a'   # 외곽선
PAL = dict(k=K, w='#ffffff', g='#e3e8ee', G='#c9d2dc', s='#9aa5b1', b='#cfe0f7', B='#5b86c9', m='#cdeedd', M='#2f9a62',
           p='#f3d6ea', P='#c42a6e', l='#e6dcf7', L='#7a3fd6', y='#fbe7b0', Y='#d69e2e', o='#f4c7a1', O='#b8642b',
           r='#f6c6c3', R='#c93030', t='#bfe6ea', T='#0b7a86', n='#8a6a4a', N='#5e4630')


class Grid:
    def __init__(s, w, h):
        s.w, s.h, s.c = w, h, [[None] * w for _ in range(h)]

    def px(s, x, y, col):
        if 0 <= x < s.w and 0 <= y < s.h:
            s.c[y][x] = col

    def rect(s, x, y, w, h, fill, line=K):
        for j in range(h):
            for i in range(w):
                edge = line and (i in (0, w - 1) or j in (0, h - 1))
                s.px(x + i, y + j, line if edge else fill)

    def fill(s, x, y, w, h, col):
        s.rect(x, y, w, h, col, None)

    def hline(s, x, y, n, col=K):
        for i in range(n): s.px(x + i, y, col)

    def vline(s, x, y, n, col=K):
        for j in range(n): s.px(x, y + j, col)

    def disc(s, cx, cy, r, fill, line=K):  # 픽셀 원 (칸 단위)
        for y in range(cy - r, cy + r + 1):
            for x in range(cx - r, cx + r + 1):
                d = (x - cx) ** 2 + (y - cy) ** 2
                if d <= r * r + r * 0.6:
                    s.px(x, y, line if d > (r - 1) ** 2 + (r - 1) * 0.6 else fill)

    def diamond(s, cx, cy, r, fill, line=K):
        for y in range(cy - r, cy + r + 1):
            k = r - abs(y - cy)
            for x in range(cx - k, cx + k + 1):
                s.px(x, y, line if abs(x - cx) == k else fill)

    def blit(s, o, ox, oy):
        for y in range(o.h):
            for x in range(o.w):
                if o.c[y][x]: s.px(ox + x, oy + y, o.c[y][x])


def P(c): return PAL.get(c, c)


# ---------- 주제 소품 (24×16) ----------
def door(g, x, y, col, open_=False):
    g.rect(x, y, 4, 8, P(col)); g.px(x + 3 if not open_ else x + 1, y + 4, P('Y'))
    if open_: g.fill(x + 1, y + 1, 2, 6, P('w'))


def frame(g, x, y, col='w'):
    g.rect(x, y, 4, 4, P(col)); g.fill(x + 1, y + 1, 2, 1, P('b')); g.fill(x + 1, y + 2, 2, 1, P('m'))


def prop(num):
    g = Grid(24, 16)
    if num == '00':                       # 복도의 15개 문 (8·15번만 초록)
        g.fill(0, 4, 24, 1, P('G'))
        for i in range(5): door(g, 1 + i * 5, 6, 'm' if i in (2, 4) else 'g')
        g.rect(6, 0, 12, 4, P('w')); g.hline(8, 2, 8, P('B'))
        g.fill(0, 14, 24, 2, P('G'))
    elif num == '01':                     # 쇼핑 화면 뒤의 서랍장
        g.rect(13, 2, 10, 13, P('y'))
        for j in range(4): g.rect(14, 3 + j * 3, 8, 3, P('w')); g.px(17, 4 + j * 3, P('Y')); g.px(18, 4 + j * 3, P('Y'))
        g.rect(2, 1, 9, 14, P('b')); g.fill(3, 2, 7, 2, P('B'))
        for j in range(3): g.rect(4, 5 + j * 3, 5, 2, P('w'))
        g.hline(11, 8, 2, P('s'))
    elif num == '02':                     # 원재료 상자 · 저울 · 선반
        for (x, y) in ((1, 9), (5, 9), (3, 5)): g.rect(x, y, 4, 4, P('o')); g.hline(x + 1, y + 2, 2, P('O'))
        g.vline(12, 4, 9); g.hline(8, 4, 9); g.rect(7, 5, 3, 2, P('y')); g.rect(15, 5, 3, 2, P('y')); g.rect(10, 13, 5, 2, P('s'))
        g.rect(18, 1, 6, 14, P('n'))
        for j in range(3): g.hline(18, 5 + j * 4, 6); g.fill(19, 3 + j * 4, 2, 2, P('m')); g.fill(21, 3 + j * 4, 2, 2, P('b'))
    elif num == '03':                     # 넘치는 서류함 · 둥근 금고 문
        g.rect(1, 4, 7, 11, P('g'))
        for j in range(3): g.fill(2, 5 + j * 3, 5, 2, P('w')); g.hline(4, 6 + j * 3, 1, P('s'))
        for (x, y) in ((2, 2), (5, 1), (8, 3)): g.rect(x, y, 3, 2, P('w'))
        g.disc(16, 8, 6, P('G')); g.disc(16, 8, 3, P('y')); g.px(16, 8, P('Y'))
        g.rect(21, 6, 3, 4, P('t')); g.px(22, 7, P('T'))
    elif num == '04':                     # 세 층 투명 건물 모형
        cols = ('l', 'm', 'b')
        for j, c in enumerate(cols):
            g.rect(5, 1 + j * 4, 14, 5, P(c))
            for i in range(3): g.fill(7 + i * 4, 3 + j * 4, 2, 1, P('w'))
        g.vline(4, 3, 10, P('s')); g.vline(19, 3, 10, P('s'))
        g.fill(2, 14, 20, 2, P('G'))
    elif num == '05':                     # 네모·동그라미·마름모 블록과 끈
        g.rect(1, 6, 6, 4, P('b')); g.rect(17, 6, 6, 4, P('b'))
        g.diamond(12, 8, 3, P('l')); g.disc(4, 2, 2, P('y')); g.disc(20, 2, 2, P('y')); g.disc(12, 13, 2, P('m'))
        g.hline(7, 8, 2, P('R')); g.hline(16, 8, 1, P('R')); g.vline(4, 4, 2, P('R')); g.vline(20, 4, 2, P('R')); g.vline(12, 11, 1, P('R'))
    elif num == '06':                     # 격자 열쇠 보관함
        g.rect(2, 1, 14, 14, P('n'))
        for j in range(4):
            for i in range(4):
                g.fill(3 + i * 3, 2 + j * 3, 2, 2, P('y')); g.px(3 + i * 3, 2 + j * 3, P('Y' if (i + j) % 3 else 'R'))
        g.rect(18, 4, 5, 8, P('n')); g.rect(19, 5, 3, 3, P('w')); g.px(20, 6, P('Y'))
        g.hline(16, 6, 3, P('B'))
    elif num == '07':                     # 체 거르기 · 카드 맞물리기
        for i in range(4): g.rect(1 + i * 2, 0 + i, 4, 3, P('pbmy'[i]))
        g.rect(0, 6, 11, 3, P('G')); g.fill(1, 7, 9, 1, P('w'))
        for i in range(3): g.px(2 + i * 3, 7, P('s'))
        g.rect(3, 11, 4, 3, P('m'))
        g.disc(17, 8, 3, P('G')); g.disc(17, 8, 1, P('s'))
        g.rect(13, 1, 4, 3, P('b')); g.rect(18, 1, 4, 3, P('p')); g.rect(15, 12, 5, 3, P('l'))
    elif num in ('08', '15'):             # 초록 문 방 — 중간 7장 / 기말 6장 + 학사모
        g.rect(0, 2, 6, 13, P('m')); g.fill(2, 3, 3, 11, P('w')); g.px(4, 9, P('Y'))
        n = 7 if num == '08' else 6
        for i in range(n): frame(g, 7 + (i % 4) * 4, 2 + (i // 4) * 5)
        if num == '15':
            g.fill(15, 12, 7, 1, K); g.fill(16, 11, 5, 1, K); g.fill(17, 13, 3, 2, K); g.px(21, 13, P('Y')); g.px(21, 14, P('Y'))
        else:
            g.rect(17, 11, 5, 4, P('y'))
    elif num == '09':                     # 진열장 틀에 규칙 홈 새기기
        g.rect(1, 1, 14, 14, P('w'))
        for j in range(3): g.hline(1, 5 + j * 3, 14); g.hline(3, 4 + j * 3, 4, P('B'))
        g.rect(17, 3, 4, 3, P('R')); g.fill(18, 6, 2, 5, P('n')); g.rect(16, 11, 6, 2, P('G'))
    elif num == '10':                     # 마트 선반 · 바구니 · 묶은 상자
        g.rect(0, 0, 11, 15, P('n'))
        for j in range(3):
            g.hline(0, 5 + j * 4, 11)
            for i in range(3): g.fill(1 + i * 3, 2 + j * 4, 2, 3, P('ybo'[(i + j) % 3]))
        g.rect(14, 8, 9, 6, P('y')); g.hline(15, 10, 7, P('Y')); g.hline(15, 7, 7, P('O'))
        g.rect(16, 3, 3, 3, P('b')); g.rect(19, 3, 3, 3, P('m')); g.vline(19, 3, 3, P('R'))
    elif num == '11':                     # 다섯 탁자 — 메모 → 스케치 → 도면 → 자재 → 모형
        for i in range(5):
            x = i * 5; g.fill(x, 12, 4, 1, P('n')); g.vline(x, 13, 2, P('N')); g.vline(x + 3, 13, 2, P('N'))
        g.rect(0, 8, 3, 3, P('y')); g.rect(1, 6, 3, 3, P('y'))
        g.rect(5, 7, 4, 4, P('w')); g.diamond(7, 9, 1, P('l'))
        g.rect(10, 7, 4, 4, P('B')); g.hline(11, 9, 2, P('w'))
        g.rect(15, 8, 4, 3, P('G')); g.px(16, 9, P('o')); g.px(17, 9, P('m'))
        g.rect(20, 5, 4, 6, P('n')); g.hline(20, 8, 4)
    elif num == '12':                     # 큰 장부 한 장 → 가위 → 네 장의 카드
        g.rect(0, 1, 10, 13, P('r'))
        for j in range(4): g.hline(1, 3 + j * 3, 8, P('R'))
        g.rect(11, 5, 2, 2, P('s')); g.rect(11, 8, 2, 2, P('s')); g.px(13, 6, K); g.px(13, 8, K); g.hline(14, 7, 2, K)
        for k, (x, y) in enumerate(((17, 1), (21, 1), (17, 8), (21, 8))): g.rect(x, y, 3, 6, P('mblp'[k]))
        for y in range(1, 15, 2): g.px(16, y, P('s'))
    elif num == '13':                     # 두 창구 · 하나의 금고 · 열쇠 걸이 · 일지
        g.rect(0, 2, 7, 6, P('b')); g.rect(17, 2, 7, 6, P('b'))
        g.fill(0, 9, 24, 2, P('n'))
        g.disc(12, 5, 4, P('y')); g.px(12, 5, P('O'))
        g.vline(3, 11, 3, P('s')); g.px(3, 14, P('Y')); g.px(4, 14, P('Y'))
        g.rect(9, 12, 6, 3, P('w')); g.vline(12, 12, 3)
        g.px(19, 12, P('Y')); g.px(21, 13, P('Y')); g.px(20, 14, P('Y'))
    elif num == '14':                     # 서류철 책장 · 스티커 봉투 · 사진 상자 · 카드함
        g.rect(0, 1, 8, 14, P('n'))
        for i in range(3): g.fill(1 + i * 2, 2, 2, 5, P('Blm'[i])); g.fill(1 + i * 2, 8, 2, 6, P('YpB'[i]))
        g.hline(0, 7, 8)
        for k, (x, y) in enumerate(((10, 3), (13, 5), (10, 8))): g.rect(x, y, 5, 3, P('w')); g.px(x + 3, y + 1, P('PRB'[k]))
        g.rect(16, 10, 7, 5, P('o')); g.rect(17, 11, 3, 3, P('b')); g.px(18, 12, P('M'))
        g.rect(17, 2, 6, 5, P('g')); g.fill(18, 3, 4, 1, P('w')); g.fill(18, 5, 4, 1, P('w'))
    return g


def scene(num):
    g = Grid(W, H)
    # 벽 · 창문(네모 칸) · 바닥 타일
    for (x, y) in ((2, 2), (38, 2)):
        g.rect(x, y, 8, 7, P('b')); g.vline(x + 4, y, 7); g.hline(x, y + 3, 8); g.px(x + 2, y + 1, P('w')); g.px(x + 6, y + 1, P('w'))
    g.blit(prop(num), 12, 2)
    out = []
    for y in range(H):
        x = 0
        while x < W:
            c = g.c[y][x]
            if c is None:
                x += 1; continue
            x2 = x
            while x2 + 1 < W and g.c[y][x2 + 1] == c: x2 += 1
            out.append('<rect x="%d" y="%d" width="%d" height="1" fill="%s"/>' % (x, y, x2 - x + 1, c))
            x = x2 + 1
    return ('<svg class="px-scene" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet" shape-rendering="crispEdges" '
            'aria-hidden="true" focusable="false">%s</svg>') % (W, H, ''.join(out))


if __name__ == '__main__':
    import sys
    for n in ['00'] + ['%02d' % i for i in range(1, 16)]:
        open('/tmp/px_%s.svg' % n, 'w').write(scene(n).replace('<svg ', '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" '))
    print('ok')
