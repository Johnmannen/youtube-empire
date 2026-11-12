#!/usr/bin/env python3
"""
generate_channel_banner.py - Professional YouTube Channel Banner for Agentic Stack B2B
Dimensions:
- 2560 x 1440 px (YouTube Recommended Master)
- 2048 x 1152 px (Exact Minimum Spec requested by User)
File size: < 6 MB (optimized PNG/JPEG)
Safe Zone: Centered area (1546 x 423 on 2560; 1236 x 338 on 2048) visible on all mobile, desktop & TV screens.
"""

import os
from PIL import Image, ImageDraw, ImageFont

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

def render_banner(width=2560, height=1440, out_path="docs/assets/youtube_channel_banner_2560x1440.png"):
    img = Image.new("RGB", (width, height), (8, 12, 24))
    draw = ImageDraw.Draw(img)

    scale = width / 2560.0

    # 1. Subtle Background Grid (TV & Wide Canvas)
    grid_spacing = int(70 * scale)
    for x in range(0, width, grid_spacing):
        draw.line([(x, 0), (x, height)], fill=(13, 18, 32), width=1)
    for y in range(0, height, grid_spacing):
        draw.line([(0, y), (width, y)], fill=(13, 18, 32), width=1)

    # Top & Bottom Gradient Neon Strips
    strip_h = max(6, int(8 * scale))
    draw.rectangle([(0, 0), (width, strip_h)], fill=(6, 182, 212))
    draw.rectangle([(0, height - strip_h), (width, height)], fill=(168, 85, 247))

    # Safe Area Coordinates:
    # 2560 x 1440 -> 1546 x 423 px centered
    safe_w = int(1546 * scale)
    safe_h = int(423 * scale)
    safe_x1 = (width - safe_w) // 2
    safe_y1 = (height - safe_h) // 2
    safe_x2 = safe_x1 + safe_w
    safe_y2 = safe_y1 + safe_h

    # ==============================================================================
    # 2. OUTER WINGS (DESKTOP & TV DISPLAY ONLY)
    # ==============================================================================
    wing_w = safe_x1 - int(60 * scale)
    if wing_w > int(220 * scale):
        f_mono_wing = get_font(int(17 * scale), mono=True)
        f_head_wing = get_font(int(19 * scale), bold=True)

        # Left Wing: Terminal Execution Box
        lw_x1 = int(50 * scale)
        lw_x2 = safe_x1 - int(40 * scale)
        draw.rounded_rectangle([(lw_x1, safe_y1 + int(20 * scale)), (lw_x2, safe_y2 - int(20 * scale))], radius=int(12 * scale), fill=(11, 15, 25), outline=(59, 130, 246), width=int(2 * scale))
        draw.rectangle([(lw_x1, safe_y1 + int(20 * scale)), (lw_x2, safe_y1 + int(60 * scale))], fill=(20, 27, 45))
        
        # Dots
        dot_r = int(6 * scale)
        draw.ellipse([(lw_x1 + int(20 * scale), safe_y1 + int(35 * scale)), (lw_x1 + int(20 * scale) + dot_r * 2, safe_y1 + int(35 * scale) + dot_r * 2)], fill=(239, 68, 68))
        draw.ellipse([(lw_x1 + int(40 * scale), safe_y1 + int(35 * scale)), (lw_x1 + int(40 * scale) + dot_r * 2, safe_y1 + int(35 * scale) + dot_r * 2)], fill=(234, 179, 8))
        draw.ellipse([(lw_x1 + int(60 * scale), safe_y1 + int(35 * scale)), (lw_x1 + int(60 * scale) + dot_r * 2, safe_y1 + int(35 * scale) + dot_r * 2)], fill=(34, 197, 94))
        draw.text((lw_x1 + int(90 * scale), safe_y1 + int(32 * scale)), "agent_runner.py", fill=(148, 163, 184), font=f_head_wing)

        lines = [
            (">> $ python deploy_agent.py", (56, 189, 248)),
            (">> [SYS]: Agent Mesh Online", (52, 211, 153)),
            (">> [VOICE]: Sub-400ms Full-Duplex", (216, 180, 254)),
            (">> [STATUS]: Zero Agency Overhead", (52, 211, 153)),
            (">> [CODE]: GitHub Verified 2026", (251, 191, 36))
        ]
        ly = safe_y1 + int(75 * scale)
        for t, c in lines:
            draw.text((lw_x1 + int(20 * scale), ly), t, fill=c, font=f_mono_wing)
            ly += int(34 * scale)

        # Right Wing: Architecture Nodes
        rw_x1 = safe_x2 + int(40 * scale)
        rw_x2 = width - int(50 * scale)
        draw.rounded_rectangle([(rw_x1, safe_y1 + int(20 * scale)), (rw_x2, safe_y2 - int(20 * scale))], radius=int(12 * scale), fill=(11, 15, 25), outline=(168, 85, 247), width=int(2 * scale))
        draw.text((rw_x1 + int(25 * scale), safe_y1 + int(40 * scale)), "SYSTEM ARCHITECTURE", fill=(168, 85, 247), font=f_head_wing)

        arch_nodes = [
            ("1. LLM Orchestration", (6, 182, 212)),
            ("2. Real-Time Voice AI", (168, 85, 247)),
            ("3. Autonomous Execution", (16, 185, 129))
        ]
        ay = safe_y1 + int(85 * scale)
        for label, col in arch_nodes:
            draw.rounded_rectangle([(rw_x1 + int(20 * scale), ay), (rw_x2 - int(20 * scale), ay + int(45 * scale))], radius=int(8 * scale), fill=(18, 24, 40), outline=col, width=1)
            draw.text((rw_x1 + int(35 * scale), ay + int(12 * scale)), label, fill=(226, 232, 240), font=f_mono_wing)
            ay += int(60 * scale)

    # ==============================================================================
    # 3. CENTER SAFE ZONE (100% VISIBLE ACROSS ALL DEVICES: MOBILE, TABLET, DESKTOP)
    # ==============================================================================
    draw.rounded_rectangle([(safe_x1, safe_y1), (safe_x2, safe_y2)], radius=int(18 * scale), fill=(11, 16, 30), outline=(6, 182, 212), width=int(3 * scale))

    # Top Category Pill
    f_badge = get_font(int(19 * scale), bold=True)
    draw.rounded_rectangle([(safe_x1 + int(45 * scale), safe_y1 + int(32 * scale)), (safe_x1 + int(390 * scale), safe_y1 + int(72 * scale))], radius=int(8 * scale), fill=(18, 28, 48), outline=(6, 182, 212), width=1)
    draw.text((safe_x1 + int(60 * scale), safe_y1 + int(40 * scale)), "// B2B PRODUCTION SYSTEMS", fill=(34, 211, 238), font=f_badge)

    # Top Right Cadence Badge
    f_sched = get_font(int(18 * scale), bold=True)
    draw.rounded_rectangle([(safe_x2 - int(410 * scale), safe_y1 + int(32 * scale)), (safe_x2 - int(45 * scale), safe_y1 + int(72 * scale))], radius=int(8 * scale), fill=(30, 20, 45), outline=(168, 85, 247), width=1)
    draw.text((safe_x2 - int(390 * scale), safe_y1 + int(40 * scale)), "NEW BUILDS: MON • WED • FRI", fill=(216, 180, 254), font=f_sched)

    # Main Channel Headline
    f_title = get_font(int(70 * scale), bold=True)
    draw.text((safe_x1 + int(45 * scale), safe_y1 + int(92 * scale)), "AGENTIC STACK B2B", fill=(255, 255, 255), font=f_title)

    # Sub-Headline
    f_sub = get_font(int(27 * scale), bold=True)
    draw.text((safe_x1 + int(45 * scale), safe_y1 + int(192 * scale)), "Autonomous AI Agents  •  Voice Engineering  •  Python Blueprints", fill=(52, 211, 153), font=f_sub)

    # 4 Tech Pills
    pills = [
        ("PYTHON 3.12", (6, 182, 212)),
        ("ELEVENLABS VOICE AI", (168, 85, 247)),
        ("MULTI-AGENT WORKFLOWS", (16, 185, 129)),
        ("OPEN-SOURCE GITHUB CODE", (251, 191, 36))
    ]
    f_pill = get_font(int(16 * scale), bold=True)
    px = safe_x1 + int(45 * scale)
    for text, col in pills:
        pw = int(len(text) * 10.5 * scale) + int(36 * scale)
        ph = int(40 * scale)
        draw.rounded_rectangle([(px, safe_y1 + int(255 * scale)), (px + pw, safe_y1 + int(255 * scale) + ph)], radius=int(8 * scale), fill=(16, 22, 36), outline=col, width=1)
        draw.text((px + int(16 * scale), safe_y1 + int(264 * scale)), text, fill=col, font=f_pill)
        px += pw + int(14 * scale)

    # Bottom Clarification Line
    f_foot = get_font(int(17 * scale))
    draw.text((safe_x1 + int(48 * scale), safe_y1 + int(342 * scale)), "Free open-source code & architecture blueprints provided in every video description.", fill=(148, 163, 184), font=f_foot)

    # Save
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, optimize=True)
    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"Generated: {out_path} ({width}x{height}, {size_mb:.2f} MB)")
    return out_path

if __name__ == "__main__":
    # Render recommended standard
    render_banner(2560, 1440, "docs/assets/youtube_channel_banner_2560x1440.png")
    # Render exact user specification
    render_banner(2048, 1152, "docs/assets/youtube_channel_banner_2048x1152.png")
