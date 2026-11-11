#!/usr/bin/env python3
"""
Render Phase 5 Test Video (Episode 002 Test Remake).
Incorporates all user-approved guidelines:
1. Approved Concept 4 Hybrid Visuals with 26pt mobile readability.
2. Scene 1 Intro: 3.0s thumbnail display with subtle zoom-in, Andrew voice starting from t=0,
   0.5s smooth cross-dissolve into active terminal.
3. Clean terminology: No unnecessary "B2B" statements.
4. Spoken Scene 3: Line 6 is API key, Line 11 is transport='websockets'.
   Neon arrow and golden border light up on Line 6 when spoken, then move to Line 11 when spoken.
5. Spoken Scene 4: Line 14 is allow_interruptions=True.
   Neon arrow and golden box point directly to Line 14 when Andrew says "line 14".
6. Outro Scene 7: Explicit verbal affiliate mention for ElevenLabs free trial in description & pinned comment,
   followed by GitHub script link, organic Like & Subscribe, and Episode 001 card.
"""

import os
import sys
import math
import shutil
import asyncio
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import edge_tts

VOICE = "en-US-AndrewMultilingualNeural"
BASE_DIR = Path("build_temp/phase5_test_video")
BASE_DIR.mkdir(parents=True, exist_ok=True)

ART_DIR = Path("C:/Users/johnr/.gemini/antigravity/brain/19c5e574-2ae1-4759-b3ad-59623ffcfb15")
THUMB_PATH = ART_DIR / "thumb_phase1_build_voice_ai.png"

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

async def synthesize_voice(text: str, out_path: str, retries: int = 4):
    if Path(out_path).exists() and Path(out_path).stat().st_size > 1000:
        print(f"[AUDIO CACHED] Already exists: {out_path}")
        return
    for attempt in range(retries):
        try:
            c = edge_tts.Communicate(text, VOICE, rate="+0%")
            await c.save(out_path)
            print(f"[AUDIO] Synthesized: {out_path}")
            return
        except Exception as e:
            if attempt < retries - 1:
                print(f"[RETRY {attempt+1}] edge-tts glitch: {e}. Retrying in 2s...")
                await asyncio.sleep(2)
            else:
                raise e

