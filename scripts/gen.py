import re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ICONS = HERE / "icons"
OUT = HERE.parent
W = 1200
MONO = "'JetBrains Mono','Fira Code',ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace"
CYAN, PINK, TEXT, MUTED, BORDER, PILL = "#4cc9f0", "#b5179e", "#c9d1d9", "#8b949e", "#30363d", "#161b22"

DEFS = f'''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#161028"/></linearGradient>
  <linearGradient id="acc" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{PINK}"/></linearGradient>
  <linearGradient id="accv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="0.5" stop-color="{PINK}"/><stop offset="1" stop-color="{CYAN}"/>
    <animate attributeName="y1" values="0;-1;0" dur="8s" repeatCount="indefinite"/><animate attributeName="y2" values="1;0;1" dur="8s" repeatCount="indefinite"/></linearGradient>
  <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.035"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{BORDER}"/><stop offset="1" stop-color="{BORDER}" stop-opacity="0"/></linearGradient>
</defs>'''


def card(h, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}">{DEFS}'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{h-1}" rx="14" fill="url(#bg)" stroke="{BORDER}"/>'
            f'<clipPath id="c"><rect width="{W}" height="{h}" rx="14"/></clipPath>'
            f'<g clip-path="url(#c)"><rect x="-400" y="0" width="300" height="{h}" fill="url(#sweep)" transform="skewX(-20)">'
            f'<animate attributeName="x" values="-400;-400;1600" keyTimes="0;0.6;1" dur="9s" repeatCount="indefinite"/></rect></g>'
            f'<rect x="0.5" y="0.5" width="4" height="{h-1}" rx="2" fill="url(#accv)"/>{inner}</svg>\n')


def label(num, name):
    w = 48 + len(f"{num} / {name}") * 9.6
    return (f'<text x="48" y="58" font-family="{MONO}" font-size="16" letter-spacing="1">'
            f'<tspan fill="{PINK}">{num}</tspan><tspan fill="{MUTED}"> / </tspan><tspan fill="{CYAN}">{name}</tspan></text>'
            f'<rect x="{w + 16}" y="52" width="{W - w - 64}" height="1" fill="url(#fade)"/>')


def about():
    lines = [
        [("Backend engineer. I care about what happens when", TEXT)],
        [("things fail: ", TEXT), ("crashed workers, duplicate requests,", CYAN)],
        [("hung endpoints.", CYAN)],
        [("", TEXT)],
        [("Go", CYAN), (" for concurrency. ", TEXT), ("Python/Django", CYAN), (" for APIs.", TEXT)],
        [("Node.js", CYAN), (" for data pipelines.", TEXT)],
        [("Currently going deeper into ", MUTED), ("DevOps", PINK), (".", MUTED)],
    ]
    out, y = [], 112
    for line in lines:
        spans = "".join(f'<tspan fill="{c}">{t}</tspan>' for t, c in line)
        out.append(f'<text x="48" y="{y}" font-family="{MONO}" font-size="22">{spans}</text>')
        y += 36
    return card(y + 20, label("01", "about") + "".join(out) + pipeline())


def node(x, y, text):
    return (f'<rect x="{x}" y="{y}" width="110" height="44" rx="10" fill="{PILL}" stroke="{BORDER}"/>'
            f'<text x="{x + 55}" y="{y + 28}" text-anchor="middle" font-family="{MONO}" font-size="15" fill="{TEXT}">{text}</text>')


def pipeline():
    y = 200
    flow = f'<path d="M775 {y + 22}H1095" stroke="{BORDER}" stroke-width="1.5"/>'
    dots = "".join(
        f'<circle r="4" fill="{CYAN}"><animateMotion path="M775 {y + 22}H1095" dur="3.6s" begin="{b}s" repeatCount="indefinite"/></circle>'
        for b in (0, 1.2, 2.4))
    arc = f"M935 {y} C935 {y - 70} 775 {y - 70} 775 {y}"
    retry = (f'<path d="{arc}" fill="none" stroke="{MUTED}" stroke-opacity="0.5" stroke-dasharray="4 5"/>'
             f'<text x="855" y="{y - 60}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUTED}">retry</text>'
             f'<circle r="4" fill="{PINK}" opacity="0"><animateMotion path="{arc}" dur="7.2s" keyPoints="0;0;1;1" keyTimes="0;0.6;0.8;1" calcMode="linear" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.59;0.6;0.8;0.81;1" dur="7.2s" repeatCount="indefinite"/></circle>')
    caption = f'<text x="935" y="{y + 90}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUTED}">ack after commit</text>'
    return flow + dots + retry + node(720, y, "queue") + node(880, y, "worker") + node(1040, y, "db") + caption


