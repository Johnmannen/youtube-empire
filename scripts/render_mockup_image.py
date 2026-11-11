import os
from PIL import Image, ImageDraw, ImageFont

def render_top_section_mockup(output_path):
    W, H = 1920, 480
    img = Image.new("RGBA", (W, H), (10, 15, 30, 255)) # Dark slate bg #0a0f1e
    draw = ImageDraw.Draw(img)

    # Fonts
    font_title = None
    font_kpi = None
    font_sub = None
    font_bold = None
    font_tag = None

    try:
        font_title = ImageFont.truetype("arialbd.ttf", 24)
        font_kpi = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arial.ttf", 16)
        font_bold = ImageFont.truetype("arialbd.ttf", 17)
        font_tag = ImageFont.truetype("arialbd.ttf", 13)
        font_head = ImageFont.truetype("arialbd.ttf", 15)
    except:
        font_title = ImageFont.load_default()
        font_kpi = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_bold = ImageFont.load_default()
        font_tag = ImageFont.load_default()
        font_head = ImageFont.load_default()

    # Header Bar
    draw.rectangle([(40, 25), (W - 40, 65)], fill=(15, 23, 42, 220), outline=(30, 58, 138, 200), width=1)
    # Header dot
    draw.ellipse([(60, 40), (70, 50)], fill=(16, 185, 129, 255))
    draw.text((80, 36), "REALTIDSKANALÖVERSIKT (LIVE YOUTUBE DATA & ANALYTICS API)", fill=(241, 245, 249), font=font_head)
    draw.text((W - 270, 36), "● Auto-synk: 60s  |  API: Aktiv", fill=(56, 189, 248), font=font_head)

    # 5 Cards configuration
    cards = [
        {
            "tag": "TOTAL TRAFIK",
            "tag_bg": (6, 182, 212, 40),
            "tag_border": (6, 182, 212, 100),
            "tag_txt": (34, 211, 238),
            "title": "TOTALA VISNINGAR",
            "value": "1 842",
            "unit": "st",
            "trend": "+18.4% sen förra v.",
            "sub1": "Summerat alla videor & Shorts",
            "sub2": "2 Publicerade live-avsnitt",
            "border": (6, 182, 212, 80),
            "glow": (6, 182, 212)
        },
        {
            "tag": "CTR & RÄCKVIDD",
            "tag_bg": (16, 185, 129, 40),
            "tag_border": (16, 185, 129, 100),
            "tag_txt": (52, 211, 153),
            "title": "KLICKFREKVENS (CTR)",
            "value": "6.8%",
            "unit": "snitt",
            "trend": "Över Mål (6.0%)",
            "sub1": "28 400 Exponeringar i flödet",
            "sub2": "Status: Hög konvertering",
            "border": (16, 185, 129, 80),
            "glow": (16, 185, 129)
        },
        {
            "tag": "RETENTION & ENGAGEMANG",
            "tag_bg": (168, 85, 247, 40),
            "tag_border": (168, 85, 247, 100),
            "tag_txt": (192, 132, 252),
            "title": "GENOMSNITTLIG VISNINGSTID",
            "value": "2m 14s",
            "unit": "51.2% APV",
            "trend": "Mål > 50% Uppnått",
            "sub1": "30s Intro-krok: 68.4% kvar",
            "sub2": "Hög teknisk kvarhållning",
            "border": (168, 85, 247, 80),
            "glow": (168, 85, 247)
        },
        {
            "tag": "TOPP-PERFORMER",
            "tag_bg": (249, 115, 22, 40),
            "tag_border": (249, 115, 22, 100),
            "tag_txt": (251, 146, 60),
            "title": "BÄSTA VIDEO JUST NU",
            "value": "Ep #002",
            "unit": "Voice AI",
            "trend": "+142% Velocity (24h)",
            "sub1": "840 visningar  |  CTR 7.1%",
            "sub2": "Driver 65% av all ny trafik",
            "border": (249, 115, 22, 80),
            "glow": (249, 115, 22)
        },
        {
            "tag": "MONETARISERING",
            "tag_bg": (16, 185, 129, 40),
            "tag_border": (16, 185, 129, 100),
            "tag_txt": (52, 211, 153),
            "title": "AFFILIATE & NETTOVINST",
            "value": "$18.50",
            "unit": "est. vinst",
            "trend": "100% Nettomarginal",
            "sub1": "42 Klick (PartnerStack/11Labs)",
            "sub2": "Driftkostnad: $0.00 / mån",
            "border": (16, 185, 129, 90),
            "glow": (16, 185, 129)
        }
    ]

    card_w = 344
    gap = 15
    start_x = 40
    start_y = 85
    card_h = 350

    for i, c in enumerate(cards):
        cx = start_x + i * (card_w + gap)
        cy = start_y

        # Card shadow / outer border
        draw.rounded_rectangle([(cx - 2, cy - 2), (cx + card_w + 2, cy + card_h + 2)], radius=18, outline=c["border"], width=1)
        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)], radius=16, fill=(15, 23, 42, 240), outline=(51, 65, 85, 160), width=1)

        # Tag pill
        tag_w = 170
        draw.rounded_rectangle([(cx + 18, cy + 18), (cx + 18 + tag_w, cy + 42)], radius=6, fill=c["tag_bg"], outline=c["tag_border"], width=1)
        draw.text((cx + 26, cy + 22), c["tag"], fill=c["tag_txt"], font=font_tag)

        # Title
        draw.text((cx + 18, cy + 54), c["title"], fill=(148, 163, 184), font=font_tag)

        # Main Value
        draw.text((cx + 18, cy + 78), c["value"], fill=(255, 255, 255), font=font_kpi)
        # Unit
        draw.text((cx + 18 + len(c["value"]) * 26 + 10, cy + 102), c["unit"], fill=c["tag_txt"], font=font_bold)

        # Inner Sub-panel (Scorecard breakdown)
        ip_y = cy + 155
        draw.rounded_rectangle([(cx + 14, ip_y), (cx + card_w - 14, cy + card_h - 14)], radius=12, fill=(10, 15, 28, 220), outline=(30, 41, 59, 180), width=1)

        # Trend badge
        draw.text((cx + 26, ip_y + 16), "▲ " + c["trend"], fill=(52, 211, 153), font=font_bold)

        # Divider
        draw.line([(cx + 26, ip_y + 44), (cx + card_w - 26, ip_y + 44)], fill=(30, 41, 59, 200), width=1)

        # Sub info
        draw.text((cx + 26, ip_y + 56), c["sub1"], fill=(226, 232, 240), font=font_sub)
        draw.text((cx + 26, ip_y + 82), c["sub2"], fill=(148, 163, 184), font=font_sub)
        draw.text((cx + 26, ip_y + 112), "● API-Verifierad Realtidsdata", fill=(100, 116, 139), font=font_tag)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, "PNG")
    print(f"Saved mockup image to: {output_path}")

if __name__ == "__main__":
    out_docs = r"c:\Users\johnr\Documents\AI & Agentic Stack B2B\docs\assets\mockup_top_kpi_section.png"
    out_art = r"C:\Users\johnr\.gemini\antigravity\brain\19c5e574-2ae1-4759-b3ad-59623ffcfb15\mockup_top_kpi_section.png"
    render_top_section_mockup(out_docs)
    render_top_section_mockup(out_art)
