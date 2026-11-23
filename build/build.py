#!/usr/bin/env python3
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))
# -*- coding: utf-8 -*-
"""데이터베이스 설계 — 연구실 해설 시리즈 빌드
   build/pages/wNN.py (페이지 명세) → weeks/wNN_slug.html (단일 파일), index.html, cover_manifest.json, data/KG_00_registry.json
   사용: python3 build/build.py   (캐릭터 그림 팩 경로는 환경변수 LAB_PACK, 기본 ../adminmrobo/ahnboat_lab_explainer/...)"""
import os, re, json, base64, html, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PACK = os.environ.get('LAB_PACK', os.path.join(HERE, 'sprites'))
CSS = open(os.path.join(HERE, 'lab.css'), encoding='utf-8').read()
JS = open(os.path.join(HERE, 'minisql.js'), encoding='utf-8').read() + '\n' + open(os.path.join(HERE, 'lab.js'), encoding='utf-8').read()
KGX = open(os.path.join(HERE, 'kgx.js'), encoding='utf-8').read()
TODAY = '2026-11-22'
COVER_RECEIVED = '2026-11-22'
SITE = 'https://adminmrobo.github.io/data_base_design/'
REPO = 'https://github.com/adminmrobo/data_base_design'
NOTION = 'https://mrobo2016.notion.site/'
SERIES = '데이터베이스 설계 연구실'
AUTHOR = '안상선'
AUTHOR_FULL = '안상선 ((주)M-Robo 대표)'
LICENSE = 'CC BY-NC 4.0'
E = html.escape

ALIAS = {'doc_front':'doc_e08','doc_board':'doc_e07','doc_judge':'doc_e10','doc_verdict':'doc_e18','doc_magic':'doc_e16','doc_think':'doc_e09',
 'asst_smile':'asst_e13','asst_firm':'asst_e12','asst_report':'asst_e07','asst_spark':'asst_e01','asst_shock':'asst_e24','asst_sigh':'asst_e02','asst_proud':'asst_e16',
 'fly_clip':'fly_e10','fly_point':'fly_e08','fly_arms':'fly_e16','fly_coffee':'fly_e13','fly_cry':'fly_e21','fly_type':'fly_e09','fly_magnify':'fly_e07',
 'robo_smile':'robo_e13','robo_coin':'robo_e16','robo_chart':'robo_e07','robo_happy':'robo_e12','robo_sigh':'robo_e20','robo_meh':'robo_e18','robo_cry':'robo_e21','robo_wow':'robo_e04','robo_blush':'robo_e14','robo_calc':'robo_e09',
 'sia_smile':'sia_e13','sia_sleepy':'sia_e22','moa_smile':'moa_e13','moa_cheer':'moa_e12'}
NAMES = {'doc':'박사','asst':'조수(하루)','fly':'초파리 연구원','robo':'주판봇','sia':'인턴 시아','moa':'인턴 모아'}
DUEL_KEYS = ['fly_point','robo_coin','fly_arms','robo_sigh','doc_judge','asst_spark','fly_cry','fly_coffee','robo_happy','doc_think','asst_smile','robo_meh','asst_report','robo_calc','asst_shock','robo_blush','doc_front','asst_firm']

def sprite_b64(key):
    k = ALIAS.get(key, key)
    who = k.split('_')[0]
    p = os.path.join(PACK, who, k + '.webp')
    if not os.path.exists(p):
        return None
    return 'data:image/webp;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def face(who, mood='front', size=56, cls=''):
    return '<img data-who="%s" data-mood="%s" width="%d" height="%d" alt="" aria-hidden="true"%s>' % (who, mood, size, size, (' class="%s"' % cls) if cls else '')

def say(who, mood, text):
    return '<div class="say">%s<div class="bub"><span class="who w-%s">%s</span><p>%s</p></div></div>' % (face(who, mood), who, NAMES[who], text)

def notion_box(items):
    out = []
    for t, url, d in items:
        out.append('<div class="notion"><span class="nb">N</span><a href="%s" target="_blank" rel="noopener">%s ↗</a><span>%s</span></div>' % (E(url), t, d))
    return ''.join(out)

def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

