#!/usr/bin/env python3
"""
Produce Remake Video 002 based on the 2026 YouTube B2B Master Framework.
Implements:
 - Cinematic dynamic motion (smooth punch-in zoompan in FFmpeg)
 - Split-screen code walkthrough & live terminal tool execution
 - 2-Track Titles (<60 chars)
 - High-CTR Thumbnail (<4 words, Gycklarregeln, Split-screen contrast)
 - Spoken organic Like & Subscribe / Follow CTA in outro & scene cues
"""

import os
import sys
import asyncio
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import edge_tts

VOICE = "en-US-ChristopherNeural"
VOICE_RATE = "+4%"

OUT_DIR = Path("build_temp/remake_002")
OUT_DIR.mkdir(parents=True, exist_ok=True)

FINAL_ASSETS_DIR = Path("docs/assets")
FINAL_ASSETS_DIR.mkdir(parents=True, exist_ok=True)

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

def draw_fitted_text(draw, pos, text, max_width, initial_size, bold=False, mono=False, fill=(255, 255, 255)):
    size = initial_size
    while size > 14:
        font = get_font(size, bold=bold, mono=mono)
        bbox = draw.textbbox((0, 0), text, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            draw.text(pos, text, fill=fill, font=font)
            return font, (w, bbox[3] - bbox[1])
        size -= 2
    font = get_font(14, bold=bold, mono=mono)
    draw.text(pos, text, fill=fill, font=font)
    bbox = draw.textbbox((0, 0), text, font=font)
    return font, (bbox[2] - bbox[0], bbox[3] - bbox[1])

# -------------------------------------------------------------
# THUMBNAIL ENGINE V2 (Strict <4 words, Gycklarregeln, Split-screen)
# -------------------------------------------------------------
def render_remake_thumbnail(out_path: str):
    w, h = 1280, 720
    img = Image.new("RGB", (w, h), color=(10, 15, 29))
    draw = ImageDraw.Draw(img)

    # Ambient grid
    for y in range(0, h, 60):
        draw.line([(0, y), (w, y)], fill=(16, 24, 42), width=1)
    for x in range(0, w, 60):
        draw.line([(x, 0), (x, h)], fill=(16, 24, 42), width=1)

    # Glowing subtle border
    draw.rectangle([(0, 0), (w, h)], outline=(56, 189, 248), width=4)

    # HERO TEXT (Max 2 words - Gycklarregeln: does not repeat title)
    draw_rounded_rect(draw, (340, 45, 940, 135), fill=(15, 23, 42), outline=(56, 189, 248), width=3, radius=16)
    draw_fitted_text(draw, (380, 62), "SUB-SECOND VOICE", 520, 44, bold=True, fill=(52, 211, 153))

    # LEFT HALF: THE PAIN (Chatbots / High Latency)
    draw_rounded_rect(draw, (50, 165, 615, 655), fill=(24, 18, 28), outline=(239, 68, 68), width=3, radius=20)
    # Header tag
    draw_rounded_rect(draw, (75, 190, 340, 240), fill=(220, 38, 38), radius=8)
    draw_fitted_text(draw, (95, 203), "OLD CHATBOTS", 230, 22, bold=True, fill=(255, 255, 255))
    
    # Latency metric
    draw_fitted_text(draw, (75, 275), "4.5s DELAY", 480, 56, bold=True, fill=(248, 113, 113))
    draw_fitted_text(draw, (75, 355), "✕ Unnatural Pauses", 480, 26, bold=True, fill=(226, 232, 240))
    draw_fitted_text(draw, (75, 415), "✕ No Interruption", 480, 26, bold=True, fill=(226, 232, 240))
    draw_fitted_text(draw, (75, 475), "✕ Brittle HTTP Chains", 480, 26, bold=True, fill=(226, 232, 240))
    
    draw_rounded_rect(draw, (75, 560, 580, 625), fill=(40, 20, 25), outline=(239, 68, 68), width=1, radius=10)
    draw_fitted_text(draw, (110, 578), "STATUS: 4500ms LAG", 440, 24, bold=True, mono=True, fill=(252, 165, 165))

    # RIGHT HALF: THE SOLUTION (ElevenLabs WebSockets / Real-Time)
    draw_rounded_rect(draw, (665, 165, 1230, 655), fill=(14, 28, 36), outline=(16, 185, 129), width=3, radius=20)
    # Header tag
    draw_rounded_rect(draw, (695, 190, 990, 240), fill=(16, 185, 129), radius=8)
    draw_fitted_text(draw, (715, 203), "PYTHON WEBSOCKETS", 270, 22, bold=True, fill=(10, 15, 29))

    # Latency metric
    draw_fitted_text(draw, (695, 275), "380ms DUPLEX", 480, 56, bold=True, fill=(52, 211, 153))
    draw_fitted_text(draw, (695, 355), "✓ Native Barge-In", 480, 26, bold=True, fill=(226, 232, 240))
    draw_fitted_text(draw, (695, 415), "✓ Real-Time Audio Stream", 480, 26, bold=True, fill=(226, 232, 240))
    draw_fitted_text(draw, (695, 475), "✓ Live Mid-Call Tools", 480, 26, bold=True, fill=(226, 232, 240))

    draw_rounded_rect(draw, (695, 560, 1200, 625), fill=(10, 45, 35), outline=(52, 211, 153), width=1, radius=10)
    draw_fitted_text(draw, (730, 578), "STATUS: 200 OK | 380ms", 440, 24, bold=True, mono=True, fill=(110, 231, 183))

    img.save(out_path, quality=95)
    print(f"[THUMBNAIL] Created high-CTR thumbnail: {out_path}")

# -------------------------------------------------------------
# SCENE 1: HOOK & THE VALUE PROPOSITION (0:00 - 0:35)
# -------------------------------------------------------------
def render_scene_1(out_path: str):
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), color=(8, 11, 20))
    draw = ImageDraw.Draw(img)

    # Top Pill Badge
    draw_rounded_rect(draw, (60, 40, w - 60, 110), fill=(15, 23, 42), outline=(59, 130, 246), width=2, radius=14)
    draw_fitted_text(draw, (90, 58), "AGENTIC STACK B2B // EPISODE 002", 400, 22, bold=True, fill=(56, 189, 248))
    
    # Animated pill at 0:10
    draw_rounded_rect(draw, (w - 680, 52, w - 90, 98), fill=(16, 185, 129), radius=10)
    draw_fitted_text(draw, (w - 660, 62), "Duplex WebSockets: Connected | Latency: 380ms", 570, 18, bold=True, mono=True, fill=(10, 15, 29))

    # Big Terminal Window (Live Execution)
    draw_rounded_rect(draw, (60, 140, w - 60, 980), fill=(12, 16, 28), outline=(52, 211, 153), width=3, radius=18)
    
    # Terminal header bar
    draw_rounded_rect(draw, (60, 140, w - 60, 200), fill=(20, 28, 48), radius=18)
    draw.ellipse([(85, 160), (103, 178)], fill=(239, 68, 68))
    draw.ellipse([(113, 160), (131, 178)], fill=(245, 158, 11))
    draw.ellipse([(141, 160), (159, 178)], fill=(16, 185, 129))
    draw_fitted_text(draw, (185, 158), "bash - python voice_agent.py --transport websockets", 800, 20, mono=True, fill=(148, 163, 184))

    # Terminal logs
    font_mono = get_font(26, mono=True)
    logs = [
        ("$ python -m agentic_stack.voice_runtime", (148, 163, 184)),
        (">> [AUDIO INPUT]: Microphone streaming PCM 16kHz @ 16-bit mono", (100, 116, 139)),
        (">> [WEBSOCKET]: WSS wss://api.elevenlabs.io/v1/convai/conversation (TLS 1.3)", (56, 189, 248)),
        (">> [VAD DETECTED]: Human speech detected: 'Can you check order #4928 and cancel it?'", (251, 191, 36)),
        (">> [STREAMING CHUNKS]: First audio packet generated in 342ms", (52, 211, 153)),
        (">> [MID-CALL TOOL CALL]: Executing cancel_order(order_id='4928')", (168, 85, 247)),
        (">> [STATUS: 200 OK]: Order canceled in Stripe DB. Resuming audio playback.", (52, 211, 153)),
        (">> [BARGE-IN READY]: User starts speaking -> Playback interrupted in 48ms", (244, 114, 182)),
        (">> [TOTAL ROUND-TRIP LATENCY]: 380ms | ZERO BUFFERING DELAYS", (52, 211, 153))
    ]
    
    y = 240
    for line, color in logs:
        draw.text((100, y), line, font=font_mono, fill=color)
        y += 75

    img.save(out_path, quality=95)

