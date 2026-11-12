#!/usr/bin/env python3
"""
generate_channel_banner.py - High-Impact YouTube Channel Banner for Agentic Stack B2B
Dimensions: 2048 x 1152 px (and 2560 x 1440 px)
Design: Cohesive full-bleed cyber-tech artwork. No "box-in-a-box" look.
Features glowing radial gradients, circuit grid, high-contrast glowing typography,
and guaranteed mobile safe-zone alignment.
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def get_font(size, bold=False, mono=False):
    win_fonts = "C:/Windows/Fonts"
    try:
        if mono and os.path.exists(f"{win_fonts}/consola.ttf"):
            return ImageFont.truetype(f"{win_fonts}/consola.ttf", size)
        if bold and os.path.exists(f"{win_fonts}/arialbd.ttf"):
            return ImageFont.truetype(f"{win_fonts}/arialbd.ttf", size)
        if os.path.exists(f"{win_fonts}/arial.ttf"):
            return ImageFont.truetype(f"{win_fonts}/arial.ttf", size)
    except Exception:
        pass
    return ImageFont.load_default()

def render_popping_banner(width=2048, height=1152, out_path="docs/assets/youtube_channel_banner_2048x1152.png"):
    scale = width / 2048.0
    
    # 1. Base Canvas & Radial Lighting Layer
    img = Image.new("RGB", (width, height), (5, 8, 18))
    
    # Create radiant center glow layer
    glow = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glow)
    
    cx, cy = width // 2, height // 2
    # Cyan center spotlight
    for r in range(int(420 * scale), 0, -int(15 * scale)):
        alpha = int(45 * (1.0 - (r / (420.0 * scale))))
        g_draw.ellipse([(cx - r * 1.8, cy - r), (cx + r * 1.8, cy + r)], fill=(6, 182, 212, alpha))
        
    # Purple secondary accent glow
    for r in range(int(320 * scale), 0, -int(15 * scale)):
        alpha = int(35 * (1.0 - (r / (320.0 * scale))))
        g_draw.ellipse([(cx - r * 1.4, cy - r * 0.8), (cx + r * 1.4, cy + r * 0.8)], fill=(168, 85, 247, alpha))

    # Apply blur to make it completely smooth
    glow = glow.filter(ImageFilter.GaussianBlur(int(40 * scale)))
    img.paste(glow, (0, 0), glow)

    draw = ImageDraw.Draw(img)

    # 2. Dynamic Cyber Grid & Circuit Traces (Full-Bleed)
    grid_gap = int(64 * scale)
    for x in range(0, width, grid_gap):
        opacity = 18 if abs(x - cx) > int(400 * scale) else 10
        draw.line([(x, 0), (x, height)], fill=(16, 26, 48), width=1)
    for y in range(0, height, grid_gap):
        draw.line([(0, y), (width, y)], fill=(16, 26, 48), width=1)

    # Angled Circuit Lines spanning from sides towards center
    circuit_color = (18, 38, 68)
    draw.line([(0, int(150 * scale)), (int(450 * scale), cy)], fill=(6, 182, 212), width=int(2 * scale))
    draw.line([(width, int(150 * scale)), (width - int(450 * scale), cy)], fill=(168, 85, 247), width=int(2 * scale))
    draw.line([(0, height - int(150 * scale)), (int(450 * scale), cy)], fill=(16, 185, 129), width=int(2 * scale))
    draw.line([(width, height - int(150 * scale)), (width - int(450 * scale), cy)], fill=(59, 130, 246), width=int(2 * scale))

    # Pulsing Nodes on Circuit Ends
    draw.ellipse([(int(440 * scale), cy - int(8 * scale)), (int(456 * scale), cy + int(8 * scale))], fill=(34, 211, 238))
    draw.ellipse([(width - int(456 * scale), cy - int(8 * scale)), (width - int(440 * scale), cy + int(8 * scale))], fill=(216, 180, 254))

    # Top & Bottom Glowing Laser Bars
    draw.rectangle([(0, 0), (width, int(8 * scale))], fill=(6, 182, 212))
    draw.rectangle([(0, height - int(8 * scale)), (width, height)], fill=(168, 85, 247))

    # Safe Area (Center Horizontal Band):
    # In 2048 x 1152, safe height is ~338px centered: y from 407 to 745.
    safe_y1 = int(cy - 169 * scale)
    safe_y2 = int(cy + 169 * scale)

    # 3. Left Side Content (Desktop View: Terminal Snippet)
    f_mono = get_font(int(17 * scale), mono=True)
    f_tag = get_font(int(15 * scale), bold=True)
    f_sub_side = get_font(int(18 * scale), bold=True)

    lx = int(70 * scale)
    draw.rounded_rectangle([(lx, cy - int(130 * scale)), (lx + int(340 * scale), cy + int(130 * scale))], radius=int(12 * scale), fill=(10, 15, 28), outline=(6, 182, 212), width=int(2 * scale))
    draw.rectangle([(lx, cy - int(130 * scale)), (lx + int(340 * scale), cy - int(92 * scale))], fill=(18, 26, 45))
    draw.ellipse([(lx + int(15 * scale), cy - int(117 * scale)), (lx + int(27 * scale), cy - int(105 * scale))], fill=(239, 68, 68))
    draw.ellipse([(lx + int(35 * scale), cy - int(117 * scale)), (lx + int(47 * scale), cy - int(105 * scale))], fill=(234, 179, 8))
    draw.ellipse([(lx + int(55 * scale), cy - int(117 * scale)), (lx + int(67 * scale), cy - int(105 * scale))], fill=(34, 197, 94))
    draw.text((lx + int(85 * scale), cy - int(120 * scale)), "agent_stack.py", fill=(148, 163, 184), font=f_tag)

    code_lines = [
        (">> $ python -m agentic_stack", (56, 189, 248)),
        (">> [STATUS]: Full-Duplex Mesh", (52, 211, 153)),
        (">> [VOICE]: Sub-400ms ElevenLabs", (216, 180, 254)),
        (">> [OPEX]: 99.7% Agency Savings", (52, 211, 153)),
        (">> [REPO]: GitHub Verified 2026", (251, 191, 36))
    ]
    term_y = cy - int(75 * scale)
    for line, col in code_lines:
        draw.text((lx + int(18 * scale), term_y), line, fill=col, font=f_mono)
        term_y += int(38 * scale)

    # 4. Right Side Content (Desktop View: 3-Stage Architecture)
    rx = width - int(410 * scale)
    draw.rounded_rectangle([(rx, cy - int(130 * scale)), (rx + int(340 * scale), cy + int(130 * scale))], radius=int(12 * scale), fill=(10, 15, 28), outline=(168, 85, 247), width=int(2 * scale))
    draw.text((rx + int(25 * scale), cy - int(110 * scale)), "AGENT ARCHITECTURE", fill=(216, 180, 254), font=f_sub_side)

    arch_cards = [
        ("1. LLM Tool Orchestration", (6, 182, 212)),
        ("2. Real-Time Voice Synthesis", (168, 85, 247)),
        ("3. Autonomous Production", (16, 185, 129))
    ]
    ay = cy - int(65 * scale)
    for text, col in arch_cards:
        draw.rounded_rectangle([(rx + int(20 * scale), ay), (rx + int(320 * scale), ay + int(50 * scale))], radius=int(8 * scale), fill=(18, 24, 42), outline=col, width=1)
        draw.text((rx + int(35 * scale), ay + int(15 * scale)), text, fill=(226, 232, 240), font=f_mono)
        ay += int(62 * scale)

    # 5. CENTER HERO (100% VISIBLE ON MOBILE & ALL SCREENS)
    # Top Category Pill
    f_badge_top = get_font(int(20 * scale), bold=True)
    cat_text = "// B2B PRODUCTION SYSTEMS • 3 BUILDS / WEEK: MON • WED • FRI"
    # Measure width of cat_text
    cat_bbox = draw.textbbox((0, 0), cat_text, font=f_badge_top)
    cat_w = cat_bbox[2] - cat_bbox[0]
    cat_x = cx - cat_w // 2
    cat_y = cy - int(120 * scale)
    draw.rounded_rectangle([(cat_x - int(24 * scale), cat_y - int(6 * scale)), (cat_x + cat_w + int(24 * scale), cat_y + int(32 * scale))], radius=int(8 * scale), fill=(16, 26, 46), outline=(6, 182, 212), width=int(2 * scale))
    draw.text((cat_x, cat_y), cat_text, fill=(34, 211, 238), font=f_badge_top)

    # Main Brand Name with Glowing Drop-Shadow
    f_brand = get_font(int(78 * scale), bold=True)
    brand_text = "AGENTIC STACK B2B"
    b_bbox = draw.textbbox((0, 0), brand_text, font=f_brand)
    b_w = b_bbox[2] - b_bbox[0]
    bx = cx - b_w // 2
    by = cy - int(65 * scale)

    # Glowing Shadow
    for off in [4, 3, 2, 1]:
        draw.text((bx - off, by), brand_text, fill=(6, 182, 212), font=f_brand)
        draw.text((bx + off, by), brand_text, fill=(168, 85, 247), font=f_brand)
        draw.text((bx, by + off), brand_text, fill=(16, 185, 129), font=f_brand)
    # Bright White Foreground
    draw.text((bx, by), brand_text, fill=(255, 255, 255), font=f_brand)

    # Sub-Headline
    f_sub = get_font(int(26 * scale), bold=True)
    sub_text = "Autonomous AI Agents • Real-Time Voice AI • Python Blueprints"
    s_bbox = draw.textbbox((0, 0), sub_text, font=f_sub)
    s_w = s_bbox[2] - s_bbox[0]
    sx = cx - s_w // 2
    sy = cy + int(35 * scale)
    draw.text((sx, sy), sub_text, fill=(52, 211, 153), font=f_sub)

    # Tech Pills (Centered)
    pills = [
        ("PYTHON 3.12", (6, 182, 212)),
        ("ELEVENLABS VOICE AI", (168, 85, 247)),
        ("MULTI-AGENT ARCHITECTURES", (16, 185, 129)),
        ("OPEN-SOURCE GITHUB BLUEPRINTS", (251, 191, 36))
    ]
    f_pill = get_font(int(15 * scale), bold=True)
    
    # Calculate total width of all pills
    pill_widths = []
    for p_text, _ in pills:
        p_bbox = draw.textbbox((0, 0), p_text, font=f_pill)
        pill_widths.append((p_bbox[2] - p_bbox[0]) + int(36 * scale))
    
    total_pills_w = sum(pill_widths) + (len(pills) - 1) * int(14 * scale)
    cur_px = cx - total_pills_w // 2
    pill_y = cy + int(85 * scale)

    for (p_text, col), pw in zip(pills, pill_widths):
        draw.rounded_rectangle([(cur_px, pill_y), (cur_px + pw, pill_y + int(36 * scale))], radius=int(6 * scale), fill=(12, 18, 32), outline=col, width=int(1.5 * scale))
        draw.text((cur_px + int(18 * scale), pill_y + int(9 * scale)), p_text, fill=col, font=f_pill)
        cur_px += pw + int(14 * scale)

    # Bottom Clarification Line (Inside Mobile Safe Area)
    f_foot = get_font(int(16 * scale))
    foot_text = "Free downloadable production code & architecture schematics in every video description."
    ft_bbox = draw.textbbox((0, 0), foot_text, font=f_foot)
    ft_w = ft_bbox[2] - ft_bbox[0]
    draw.text((cx - ft_w // 2, cy + int(135 * scale)), foot_text, fill=(148, 163, 184), font=f_foot)

    # Save Image
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, optimize=True)
    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"Generated Popping Banner: {out_path} ({width}x{height}, {size_mb:.2f} MB)")
    return out_path

if __name__ == "__main__":
    # Render 2048 x 1152 (Exact user spec)
    render_popping_banner(2048, 1152, "docs/assets/youtube_channel_banner_2048x1152.png")
    # Render 2560 x 1440 (Official YouTube standard)
    render_popping_banner(2560, 1440, "docs/assets/youtube_channel_banner_2560x1440.png")