# ── 지식 그래프 자동 생성 (스킬 O1-8 규칙) ─────────────────────────
def build_kg(P, fname):
    page = P['id']
    nodes, edges, seen = [], [], set()
    def N(id, type, ko, en, anchor, **kw):
        if id in seen:
            return
        seen.add(id)
        n = {'id': id, 'type': type, 'label': {'ko': ko, 'en': en}, 'page': page, 'anchor': anchor,
             'domain': ['db'], 'status': 'known', 'confidence': kw.pop('confidence', 'high')}
        n.update({k: v for k, v in kw.items() if v is not None})
        nodes.append(n)
    def L(s, p, o, anchor, conf='high'):
        edges.append({'s': s, 'p': 'lab:' + p, 'o': o, 'anchor': anchor, 'confidence': conf})
    topic = 'lab:topic/db-w%s' % P['num']
    N(topic, 'Topic', P['title'], P['title_en'], '#top', definition={'ko': P['question']})
    N('lab:topic/database-design', 'Area', '데이터베이스 설계', 'database design', '#top', definition={'ko': '데이터를 정확하고 효율적으로 저장·관리하도록 구조를 정하는 일.'})
    L(topic, 'broader', 'lab:topic/database-design', '#top')
    if P.get('practice'):
        pid = 'lab:simulation/%s-practice' % page
        N(pid, 'Simulation', '실전 연습장 — ' + P['practice']['title'], 'practice dashboard: ' + P['practice'].get('en', P['title_en']), '#practice',
          definition={'ko': re.sub('<[^>]+>', '', P['practice']['scenario'])[:160]})
        L(topic, 'demonstratedBy', pid, '#practice')
    steps = P['steps']
    cids = []
    for i, s in enumerate(steps):
        cid = s.get('cid') or ('lab:concept/' + slugify(s['en']))
        cids.append(cid)
        anc = '#' + s['id']
        N(cid, s.get('ctype', 'Concept'), s['concept'], s['en'], anc, definition={'ko': s['def']}, level=i + 1, family='db', anchorType=P.get('anchor', 'D'), flyStrength='none',
          evidence=[f[0] for f in P.get('facts', []) if f[4] == s['id']] or None)
        L(cid, 'broader', topic, anc)
        sec = 'lab:section/%s-%s' % (page, s['id'])
        N(sec, 'Section', '%s 칸 %d' % (P['short'], i + 1), 'step %d' % (i + 1), anc)
        L(cid, 'explainedIn', sec, anc)
        if i > 0:
            L(cids[i - 1], 'prerequisiteOf', cid, anc)
        if s.get('limit'):
            lid = 'lab:limitation/%s-%s' % (page, s['id'])
            N(lid, 'Limitation', s['limit_label'], s.get('limit_en', 'limitation of ' + s['en']), anc, definition={'ko': s['limit']})
            L(cid, 'hasLimitation', lid, anc)
            if i + 1 < len(steps):
                nxt = steps[i + 1].get('cid') or ('lab:concept/' + slugify(steps[i + 1]['en']))
                L(lid, 'addressedBy', nxt, '#' + steps[i + 1]['id'])
        if s.get('pair'):
            aid = 'lab:analogy/%s-%s' % (page, s['id'])
            N(aid, 'Analogy', s.get('analogy', s['pair'][0][0]), 'analogy: ' + s['en'], anc, definition={'ko': re.sub('<[^>]+>', '', s['pair'][0][1])[:160]})
            L(aid, 'analogyOf', cid, anc)
        if s.get('sim'):
            sid = 'lab:simulation/%s-%s' % (page, s['id'])
            N(sid, 'Simulation', s['sim'], 'simulation: ' + s['en'], anc)
            L(cid, 'demonstratedBy', sid, anc)
        for qi, q in enumerate(s.get('quiz', [])):
            qid = 'lab:quiz/%s-%s-%d' % (page, s['id'], qi + 1)
            N(qid, 'QuizItem', re.sub('<[^>]+>', '', q['q'])[:60], 'quiz %s-%d' % (s['id'], qi + 1), anc)
            L(qid, 'assesses', cid, anc)
    # 용어
    for k, g in P.get('gloss', {}).items():
        tid = 'lab:term/' + g[3]
        stepid = g[4] if len(g) > 4 else steps[0]['id']
        N(tid, 'Term' if g[1] in ('기호', '용어', '명령어') else 'Concept', k, g[3].replace('-', ' '), '#' + stepid, definition={'ko': g[2]})
        ci = [s['id'] for s in steps].index(stepid) if stepid in [s['id'] for s in steps] else 0
        L(tid, 'explainedIn', 'lab:section/%s-%s' % (page, steps[ci]['id']), '#' + stepid)
        L(tid, 'partOf', cids[ci], '#' + stepid)
    # 문헌
    for r in P['refs']:
        N('lab:work/' + r['id'], 'Work', r['title'], r.get('title_en', r['title']), '#sources')
    # 사실 → 주장
    for f in P.get('facts', []):
        fid, text, kind, ref, stepid, loc = f
        cl = 'lab:claim/%s-%s' % (page, fid.lower())
        if kind == '미확인':
            N(cl.replace('claim', 'question'), 'Question', text, 'open question ' + fid, '#' + stepid, confidence='low')
            ci = [s['id'] for s in steps].index(stepid)
            L(cids[ci], 'raises', cl.replace('claim', 'question'), '#' + stepid, 'low')
            continue
        N(cl, 'Claim', text, 'claim ' + fid, '#' + stepid, evidence=[fid], source=[{'ref': ref, 'loc': loc}])
        ci = [s['id'] for s in steps].index(stepid) if stepid in [s['id'] for s in steps] else 0
        L(cl, 'supports', cids[ci], '#' + stepid)
        L(cl, 'assertedIn', 'lab:work/' + ref, '#' + stepid)
    used = {f[3] for f in P.get('facts', []) if f[2] != '미확인'}
    for r in P['refs']:
        if r['id'] not in used:
            L(topic, 'derivedFrom', 'lab:work/' + r['id'], '#sources')
    # 질문
    N('lab:question/%s-core' % page, 'Question', P['question'], 'core question', '#top')
    L(topic, 'raises', 'lab:question/%s-core' % page, '#top')
    d = P['duel']
    dq = 'lab:question/%s-duel' % page
    N(dq, 'Question', d['q'], 'duel question', '#duel')
    L(cids[-1], 'raises', dq, '#duel')
    m1, m2, mt = 'lab:method/%s-fly' % page, 'lab:method/%s-robo' % page, 'lab:metric/%s' % page
    N(m1, 'Method', d['fly_pick'], 'option A (fly)', '#duel', definition={'ko': d['fly_line']})
    N(m2, 'Method', d['robo_pick'], 'option B (jupanbot)', '#duel', definition={'ko': d['robo_line']})
    N(mt, 'Metric', d['metric'], 'duel metric', '#duel')
    L(m1, 'contrastsWith', m2, '#duel'); L(m1, 'evaluatedBy', mt, '#duel'); L(m2, 'evaluatedBy', mt, '#duel')
    L(m1, 'relatedTo', cids[d.get('step', len(cids) - 1)], '#duel'); L(m2, 'relatedTo', cids[d.get('step', len(cids) - 1)], '#duel')
    # 앞뒤 회차
    for pre in P.get('prereq', []):
        pid = 'lab:topic/db-w%s' % pre
        N(pid, 'Topic', '%s주차' % int(pre), 'week %d' % int(pre), '#top')
        L(pid, 'prerequisiteOf', topic, '#top')
    kg = {'version': '1.0', 'page': page, 'domain': ['db'], 'nodes': nodes, 'edges': edges}
    # 점검
    ids = {n['id'] for n in nodes}
    for e in edges:
        assert e['s'] in ids and e['o'] in ids, (page, e)
    deg = {i: 0 for i in ids}
    for e in edges:
        deg[e['s']] += 1; deg[e['o']] += 1
    iso = [i for i, v in deg.items() if v == 0]
    assert not iso, (page, iso)
    return kg