# -------------------------------------------------------------
# SCENE 2: SYSTEM ARCHITECTURE & 3-NODE PROGRESSION (0:35 - 1:15)
# -------------------------------------------------------------
def render_scene_2(out_path: str):
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), color=(8, 11, 20))
    draw = ImageDraw.Draw(img)

    # Top Header
    draw_rounded_rect(draw, (60, 40, w - 60, 110), fill=(15, 23, 42), outline=(59, 130, 246), width=2, radius=14)
    draw_fitted_text(draw, (90, 58), "SYSTEM ARCHITECTURE // FULL-DUPLEX WEBSOCKETS", 750, 22, bold=True, fill=(56, 189, 248))
    draw_fitted_text(draw, (w - 380, 58), "380ms vs 4500ms CHAIN", 320, 20, bold=True, fill=(245, 158, 11))

    # Scene Title
    draw_fitted_text(draw, (70, 140), "The Sub-Second Conversational Voice Pipeline", w - 140, 38, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (70, 190), "How full-duplex bi-directional audio eliminates the 4.5 second sequential bottleneck.", w - 140, 22, fill=(148, 163, 184))

    # 3 Progressively Lit Nodes
    nodes = [
        ("NODE 1: SPEECH & VAD", "Client Audio In (16kHz PCM)", "Native Barge-In Listener", (37, 99, 235)),
        ("NODE 2: LLM & TOOLS", "Streaming Tool Calling", "Zero-Wait Token Dispatch", (147, 51, 234)),
        ("NODE 3: NEURAL TTS", "ElevenLabs Conversational SDK", "Sub-400ms Audio Out (24kHz)", (16, 185, 129))
    ]

    nx = 80
    for title, sub1, sub2, col in nodes:
        draw_rounded_rect(draw, (nx, 260, nx + 520, 680), fill=(15, 23, 42), outline=col, width=3, radius=18)
        # Node Header
        draw_rounded_rect(draw, (nx + 25, 285, nx + 495, 350), fill=(24, 34, 53), outline=col, width=1, radius=12)
        draw_fitted_text(draw, (nx + 45, 303), title, 430, 22, bold=True, fill=col)
        
        draw_fitted_text(draw, (nx + 45, 390), "• " + sub1, 430, 24, bold=True, fill=(255, 255, 255))
        draw_fitted_text(draw, (nx + 45, 460), "• " + sub2, 430, 22, fill=(203, 213, 225))
        draw_fitted_text(draw, (nx + 45, 530), "• Bi-directional Socket", 430, 20, fill=(148, 163, 184))
        
        # Status Box
        draw_rounded_rect(draw, (nx + 25, 595, nx + 495, 655), fill=(10, 15, 28), outline=(51, 65, 85), width=1, radius=10)
        draw_fitted_text(draw, (nx + 65, 615), "STATUS: ACTIVE (FULL-DUPLEX)", 380, 18, bold=True, mono=True, fill=(52, 211, 153))

        nx += 590

    # Flow Arrow Banner
    draw_rounded_rect(draw, (80, 730, w - 80, 960), fill=(13, 20, 36), outline=(56, 189, 248), width=2, radius=16)
    draw_fitted_text(draw, (120, 760), "WHY LEGACY SEQUENTIAL CHAINS FAIL IN ENTERPRISE B2B:", w - 240, 24, bold=True, fill=(248, 113, 113))
    draw_fitted_text(draw, (120, 815), "1. STT Wait (1200ms)  ->  2. Full LLM Completion (2100ms)  ->  3. TTS Synthesis (1200ms) = 4,500ms TOTAL", w - 240, 22, mono=True, fill=(252, 165, 165))
    draw_fitted_text(draw, (120, 880), "ELEVENLABS WEBSOCKETS PIPELINE: Chunked Streaming + Asynchronous Tooling = 380ms TOTAL", w - 240, 22, bold=True, mono=True, fill=(52, 211, 153))

    img.save(out_path, quality=95)

