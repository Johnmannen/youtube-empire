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
    return ImageFont.load_default()

def draw_rounded_rect(draw, bbox, fill, outline=None, width=1, radius=14):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_hybrid():
    w, h = 1280, 720
    img = Image.new("RGB", (w, h), color=(8, 12, 22))
    draw = ImageDraw.Draw(img)

    # Ambient subtle grid
    for y in range(0, h, 60):
        draw.line([(0, y), (w, y)], fill=(15, 22, 38), width=1)
    for x in range(0, w, 60):
        draw.line([(x, 0), (x, h)], fill=(15, 22, 38), width=1)

    # Glowing subtle frame
    draw.rectangle([(0, 0), (w, h)], outline=(56, 189, 248), width=5)

    # 1. TOP PUNCHY HERO BADGE (Max 2 words, Gycklarregeln)
    draw_rounded_rect(draw, (360, 35, 920, 125), fill=(15, 23, 42), outline=(56, 189, 248), width=3, radius=16)
    draw.text((400, 50), "SUB-SECOND VOICE", fill=(52, 211, 153), font=get_font(46, bold=True))

    # 2. LEFT SIDE (CONCEPT 1: THE SPLIT-SCREEN CONTRAST / THE PROBLEM)
    # Width: 460px (x=50 to 510)
    draw_rounded_rect(draw, (50, 155, 510, 665), fill=(26, 16, 24), outline=(239, 68, 68), width=3, radius=20)
    
    # Top Tag
    draw_rounded_rect(draw, (75, 180, 320, 230), fill=(220, 38, 38), radius=8)
    draw.text((95, 192), "OLD CHATBOTS", fill=(255, 255, 255), font=get_font(22, bold=True))

    # Big Lag Callout
    draw.text((75, 265), "4.5s DELAY", fill=(248, 113, 113), font=get_font(52, bold=True))
    draw.text((75, 350), "✕ Sequential HTTP Chain", fill=(226, 232, 240), font=get_font(24, bold=True))
    draw.text((75, 410), "✕ No Interruption (Barge-In)", fill=(226, 232, 240), font=get_font(24, bold=True))
    draw.text((75, 470), "✕ High Customer Churn", fill=(226, 232, 240), font=get_font(24, bold=True))

    draw_rounded_rect(draw, (75, 560, 485, 630), fill=(45, 18, 25), outline=(239, 68, 68), width=1, radius=10)
    draw.text((105, 578), "STATUS: 4500ms TIMEOUT", fill=(252, 165, 165), font=get_font(22, bold=True, mono=True))

    # 3. RIGHT SIDE (CONCEPT 3: MINIMALIST ARCHITECTURE + TERMINAL PROOF)
    # Width: 700px (x=540 to 1230)
    draw_rounded_rect(draw, (540, 155, 1230, 665), fill=(12, 18, 32), outline=(16, 185, 129), width=3, radius=20)

    # Top Tag
    draw_rounded_rect(draw, (565, 180, 890, 230), fill=(16, 185, 129), radius=8)
    draw.text((585, 192), "WEBSOCKET ARCHITECTURE", fill=(10, 15, 29), font=get_font(22, bold=True))

    # Big Speed Callout
    draw.text((565, 265), "380ms REAL-TIME", fill=(52, 211, 153), font=get_font(52, bold=True))

    # 3 Glowing Connected Nodes (The Concept 3 architectural element!)
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

    # Connecting Arrows between nodes
    # Node 1 -> 2
    draw.line([(760, 420), (790, 420)], fill=(56, 189, 248), width=4)
    draw.polygon([(790, 420), (780, 412), (780, 428)], fill=(56, 189, 248))
    # Node 2 -> 3
    draw.line([(985, 420), (1015, 420)], fill=(52, 211, 153), width=4)
    draw.polygon([(1015, 420), (1005, 412), (1005, 428)], fill=(52, 211, 153))

    # Bottom Terminal Proof Pill
    draw_rounded_rect(draw, (565, 540, 1205, 630), fill=(10, 38, 30), outline=(52, 211, 153), width=2, radius=12)
    draw.text((595, 565), "LIVE DEMO: 42ms BARGE-IN | STRIPE 200 OK", fill=(110, 231, 183), font=get_font(24, bold=True, mono=True))

    out_p = art_dir / "thumb_hybrid_concept_1_and_3.png"
    img.save(out_p, quality=95)
    print(f"Saved: {out_p}")

render_hybrid()
