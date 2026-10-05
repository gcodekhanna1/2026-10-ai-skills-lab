"""Seating board for the room screen (and for printing), built from the participant lists.

Reads `Lab_Participants - Session 1.md` and `Lab_Participants - Session 2.md` in the main
working folder and writes `Seating Board.html` next to this script. Open it in a browser,
press F11 (Windows) or Control + Command + F (Mac) for full screen, and switch sessions with
the buttons or the 1 / 2 keys. Print it (landscape) for the paper copies.

Last-minute change? Edit the participant .md file, double-click "Update Seating Board.command",
then refresh the browser. Not published: it lives in the Logistics folder.

It also writes `Seating Board - Session 01.pdf` and `… Session 02.pdf` (white background, landscape) to put
on the tables for people who arrive late. The HTML only needs Python's standard library;
the PDF needs reportlab (pip3 install reportlab) and is skipped with a message if it's missing."""
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SESSIONS = [("Session 1", ROOT / "Lab_Participants - Session 1.md"),
            ("Session 2", ROOT / "Lab_Participants - Session 2.md")]
OUT = HERE / "Seating Board.html"


def read_people(md: Path) -> list[tuple[str, str, str]]:
    """(last, first, desk number) for every row of the participant table."""
    people = []
    for line in md.read_text(encoding="utf-8").splitlines():
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and re.fullmatch(r"demo-\d+", cells[2], re.I):
            people.append((cells[0], cells[1], cells[2].split("-")[1]))
    return sorted(people, key=lambda p: (p[0].lower(), p[1].lower()))


def board(name: str, people: list[tuple[str, str, str]]) -> str:
    rows = "".join(
        '<li><span class="who"><b>' + html.escape(last) + "</b>, " + html.escape(first)
        + '</span><span class="desk">Demo-' + html.escape(num) + "</span></li>"
        for last, first, num in people)
    return ('<section class="board" id="' + name.lower().replace(" ", "") + '"><header><div><div class="kicker">'
            'WebexOne 2026 · Building AI Projects · ' + html.escape(name) + '</div><h1>Find Your Seat</h1></div>'
            '<p>Sit at the desk with your Demo number.<br>Your lab account is <code>demo-<i>number</i>@paradigmventures.ai</code></p>'
            '</header><ol>' + rows + "</ol></section>")


CSS = """
*{box-sizing:border-box}html,body{margin:0;height:100%}
body{background:#0b0f19;color:#eef2f8;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
.board{display:none;height:100vh;padding:2.2vh 2.5vw;flex-direction:column}.board.on{display:flex}
header{display:flex;justify-content:space-between;align-items:flex-end;gap:2vw;padding-bottom:1.4vh;border-bottom:.5vh solid;
 border-image:linear-gradient(90deg,#ff8a3d,#e0409b,#7b4dff,#2f6bff) 1}
.kicker{font-size:min(1.5vh,0.84vw);letter-spacing:.14em;text-transform:uppercase;color:#a99bff;font-weight:700}
h1{margin:.2vh 0 0;font-size:min(5.0vh,2.81vw);line-height:1.1}
header p{margin:0;text-align:right;font-size:min(1.9vh,1.07vw);color:#b9c3d3;line-height:1.5}code{color:#fff;font-size:1.05em}
ol{list-style:none;margin:1.8vh 0 0;padding:0;flex:1;display:grid;grid-template-columns:repeat(3,1fr);
 grid-auto-flow:column;grid-template-rows:repeat(var(--rows),1fr);column-gap:2vw;row-gap:.7vh}
li{display:flex;align-items:center;justify-content:space-between;gap:1vw;background:#151c2c;border-radius:1vh;padding:0 1vw;min-height:0}
.who{font-size:min(2.6vh,1.46vw);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.who b{font-weight:700}
.desk{flex:0 0 auto;font-weight:800;font-size:min(2.7vh,1.52vw);min-width:9vh;text-align:center;border-radius:.8vh;padding:.2vh .6vw;
 background:linear-gradient(135deg,#7b4dff,#2f6bff);color:#fff}
nav{position:fixed;right:1.2vw;bottom:1vh;display:flex;gap:.5vw;opacity:.35}nav:hover{opacity:1}
nav button{font:inherit;font-size:min(1.4vh,0.79vw);background:#1d2538;color:#cfd7e6;border:1px solid #33405a;border-radius:.6vh;padding:.4vh .8vw;cursor:pointer}
nav button.on{background:#7b4dff;color:#fff;border-color:#7b4dff}
@media print{@page{size:landscape;margin:10mm}
 body{background:#fff;color:#111}.board{height:auto;min-height:0;padding:0;page-break-after:always}
 .board.on,.board{display:flex}nav{display:none}
 .kicker{color:#5b3fd6}header p{color:#333}code{color:#111}
 ol{grid-template-rows:repeat(var(--rows),auto);row-gap:2mm;margin-top:4mm}
 li{background:#f2f4f8;border-radius:2mm;padding:1.6mm 3mm}.who{font-size:13pt}.desk{font-size:13pt;min-width:12mm;
 -webkit-print-color-adjust:exact;print-color-adjust:exact}
 h1{font-size:22pt}.kicker{font-size:8pt}header p{font-size:9pt}}
"""