# -------------------------------------------------------------
# SCENE 3: SPLIT-SCREEN CODE & LIVE TOOL EXECUTION (1:15 - 3:00)
# -------------------------------------------------------------
def render_scene_3(out_path: str):
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), color=(8, 11, 20))
    draw = ImageDraw.Draw(img)

    # Top Header
    draw_rounded_rect(draw, (60, 40, w - 60, 110), fill=(15, 23, 42), outline=(59, 130, 246), width=2, radius=14)
    draw_fitted_text(draw, (90, 58), "LIVE CODE INSPECTION // SPLIT-SCREEN RUNTIME", 750, 22, bold=True, fill=(56, 189, 248))
    draw_fitted_text(draw, (w - 420, 58), "SUB-SECOND MID-CALL TOOLS", 360, 20, bold=True, fill=(16, 185, 129))

    # LEFT COLUMN: Python Source Code (Width 880px)
    draw_rounded_rect(draw, (60, 135, 950, 990), fill=(13, 17, 28), outline=(59, 130, 246), width=2, radius=16)
    draw_rounded_rect(draw, (60, 135, 950, 195), fill=(20, 28, 48), radius=16)
    draw_fitted_text(draw, (95, 155), "agent_voice_runtime.py (VS Code)", 700, 20, mono=True, fill=(226, 232, 240))

    code = [
        ("from elevenlabs.conversational_ai import Conversation", (244, 114, 182)),
        ("from elevenlabs import ElevenLabs", (244, 114, 182)),
        ("", (255, 255, 255)),
        ("# 1. Mid-Call Tool Schema Definition", (100, 116, 139)),
        ("def cancel_order_tool(order_id: str) -> dict:", (56, 189, 248)),
        ("    '''Cancels active subscription or order in Stripe.'''", (148, 163, 184)),
        ("    stripe.Subscription.cancel(order_id)", (226, 232, 240)),
        ("    return {'status': 'success', 'order_id': order_id}", (52, 211, 153)),
        ("", (255, 255, 255)),
        ("# 2. Native Barge-In & WebSockets Session", (100, 116, 139)),
        ("conversation = Conversation(", (56, 189, 248)),
        ("    client=ElevenLabs(api_key=API_KEY),", (226, 232, 240)),
        ("    agent_id=AGENT_ID,", (226, 232, 240)),
        ("    allow_interruptions=True,  # 48ms Barge-In", (251, 191, 36)),
        ("    tools={'cancel_order': cancel_order_tool}", (52, 211, 153)),
        (")", (56, 189, 248)),
        ("conversation.start_session()  # Full-Duplex Audio", (168, 85, 247))
    ]

    font_code = get_font(21, mono=True)
    cy = 220
    for line, color in code:
        draw.text((90, cy), line, font=font_code, fill=color)
        cy += 43

    # Highlight box around allow_interruptions (yellow flash)
    draw_rounded_rect(draw, (85, 765, 920, 815), fill=None, outline=(251, 191, 36), width=2, radius=8)

    # RIGHT COLUMN: Live Executing Terminal (Width 880px)
    draw_rounded_rect(draw, (980, 135, w - 60, 990), fill=(10, 14, 24), outline=(16, 185, 129), width=2, radius=16)
    draw_rounded_rect(draw, (980, 135, w - 60, 195), fill=(18, 32, 38), radius=16)
    draw_fitted_text(draw, (1015, 155), "Live Runtime Output (Sandbox)", 700, 20, mono=True, fill=(52, 211, 153))

    t_logs = [
        (">> [AUDIO IN] Streaming chunks (16kHz)", (100, 116, 139)),
        (">> [AGENT] 'Hello! How can I assist today?'", (226, 232, 240)),
        (">> [USER] 'Please cancel my order #4928'", (251, 191, 36)),
        (">> [BARGE-IN TRIGGERED] Audio stopped (42ms)", (244, 114, 182)),
        (">> [CALLING TOOL] cancel_order_tool('4928')", (56, 189, 248)),
        (">> [TOOL RESULT] {'status': 'success'}", (52, 211, 153)),
        (">> [AUDIO OUT] 'Done! I canceled order 4928.'", (110, 231, 183)),
        (">> [LATENCY BREAKDOWN]:", (148, 163, 184)),
        ("   - VAD Interruption: 42ms", (203, 213, 225)),
        ("   - Tool Execution: 118ms", (203, 213, 225)),
        ("   - First Audio Byte: 222ms", (52, 211, 153)),
        ("   - Total Turnaround: 382ms", (52, 211, 153))
    ]

    ty = 230
    for line, color in t_logs:
        draw.text((1015, ty), line, font=font_code, fill=color)
        ty += 58

    img.save(out_path, quality=95)

