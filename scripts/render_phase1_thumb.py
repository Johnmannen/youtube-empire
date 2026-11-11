import base64
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

art_dir = Path("C:/Users/johnr/.gemini/antigravity/brain/19c5e574-2ae1-4759-b3ad-59623ffcfb15")

def get_font(size, bold=False, mono=False):
    windows_fonts = Path("C:/Windows/Fonts")
    if mono and (windows_fonts / "consola.ttf").exists():
        return ImageFont.truetype(str(windows_fonts / "consola.ttf"), size)
    if bold and (windows_fonts / "segoeuib.ttf").exists():
        return ImageFont.truetype(str(windows_fonts / "segoeuib.ttf"), size)
    if bold and (windows_fonts / "arialbd.ttf").exists():
        return ImageFont.truetype(str(windows_fonts / "arialbd.ttf"), size)
    if (windows_fonts / "segoeui.ttf").exists():
        return ImageFont.truetype(str(windows_fonts / "segoeui.ttf"), size)
    if (windows_fonts / "arial.ttf").exists():
        return ImageFont.truetype(str(windows_fonts / "arial.ttf"), size)
    return ImageFont.load_default()

def draw_rounded_rect(draw, bbox, fill, outline=None, width=1, radius=14):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_phase1_thumbnail():
    w, h = 1280, 720
    img = Image.new("RGB", (w, h), color=(8, 12, 22))
    draw = ImageDraw.Draw(img)

    # Ambient grid
    for y in range(0, h, 60):
        draw.line([(0, y), (w, y)], fill=(16, 24, 40), width=1)
    for x in range(0, w, 60):
        draw.line([(x, 0), (x, h)], fill=(16, 24, 40), width=1)

    # Frame glow
    draw.rectangle([(0, 0), (w, h)], outline=(56, 189, 248), width=5)

    # 1. TOP SELLING HEADLINE (Centered, tight spacing, completely unified)
    # "BUILD VOICE AI AGENTS IN PYTHON"
    font_title = get_font(44, bold=True)
    text_part1 = "BUILD VOICE AI AGENTS "
    text_part2 = "IN PYTHON"

    bbox1 = draw.textbbox((0, 0), text_part1, font=font_title)
    w1 = bbox1[2] - bbox1[0]
    bbox2 = draw.textbbox((0, 0), text_part2, font=font_title)
    w2 = bbox2[2] - bbox2[0]
    total_w = w1 + w2

    # Center the banner card (height 100px: y=30 to 130)
    card_w = total_w + 80
    card_x1 = int((w - card_w) / 2)
    card_x2 = card_x1 + card_w
    draw_rounded_rect(draw, (card_x1, 30, card_x2, 130), fill=(15, 23, 42), outline=(56, 189, 248), width=3, radius=16)

    # Center text inside card
    text_start_x = int((w - total_w) / 2)
    text_y = 52
    draw.text((text_start_x, text_y), text_part1, fill=(255, 255, 255), font=font_title)
    draw.text((text_start_x + w1, text_y), text_part2, fill=(52, 211, 153), font=font_title)

    # 2. LEFT SIDE: THE PAIN (Old Text Chatbots / High Latency)
    draw_rounded_rect(draw, (50, 155, 510, 665), fill=(26, 16, 24), outline=(239, 68, 68), width=3, radius=20)
    
    # Header tag
    draw_rounded_rect(draw, (75, 180, 340, 230), fill=(220, 38, 38), radius=8)
    draw.text((95, 192), "OLD TEXT BOTS", fill=(255, 255, 255), font=get_font(22, bold=True))

    # Big Lag callout
    draw.text((75, 265), "4.5s DELAY", fill=(248, 113, 113), font=get_font(52, bold=True))
    draw.text((75, 350), "✕ Awkward Pauses", fill=(226, 232, 240), font=get_font(24, bold=True))
    draw.text((75, 410), "✕ No Real Interruption", fill=(226, 232, 240), font=get_font(24, bold=True))
    draw.text((75, 470), "✕ Sequential HTTP Chain", fill=(226, 232, 240), font=get_font(24, bold=True))

    draw_rounded_rect(draw, (75, 560, 485, 630), fill=(45, 18, 25), outline=(239, 68, 68), width=1, radius=10)
    draw.text((105, 578), "STATUS: 4500ms LAG", fill=(252, 165, 165), font=get_font(22, bold=True, mono=True))

    # 3. RIGHT SIDE: THE WEBSOCKET ARCHITECTURE SOLUTION
    draw_rounded_rect(draw, (540, 155, 1230, 665), fill=(12, 18, 32), outline=(16, 185, 129), width=3, radius=20)

    # Header tag
    draw_rounded_rect(draw, (565, 180, 890, 230), fill=(16, 185, 129), radius=8)
    draw.text((585, 192), "WEBSOCKET ARCHITECTURE", fill=(10, 15, 29), font=get_font(22, bold=True))

    # Big Speed callout
    draw.text((565, 265), "<400ms REAL-TIME", fill=(52, 211, 153), font=get_font(52, bold=True))

    # 3 Connected Nodes
    nodes = [
        ("AUDIO IN", "16kHz VAD", (37, 99, 235)),
        ("WEBSOCKET", "Duplex", (147, 51, 234)),
        ("STRIPE TOOL", "Mid-Call", (16, 185, 129))
    ]
    nx = 565
    for title, sub, col in nodes:
        draw_rounded_rect(draw, (nx, 360, nx + 195, 480), fill=(18, 26, 44), outline=col, width=2, radius=12)
        draw.text((nx + 18, 385), title, fill=(255, 255, 255), font=get_font(20, bold=True))
        draw.text((nx + 18, 425), sub, fill=col, font=get_font(18, bold=True, mono=True))
        nx += 225

    # Connecting Arrows
    draw.line([(760, 420), (790, 420)], fill=(56, 189, 248), width=4)
    draw.polygon([(790, 420), (780, 412), (780, 428)], fill=(56, 189, 248))
    draw.line([(985, 420), (1015, 420)], fill=(52, 211, 153), width=4)
    draw.polygon([(1015, 420), (1005, 412), (1005, 428)], fill=(52, 211, 153))

    # Status Proof Pill
    draw_rounded_rect(draw, (565, 540, 1205, 630), fill=(10, 38, 30), outline=(52, 211, 153), width=2, radius=12)
    draw.text((595, 565), "LIVE DEMO: 42ms BARGE-IN | STRIPE 200 OK", fill=(110, 231, 183), font=get_font(24, bold=True, mono=True))

    out_p = art_dir / "thumb_phase1_build_voice_ai.png"
    img.save(out_p, quality=95)
    print(f"Saved: {out_p}")

    # Also update gallery
    with open(out_p, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    gallery_html = f"""<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <title>YouTube B2B - Miniatyrbildsgalleri</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
<body class="bg-[var(--background)] text-[var(--foreground)] antialiased p-6">
  <div class="max-w-5xl mx-auto space-y-8">
    <div class="border-b border-[var(--border)] pb-4">
      <h1 class="text-3xl font-extrabold text-[var(--foreground)]">Justerad Miniatyrbild (Fas 1)</h1>
      <p class="text-sm text-[var(--muted-foreground)] mt-1">Rubriken <strong>BUILD VOICE AI AGENTS IN PYTHON</strong> är nu helt samlad med perfekt avstånd och enhetligt typsnitt.</p>
    </div>

    <div class="bg-[var(--card)] border-2 border-emerald-500 rounded-2xl p-6 shadow-xl ring-4 ring-emerald-500/10">
      <div class="flex items-center justify-between mb-3">
        <span class="text-xs font-black uppercase tracking-wider text-emerald-300 bg-emerald-950 px-3 py-1.5 rounded-lg border border-emerald-500">⭐ FÖRSLAG TILL GODKÄNNANDE: FAS 1 (JUSTERAD)</span>
        <span class="text-sm font-semibold text-emerald-400">BUILD VOICE AI AGENTS IN PYTHON</span>
      </div>
      <img src="data:image/png;base64,{img_b64}" class="w-full rounded-xl border border-[var(--border)] shadow-2xl" alt="Fas 1 Miniatyrbild" />
    </div>
  </div>
</body>
</html>"""
    with open(art_dir / "thumbnail_gallery.html", "w", encoding="utf-8") as f:
        f.write(gallery_html)
    print("Updated thumbnail_gallery.html")

render_phase1_thumbnail()