JS = """
const boards=[...document.querySelectorAll('.board')],btns=[...document.querySelectorAll('nav button')];
function show(i){boards.forEach((b,k)=>b.classList.toggle('on',k===i));btns.forEach((b,k)=>b.classList.toggle('on',k===i));
 history.replaceState(null,'','#'+boards[i].id)}
btns.forEach((b,i)=>b.onclick=()=>show(i));
document.addEventListener('keydown',e=>{const n=parseInt(e.key,10);if(n>=1&&n<=boards.length)show(n-1)});
show(Math.max(0,boards.findIndex(b=>'#'+b.id===location.hash)));
"""


def pdf_out(session: str) -> Path:
    """e.g. "Session 1" -> Seating Board - Session 01.pdf"""
    num = re.sub(r"\D", "", session)
    return HERE / (f"Seating Board - Session {int(num):02d}.pdf" if num else f"Seating Board - {session}.pdf")


def make_pdf(boards: list[tuple[str, list[tuple[str, str, str]]]]) -> None:
    """White, printable version for the tables: one landscape US Letter PDF per session.
    Needs the reportlab library (the same one the placards use); skipped with a message if missing."""
    try:
        from reportlab.lib.colors import HexColor, white
        from reportlab.lib.pagesizes import landscape, letter
        from reportlab.lib.units import inch
        from reportlab.pdfbase.pdfmetrics import stringWidth
        from reportlab.pdfgen import canvas
    except ImportError:
        print("Skipped the PDF: the reportlab library isn't installed (pip3 install reportlab).")
        return
    W, H = landscape(letter)
    M = 0.5 * inch
    INK, MUTED, PURPLE, CELL = HexColor("#111827"), HexColor("#4B5563"), HexColor("#6D3FE6"), HexColor("#F1F3F8")
    GRAD = ["#ff8a3d", "#e0409b", "#7b4dff", "#2f6bff"]
    for name, people in boards:
        out = pdf_out(name)
        c = canvas.Canvas(str(out), pagesize=(W, H))
        c.setTitle("Find Your Seat — Building AI Projects (WebexOne 2026) — " + name)
        # header
        top = H - M
        c.setFillColor(PURPLE); c.setFont("Helvetica-Bold", 9)
        c.drawString(M, top - 9, ("WebexOne 2026 · Building AI Projects · " + name).upper())
        c.setFillColor(INK); c.setFont("Helvetica-Bold", 28)
        c.drawString(M, top - 40, "Find Your Seat")
        c.setFillColor(MUTED); c.setFont("Helvetica", 11)
        c.drawRightString(W - M, top - 22, "Sit at the desk with your Demo number.")
        c.drawRightString(W - M, top - 38, "Your lab account is demo-number@paradigmventures.ai")
        seg = (W - 2 * M) / len(GRAD)
        for i, col in enumerate(GRAD):
            c.setFillColor(HexColor(col)); c.rect(M + i * seg, top - 52, seg + 0.5, 3, stroke=0, fill=1)
        # grid: 3 columns, filled top to bottom
        rows = max(1, -(-len(people) // 3))
        gap_x, gap_y = 0.25 * inch, 5
        grid_top, grid_bottom = top - 64, M
        cw = (W - 2 * M - 2 * gap_x) / 3
        ch = (grid_top - grid_bottom - (rows - 1) * gap_y) / rows
        size = min(14, ch * 0.42)
        for i, (last, first, num) in enumerate(people):
            col, row = divmod(i, rows)
            x = M + col * (cw + gap_x)
            y = grid_top - (row + 1) * ch - row * gap_y
            c.setFillColor(CELL); c.roundRect(x, y, cw, ch, 5, stroke=0, fill=1)
            label = "Demo-" + num
            pw = stringWidth(label, "Helvetica-Bold", size) + 12
            c.setFillColor(PURPLE); c.roundRect(x + cw - pw - 6, y + (ch - size - 8) / 2, pw, size + 8, 4, stroke=0, fill=1)
            c.setFillColor(white); c.setFont("Helvetica-Bold", size)
            c.drawCentredString(x + cw - 6 - pw / 2, y + (ch - size) / 2 + size * 0.22, label)
            # name: bold last name, regular first name, shrunk if it's too long for the cell
            room = cw - pw - 22
            fs = size
            while fs > 8 and (stringWidth(last, "Helvetica-Bold", fs) + stringWidth(", " + first, "Helvetica", fs)) > room:
                fs -= 0.5
            base = y + (ch - fs) / 2 + fs * 0.22
            c.setFillColor(INK); c.setFont("Helvetica-Bold", fs); c.drawString(x + 8, base, last)
            c.setFont("Helvetica", fs); c.drawString(x + 8 + stringWidth(last, "Helvetica-Bold", fs), base, ", " + first)
        c.showPage()
        c.save()
        print(f"Saved {out.name}")


def main() -> None:
    sections, buttons, rows, boards = [], [], 1, []
    for name, md in SESSIONS:
        if not md.is_file():
            print(f"Skipped {name}: {md.name} not found.")
            continue
        people = read_people(md)
        boards.append((name, people))
        rows = max(rows, -(-len(people) // 3))
        sections.append(board(name, people))
        buttons.append("<button>" + html.escape(name) + "</button>")
        print(f"{name}: {len(people)} participants")
    page = ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>Find Your Seat — Building AI Projects</title><style>:root{--rows:" + str(rows) + "}" + CSS
            + "</style></head><body>" + "".join(sections) + "<nav>" + "".join(buttons) + "</nav><script>" + JS
            + "</script></body></html>\n")
    OUT.write_text(page, encoding="utf-8")
    print(f"Saved {OUT.name}")
    make_pdf(boards)


if __name__ == "__main__":
    main()