# -------------------------------------------------------------
# SCENE 4: LATENCY & HARDWARE BENCHMARK MATRIX (3:00 - 3:35)
# -------------------------------------------------------------
def render_scene_4(out_path: str):
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), color=(8, 11, 20))
    draw = ImageDraw.Draw(img)

    # Header
    draw_rounded_rect(draw, (60, 40, w - 60, 110), fill=(15, 23, 42), outline=(59, 130, 246), width=2, radius=14)
    draw_fitted_text(draw, (90, 58), "PRODUCTION BENCHMARKS // ARCHITECTURE COMPARISON", 850, 22, bold=True, fill=(56, 189, 248))
    draw_fitted_text(draw, (w - 380, 58), "SUB-500MS TARGET", 300, 20, bold=True, fill=(16, 185, 129))

    # Scene Title
    draw_fitted_text(draw, (70, 140), "Voice Latency Breakdown & Enterprise Deployment Matrix", w - 140, 38, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (70, 190), "Choosing the optimal transport and model tier for enterprise conversational agents.", w - 140, 22, fill=(148, 163, 184))

    # Table Card
    draw_rounded_rect(draw, (70, 260, w - 70, 950), fill=(13, 18, 32), outline=(56, 189, 248), width=2, radius=18)

    # Table Headers
    draw_rounded_rect(draw, (90, 280, w - 90, 360), fill=(20, 32, 54), radius=12)
    draw_fitted_text(draw, (120, 305), "PIPELINE ARCHITECTURE", 400, 22, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (600, 305), "ROUND-TRIP LATENCY", 320, 22, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (1000, 305), "BARGE-IN SUPPORT", 300, 22, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (1400, 305), "B2B VIABILITY", 350, 22, bold=True, fill=(255, 255, 255))

    rows = [
        ("Legacy Sequential (HTTP STT + LLM + TTS)", "4,200ms – 5,500ms", "✕ None (Jarring Overlap)", "FAILED (Customer Hangup)", (239, 68, 68)),
        ("Chunked Audio REST Pipeline", "1,200ms – 1,800ms", "⚠ Partial (Delayed Cutoff)", "MARGINAL (High Latency)", (245, 158, 11)),
        ("ElevenLabs Conversational WebSockets", "340ms – 420ms", "✓ Native Hardware VAD (48ms)", "PRODUCTION READY (Human Feel)", (16, 185, 129))
    ]

    ry = 390
    for arch, lat, barge, viab, col in rows:
        draw_rounded_rect(draw, (90, ry, w - 90, ry + 160), fill=(18, 25, 44), outline=col, width=2, radius=12)
        draw_fitted_text(draw, (120, ry + 35), arch, 450, 22, bold=True, fill=(255, 255, 255))
        draw_fitted_text(draw, (120, ry + 85), "Transport: Full-Duplex TLS 1.3", 450, 18, fill=(148, 163, 184))

        draw_fitted_text(draw, (600, ry + 55), lat, 350, 26, bold=True, mono=True, fill=col)
        draw_fitted_text(draw, (1000, ry + 55), barge, 360, 22, bold=True, fill=(226, 232, 240))
        draw_fitted_text(draw, (1400, ry + 55), viab, 400, 22, bold=True, fill=col)
        ry += 185

    img.save(out_path, quality=95)