def jsonld(kg, meta):
    ctx = {'@vocab': 'urn:lab:', 'lab': 'urn:lab:', 'skos': 'http://www.w3.org/2004/02/skos/core#', 'schema': 'https://schema.org/',
           'dct': 'http://purl.org/dc/terms/', 'prov': 'http://www.w3.org/ns/prov#', 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'}
    g = []
    for n in kg['nodes']:
        t = ['lab:' + n['type']]
        if n['type'] in ('Concept', 'Method', 'Term', 'Limitation', 'Metric', 'Topic', 'Area'):
            t += ['skos:Concept', 'schema:DefinedTerm']
        o = {'@id': n['id'], '@type': t, 'skos:prefLabel': [{'@value': n['label']['ko'], '@language': 'ko'}, {'@value': n['label']['en'], '@language': 'en'}]}
        if n.get('definition'):
            o['skos:definition'] = {'@value': n['definition']['ko'], '@language': 'ko'}
        g.append(o)
    for e in kg['edges']:
        g.append({'@id': e['s'], e['p']: {'@id': e['o']}})
    g.append({'@id': meta['url'] or ('urn:page:' + meta['number']), '@type': 'schema:LearningResource', 'schema:name': meta['title'], 'schema:inLanguage': 'ko',
              'schema:author': {'@type': 'schema:Person', 'schema:name': AUTHOR}, 'schema:license': LICENSE})
    return {'@context': ctx, '@graph': g}

# ── 페이지 조립 ─────────────────────────────────────────────
def esc_json(o):
    return json.dumps(o, ensure_ascii=False).replace('</', '<\\/')

_ALT = None
def cover_alt(key, alt):
    global _ALT
    if _ALT is None:
        import re as _r
        _ALT = {}
        p = os.path.join(ROOT, 'docs', 'COVER_PROMPTS_data_base_design.md')
        if os.path.exists(p):
            for m in _r.finditer(r'<a id="(cover_\w+)"></a>.*?\| 대체 글 \(alt\) \| (.*?) \|', open(p, encoding='utf-8').read(), _r.S):
                _ALT[m.group(1)] = m.group(2).strip()
    return _ALT.get(key, alt)

def cover_img(key, alt, pre):
    alt = cover_alt(key, alt)
    f = os.path.join(ROOT, 'assets', 'img', key + '.webp')
    if not os.path.exists(f):
        return None
    return ('<img class="cover-img" src="%sassets/img/%s.webp" srcset="%sassets/img/%s_960.webp 960w, %sassets/img/%s.webp 1600w" '
            'sizes="100vw" width="1600" height="900" alt="%s" fetchpriority="high" decoding="async">') % (pre, key, pre, key, pre, key, E(alt))

def cover(P, strip=False):
    im = cover_img('cover_%s' % P['num'], P['cover_alt'], '../')
    if im:
        return ('<!-- lab-cover --><header class="cover has-img%s" id="cover" data-img="cover_%s">%s'
                '<span class="cover-chip">%s · %s</span></header><!-- /lab-cover -->') % (' cover-strip' if strip else '', P['num'], im, SERIES, P['chip'])
    import pixel_cover
    prop = pixel_cover.scene(P['num'])
    shelf = ''.join(face(w, m, 128) for w, m in (('fly', 'point'), ('asst', 'smile'), ('doc', 'front'), ('robo', 'coin')))
    return ('<!-- lab-cover --><header class="cover%s" id="cover" data-img="cover_%s" role="img" aria-label="%s">'
            '%s<div class="shelf">%s</div>'
            '<span class="cover-chip">%s · %s</span></header><!-- /lab-cover -->') % (
        ' cover-strip' if strip else '', P['num'], E(P['cover_alt']), prop, shelf, SERIES, P['chip'])

def step_html(P, i, s):
    h = ['<section class="level" id="%s">' % s['id'], '<div class="wrap">']
    h.append('<div class="lvhead"><span class="hex">%d</span><div><h2>%s</h2><span class="tag m">개념: %s</span><span class="tag a">%s</span></div></div>' % (i + 1, s['title'], s['concept'], s['tag']))
    if s.get('situation'):
        h.append('<p class="kicker" style="margin-top:10px">상황</p><p>%s</p>' % s['situation'])
    if s.get('pair'):
        (lt, lb), (rt, rb) = s['pair']
        h.append('<div class="pair"><div><h4>%s</h4><p>%s</p></div><div><h4>%s</h4><p>%s</p></div></div>' % (lt, lb, rt, rb))
    if s.get('body'):
        h.append(s['body'])
    if s.get('panel'):
        h.append('<div class="panel"><p class="ptitle">%s</p>%s</div>' % (s.get('panel_title', '직접 해 보기'), s['panel']))
    if s.get('flow'):
        f = s['flow']
        h.append('<div class="panel"><p class="ptitle">행동으로 보기 — %s</p><canvas class="cv flow" id="%s" style="height:%dpx" role="img" aria-label="%s"></canvas><p class="cvcap">%s</p></div>' % (
            f['title'], f['id'], f.get('h', 230), E(f['alt']), f['cap']))
    if s.get('explain'):
        h.append('<div class="explain"><b>풀어서 보면</b>%s%s</div>' % (s['explain'], ('<p class="limit"><b>이 칸의 한계 —</b> %s</p>' % s['limit']) if s.get('limit') else ''))
    if s.get('formula'):
        h.append('<details><summary>%s</summary>%s</details>' % (s.get('formula_title', '더 깊이 — 정확한 정의'), s['formula']))
    if s.get('aicheck'):
        h.append('<div class="ai-check"><h4>AI·도구 결과 판단 코너</h4>%s</div>' % s['aicheck'])
    if s.get('bridge'):
        g, f, lim = s['bridge']
        h.append('<div class="bridge"><div class="gen"><h4>생성 AI로 치면</h4><p>%s</p></div><div class="field"><h4>현장에 옮기면</h4><p>%s</p></div></div><p class="limit">%s</p>' % (g, f, lim))
    if s.get('say'):
        h.append(say(*s['say']))
    if s.get('quiz'):
        h.append('<div class="quiz" data-quiz="%s"></div>' % s['id'])
    h.append('</div></section>')
    return '\n'.join(h)

def duel_html(d):
    return '''<section class="level" id="duel"><div class="wrap">
<h2>대결 — %s</h2><p>%s</p>
<div class="duel" id="duelbox">
 <div class="head"><div>%s<div><b>초파리 연구원</b></div></div><div class="vs">VS</div><div>%s<div><b>주판봇</b></div></div></div>
 <div class="cards"><div><b>초파리의 선택: %s</b><p>“%s”</p></div><div><b>주판봇의 선택: %s</b><p>“%s”</p></div></div>
 <p style="margin:6px 0 4px;font-size:14px;color:#5b6874">먼저 맞혀 보기 — 판정 기준: <b>%s</b></p>
 <div class="ctrl guess"><button type="button" class="bt" aria-pressed="false">초파리가 이길 것 같다</button><button type="button" class="bt" aria-pressed="false">주판봇이 이길 것 같다</button><span class="gnote" style="font-size:13px;color:#5b6874"></span></div>
 <div class="ctrl"><button type="button" class="bt primary go">결과 보기</button><button type="button" class="bt reset">다시 닫기</button></div>
 <div class="res" aria-live="polite">
  <div class="bars"><div class="bar f"><span>초파리</span><i><s></s></i><b></b></div><div class="bar r"><span>주판봇</span><i><s></s></i><b></b></div></div>
  <div class="say">%s<div class="bub"><span class="who w-asst">조수(하루)</span><p class="ann"></p></div></div>
  <div class="say">%s<div class="bub"><span class="who w-doc">박사</span><p class="ver"></p></div></div>
 </div>
</div>
%s
</div></section>''' % (d['q'], d['intro'], face('fly', 'point', 84), face('robo', 'coin', 84), d['fly_pick'], d['fly_line'], d['robo_pick'], d['robo_line'], d['metric'],
       face('asst', 'firm'), face('doc', 'front'), d.get('after', ''))

def page_html(P, prev, nxt, fname):
    kg = build_kg(P, fname)
    url = SITE + 'weeks/' + fname
    meta = {'title': P['title'] + ' — ' + P['subtitle'], 'series': SERIES, 'number': P['num'],
            'creator': [{'name': AUTHOR_FULL, 'role': 'author'}], 'contributor': [{'name': 'AI 보조 제작', 'role': 'assistant'}],
            'date': TODAY, 'version': '1.0', 'language': ['ko'], 'license': LICENSE, 'url': url,
            'about': [kg['nodes'][2]['id']] + [n['id'] for n in kg['nodes'] if n['type'] == 'Concept'][:5],
            'educationalLevel': '입문~중급 (학부 전공 기초)', 'learningResourceType': 'interactive explainer',
            'basedOn': [r['id'] for r in P['refs']], 'registry': 'data/KG_00_registry.json',
            'suggestedCitation': '%s (2026). %s — %s. %s %s, v1.0. %s' % (AUTHOR, P['title'], P['subtitle'], SERIES, P['num'], url)}
    refs = []
    for r in P['refs']:
        c = {k: v for k, v in r.items() if k not in ('title_en', 'role', 'verified', 'supports', 'note')}
        c['lab'] = {'work': 'lab:work/' + r['id'], 'role': r.get('role', 'background'), 'supports': r.get('supports', []),
                    'verified': r.get('verified', {'title': True, 'authors': True, 'year': True}), 'checkedBy': '저자 자료·웹 확인 ' + TODAY, 'note': r.get('note', '')}
        refs.append(c)
    # 그림 키 수집
    body_parts = []
    body_parts.append('<nav class="top" aria-label="이 페이지 차례"><a class="brand" href="../index.html"><span class="hex">DB</span>%s</a><div class="links">%s</div></nav>' % (
        SERIES, ''.join('<a href="#%s">%s</a>' % a for a in [('top', '처음'), ('crew', '사용법'), ('why', '왜')] + [(s['id'], '%d %s' % (i + 1, s['short'])) for i, s in enumerate(P['steps'])] + P.get('nav_extra', []) + [('duel', '대결'), ('summary', '정리')] + ([('practice', '연습장')] if P.get('practice') else []) + [('kg', '색인'), ('export', '꾸러미')])))
    body_parts.append(cover(P))
    talk = ''.join(say(*t) for t in P['hero_talk'])
    kp = ''.join('<div><b>%s</b><span>%s</span></div>' % (a, b) for a, b in P['kpis'])
    body_parts.append('<main id="top"><header class="hero"><div class="wrap"><div class="kicker">%s</div><h1>%s</h1><p class="question">%s</p>%s'
                      '<section class="kpis" aria-label="이 페이지의 숫자 요약">%s</section><p style="font-size:13px;color:#5b6874">%s</p><div class="talk">%s</div></div></header>' % (
                          P['kicker'], P['title'] + '<br><span style="font-size:.55em;color:#5b6874">' + P['subtitle'] + '</span>', P['question'], P['intro'], kp, P.get('kpi_note', ''), talk))
    crew = ''.join('<div>%s<div><b>%s</b><span>%s</span></div></div>' % (face(w, m, 52), NAMES[w], r) for w, m, r in P['crew'])
    body_parts.append('<section class="level" id="crew"><div class="wrap"><h2>등장인물과 이 페이지 사용법</h2><div class="crew">%s</div>'
                      '<div class="steps"><div><b>밑줄 친 낱말</b>점선 밑줄을 누르거나 손가락으로 대면 뜻이 나옵니다.</div><div><b>직접 해 보기</b>버튼·SQL 실습실은 눌러도 아무것도 망가지지 않습니다. 언제든 「처음 상태로」.</div><div><b>진행 표시</b><span id="qprog">퀴즈 0/0</span> · 맨 위 초록 막대는 읽은 만큼 차오릅니다.</div></div>%s%s</div></section>' % (
                          crew, ('<div class="recap"><b>30초 복습 — </b>%s</div>' % P['recap']) if P.get('recap') else '', notion_box(P.get('notion', []))))
    why = ''.join('<div><span class="n">%d</span><b>%s</b>%s</div>' % (i + 1, a, b) for i, (a, b) in enumerate(P['why']))
    body_parts.append('<section class="level" id="why"><div class="wrap"><h2>%s</h2><div class="steps">%s</div>%s%s</div></section>' % (P.get('why_title', '왜 이 주제인가'), why, P.get('bigpicture', ''), say(*P['why_say']) if P.get('why_say') else ''))
    for i, s in enumerate(P['steps']):
        body_parts.append(step_html(P, i, s))
    for xs in P.get('extra_sections', []):
        body_parts.append(xs)
    body_parts.append(duel_html(P['duel']))
    body_parts.append('<section class="level" id="summary"><div class="wrap"><h2>정리 — 한 장으로</h2>%s</div></section>' % P['summary'])
    body_parts.append('<section class="level outro" id="outro"><div class="wrap"><h2>오늘의 마무리</h2><div class="talk">%s</div>%s</div></section>' % (''.join(say(*t) for t in P['outro']), P.get('next_note', '')))
    if P.get('practice'):
        pr = P['practice']
        tasks = ''.join('<li><label><input type="checkbox"> %s</label></li>' % t for t in pr.get('tasks', []))
        body_parts.append('<section class="level practice" id="practice"><div class="wrap"><h2>실전 연습장 — %s</h2><p class="kicker">%s</p><div class="pr-scn">%s</div>'
                          '<div class="dash" id="dash">%s</div>%s%s</div></section>' % (
            pr['title'], pr.get('kicker', '배운 것을 대시보드에서 직접 돌려 보기'), pr['scenario'], pr['html'],
            ('<div class="pr-tasks"><h3>미션</h3><ol>%s</ol></div>' % tasks) if tasks else '', pr.get('after', '')))
    body_parts.append('<section class="kgx kgx-sec level" id="kg"><div class="kgx-wrap"><h2>지식 색인 — 이 페이지에서 찾아보기</h2><p class="kgx-sub">이 페이지에 나온 개념, 용어, 주장, 열린 질문을 한곳에 모았습니다. 검색하고, 항목을 눌러 관계를 보고, "본문"으로 돌아갑니다.</p><div id="kg-mount"></div></div></section>')
    body_parts.append('<section class="kgx kgx-sec level" id="export"><div class="kgx-wrap"><h2>온톨로지·서지 꾸러미 — 이 페이지의 지식을 가져가기</h2><p class="kgx-sub">지식 색인을 출처와 함께 파일로 내려받습니다. Zotero(BibTeX·RIS), Protégé(Turtle), Neo4j·Gephi(CSV), 여러 페이지 합치기(kg.json)에 씁니다.</p><div id="export-mount"></div></div></section></main>')
    # 바닥글
    src_rows = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (E(r['title']), E(', '.join(a.get('family', a.get('literal', '')) + a.get('given', '') for a in r.get('author', [])) or r.get('publisher', '')), ('<a href="%s" target="_blank" rel="noopener">열기</a>' % E(r['URL'])) if r.get('URL') else '') for r in P['refs'])
    pager = '<div class="pager">%s%s</div>' % (
        ('<a href="%s"><small>← 이전</small>%s</a>' % (prev[0], E(prev[1]))) if prev else '<span></span>',
        ('<a href="%s" style="text-align:right"><small>다음 →</small>%s</a>' % (nxt[0], E(nxt[1]))) if nxt else '<a href="../index.html" style="text-align:right"><small>처음으로</small>목차</a>')
    foot = ('<footer id="sources"><div class="wrap"><h4>출처</h4><div class="tbl"><table><thead><tr><th>자료</th><th>저자·발행</th><th>링크</th></tr></thead><tbody>%s</tbody></table></div>'
            '<h4>예시값·설명용 모형인 것</h4><ul>%s</ul><h4>이 페이지</h4><p>글 · %s · 시리즈 「%s」 %s · 라이선스 %s · <a href="%s">저장소</a> · <a href="../index.html">목차</a></p>'
            '<p>캐릭터 그림: 연구실 캐릭터 팩(fruitfly-lab-expressions). SQL 실습실은 브라우저 안에서 MariaDB 문법을 흉내 낸 교육용 모의 엔진이며, 실제 서버 결과와 다를 수 있습니다(특히 오류 번호·경고 문구).</p>%s</div></footer>') % (
        src_rows, ''.join('<li>%s</li>' % x for x in P['models']), AUTHOR_FULL, SERIES, P['num'], LICENSE, REPO, pager)
    body = '\n'.join(body_parts) + '\n' + foot
    # 그림
    keys = set(re.findall(r'data-who="(\w+)" data-mood="(\w+)"', body))
    want = {'%s_%s' % k for k in keys} | set(DUEL_KEYS) | {'doc_front', 'asst_smile', 'fly_clip', 'robo_smile'}
    sprites = {}
    for k in sorted(want):
        b = sprite_b64(k)
        if b:
            sprites[ALIAS.get(k, k)] = b
    quiz = {s['id']: s['quiz'] for s in P['steps'] if s.get('quiz')}
    quiz.update(P.get('extra_quiz', {}))
    data_js = 'var SPRITE=%s;\nvar QUIZ=%s;\nvar GL=%s;\nvar FLOWS={%s};\nvar LABS={%s};\nvar CARDS=%s;\n' % (
        esc_json(sprites), esc_json(quiz), esc_json({k: v[:3] for k, v in P.get('gloss', {}).items()}),
        ','.join('%s:%s' % (json.dumps(s['flow']['id']), s['flow']['js']) for s in P['steps'] if s.get('flow')) + (',' + P['flows_extra'] if P.get('flows_extra') else ''),
        ','.join(x for x in [P.get('labs', ''), P.get('practice', {}).get('labs', '')] if x), esc_json(P.get('cards', {})))
    duel_js = 'var DUEL={el:"#duelbox",higherIsBetter:%s,drawMargin:%s,run:function(){%s},announce:function(r){%s},verdict:function(res,r){%s}};' % (
        'true' if P['duel'].get('higher', True) else 'false', P['duel'].get('margin', 0), P['duel']['run'], P['duel']['announce'], P['duel']['verdict'])
    head_meta = ''.join('<meta name="%s" content="%s">' % (k, E(v)) for k, v in [
        ('description', P['desc']), ('citation_title', meta['title']), ('citation_author', AUTHOR), ('citation_publication_date', '2026/11/20'),
        ('citation_language', 'ko'), ('dc.title', meta['title']), ('dc.creator', AUTHOR), ('dc.date', TODAY), ('dc.language', 'ko'), ('dc.rights', LICENSE),
        ('dcterms.isPartOf', SERIES)])
    doc = '''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s — %s · %s</title>%s
<meta property="og:title" content="%s"><meta property="og:type" content="article"><meta property="og:url" content="%s"><meta property="og:image" content="__OGIMG__">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>%s%s</style></head>
<body><div id="prog"></div><div id="tip" role="tooltip"></div>
%s
<script type="application/json" id="kg-raw">%s</script>
<script type="application/ld+json" id="kg-ld">%s</script>
<script type="application/json" id="refs-csl">%s</script>
<script type="application/json" id="page-meta">%s</script>
<script>%s
%s
var PAGE={init:function(LAB){%s}};
</script>
<script>%s</script>
<script>%s</script>
</body></html>''' % (P['title'], P['subtitle'], SERIES, head_meta, E(meta['title']), url, CSS, P.get('css', ''), body,
                     esc_json(kg), esc_json(jsonld(kg, meta)), esc_json(refs), esc_json(meta), data_js, duel_js, P.get('js', '') + '\n;(function(){' + P.get('practice', {}).get('js', '') + '})();', JS, KGX)
    return doc.replace("__OGIMG__", SITE + "assets/img/cover_%s.webp" % P["num"]), kg

