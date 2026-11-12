"""Regenerate the optional one-page employer PDF with ReportLab.

Run from the repository root: python3 presentation/build_employer_brief.py
ReportLab is needed only to rebuild this PDF, not to run portfolio checks.
"""

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import __file__ as reportlab_file


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/Juan_Martinez_AI_Governance_Brief.pdf"
NAVY = colors.HexColor("#111E2B")
GREEN = colors.HexColor("#2EAD86")
INK = colors.HexColor("#203345")
MUTED = colors.HexColor("#516371")
LINE = colors.HexColor("#D8E2E5")
PALE = colors.HexColor("#F2F6F6")
BASE = "https://github.com/JuanAMartinezDiaz/ai-governance-portfolio"
FONT_DIR = Path(reportlab_file).parent / "fonts"
pdfmetrics.registerFont(TTFont("PortfolioSans", str(FONT_DIR / "Vera.ttf")))
pdfmetrics.registerFont(TTFont("PortfolioSans-Bold", str(FONT_DIR / "VeraBd.ttf")))
pdfmetrics.registerFontFamily("PortfolioSans", normal="PortfolioSans", bold="PortfolioSans-Bold")


def paragraph(pdf, text, x, top, width, size=10, color=INK, leading=14):
    style = ParagraphStyle("body", fontName="PortfolioSans", fontSize=size,
                           leading=leading, textColor=color)
    p = Paragraph(text, style)
    _, height = p.wrap(width, 200)
    p.drawOn(pdf, x, top - height)
    return height