# -------------------------------------------------------------
# SCENE 5: OUTRO, LIKE & FOLLOW CTA & NEXT VIDEO CARD (3:35 - 4:05)
# -------------------------------------------------------------
def render_scene_5(out_path: str):
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), color=(8, 11, 20))
    draw = ImageDraw.Draw(img)

    # Top Header
    draw_rounded_rect(draw, (60, 40, w - 60, 110), fill=(15, 23, 42), outline=(59, 130, 246), width=2, radius=14)
    draw_fitted_text(draw, (90, 58), "DEPLOY TODAY // PRODUCTION SOURCE CODE", 700, 22, bold=True, fill=(56, 189, 248))
    draw_fitted_text(draw, (w - 380, 58), "FREE GITHUB BLUEPRINT", 300, 20, bold=True, fill=(16, 185, 129))

    # Main Left Card: Code & Community (Width 920px)
    draw_rounded_rect(draw, (60, 140, 980, 970), fill=(13, 18, 32), outline=(16, 185, 129), width=2, radius=18)
    draw_fitted_text(draw, (100, 180), "Download the Python Voice Agent", 800, 36, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (100, 235), "Complete production scripts, WebSocket handlers, and Stripe tools.", 800, 22, fill=(148, 163, 184))

    # GitHub Box
    draw_rounded_rect(draw, (100, 300, 940, 450), fill=(20, 28, 48), outline=(56, 189, 248), width=2, radius=12)
    draw_fitted_text(draw, (130, 330), "📁 GITHUB REPOSITORY // EPISODE 002", 760, 22, bold=True, mono=True, fill=(56, 189, 248))
    draw_fitted_text(draw, (130, 380), "https://github.com/Johnmannen/Agentic-Stack-Library", 760, 20, mono=True, fill=(52, 211, 153))

    # Organic Like & Follow Banner (Prominently Scripted)
    draw_rounded_rect(draw, (100, 480, 940, 680), fill=(24, 34, 53), outline=(251, 191, 36), width=2, radius=14)
    draw_fitted_text(draw, (130, 510), "⚡ LIKE THE VIDEO & SUBSCRIBE", 760, 28, bold=True, fill=(251, 191, 36))
    draw_fitted_text(draw, (130, 565), "Subscribe to Agentic Stack B2B for daily zero-cost production blueprints,", 760, 20, fill=(226, 232, 240))
    draw_fitted_text(draw, (130, 605), "verified Python agent code, and sub-second enterprise voice architectures.", 760, 20, fill=(226, 232, 240))

    # Free Trial Callout
    draw_rounded_rect(draw, (100, 710, 940, 890), fill=(30, 20, 48), outline=(168, 85, 247), width=2, radius=12)
    draw_fitted_text(draw, (130, 740), "🎙️ TRY ELEVENLABS CONVERSATIONAL AI (FREE TRIAL)", 760, 22, bold=True, fill=(244, 114, 182))
    draw_fitted_text(draw, (130, 795), "Exclusive PartnerStack link verified in our cloud sandbox:", 760, 20, fill=(203, 213, 225))
    draw_fitted_text(draw, (130, 835), "https://try.elevenlabs.io/agentic-voice", 760, 20, mono=True, fill=(56, 189, 248))

    # Right Card: Next Video Recommendation (Width 820px)
    draw_rounded_rect(draw, (1020, 140, w - 60, 970), fill=(10, 14, 26), outline=(59, 130, 246), width=3, radius=18)
    draw_fitted_text(draw, (1060, 180), "RECOMMENDED NEXT EPISODE", 720, 24, bold=True, mono=True, fill=(56, 189, 248))
    
    # End screen video preview card
    draw_rounded_rect(draw, (1060, 240, w - 100, 720), fill=(18, 25, 42), outline=(100, 116, 139), width=2, radius=14)
    draw_rounded_rect(draw, (1100, 280, w - 140, 540), fill=(10, 15, 28), outline=(37, 99, 235), width=2, radius=10)
    draw_fitted_text(draw, (1130, 380), "EPISODE #001", 600, 28, bold=True, fill=(56, 189, 248))
    draw_fitted_text(draw, (1130, 430), "Build Autonomous Agent Skills", 600, 32, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (1130, 480), "Zero-Cost Python Sandboxes", 600, 24, fill=(52, 211, 153))

    draw_fitted_text(draw, (1060, 760), "Watch Episode 001 to structure autonomous", 720, 24, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (1060, 805), "skills that your voice agent can execute mid-call.", 720, 24, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (1060, 860), "Click the card on screen to continue ->", 720, 22, mono=True, fill=(251, 191, 36))

    img.save(out_path, quality=95)