# ── 목차 ─────────────────────────────────────────────────
def index_html(pages, IDX):
    cards = []
    for P, fn in pages:
        rev = P['kind'] == 'review'
        cards.append('<a href="weeks/%s"%s><span class="wk">%s</span><b>%s</b><span>%s</span><div class="imgs">%s</div></a>' % (
            fn, ' class="rev"' if rev else '', P['chip'], E(P['title']), E(P['toc']), ''.join(face(w, m, 30) for w, m in P.get('toc_faces', [('doc', 'front'), ('asst', 'smile')]))))
    body = IDX['body'].replace('{{TOC}}', '<div class="toc">%s</div>' % ''.join(cards))
    shelf = ''.join(face(w, m, 128) for w, m in (('fly', 'point'), ('asst', 'proud'), ('doc', 'front'), ('robo', 'smile')))
    cov = ('<!-- lab-cover --><header class="cover" id="cover" data-img="cover_index" role="img" aria-label="%s">%s<div class="shelf">%s</div>'
           '<span class="cover-chip">%s · 목차</span></header><!-- /lab-cover -->') % (E(IDX['cover_alt']), __import__('pixel_cover').scene('00'), shelf, SERIES)
    _im = cover_img('cover_index', IDX['cover_alt'], '')
    if _im:
        cov = ('<!-- lab-cover --><header class="cover has-img" id="cover" data-img="cover_index">%s'
               '<span class="cover-chip">%s · 목차</span></header><!-- /lab-cover -->') % (_im, SERIES)
    keys = set(re.findall(r'data-who="(\w+)" data-mood="(\w+)"', body + cov + ''.join(cards)))
    sprites = {}
    for k in sorted({'%s_%s' % k for k in keys}):
        b = sprite_b64(k)
        if b:
            sprites[ALIAS.get(k, k)] = b
    return '''<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s — 데이터베이스 설계 15회차 연구실 해설</title><meta name="description" content="%s">
<meta property="og:title" content="%s"><meta property="og:url" content="%s"><meta property="og:image" content="__OGIDX__">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>%s</style></head><body><div id="prog"></div><div id="tip"></div>
<nav class="top"><a class="brand" href="index.html"><span class="hex">DB</span>%s</a><div class="links"><a href="#course">강좌 안내</a><a href="#toc">15회차</a><a href="#how">공부하는 법</a><a href="#tools">실습 도구</a><a href="#archive">보관함</a></div></nav>
%s<main id="top">%s</main>
<script>var SPRITE=%s;</script><script>%s</script></body></html>''' % (
        SERIES, E(IDX['desc']), SERIES, SITE, CSS, SERIES, cov, body, esc_json(sprites), JS)