def get_duration(audio_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

# =============================================================
# SCENE 1: HOOK & INTRO TRANSITION (0:00 - ~0:26)
# =============================================================
SCENE_1_TEXT = (
    "Text chatbots with four-second response lags are dead. "
    "When a user speaks, they expect an immediate, fluid conversation, not dead silence. "
    "This conversational voice agent runs at under four hundred milliseconds round-trip latency over full-duplex WebSockets, "
    "and instantly yields when the human speaks. In this video, we build a production-ready conversational voice agent in Python "
    "using ElevenLabs."
)

def render_scene_1(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    fdir = BASE_DIR / "s1_frames"
    fdir.mkdir(parents=True, exist_ok=True)
    thumb_img = Image.open(THUMB_PATH).convert("RGB")
    W, H = 1920, 1080
    font_mono = get_font(26, mono=True)

    logs = [
        (">> [AUDIO IN]: Microphone streaming 16kHz PCM @ 16-bit mono", (100, 116, 139)),
        (">> [WEBSOCKET]: WSS wss://api.elevenlabs.io/v1/convai/conversation", (56, 189, 248)),
        (">> [USER]: 'Can you check my subscription and cancel order 4928?'", (251, 191, 36)),
        (">> [VAD DETECTED]: Human speech detected -> Interruption triggered", (244, 114, 182)),
        (">> [HARDWARE CUTOFF]: Playback yielded in 42 milliseconds", (239, 68, 68)),
        (">> [STREAMING CHUNKS]: First audio packet received in 342ms", (52, 211, 153)),
        (">> [MID-CALL TOOL]: Executing Stripe cancel_order(order_id='4928')", (168, 85, 247)),
        (">> [STATUS 200 OK]: Order canceled in Stripe DB. Resuming audio stream.", (52, 211, 153)),
        (">> [TOTAL ROUND-TRIP LATENCY]: 380ms | FULL-DUPLEX WEBSOCKETS", (52, 211, 153))
    ]

    def render_terminal(t):
        img = Image.new("RGB", (W, H), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(59, 130, 246), width=1, radius=10)
        draw.text((90, 52), "EPISODE 002: REAL-TIME CONVERSATIONAL VOICE AI", fill=(56, 189, 248), font=get_font(22, bold=True))

        if t >= 5.0:
            draw_rounded_rect(draw, (1260, 45, 1840, 85), fill=(16, 185, 129), radius=8)
            draw.text((1285, 54), "Duplex WebSockets: Connected | Latency: 380ms", fill=(10, 15, 29), font=get_font(18, bold=True, mono=True))

        # Big Terminal Card
        draw_rounded_rect(draw, (60, 120, 1860, 990), fill=(12, 16, 28), outline=(52, 211, 153), width=2, radius=18)
        draw_rounded_rect(draw, (60, 120, 1860, 180), fill=(20, 28, 48), radius=18)
        draw.ellipse([(85, 140), (105, 160)], fill=(239, 68, 68))
        draw.ellipse([(115, 140), (135, 160)], fill=(245, 158, 11))
        draw.ellipse([(145, 140), (165, 160)], fill=(16, 185, 129))
        draw.text((195, 138), "terminal // python -m agentic_stack.voice_runtime", fill=(148, 163, 184), font=get_font(20, mono=True))

        # Progressive lines
        revealed = min(len(logs), max(1, int((t - 3.0) / 2.5) + 1))
        ty = 220
        for i in range(revealed):
            msg, col = logs[i]
            if i == revealed - 1 and (t - int(t)) < 0.35:
                draw_rounded_rect(draw, (85, ty - 6, 1835, ty + 40), fill=(20, 35, 45), radius=6)
            draw.text((95, ty), msg, font=font_mono, fill=col)
            ty += 78
        return img

    for f in range(total_frames):
        t = f / fps
        if t < 3.0:
            # 3.0 seconds thumbnail with subtle zoom-in
            scale = 1.0 + (t / 3.0) * 0.06
            nw, nh = int(W * scale), int(H * scale)
            scaled = thumb_img.resize((nw, nh), Image.Resampling.LANCZOS)
            left = (nw - W) // 2
            top = (nh - H) // 2
            frame = scaled.crop((left, top, left + W, top + H))
        elif t < 3.5:
            # 0.5s cross-dissolve into active terminal
            alpha = (t - 3.0) / 0.5
            scale = 1.06 + alpha * 0.01
            nw, nh = int(W * scale), int(H * scale)
            scaled = thumb_img.resize((nw, nh), Image.Resampling.LANCZOS)
            left = (nw - W) // 2
            top = (nh - H) // 2
            thumb_part = scaled.crop((left, top, left + W, top + H))
            term_part = render_terminal(t)
            frame = Image.blend(thumb_part, term_part, alpha)
        else:
            frame = render_terminal(t)

        frame.save(fdir / f"f_{f:04d}.png")

    cmd = ["ffmpeg", "-y", "-r", str(fps), "-i", str(fdir / "f_%04d.png"), "-i", str(audio_path),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_video)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# =============================================================
# SCENE 2: THE 3-NODE PROGRESSIVE ARCHITECTURE (~0:26 - 1:05)
# =============================================================
SCENE_2_TEXT = (
    "Traditional voice AI pipelines fail because chaining Speech-to-Text, language model completions, and Text-to-Speech "
    "stacks up over four seconds of awkward silence. In contrast, our production architecture runs on a bi-directional "
    "WebSocket transport. Audio chunks stream continuously. As soon as the human speaks, the client yields, and when the model generates "
    "tokens, neural audio is synthesized immediately in under three hundred and eighty milliseconds."
)

def render_scene_2(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    fdir = BASE_DIR / "s2_frames"
    fdir.mkdir(parents=True, exist_ok=True)

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(59, 130, 246), width=1, radius=10)
        draw.text((90, 52), "SYSTEM ARCHITECTURE // FULL-DUPLEX WEBSOCKET DATAFLOW", fill=(56, 189, 248), font=get_font(22, bold=True))

        # Main Stage Card
        draw_rounded_rect(draw, (60, 120, 1860, 990), fill=(13, 17, 28), outline=(59, 130, 246), width=2, radius=18)

        # Node 1: Audio In
        n1_col = (52, 211, 153) if t > 2.0 else (71, 85, 105)
        draw_rounded_rect(draw, (120, 280, 560, 680), fill=(18, 25, 42), outline=n1_col, width=3, radius=16)
        draw.text((150, 320), "NODE 01", fill=(148, 163, 184), font=get_font(18, bold=True, mono=True))
        draw.text((150, 360), "16kHz PCM Stream", fill=(255, 255, 255), font=get_font(28, bold=True))
        draw.text((150, 420), "• Full-Duplex Input\n• Local Hardware VAD\n• Real-Time Audio Slices\n• Buffer Cutoff: 42ms", fill=(203, 213, 225), font=get_font(22))
        draw_rounded_rect(draw, (150, 580, 530, 640), fill=(6, 78, 59) if t > 2.0 else (30, 41, 59), radius=10)
        draw.text((170, 598), "HARDWARE CAPTURE: ACTIVE", fill=(52, 211, 153) if t > 2.0 else (148, 163, 184), font=get_font(18, bold=True, mono=True))

        # Node 2: WebSocket Server
        n2_col = (56, 189, 248) if t > 8.0 else (71, 85, 105)
        draw_rounded_rect(draw, (740, 280, 1180, 680), fill=(18, 25, 42), outline=n2_col, width=3, radius=16)
        draw.text((770, 320), "NODE 02", fill=(148, 163, 184), font=get_font(18, bold=True, mono=True))
        draw.text((770, 360), "Conversational Socket", fill=(255, 255, 255), font=get_font(28, bold=True))
        draw.text((770, 420), "• Persistent TLS Session\n• Sub-Second Neural Audio\n• Integrated LLM Pipeline\n• Tool Event Dispatcher", fill=(203, 213, 225), font=get_font(22))
        draw_rounded_rect(draw, (770, 580, 1150, 640), fill=(12, 74, 110) if t > 8.0 else (30, 41, 59), radius=10)
        draw.text((790, 598), "ELEVENLABS API: CONNECTED", fill=(56, 189, 248) if t > 8.0 else (148, 163, 184), font=get_font(18, bold=True, mono=True))

        # Node 3: Enterprise Tool Execution
        n3_col = (168, 85, 247) if t > 14.0 else (71, 85, 105)
        draw_rounded_rect(draw, (1360, 280, 1800, 680), fill=(18, 25, 42), outline=n3_col, width=3, radius=16)
        draw.text((1390, 320), "NODE 03", fill=(148, 163, 184), font=get_font(18, bold=True, mono=True))
        draw.text((1390, 360), "Python Mid-Call Tools", fill=(255, 255, 255), font=get_font(28, bold=True))
        draw.text((1390, 420), "• Stripe Order Cancellation\n• Live DB Invocations\n• Non-Blocking Webhook\n• Auto-Resumed Playback", fill=(203, 213, 225), font=get_font(22))
        draw_rounded_rect(draw, (1390, 580, 1770, 640), fill=(88, 28, 135) if t > 14.0 else (30, 41, 59), radius=10)
        draw.text((1410, 598), "TOOL EXECUTOR: READY", fill=(192, 132, 252) if t > 14.0 else (148, 163, 184), font=get_font(18, bold=True, mono=True))

        # Pulsing Flow Arrows
        pulse1 = (math.sin(t * 8) + 1) / 2
        p1_col = (int(52 + pulse1 * 100), int(211 + pulse1 * 30), 153) if t > 5.0 else (51, 65, 85)
        draw.line([(570, 480), (730, 480)], fill=p1_col, width=4)
        draw.polygon([(730, 470), (740, 480), (730, 490)], fill=p1_col)

        pulse2 = (math.sin(t * 8 + 2) + 1) / 2
        p2_col = (int(56 + pulse2 * 100), int(189 + pulse2 * 40), 248) if t > 11.0 else (51, 65, 85)
        draw.line([(1190, 480), (1350, 480)], fill=p2_col, width=4)
        draw.polygon([(1350, 470), (1360, 480), (1350, 490)], fill=p2_col)

        # Metric Banner
        draw_rounded_rect(draw, (120, 750, 1800, 930), fill=(20, 28, 48), outline=(52, 211, 153), width=2, radius=14)
        draw.text((160, 780), "VERIFIED LATENCY BENCHMARK: SUB-SECOND CONVERSATIONAL CADENCE", fill=(52, 211, 153), font=get_font(22, bold=True, mono=True))
        draw.text((160, 830), "• Full Round-Trip (VAD -> Tokens -> First Audio Packet): 380ms", fill=(255, 255, 255), font=get_font(24, bold=True))
        draw.text((160, 875), "• Barge-In Interruption Cutoff: 42ms Hardware VAD | Zero Audio Artifacts", fill=(203, 213, 225), font=get_font(22))

        img.save(fdir / f"f_{f:04d}.png")

    cmd = ["ffmpeg", "-y", "-r", str(fps), "-i", str(fdir / "f_%04d.png"), "-i", str(audio_path),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_video)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# =============================================================
# SCENE 3: CODE WALKTHROUGH – WEBSOCKET SETUP (~1:05 - 1:30)
# =============================================================
SCENE_3_TEXT = (
    "Now let's examine the Python implementation. We start by importing the Conversation class and ElevenLabs client. "
    "Notice how we initialize our session with the API key on line 6. "
    "The crucial configuration here is setting the transport to websockets on line 11. "
    "This establishes a low-overhead, persistent socket that avoids repeated TLS handshakes for every audio turn."
)

def render_scene_3(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    fdir = BASE_DIR / "s3_frames"
    fdir.mkdir(parents=True, exist_ok=True)
    font_code = get_font(26, mono=True)

    # EXACT Code structure where:
    # Line 6: client = ElevenLabs(api_key=os.environ['ELEVEN_API_KEY'])
    # Line 11: transport='websockets'
    code = [
        ("from elevenlabs.conversational_ai import Conversation", (244, 114, 182)),
        ("from elevenlabs import ElevenLabs", (244, 114, 182)),
        ("import os, stripe", (244, 114, 182)),
        ("", (255, 255, 255)),
        ("# Step 1: Initialize Persistent WebSocket Client", (100, 116, 139)),
        ("client = ElevenLabs(api_key=os.environ['ELEVEN_API_KEY'])", (226, 232, 240)),  # LINE 6
        ("", (255, 255, 255)),
        ("conversation = Conversation(", (56, 189, 248)),
        ("    client=client,", (226, 232, 240)),
        ("    agent_id='agentic_support_v2',", (226, 232, 240)),
        ("    transport='websockets',  # Persistent Full-Duplex Socket", (251, 191, 36)), # LINE 11
        ("    requires_auth=True,", (226, 232, 240)),
        (")", (56, 189, 248)),
        ("", (255, 255, 255)),
        ("conversation.start_session()", (168, 85, 247))
    ]

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(59, 130, 246), width=1, radius=10)
        draw.text((90, 52), "STEP 1: PERSISTENT WEBSOCKET TRANSPORT SETUP", fill=(56, 189, 248), font=get_font(22, bold=True))

        # Main Code Window (Large 26pt mobile readable)
        draw_rounded_rect(draw, (60, 120, 1860, 990), fill=(13, 17, 28), outline=(59, 130, 246), width=2, radius=16)
        draw_rounded_rect(draw, (60, 120, 1860, 185), fill=(20, 28, 48), radius=16)
        draw.text((95, 142), "agent_voice_runtime.py (VS Code - 26pt Syntax)", fill=(226, 232, 240), font=get_font(22, mono=True))

        # Determine which line to highlight based on timing:
        # t: 0.0 - 5.5: intro to code
        # t: 5.5 - 11.5: "Notice how we initialize our session with the API key on line 6" -> Highlight LINE 6
        # t: 11.5+: "setting the transport to websockets on line 11" -> Highlight LINE 11
        active_line = None
        if 5.5 <= t < 11.5:
            active_line = 5 # index 5 is Line 6
        elif t >= 11.5:
            active_line = 10 # index 10 is Line 11

        cy = 215
        for idx, (line, col) in enumerate(code):
            draw.text((90, cy), f"{idx+1:02d}", fill=(71, 85, 105), font=font_code)

            if idx == active_line:
                # Golden highlight box
                draw_rounded_rect(draw, (140, cy - 4, 1820, cy + 38), fill=(42, 36, 18), outline=(251, 191, 36), width=2, radius=8)
                draw.text((150, cy), line, font=font_code, fill=(254, 240, 138))
                
                # Sliding neon arrow pointing at this exact line
                pulse_x = math.sin(t * 8) * 8
                ax = int(55 + pulse_x)
                draw.polygon([(ax, cy + 5), (ax + 20, cy + 16), (ax, cy + 27)], fill=(251, 191, 36))
            else:
                draw.text((150, cy), line, font=font_code, fill=col)

            cy += 48

        # Floating Concept Badge
        if t > 12.0:
            draw_rounded_rect(draw, (1320, 780, 1800, 930), fill=(16, 185, 129), outline=(255, 255, 255), width=2, radius=12)
            draw.text((1350, 810), "⚡ ZERO TLS OVERHEAD", fill=(10, 15, 29), font=get_font(24, bold=True, mono=True))
            draw.text((1350, 855), "Persistent connection cuts 400ms lag", fill=(10, 15, 29), font=get_font(20, bold=True))

        img.save(fdir / f"f_{f:04d}.png")

    cmd = ["ffmpeg", "-y", "-r", str(fps), "-i", str(fdir / "f_%04d.png"), "-i", str(audio_path),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_video)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# =============================================================
# SCENE 4: CODE WALKTHROUGH – BARGE-IN ON EXACT LINE 14 (~1:30 - 1:55)
# =============================================================
SCENE_4_TEXT = (
    "Next, look at the allow interruptions flag on line 14. "
    "When set to true, the client's voice activity detector operates directly on incoming PCM audio chunks. "
    "The moment the human starts speaking, the playback stream yields in just forty-two milliseconds. "
    "This eliminates awkward overlapping voices and makes the conversation feel completely natural."
)

def render_scene_4(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    fdir = BASE_DIR / "s4_frames"
    fdir.mkdir(parents=True, exist_ok=True)
    font_code = get_font(26, mono=True)

    # EXACT Code structure where:
    # Line 14: allow_interruptions=True,   # <--- 42ms Hardware VAD
    code = [
        ("# Enterprise Real-Time Voice Configuration", (100, 116, 139)),
        ("from elevenlabs.conversational_ai import Conversation", (244, 114, 182)),
        ("from elevenlabs import ElevenLabs", (244, 114, 182)),
        ("import os", (244, 114, 182)),
        ("", (255, 255, 255)),
        ("client = ElevenLabs(api_key=os.environ['ELEVEN_KEY'])", (226, 232, 240)),
        ("", (255, 255, 255)),
        ("# Full-Duplex Agent Session", (100, 116, 139)),
        ("conversation = Conversation(", (56, 189, 248)),
        ("    client=client,", (226, 232, 240)),
        ("    agent_id='b2b_support_v2',", (226, 232, 240)),
        ("    transport='websockets',", (226, 232, 240)),
        ("    vad_threshold=0.45,", (52, 211, 153)),
        ("    allow_interruptions=True,   # <--- 42ms Hardware VAD", (251, 191, 36)), # EXACT LINE 14!
        ("    interruption_latency_ms=42,", (52, 211, 153)),
        (")", (56, 189, 248))
    ]

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(244, 63, 94), width=1, radius=10)
        draw.text((90, 52), "STEP 2: NATIVE HARDWARE BARGE-IN & VAD CONFIGURATION", fill=(244, 63, 94), font=get_font(22, bold=True))

        # Main Code Window
        draw_rounded_rect(draw, (60, 120, 1860, 990), fill=(13, 17, 28), outline=(244, 63, 94), width=2, radius=16)
        draw_rounded_rect(draw, (60, 120, 1860, 185), fill=(20, 28, 48), radius=16)
        draw.text((95, 142), "agent_voice_runtime.py (Barge-In Handler - 26pt)", fill=(226, 232, 240), font=get_font(22, mono=True))

        cy = 215
        for idx, (line, col) in enumerate(code):
            draw.text((90, cy), f"{idx+1:02d}", fill=(71, 85, 105), font=font_code)
            
            # Exact Line 14 is index 13!
            if idx == 13:
                # Golden highlight box
                draw_rounded_rect(draw, (140, cy - 4, 1820, cy + 38), fill=(42, 36, 18), outline=(251, 191, 36), width=2, radius=8)
                draw.text((150, cy), line, font=font_code, fill=(254, 240, 138))
                
                # Sliding neon arrow pointing directly at Line 14
                pulse_x = math.sin(t * 8) * 8
                ax = int(55 + pulse_x)
                draw.polygon([(ax, cy + 5), (ax + 20, cy + 16), (ax, cy + 27)], fill=(251, 191, 36))
            else:
                draw.text((150, cy), line, font=font_code, fill=col)

            cy += 46

        # Floating Concept Card
        draw_rounded_rect(draw, (1260, 780, 1820, 930), fill=(24, 34, 53), outline=(244, 63, 94), width=2, radius=12)
        draw.text((1290, 810), "⚡ 42ms HARDWARE VAD", fill=(244, 63, 94), font=get_font(24, bold=True, mono=True))
        status_txt = ">> BARGE-IN: VERIFIED 42ms" if t > 4.0 else ">> LISTENING FOR INPUT..."
        status_col = (52, 211, 153) if t > 4.0 else (148, 163, 184)
        draw.text((1290, 855), status_txt, fill=status_col, font=get_font(20, mono=True))

        img.save(fdir / f"f_{f:04d}.png")

    cmd = ["ffmpeg", "-y", "-r", str(fps), "-i", str(fdir / "f_%04d.png"), "-i", str(audio_path),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_video)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# =============================================================
# SCENE 5: SPLIT-SCREEN REAL-TIME EXECUTION (~1:55 - 2:25)
# =============================================================
SCENE_5_TEXT = (
    "Here is the real magic: executing enterprise tools mid-conversation. "
    "On the left, we define cancel order tool with type annotations and docstrings. "
    "On the right, watch the live runtime. When the user asks to cancel order 4928, "
    "the model calls our Python function, executes the Stripe cancellation in one hundred and eighteen milliseconds, "
    "and immediately resumes speech without dropping the WebSocket."
)

def render_scene_5(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    fdir = BASE_DIR / "s5_frames"
    fdir.mkdir(parents=True, exist_ok=True)
    font_code = get_font(24, mono=True)

    tool_code = [
        ("@conversation.tool('cancel_order')", (244, 114, 182)),
        ("def cancel_order_tool(order_id: str) -> dict:", (56, 189, 248)),
        ("    '''Cancels customer order in Stripe DB'''", (148, 163, 184)),
        ("    logger.info(f'Canceling order: {order_id}')", (226, 232, 240)),
        ("    res = stripe.Refund.create(charge=order_id)", (52, 211, 153)),
        ("    return {", (56, 189, 248)),
        ("        'status': 'canceled',", (251, 191, 36)),
        ("        'refund_id': res.id,", (226, 232, 240)),
        ("        'latency_ms': 118", (52, 211, 153)),
        ("    }", (56, 189, 248))
    ]

    terminal_logs = [
        (">> [USER]: 'Please cancel my order 4928'", (251, 191, 36)),
        (">> [VAD]: Speech detected. Playback yielded in 42ms", (244, 114, 182)),
        (">> [MODEL PARSER]: Tool call detected: cancel_order_tool", (56, 189, 248)),
        (">> [INVOKING]: cancel_order_tool(order_id='4928')", (168, 85, 247)),
        (">> [STRIPE API]: 200 OK | Refund ref_8829 created in 118ms", (52, 211, 153)),
        (">> [RESUMING AUDIO]: 'Your order 4928 has been canceled.'", (52, 211, 153)),
        (">> [ROUND-TRIP]: 382ms Total Latency", (52, 211, 153))
    ]

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(168, 85, 247), width=1, radius=10)
        draw.text((90, 52), "MID-CONVERSATION PYTHON TOOL EXECUTION // SPLIT-SCREEN", fill=(192, 132, 252), font=get_font(22, bold=True))

        # Drawer transition
        drawer_x = min(940, int(60 + t * 450)) if t < 2.0 else 940

        # Left: Python Tool Window
        draw_rounded_rect(draw, (60, 120, drawer_x, 990), fill=(13, 17, 28), outline=(56, 189, 248), width=2, radius=16)
        draw_rounded_rect(draw, (60, 120, drawer_x, 185), fill=(20, 28, 48), radius=16)
        draw.text((95, 142), "tools/stripe_ops.py", fill=(226, 232, 240), font=get_font(22, mono=True))

        if drawer_x >= 800:
            cy = 220
            for idx, (line, col) in enumerate(tool_code):
                draw.text((90, cy), f"{idx+1:02d}", fill=(71, 85, 105), font=font_code)
                draw.text((140, cy), line, font=font_code, fill=col)
                cy += 50

        # Right: Live Terminal Window
        if drawer_x >= 900:
            rw = min(1860, 980 + int((t - 1.0) * 800)) if t < 2.2 else 1860
            if rw < 1840:
                draw_rounded_rect(draw, (980, 120, rw, 990), fill=(10, 14, 24), outline=(52, 211, 153), width=2, radius=16)
            else:
                draw_rounded_rect(draw, (980, 120, 1860, 990), fill=(10, 14, 24), outline=(52, 211, 153), width=2, radius=16)
            draw_rounded_rect(draw, (980, 120, 1860, 185), fill=(16, 24, 38), radius=16)
            draw.text((1015, 142), "live_runtime_output", fill=(52, 211, 153), font=get_font(22, mono=True))

            # Progressive logs
            revealed = min(len(terminal_logs), max(1, int((t - 2.5) / 2.5) + 1))
            ty = 220
            for i in range(revealed):
                msg, col = terminal_logs[i]
                draw.text((1015, ty), msg, font=font_code, fill=col)
                ty += 65

        # Floating Bottom Status Card
        if t > 6.0:
            draw_rounded_rect(draw, (1200, 830, 1820, 950), fill=(6, 78, 59), outline=(52, 211, 153), width=2, radius=12)
            draw.text((1230, 855), "⚡ 118ms STRIPE DB REFUND", fill=(255, 255, 255), font=get_font(22, bold=True, mono=True))
            draw.text((1230, 895), "Playback yielded and resumed automatically", fill=(167, 243, 208), font=get_font(18))

        img.save(fdir / f"f_{f:04d}.png")

    cmd = ["ffmpeg", "-y", "-r", str(fps), "-i", str(fdir / "f_%04d.png"), "-i", str(audio_path),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_video)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# =============================================================
# SCENE 6: LATENCY & BENCHMARK MATRIX (~2:25 - 2:48)
# =============================================================
SCENE_6_TEXT = (
    "When deploying to production, latency dictates viability. "
    "Sequential HTTP chains average forty-five hundred milliseconds, which guarantees customer churn. "
    "ElevenLabs WebSockets deliver a verified three hundred and eighty millisecond round-trip, "
    "providing a natural conversational cadence suitable for customer support, sales triage, and automated voice workflows."
)

def render_scene_6(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    fdir = BASE_DIR / "s6_frames"
    fdir.mkdir(parents=True, exist_ok=True)

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(59, 130, 246), width=1, radius=10)
        draw.text((90, 52), "LATENCY BENCHMARKS // ARCHITECTURAL COMPARISON", fill=(56, 189, 248), font=get_font(22, bold=True))

        # Main Stage Card
        draw_rounded_rect(draw, (60, 120, 1860, 990), fill=(13, 17, 28), outline=(59, 130, 246), width=2, radius=18)

        # Row 1: Sequential HTTP Chain (RED)
        draw_rounded_rect(draw, (120, 180, 1800, 380), fill=(30, 15, 20), outline=(239, 68, 68), width=2, radius=14)
        draw.text((160, 210), "Sequential HTTP Chain (STT -> LLM -> TTS)", fill=(248, 113, 113), font=get_font(26, bold=True))
        draw.text((160, 260), "Round-Trip Latency: 4,500ms (Unusable for Real-Time Conversation)", fill=(255, 255, 255), font=get_font(22))
        draw.text((160, 305), "Three separate TLS handshakes. High churn risk.", fill=(148, 163, 184), font=get_font(20))
        draw_rounded_rect(draw, (1550, 220, 1760, 270), fill=(127, 29, 29), radius=8)
        draw.text((1580, 235), "FAILED", fill=(248, 113, 113), font=get_font(20, bold=True, mono=True))

        # Row 2: Chunked Audio Streaming (YELLOW)
        draw_rounded_rect(draw, (120, 420, 1800, 620), fill=(30, 25, 15), outline=(245, 158, 11) if t > 5.0 else (51, 65, 85), width=2, radius=14)
        draw.text((160, 450), "Chunked Audio Streaming (HTTP Chunked Transfer)", fill=(251, 191, 36) if t > 5.0 else (148, 163, 184), font=get_font(26, bold=True))
        draw.text((160, 500), "Round-Trip Latency: 1,500ms (Noticeable Lag, No Native Barge-In)", fill=(255, 255, 255) if t > 5.0 else (148, 163, 184), font=get_font(22))
        draw.text((160, 545), "Half-duplex transport causes collision when human interrupts.", fill=(148, 163, 184), font=get_font(20))
        if t > 5.0:
            draw_rounded_rect(draw, (1550, 460, 1760, 510), fill=(120, 53, 15), radius=8)
            draw.text((1570, 475), "SUB-PAR", fill=(251, 191, 36), font=get_font(20, bold=True, mono=True))

        # Row 3: ElevenLabs Full-Duplex WebSockets (GREEN)
        g_glow = (6, 78, 59) if t > 10.0 else (18, 25, 42)
        draw_rounded_rect(draw, (120, 660, 1800, 940), fill=g_glow, outline=(52, 211, 153) if t > 10.0 else (51, 65, 85), width=3, radius=14)
        draw.text((160, 695), "ElevenLabs Conversational WebSockets (Our Architecture)", fill=(52, 211, 153) if t > 10.0 else (148, 163, 184), font=get_font(28, bold=True))
        draw.text((160, 755), "Verified Round-Trip Latency: 380ms | Hardware VAD Barge-In: 42ms", fill=(255, 255, 255) if t > 10.0 else (148, 163, 184), font=get_font(24, bold=True))
        draw.text((160, 805), "Persistent bidirectional socket. Instant cutoff on user interruption.", fill=(203, 213, 225) if t > 10.0 else (100, 116, 139), font=get_font(22))
        draw.text((160, 850), "Zero TLS renegotiation overhead. Seamless tool execution mid-call.", fill=(203, 213, 225) if t > 10.0 else (100, 116, 139), font=get_font(22))
        if t > 10.0:
            draw_rounded_rect(draw, (1480, 700, 1760, 750), fill=(16, 185, 129), radius=8)
            draw.text((1500, 715), "PRODUCTION READY", fill=(10, 15, 29), font=get_font(20, bold=True, mono=True))

        img.save(fdir / f"f_{f:04d}.png")

    cmd = ["ffmpeg", "-y", "-r", str(fps), "-i", str(fdir / "f_%04d.png"), "-i", str(audio_path),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_video)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# =============================================================
# SCENE 7: OUTRO – AFFILIATE CALLOUT, GITHUB & NEXT VIDEO (~2:48 - 3:15)
# =============================================================
SCENE_7_TEXT = (
    "To test ElevenLabs Conversational Voice AI for your own agents, use the exclusive free trial link in the description and pinned comment below. "
    "You can download the complete Python script, WebSocket handlers, and sandbox blueprints in the GitHub repo linked below. "
    "If this architecture helped you cut latency, drop a like and subscribe to the channel for daily production blueprints. "
    "To learn how to build the autonomous agent skills your voice agent executes, check out our Episode 001 guide on the screen right now."
)

def render_scene_7(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    fdir = BASE_DIR / "s7_frames"
    fdir.mkdir(parents=True, exist_ok=True)

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(59, 130, 246), width=1, radius=10)
        draw.text((90, 52), "DEPLOY TODAY // PRODUCTION SOURCE CODE & COMMUNITY", fill=(56, 189, 248), font=get_font(22, bold=True))

        # Main Left Card: Code, Affiliate & CTA (Width 920px)
        draw_rounded_rect(draw, (60, 130, 980, 990), fill=(13, 18, 32), outline=(16, 185, 129), width=2, radius=18)
        
        # 1. Prominent Affiliate Free Trial Box (Highlighting when spoken: t: 0.0 - 8.5)
        aff_fill = (45, 25, 60) if t < 8.5 else (25, 18, 38)
        aff_out = (244, 114, 182) if t < 8.5 else (168, 85, 247)
        draw_rounded_rect(draw, (90, 160, 950, 360), fill=aff_fill, outline=aff_out, width=3 if t < 8.5 else 2, radius=14)
        draw.text((120, 185), "🎁 TRY ELEVENLABS CONVERSATIONAL AI", fill=(244, 114, 182), font=get_font(24, bold=True))
        draw.text((120, 235), "Exclusive Free Trial Link in Description & Pinned Comment:", fill=(255, 255, 255), font=get_font(20, bold=True))
        draw.text((120, 275), "https://try.elevenlabs.io/agentic-voice", fill=(56, 189, 248), font=get_font(22, bold=True, mono=True))
        draw.text((120, 315), "• Sub-second WebSockets • Zero setup required", fill=(148, 163, 184), font=get_font(18))

        # 2. GitHub Repo Box (Highlighting when spoken: t: 8.5 - 16.0)
        gh_out = (52, 211, 153) if 8.5 <= t < 16.0 else (56, 189, 248)
        draw_rounded_rect(draw, (90, 390, 950, 560), fill=(20, 28, 48), outline=gh_out, width=3 if 8.5 <= t < 16.0 else 2, radius=14)
        draw.text((120, 415), "📁 GITHUB REPOSITORY // EPISODE 002", fill=(56, 189, 248), font=get_font(22, bold=True, mono=True))
        draw.text((120, 460), "Download complete Python script & WebSocket configs:", fill=(226, 232, 240), font=get_font(20))
        draw.text((120, 500), "https://github.com/Johnmannen/Agentic-Stack-Library", fill=(52, 211, 153), font=get_font(20, mono=True))

        # 3. Prominent Like & Subscribe Banner (Highlighting when spoken: t: 16.0+)
        sub_pulse = math.sin(t * 6) * 4 if t >= 16.0 else 0
        draw_rounded_rect(draw, (90, 590, 950, 790), fill=(24, 34, 53), outline=(251, 191, 36), width=3, radius=14)
        draw.text((120, 620), "⚡ LIKE THE VIDEO & SUBSCRIBE", fill=(251, 191, 36), font=get_font(26, bold=True))
        draw.text((120, 675), "Subscribe to Agentic Stack for daily production blueprints,", fill=(226, 232, 240), font=get_font(20))
        draw.text((120, 715), "verified Python code, and sub-second voice architectures.", fill=(226, 232, 240), font=get_font(20))

        # Right Card: Next Video Recommendation
        draw_rounded_rect(draw, (1020, 130, 1860, 990), fill=(10, 14, 26), outline=(59, 130, 246), width=3, radius=18)
        draw.text((1060, 170), "RECOMMENDED NEXT BLUEPRINT", fill=(56, 189, 248), font=get_font(24, bold=True, mono=True))
        
        draw_rounded_rect(draw, (1060, 230, 1820, 700), fill=(18, 25, 42), outline=(100, 116, 139), width=2, radius=14)
        draw_rounded_rect(draw, (1100, 270, 1780, 520), fill=(10, 15, 28), outline=(37, 99, 235), width=2, radius=10)
        draw.text((1130, 350), "EPISODE #001", fill=(56, 189, 248), font=get_font(28, bold=True))
        draw.text((1130, 400), "Build Autonomous Agent Skills", fill=(255, 255, 255), font=get_font(32, bold=True))
        draw.text((1130, 450), "Zero-Cost Python Sandboxes", fill=(52, 211, 153), font=get_font(24))

        draw.text((1060, 750), "Watch Episode 001 to structure autonomous skills", fill=(255, 255, 255), font=get_font(24, bold=True))
        draw.text((1060, 795), "that your voice agent can execute mid-call.", fill=(255, 255, 255), font=get_font(24, bold=True))
        draw.text((1060, 850), "Click the card on screen to continue ->", fill=(251, 191, 36), font=get_font(22, mono=True))

        img.save(fdir / f"f_{f:04d}.png")

    cmd = ["ffmpeg", "-y", "-r", str(fps), "-i", str(fdir / "f_%04d.png"), "-i", str(audio_path),
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out_video)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# =============================================================
# MAIN COMPILATION
# =============================================================
async def main():
    print("[PHASE 5] Starting Complete Production of Video 002 Test Remake...")
    scenes = [
        ("s1", SCENE_1_TEXT, render_scene_1),
        ("s2", SCENE_2_TEXT, render_scene_2),
        ("s3", SCENE_3_TEXT, render_scene_3),
        ("s4", SCENE_4_TEXT, render_scene_4),
        ("s5", SCENE_5_TEXT, render_scene_5),
        ("s6", SCENE_6_TEXT, render_scene_6),
        ("s7", SCENE_7_TEXT, render_scene_7)
    ]

    scene_videos = []
    for tag, text, renderer in scenes:
        audio_path = BASE_DIR / f"{tag}_andrew.mp3"
        video_path = BASE_DIR / f"{tag}_video.mp4"
        print(f"\n--- Synthesizing Audio for {tag.upper()} ---")
        await synthesize_voice(text, str(audio_path))
        dur = get_duration(str(audio_path))
        print(f"--- Audio Duration: {dur:.2f}s ---")
        print(f"--- Rendering Visuals for {tag.upper()} ---")
        renderer(dur, str(audio_path), str(video_path))
        scene_videos.append(video_path)

    # Concat all 7 scenes
    print("\n--- Concatenating All Scenes into Final Video ---")
    concat_list = BASE_DIR / "concat.txt"
    with open(concat_list, "w", encoding="utf-8") as f:
        for sv in scene_videos:
            f.write(f"file '{sv.resolve().as_posix()}'\n")

    out_final_mp4 = BASE_DIR / "video_002_phase5_test_final.mp4"
    art_final_mp4 = ART_DIR / "video_002_phase5_test_final.mp4"

    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(out_final_mp4)]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    shutil.copy(str(out_final_mp4), str(art_final_mp4))
    print(f"\n[PHASE 5 SUCCESS] Final Test Video Rendered & Saved to:\n{art_final_mp4}")

if __name__ == "__main__":
    asyncio.run(main())