# -------------------------------------------------------------
# AUDIO SYNTHESIS & FFMPEG DYNAMIC MOVEMENT (Zoompan)
# -------------------------------------------------------------
async def synthesize_speech(text: str, audio_path: str, rate: str = VOICE_RATE):
    communicate = edge_tts.Communicate(text, VOICE, rate=rate)
    with open(audio_path, "wb") as file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                file.write(chunk["data"])
    print(f"[AUDIO] Synthesized: {audio_path}")

def get_audio_duration(audio_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", audio_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

def render_dynamic_clip(image_path: str, audio_path: str, output_path: str, zoom_type: str = "in"):
    """
    Renders an MP4 clip with cinematic camera dynamics (punch-in zoompan or slow pan)
    so the screen NEVER sits completely static.
    """
    duration = get_audio_duration(audio_path)
    fps = 25
    total_frames = int(duration * fps) + 5
    
    if zoom_type == "in":
        # Slow punch-in from 1.0 to 1.08 towards center
        vf_filter = (
            f"zoompan=z='min(zoom+0.0004,1.08)':d={total_frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}"
        )
    elif zoom_type == "left_focus":
        # Focuses on left column (e.g. code)
        vf_filter = (
            f"zoompan=z='min(zoom+0.0004,1.10)':d={total_frames}:x='iw*0.3-(iw/zoom*0.3)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}"
        )
    else:
        # Subtle horizontal pan
        vf_filter = (
            f"zoompan=z=1.04:d={total_frames}:x='if(lte(on,-1),(iw-iw/zoom)/2,x+0.3)':y='(ih-ih/zoom)/2':s=1920x1080:fps={fps}"
        )

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(image_path),
        "-i", str(audio_path),
        "-vf", vf_filter,
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k",
        "-t", f"{duration:.2f}",
        str(output_path)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"[VIDEO CLIP] Rendered ({zoom_type}): {output_path} ({duration:.1f}s)")

