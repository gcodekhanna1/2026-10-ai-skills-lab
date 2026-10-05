"""Table placards (tent cards) for the Building AI Projects lab, WebexOne 2026.

One US Letter page per seat (demo-01 ... demo-30), printed portrait and folded in half at 5.5"
(the fold runs parallel to the 8.5" side). The bottom half is upright and the top half is upside
down, so both sides of the tent read correctly. Both sessions share the same 30 cards.

Run:  python3 make_table_placards.py              -> all 30 cards, saved next to this script
      python3 make_table_placards.py out.pdf 1 5  -> only demo-01 to demo-05
Needs the reportlab library (pip3 install reportlab)."""
import sys
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

W, H = letter                      # 612 x 792 pt
HALF = H / 2                        # fold line at 5.5"
DOMAIN = "paradigmventures.ai"
PASSWORD = "Cisco123#"
INK = HexColor("#111827")
MUTED = HexColor("#6B7280")
ACCENT = HexColor("#0A60FF")

def panel(c, n):
    """Draw one 8.5 x 5.5 panel with its origin at the panel's bottom-left; the fold is at the panel's top."""
    demo = f"demo-{n:02d}"          # email address (lowercase)
    name = f"Demo-{n:02d}"          # Claude user name (capital D)
    cx = W / 2
    # big demo number
    from reportlab.pdfbase.pdfmetrics import stringWidth
    size = min(140, 6.8 * inch / stringWidth("Demo-00", "Helvetica-Bold", 1))   # same size on every card, 6.8" wide max
    c.setFillColor(INK); c.setFont("Helvetica-Bold", size)
    c.drawCentredString(cx, 2.65 * inch, name)
    # org email
    c.setFillColor(MUTED); c.setFont("Helvetica", 13)
    c.drawCentredString(cx, 1.95 * inch, "ORG. EMAIL")
    c.setFillColor(INK); c.setFont("Helvetica", 30)
    c.drawCentredString(cx, 1.55 * inch, f"{demo}@{DOMAIN}")
    # Webex password
    c.setFillColor(MUTED); c.setFont("Helvetica", 13)
    c.drawCentredString(cx, 1.0 * inch, "WEBEX PASSWORD")
    c.setFillColor(INK); c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(cx, 0.6 * inch, PASSWORD)
    # thin accent bar near the fold (top of the panel)
    c.setFillColor(ACCENT); c.rect(cx - 1.25 * inch, HALF - 1.05 * inch, 2.5 * inch, 0.06 * inch, stroke=0, fill=1)

def page(c, n):
    panel(c, n)                                    # front: bottom half, upright
    c.saveState(); c.translate(W, H); c.rotate(180)
    panel(c, n)                                    # back: top half, upside down
    c.restoreState()
    # fold guide
    c.setStrokeColor(HexColor("#C7CBD1")); c.setDash(4, 4); c.setLineWidth(0.5)
    c.line(0.3 * inch, HALF, W - 0.3 * inch, HALF)
    c.showPage()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        out, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    else:
        out = str(Path(__file__).resolve().parent / "Table Placards - demo-01 to demo-30.pdf")
        first, last = 1, 30
    c = canvas.Canvas(out, pagesize=letter)
    c.setTitle("Table Placards — Building AI Projects (WebexOne 2026)")
    for n in range(first, last + 1):
        page(c, n)
    c.save()
    print("saved", out)
