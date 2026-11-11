#!/usr/bin/env python3
"""
Concept 4: Seamless Fusion of Concept 1 & 3
Features:
- Large, mobile-crisp code typography (26pt)
- Dynamic camera punch-in on code lines 12-16
- Sliding animated neon arrow & pulsing highlight box
- Floating concept pill: 'HARDWARE BARGE-IN VAD (42ms)'
- Smooth camera punch-out / split-screen drawer reveal for live execution
- Synchronized terminal typing & status confirmation
"""

import os
import sys
import math
import asyncio
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import edge_tts

VOICE = "en-US-AndrewMultilingualNeural"
BASE_DIR = Path("build_temp/visual_tests")
BASE_DIR.mkdir(parents=True, exist_ok=True)

ART_DIR = Path("C:/Users/johnr/.gemini/antigravity/brain/19c5e574-2ae1-4759-b3ad-59623ffcfb15")

def get_font(size: int, bold: bool = False, mono: bool = False):
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

def draw_rounded_rect(draw, bbox, fill, outline=None, width=1, radius=12):
    draw.rounded_rectangle(bbox, radius=radius, fill=fill, outline=outline, width=width)

def render_concept_4_video():
    fps = 25
    audio_path = BASE_DIR / "andrew_narration.mp3"
    
    # Get duration
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    duration = float(res.stdout.strip())
    total_frames = int(duration * fps) + 5

    frames_dir = BASE_DIR / "c4_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    font_code = get_font(26, mono=True)
    font_bold = get_font(24, bold=True)
    font_mono_small = get_font(20, mono=True)

    code_lines = [
        ("from elevenlabs.conversational_ai import Conversation", (244, 114, 182)),
        ("from elevenlabs import ElevenLabs", (244, 114, 182)),
        ("", (255, 255, 255)),
        ("# 1. Mid-Call Tool Schema Definition", (100, 116, 139)),
        ("def cancel_order_tool(order_id: str) -> dict:", (56, 189, 248)),
        ("    '''Cancels active subscription in Stripe.'''", (148, 163, 184)),
        ("    stripe.Subscription.cancel(order_id)", (226, 232, 240)),
        ("    return {'status': 'success', 'id': order_id}", (52, 211, 153)),
        ("", (255, 255, 255)),
        ("# 2. Initialize WebSocket agent with Barge-In", (100, 116, 139)),
        ("conversation = Conversation(", (56, 189, 248)),
        ("    client=ElevenLabs(api_key=API_KEY),", (226, 232, 240)),
        ("    agent_id='b2b_support_v2',", (226, 232, 240)),
        ("    allow_interruptions=True,  # 42ms Hardware VAD", (251, 191, 36)),
        ("    tools={'cancel_order': cancel_order_tool},", (52, 211, 153)),
        ("    transport='websockets'", (244, 114, 182)),
        (")", (56, 189, 248)),
        ("conversation.start_session()  # Full-Duplex Stream", (168, 85, 247))
    ]

    terminal_events = [
        (">> [AUDIO IN] Streaming 16kHz PCM", (100, 116, 139)),
        (">> [AGENT] 'Hello! How can I assist you?'", (226, 232, 240)),
        (">> [USER] 'Cancel order 4928 please'", (251, 191, 36)),
        (">> [VAD DETECTED] Interruption fired!", (244, 114, 182)),
        (">> [AUDIO MUTED] Yielded in 42ms", (239, 68, 68)),
        (">> [CALLING TOOL] cancel_order('4928')", (56, 189, 248)),
        (">> [STRIPE API] Status: 200 OK", (52, 211, 153)),
        (">> [RESUMING] 'Order 4928 canceled.'", (110, 231, 183)),
    ]

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Top Navigation Bar
        draw_rounded_rect(draw, (60, 30, 1860, 90), fill=(15, 23, 42), outline=(59, 130, 246), width=1, radius=10)
        draw.text((90, 47), "CONCEPT 4: DEEP CODE FOCUS + DYNAMIC ARROW + LIVE TERMINAL SYNC", fill=(56, 189, 248), font=font_bold)

        # Dynamic layout transition:
        # Phase A (0.0s - 7.5s): Focus primarily on code (wide, large font)
        # Phase B (7.5s - 9.0s): Smooth transition to split-screen (terminal slides in, code moves left)
        # Phase C (9.0s - end): Split-screen with synced live execution
        
        if t < 7.5:
            # Code window takes full width (1740px)
            code_w = 1740
            term_w = 0
            term_x = 1920
        elif 7.5 <= t < 9.0:
            # Smooth transition over 1.5 seconds
            progress = (t - 7.5) / 1.5
            # Ease out quad
            progress = progress * (2 - progress)
            code_w = int(1740 - (1740 - 920) * progress)
            term_w = int(840 * progress)
            term_x = int(1920 - (1920 - 1020) * progress)
        else:
            code_w = 920
            term_w = 840
            term_x = 1020

        # Draw Code Window
        draw_rounded_rect(draw, (60, 115, 60 + code_w, 1000), fill=(13, 17, 28), outline=(59, 130, 246), width=2, radius=16)
        draw_rounded_rect(draw, (60, 115, 60 + code_w, 175), fill=(20, 28, 48), radius=16)
        draw.text((95, 135), "voice_runtime.py (VS Code - 26pt Mobile Optimized)", fill=(226, 232, 240), font=get_font(20, mono=True))

        # Render Code Lines with Line Numbers
        cy = 205
        line_spacing = 42
        
        # When zoomed/in Phase A, we show lines 4 to 17
        start_line = 3 if t < 7.5 else 0
        end_line = min(len(code_lines), start_line + 15)

        for idx in range(start_line, end_line):
            line_text, col = code_lines[idx]
            line_num = idx + 1
            
            # Line number
            draw.text((85, cy), f"{line_num:02d}", fill=(71, 85, 105), font=font_code)
            
            # Line 14 highlight (allow_interruptions=True)
            if idx == 13:
                # Highlight box
                highlight_bg = (42, 36, 18) if 1.2 <= t <= 8.5 else (18, 25, 38)
                highlight_border = (251, 191, 36) if 1.2 <= t <= 8.5 else (51, 65, 85)
                draw_rounded_rect(draw, (135, cy - 4, 60 + code_w - 30, cy + 38), fill=highlight_bg, outline=highlight_border, width=2, radius=8)
                draw.text((150, cy), line_text, font=font_code, fill=(254, 240, 138) if 1.2 <= t <= 8.5 else col)
                
                # Dynamic sliding neon arrow (active between t=1.5s and t=7.5s)
                if 1.5 <= t <= 7.5:
                    slide_in = min(1.0, (t - 1.5) / 0.4)
                    pulse_x = math.sin((t - 1.5) * 8) * 8
                    ax = int(50 - (1 - slide_in) * 60 + pulse_x)
                    ay = cy + 16
                    # Arrow head
                    draw.polygon([(ax + 80, ay), (ax + 50, ay - 14), (ax + 50, ay + 14)], fill=(251, 191, 36))
                    # Arrow tail
                    draw.rectangle([(ax + 20, ay - 6), (ax + 50, ay + 6)], fill=(251, 191, 36))
            else:
                draw.text((150, cy), line_text, font=font_code, fill=col)

            cy += line_spacing

        # Concept Badge in Phase A (t=2.0s to 7.0s)
        if 2.0 <= t <= 7.0:
            badge_alpha = min(1.0, (t - 2.0) / 0.3)
            draw_rounded_rect(draw, (980, 205, 1720, 340), fill=(20, 25, 45), outline=(244, 114, 182), width=3, radius=14)
            draw.text((1010, 225), "⚡ NATIVE HARDWARE BARGE-IN", fill=(244, 114, 182), font=get_font(24, bold=True))
            draw.text((1010, 275), "Client Voice Activity Detector terminates", fill=(226, 232, 240), font=get_font(20))
            draw.text((1010, 305), "audio playback within 42 milliseconds.", fill=(52, 211, 153), font=get_font(20, bold=True, mono=True))

        # Right Side: Terminal Execution Window (Slides in during Phase B & C)
        if term_w > 50:
            draw_rounded_rect(draw, (term_x, 115, 1860, 1000), fill=(10, 14, 24), outline=(16, 185, 129), width=2, radius=16)
            draw_rounded_rect(draw, (term_x, 115, 1860, 175), fill=(18, 36, 32), radius=16)
            draw.text((term_x + 30, 135), "Live Transport & Tool Execution", fill=(52, 211, 153), font=get_font(20, mono=True))

            # Reveal terminal lines progressively from t=8.0s to end
            term_revealed = 0
            if t > 8.0: term_revealed = 1
            if t > 9.0: term_revealed = 2
            if t > 10.0: term_revealed = 3
            if t > 11.2: term_revealed = 4
            if t > 12.2: term_revealed = 5
            if t > 13.2: term_revealed = 6
            if t > 14.2: term_revealed = 7
            if t > 15.0: term_revealed = 8

            ty = 205
            for i in range(term_revealed):
                t_msg, t_col = terminal_events[i]
                # If it's the newest event, subtle highlight bar
                if i == term_revealed - 1 and (t - int(t)) < 0.4:
                    draw_rounded_rect(draw, (term_x + 20, ty - 4, 1840, ty + 38), fill=(24, 40, 48), radius=6)
                draw.text((term_x + 30, ty), t_msg, font=font_mono_small, fill=t_col)
                ty += 52

            # Bottom Status Confirmation Pill
            if t > 13.0:
                draw_rounded_rect(draw, (term_x + 30, 880, 1830, 960), fill=(12, 38, 30), outline=(52, 211, 153), width=2, radius=10)
                draw.text((term_x + 60, 905), "✓ STRIPE DB UPDATED | LATENCY: 382ms ROUNDTRIP", fill=(110, 231, 183), font=get_font(20, bold=True, mono=True))

        frame_path = frames_dir / f"f_{f:04d}.png"
        img.save(frame_path)

    out_video = ART_DIR / "visual_concept_4_hybrid_split_focus.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-r", str(fps),
        "-i", str(frames_dir / "f_%04d.png"),
        "-i", str(audio_path),
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(out_video)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"[CONCEPT 4 VIDEO] Rendered successfully: {out_video}")

if __name__ == "__main__":
    render_concept_4_video()
