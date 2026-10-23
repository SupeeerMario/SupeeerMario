from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
W, H = 1200, 220
MONO = "'JetBrains Mono','Fira Code',ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace"
CYAN, PINK, TEXT, MUTED, BORDER, PILL = "#4cc9f0", "#b5179e", "#c9d1d9", "#8b949e", "#30363d", "#161b22"

DEFS = f'''<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d1117"/><stop offset="1" stop-color="#161028"/></linearGradient>
  <linearGradient id="accv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="0.5" stop-color="{PINK}"/><stop offset="1" stop-color="{CYAN}"/>
    <animate attributeName="y1" values="0;-1;0" dur="8s" repeatCount="indefinite"/><animate attributeName="y2" values="1;0;1" dur="8s" repeatCount="indefinite"/></linearGradient>
  <linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.035"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>'''


def node(x, y, text):
    return (f'<rect x="{x}" y="{y}" width="110" height="44" rx="10" fill="{PILL}" stroke="{BORDER}"/>'
            f'<text x="{x + 55}" y="{y + 28}" text-anchor="middle" font-family="{MONO}" font-size="15" fill="{TEXT}">{text}</text>')


def pipeline():
    y, q, w, d = 100, 352, 545, 738  # node row and left edges of queue, worker, db
    line = f"M{q + 55} {y + 22}H{d + 55}"
    arc = f"M{w + 55} {y} C{w + 55} {y - 70} {q + 55} {y - 70} {q + 55} {y}"
    dots = "".join(
        f'<circle r="4" fill="{CYAN}"><animateMotion path="{line}" dur="3.6s" begin="{b}s" repeatCount="indefinite"/></circle>'
        for b in (0, 1.2, 2.4))
    retry = (f'<path d="{arc}" fill="none" stroke="{MUTED}" stroke-opacity="0.5" stroke-dasharray="4 5"/>'
             f'<text x="{(q + w) // 2 + 55}" y="{y - 60}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUTED}">retry</text>'
             f'<circle r="4" fill="{PINK}" opacity="0"><animateMotion path="{arc}" dur="7.2s" keyPoints="0;0;1;1" keyTimes="0;0.6;0.8;1" calcMode="linear" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.59;0.6;0.8;0.81;1" dur="7.2s" repeatCount="indefinite"/></circle>')
    caption = f'<text x="{w + 55}" y="{y + 90}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUTED}">ack after commit</text>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{DEFS}'
            f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="url(#bg)" stroke="{BORDER}"/>'
            f'<g clip-path="url(#c)"><rect x="-400" y="0" width="300" height="{H}" fill="url(#sweep)" transform="skewX(-20)">'
            f'<animate attributeName="x" values="-400;-400;1600" keyTimes="0;0.6;1" dur="9s" repeatCount="indefinite"/></rect></g>'
            f'<rect x="0.5" y="0.5" width="4" height="{H - 1}" rx="2" fill="url(#accv)"/>'
            f'<path d="{line}" stroke="{BORDER}" stroke-width="1.5"/>{dots}{retry}'
            f'{node(q, y, "queue")}{node(w, y, "worker")}{node(d, y, "db")}{caption}</svg>\n')


(OUT / "pipeline.svg").write_text(pipeline())