def icon(slug, x, y, size):
    d = re.search(r' d="([^"]+)"', (ICONS / f"{slug}.svg").read_text()).group(1)
    s = size / 24
    return f'<path transform="translate({x} {y}) scale({s})" d="{d}" fill="{CYAN}"/>'


def stack():
    rows = [
        ("languages", [("go", "Go"), ("python", "Python"), ("javascript", "JavaScript")]),
        ("frameworks", [("django", "Django"), ("express", "Express"), ("gin", "Gin")]),
        ("data", [("postgresql", "PostgreSQL"), ("mongodb", "MongoDB"), ("minio", "MinIO")]),
        ("queues", [("redis", "Redis"), ("celery", "Celery")]),
        ("infra", [("docker", "Docker"), ("linux", "Linux"), ("git", "Git")]),
    ]
    out, y, n = [], 96, 0
    for name, items in rows:
        out.append(f'<text x="48" y="{y + 27}" font-family="{MONO}" font-size="15" fill="{MUTED}">{name}</text>')
        x = 220
        for slug, text in items:
            w = 20 + 20 + 10 + len(text) * 10.2 + 20
            n += 1
            d = 0.3 + n * 0.08
            out.append(f'<g><animate attributeName="opacity" values="0;0;1" keyTimes="0;{d / (d + 0.4):.3f};1" dur="{d + 0.4:.2f}s" fill="freeze"/>')
            out.append(f'<rect x="{x}" y="{y}" width="{w}" height="40" rx="10" fill="{PILL}" stroke="{BORDER}"/>')
            out.append(icon(slug, x + 20, y + 10, 20))
            out.append(f'<text x="{x + 50}" y="{y + 26}" font-family="{MONO}" font-size="17" fill="{TEXT}">{text}</text></g>')
            x += w + 14
        y += 58
    return card(y + 30, label("02", "stack") + "".join(out))


def terminal():
    # (is_command, text, colour); commands type out, output lines pop in after
    lines = [
        (True, "whoami", TEXT),
        (False, "khaled · backend engineer", MUTED),
        (True, "cat now.txt", TEXT),
        (False, "going deeper into devops: containers, pipelines, deploys", CYAN),
        (True, "uptime", TEXT),
        (False, "up and shipping", PINK),
    ]
    loop, t, events = 14.0, 0.6, []
    for cmd, text, _ in lines:
        dur = 0.06 * len(text) if cmd else 0.01
        events.append((t, t + dur))
        t += dur + (0.35 if cmd else 0.9)
    chrome = "".join(f'<circle cx="{48 + i * 22}" cy="44" r="6" fill="{c}"/>'
                     for i, c in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")))
    chrome += f'<text x="600" y="49" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{MUTED}">khaled@home: ~</text>'
    chrome += f'<rect x="1" y="74" width="{W - 2}" height="1" fill="{BORDER}"/>'
    out, y = [], 118
    for i, ((cmd, text, colour), (a, b)) in enumerate(zip(lines, events)):
        ka, kb = a / loop, b / loop
        reveal = (f'<animate attributeName="width" values="0;0;{W};{W};0" keyTimes="0;{ka:.4f};{kb:.4f};0.97;1" '
                  f'dur="{loop}s" repeatCount="indefinite"/>')
        out.append(f'<clipPath id="l{i}"><rect x="{48 + (26 if cmd else 0)}" y="{y - 22}" width="0" height="30">{reveal}</rect></clipPath>')
        prompt = f'<tspan fill="{PINK}">$ </tspan>' if cmd else ""
        body = f'<tspan fill="{colour}">{text}</tspan>'
        if cmd:
            # prompt shows as soon as the previous line finishes
            out.append(f'<text x="48" y="{y}" font-family="{MONO}" font-size="19" opacity="0">{prompt}'
                       f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{max(ka - 0.02, 0):.4f};{max(ka - 0.019, 0.0001):.4f};0.97;1" dur="{loop}s" repeatCount="indefinite"/></text>')
            out.append(f'<text x="74" y="{y}" font-family="{MONO}" font-size="19" clip-path="url(#l{i})">{body}</text>')
        else:
            out.append(f'<text x="48" y="{y}" font-family="{MONO}" font-size="19" clip-path="url(#l{i})">{body}</text>')
        y += 34
    show = (f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{t / loop - 0.001:.4f};{t / loop:.4f};0.97;1" '
            f'dur="{loop}s" repeatCount="indefinite"/>')
    cursor = (f'<g opacity="0">{show}<text x="48" y="{y}" font-family="{MONO}" font-size="19" fill="{PINK}">$</text>'
              f'<rect x="74" y="{y - 17}" width="11" height="21" fill="{CYAN}">'
              f'<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect></g>')
    return card(y + 36, chrome + "".join(out) + cursor)


(OUT / "terminal.svg").write_text(terminal())
(OUT / "about.svg").write_text(about())
(OUT / "stack.svg").write_text(stack())