def link(pdf, label, url, x, y, size=9):
    pdf.setFillColor(colors.HexColor("#147357"))
    pdf.setFont("PortfolioSans-Bold", size)
    pdf.drawString(x, y, label)
    width = pdf.stringWidth(label, "PortfolioSans-Bold", size)
    pdf.linkURL(url, (x, y - 2, x + width, y + size + 2), relative=0)


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(OUTPUT), pagesize=(612, 792), invariant=1)
    pdf.setTitle("Juan A. Martinez Diaz - AI Governance Employer Brief")
    pdf.setAuthor("Juan A. Martinez Diaz")
    pdf.setSubject("Experience, inspectable work samples, and evidence scope")
    pdf.setFillColor(NAVY)
    pdf.rect(0, 642, 612, 150, fill=1, stroke=0)
    pdf.setFillColor(GREEN)
    pdf.rect(0, 637, 612, 5, fill=1, stroke=0)
    pdf.setFont("PortfolioSans-Bold", 9)
    pdf.drawString(42, 765, "APPLIED AI GOVERNANCE")
    pdf.setFillColor(colors.HexColor("#D9E8E5"))
    pdf.setFont("PortfolioSans", 8)
    pdf.drawRightString(570, 765, "PORTFOLIO BRIEF | 12 NOVEMBER 2026")
    pdf.setFillColor(colors.white)
    pdf.setFont("PortfolioSans-Bold", 28)
    pdf.drawString(42, 724, "Juan A. Martinez Diaz, MBA")
    pdf.setFont("PortfolioSans", 12)
    pdf.drawString(42, 700, "AI Governance | Technology Risk | Control Assurance")
    pdf.setFont("PortfolioSans", 9.5)
    pdf.drawString(42, 679, "Former Wells Fargo Vice President | Founder, Bounded Agentic Intelligence")
    pdf.setFillColor(colors.HexColor("#C9DED8"))
    pdf.drawString(42, 660, "North Carolina | Seeking remote governance and risk opportunities")

    paragraph(pdf, "I connect AI adoption to clear business purpose, accountable ownership, "
              "independent challenge, and evidence that supports a defensible decision.",
              42, 616, 528, 11, leading=16)
    pdf.setFillColor(INK)
    pdf.setFont("PortfolioSans-Bold", 10)
    pdf.drawString(42, 566, "THREE WORK SAMPLES TO REVIEW")

    samples = [
        ("01", "Independent AI risk challenge",
         "A candidate-ranking assessment examines risk, alternatives, and the evidence needed to reconsider a hold on live use.",
         "Read the decision", BASE + "/blob/main/project-02-risk-assessment/governance-review-memo.md"),
        ("02", "Governance and decision authority",
         "An operating model separates business ownership, independent validation, second-line challenge, escalation, and audit.",
         "Inspect the model", BASE + "/blob/main/project-03-responsible-ai-policy/governance-operating-model.md"),
        ("03", "A finding, remediation, and retest",
         "A bounded synthetic output-contract demonstration records accepted and rejected cases and invalidates a decision when scope changes.",
         "Inspect the evidence", BASE + "/blob/main/evidence/control-lifecycle.md"),
    ]
    for index, (number, title, description, label, url) in enumerate(samples):
        top = 549 - index * 80
        pdf.setFillColor(PALE)
        pdf.roundRect(42, top - 70, 528, 70, 5, fill=1, stroke=0)
        pdf.setFillColor(GREEN)
        pdf.setFont("PortfolioSans-Bold", 14)
        pdf.drawString(54, top - 23, number)
        pdf.setFillColor(INK)
        pdf.setFont("PortfolioSans-Bold", 10.5)
        pdf.drawString(86, top - 18, title)
        paragraph(pdf, description, 86, top - 26, 467, 9, leading=12)
        link(pdf, label, url, 86, top - 61, 8.5)

    pdf.setFont("PortfolioSans-Bold", 10)
    pdf.setFillColor(INK)
    pdf.drawString(42, 296, "EXPERIENCE BEHIND THE WORK")
    paragraph(pdf, "<b>Banking:</b> second-line technology and information security risk oversight; RCSA and control-review experience. "
              "<b>Leadership:</b> U.S. Army technology operations. <b>Education:</b> MBA, Strategy &amp; Leadership, Wake Forest University. "
              "<b>Applied work:</b> builder of Sentinel, a public reference for AI-agent authority controls.",
              42, 282, 528, 9.5, leading=14)

    pdf.setStrokeColor(LINE)
    pdf.line(42, 211, 570, 211)
    pdf.setFont("PortfolioSans-Bold", 9.5)
    pdf.drawString(42, 194, "FIVE CONNECTED CASE STUDIES")
    paragraph(pdf, "Inventory and classification  |  Risk assessment  |  Responsible AI policy<br/>"
              "Incident response  |  High-risk documentation", 42, 182, 528, 9.5, leading=14)

    paragraph(pdf, "<b>Evidence scope.</b> Original, AI-assisted synthetic work developed at Juan's direction. "
              "Selected checks are reproducible; broader operating controls remain proposed unless a specific test result is recorded. "
              "No employer/client data, achieved customer savings, or production certification is claimed. "
              "Authorship and personal-walkthrough status are disclosed in the repository.",
              42, 141, 528, 8.2, MUTED, 11)

    pdf.setFillColor(NAVY)
    pdf.rect(0, 0, 612, 72, fill=1, stroke=0)
    pdf.setFillColor(colors.white)
    pdf.setFont("PortfolioSans-Bold", 11)
    pdf.drawString(42, 49, "juan@boundedagenticai.com")
    pdf.linkURL("mailto:juan@boundedagenticai.com", (42, 46, 215, 62), relative=0)
    pdf.setFont("PortfolioSans", 8.8)
    pdf.setFillColor(colors.HexColor("#C9DED8"))
    pdf.drawString(42, 30, "github.com/JuanAMartinezDiaz/ai-governance-portfolio")
    pdf.linkURL(BASE, (42, 26, 370, 41), relative=0)
    pdf.drawRightString(570, 49, "juanmartinez.ai")
    pdf.linkURL("https://www.juanmartinez.ai", (478, 46, 570, 62), relative=0)
    pdf.drawRightString(570, 30, "LinkedIn profile")
    pdf.linkURL("https://www.linkedin.com/in/juan-martinez-diaz-50943411", (490, 26, 570, 41), relative=0)
    pdf.showPage()
    pdf.save()
    print(OUTPUT)


if __name__ == "__main__":
    build()