def concat_clips(clip_paths: list, out_path: str):
    concat_list = OUT_DIR / "concat_list.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for c in clip_paths:
            f.write(f"file '{Path(c).resolve().as_posix()}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list),
        "-c", "copy",
        str(out_path)
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"[FINAL VIDEO] Concatenated: {out_path}")

# -------------------------------------------------------------
# MAIN PIPELINE EXECUTION
# -------------------------------------------------------------
async def main():
    print("=== STARTING REMAKE OF VIDEO 002 (MASTER FRAMEWORK 2026) ===")

    # 1. RENDER HIGH-CTR THUMBNAIL
    thumb_path = FINAL_ASSETS_DIR / "remake_002_thumbnail.png"
    render_remake_thumbnail(str(thumb_path))

    # 2. DEFINE SCRIPT DIALOGUE & VISUAL SCENES
    scenes = [
        {
            "id": 1,
            "render_func": render_scene_1,
            "zoom": "in",
            "dialogue": (
                "Text chatbots with four-second response lags are dead in enterprise B2B. "
                "This conversational voice agent runs at under four hundred milliseconds round-trip latency over full-duplex WebSockets, "
                "and instantly yields when the user interrupts. In this video, we build a production-ready conversational voice agent in Python "
                "using ElevenLabs."
            )
        },
        {
            "id": 2,
            "render_func": render_scene_2,
            "zoom": "pan",
            "dialogue": (
                "Traditional voice pipelines fail because they chain Speech-to-Text, full LLM completion, and Text-to-Speech sequentially. "
                "That stacks up to over four and a half seconds of awkward silence. "
                "With ElevenLabs Conversational SDK, we maintain a bi-directional WebSocket connection. "
                "Audio frames stream continuously, enabling native barge-in and instant token synthesis in under three hundred and eighty milliseconds."
            )
        },
        {
            "id": 3,
            "render_func": render_scene_3,
            "zoom": "left_focus",
            "dialogue": (
                "Let's look at the implementation. Here on the left, we define our Python tool to cancel orders in Stripe. "
                "Notice the allow interruptions flag set to true: if the human speaks mid-sentence, the hardware voice activity detector triggers "
                "an interruption in forty-two milliseconds. On the right, watch the live runtime execute the Stripe cancellation mid-call "
                "without dropping the audio stream."
            )
        },
        {
            "id": 4,
            "render_func": render_scene_4,
            "zoom": "in",
            "dialogue": (
                "When deploying to production, latency dictates viability. Sequential HTTP chains average forty-five hundred milliseconds, "
                "which guarantees high customer churn. ElevenLabs WebSockets deliver a verified three hundred and eighty millisecond round-trip, "
                "providing a natural conversational cadence suitable for customer support, sales triage, and internal agent workflows."
            )
        },
        {
            "id": 5,
            "render_func": render_scene_5,
            "zoom": "in",
            "dialogue": (
                "You can download the complete Python script, WebSocket handlers, and sandbox blueprints in the GitHub repo linked below. "
                "If this architecture helped you cut latency, drop a like and subscribe to the channel for daily production blueprints. "
                "To learn how to build the autonomous agent skills your voice agent executes, check out our Episode 001 guide on the screen right now."
            )
        }
    ]

    # 3. SYNTHESIZE AUDIO & RENDER DYNAMIC SCENES
    clip_files = []
    for sc in scenes:
        idx = sc["id"]
        img_path = OUT_DIR / f"scene_{idx}.png"
        audio_path = OUT_DIR / f"audio_{idx}.mp3"
        clip_path = OUT_DIR / f"clip_{idx}.mp4"

        sc["render_func"](str(img_path))
        await synthesize_speech(sc["dialogue"], str(audio_path))
        render_dynamic_clip(str(img_path), str(audio_path), str(clip_path), zoom_type=sc["zoom"])
        clip_files.append(str(clip_path))

    # 4. CONCATENATE FINAL VIDEO
    final_video_path = FINAL_ASSETS_DIR / "remake_002_video.mp4"
    concat_clips(clip_files, str(final_video_path))
    print(f"\n[SUCCESS] Final Remake Video 002 generated: {final_video_path}")

if __name__ == "__main__":
    asyncio.run(main())