def main():
    specs = sorted(glob.glob(os.path.join(HERE, 'pages', 'w*.py')))
    pages = []
    for f in specs:
        g = {'say': say, 'face': face, 'NOTION': NOTION, 'E': E}
        exec(open(f, encoding='utf-8').read(), g)
        P = g['PAGE']
        P.setdefault('id', 'db_w' + P['num'])
        if 'practice' not in P:
            import practice_a, practice_b
            PR = dict(practice_a.PRACTICE); PR.update(practice_b.PRACTICE)
            if P['num'] in PR:
                P['practice'] = PR[P['num']]
        fn = 'w%s_%s.html' % (P['num'], P['slug'])
        pages.append((P, fn))
    os.makedirs(os.path.join(ROOT, 'weeks'), exist_ok=True)
    registry = {'version': '1.0', 'series': SERIES, 'updated': TODAY, 'domain': 'db', 'ids': {}}
    report = []
    for i, (P, fn) in enumerate(pages):
        prev = (pages[i - 1][1], pages[i - 1][0]['chip'] + ' ' + pages[i - 1][0]['title']) if i else None
        nxt = (pages[i + 1][1], pages[i + 1][0]['chip'] + ' ' + pages[i + 1][0]['title']) if i + 1 < len(pages) else None
        doc, kg = page_html(P, prev, nxt, fn)
        open(os.path.join(ROOT, 'weeks', fn), 'w', encoding='utf-8').write(doc)
        for n in kg['nodes']:
            if n['type'] in ('Concept', 'Term', 'Topic', 'Area', 'Method', 'Work'):
                registry['ids'].setdefault(n['id'], {'ko': n['label']['ko'], 'en': n['label']['en'], 'type': n['type'], 'pages': []})
                if P['id'] not in registry['ids'][n['id']]['pages']:
                    registry['ids'][n['id']]['pages'].append(P['id'])
        nq = sum(len(s.get('quiz', [])) for s in P['steps']) + sum(len(v) for v in P.get('extra_quiz', {}).values())
        report.append('%s %-34s %6.0f KB  nodes %3d edges %3d quiz %2d' % (P['num'], fn, len(doc.encode()) / 1024, len(kg['nodes']), len(kg['edges']), nq))
    IDX = {}
    exec(open(os.path.join(HERE, 'pages', 'index.py'), encoding='utf-8').read(), {'face': face, 'say': say, 'NOTION': NOTION, 'E': E, 'IDX': IDX})
    open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(index_html(pages, IDX).replace('__OGIDX__', SITE + 'assets/img/cover_index.webp'))
    os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)
    json.dump(registry, open(os.path.join(ROOT, 'data', 'KG_00_registry.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # 표지 목록 (현황판 연결, 스킬 18-16)
    import re as _re
    _pr = {}
    _cp = os.path.join(ROOT, 'docs', 'COVER_PROMPTS_data_base_design.md')
    if os.path.exists(_cp):
        for _m in _re.finditer(r'<a id="(cover_\w+)"></a>.*?아래 영어 프롬프트를 그대로 써 줘\.\n\n(.*?)\n```', open(_cp, encoding='utf-8').read(), _re.S):
            _pr[_m.group(1)] = _m.group(2).strip()
    def _item(key, page):
        f = os.path.join(ROOT, 'assets', 'img', key + '.webp'); ok = os.path.exists(f)
        it = {'id': key, 'role': 'cover', 'path': 'assets/img/%s.webp' % key if ok else None, 'page': page, 'size': [1600, 900],
              'characters': ['doc', 'asst', 'fly', 'jupanbot'], 'robot': 'jupanbot-v2' if ok else 'none', 'prompt_en': _pr.get(key),
              'source_of': None, 'status': 'ok' if ok else 'redraw'}
        if ok:
            it['kb'] = round(os.path.getsize(f) / 1024, 1); it['received'] = COVER_RECEIVED
        return [it] + ([{'id': key + '_960', 'role': 'cover', 'path': 'assets/img/%s_960.webp' % key, 'page': page, 'size': [960, 540],
                         'characters': ['doc', 'asst', 'fly', 'jupanbot'], 'robot': 'jupanbot-v2', 'prompt_en': None, 'source_of': key, 'status': 'ok'}] if ok else [])
    items = _item('cover_index', 'index.html')
    for P, fn in pages:
        items += _item('cover_%s' % P['num'], 'weeks/' + fn)
    man = {'series_ko': SERIES, 'title_ko': '데이터베이스 설계 15회차 (중간·기말 REVIEW 포함)', 'site_url': SITE, 'site_title': SERIES,
           'ontology': {'pages': [{'path': 'index.html', 'kg': False, 'export': False}] + [{'path': 'weeks/' + fn, 'kg': True, 'export': True} for P, fn in pages],
                        'registry': 'data/KG_00_registry.json'},
           'i18n': {'langs': ['ko'], 'pages': {'ko': len(pages) + 1}, 'readme_langs': ['ko']},
           'items': items, 'updated': TODAY,
           'archive': {'from': 'adminmrobo/database_01of04', 'path': 'archive/database_01of04/', 'status': 'archived'}}
    json.dump(man, open(os.path.join(ROOT, 'cover_manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('\n'.join(report))

if __name__ == '__main__':
    main()


# ── 분야 뼈대 다시 걸기 (kg/rehang.json, ai-lab-retrofit 15장) ──
# 빌드가 페이지를 다시 쓴 뒤, 덧씌우기를 kg-raw·kg-ld에 다시 적용한다. 파일이 없으면 아무것도 하지 않는다.
if __name__ == "__main__":
    import os as _os, sys as _sys, subprocess as _sp
    _r = _os.path.dirname(_os.path.abspath(__file__))
    for _i in range(3):
        if _os.path.exists(_os.path.join(_r, "kg", "rehang.json")): break
        _r = _os.path.dirname(_r)
    if _os.path.exists(_os.path.join(_r, "kg", "rehang.json")):
        _sp.run([_sys.executable, _os.path.join(_r, "kg", "rehang.py"), "apply", _r])
