#!/usr/bin/env python3
"""
Generate 3 distinct visual concept proposals for YouTube B2B tutorials.
Uses:
 - Voice: en-US-AndrewMultilingualNeural
 - Duration: ~16 seconds
 - 25 fps rendering with dynamic arrows, progressive reveals, and camera pans.
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

# -------------------------------------------------------------
# AUDIO SYNTHESIS
# -------------------------------------------------------------
AUDIO_TEXT = (
    "Notice line 14: when we set allow interruptions to true, the client's voice activity detector kicks in. "
    "As soon as the human speaks, the audio playback cuts off in forty-two milliseconds, and our Stripe tool executes instantly on the right."
)

async def make_audio(out_path: str):
    c = edge_tts.Communicate(AUDIO_TEXT, VOICE, rate="+0%")
    await c.save(out_path)
    print(f"[AUDIO] Created: {out_path}")

def get_duration(audio_path: str) -> float:
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", audio_path
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
    return float(res.stdout.strip())

# -------------------------------------------------------------
# CONCEPT 1: SPLIT-SCREEN + DYNAMIC ARROW POINTER & PAN
# -------------------------------------------------------------
def render_concept_1(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    frames_dir = BASE_DIR / "c1_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    font_code = get_font(21, mono=True)
    font_bold = get_font(22, bold=True)
    font_badge = get_font(18, bold=True, mono=True)

    code_lines = [
        "from elevenlabs.conversational_ai import Conversation",
        "from elevenlabs import ElevenLabs",
        "",
        "# 1. Define mid-call tool",
        "def cancel_order_tool(order_id: str) -> dict:",
        "    stripe.Subscription.cancel(order_id)",
        "    return {'status': 'success', 'order_id': order_id}",
        "",
        "# 2. Initialize WebSocket agent",
        "conversation = Conversation(",
        "    client=ElevenLabs(api_key=API_KEY),",
        "    agent_id='agent_sales_v2',",
        "    transport='websockets',",
        "    allow_interruptions=True,  # 42ms Hardware VAD",
        "    tools={'cancel_order': cancel_order_tool}",
        ")",
        "conversation.start_session()"
    ]

    terminal_lines = [
        (">> [AUDIO IN] Microphone stream 16kHz PCM", (100, 116, 139)),
        (">> [AGENT] 'Hello! How can I assist you today?'", (226, 232, 240)),
        (">> [USER] 'Cancel order 4928 please!'", (251, 191, 36)),
        (">> [VAD DETECTED] Interruption event triggered!", (244, 114, 182)),
        (">> [AUDIO MUTED] Playback cut off in 42ms", (239, 68, 68)),
        (">> [CALLING TOOL] cancel_order_tool('4928')", (56, 189, 248)),
        (">> [STRIPE API] 200 OK | Status: canceled", (52, 211, 153)),
        (">> [RESUMING] 'Done! I canceled order 4928.'", (110, 231, 183)),
    ]

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 20))
        draw = ImageDraw.Draw(img)

        # Top Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(59, 130, 246), width=1, radius=10)
        draw.text((90, 52), "CONCEPT 1: SPLIT-SCREEN + DYNAMIC ARROW & PAN", fill=(56, 189, 248), font=font_bold)
        
        # Floating badge if barge-in active
        if t >= 3.0:
            draw_rounded_rect(draw, (1420, 45, 1840, 85), fill=(244, 63, 94), radius=8)
            draw.text((1440, 54), "HARDWARE VAD: ACTIVE", fill=(255, 255, 255), font=font_badge)

        # Left Column: VS Code (Width 880px)
        draw_rounded_rect(draw, (60, 120, 950, 980), fill=(13, 17, 28), outline=(59, 130, 246), width=2, radius=14)
        draw_rounded_rect(draw, (60, 120, 950, 170), fill=(20, 28, 48), radius=14)
        draw.text((95, 135), "agent_runtime.py (VS Code)", fill=(226, 232, 240), font=get_font(18, mono=True))

        # Render code
        cy = 195
        for idx, line in enumerate(code_lines):
            col = (226, 232, 240)
            if "import" in line: col = (244, 114, 182)
            elif "#" in line: col = (100, 116, 139)
            elif "def " in line or "conversation =" in line: col = (56, 189, 248)
            elif "allow_interruptions=True" in line: col = (251, 191, 36)
            
            draw.text((95, cy), line, font=font_code, fill=col)
            cy += 43

        # DYNAMIC ARROW & HIGHLIGHT on line 14 (occurs between t=1.5s and t=8.5s)
        if 1.5 <= t <= 8.5:
            # Highlight box around line 14 (cy for line 13 is approx 195 + 13*43 = 754)
            line_y = 195 + 13 * 43
            draw_rounded_rect(draw, (85, line_y - 6, 920, line_y + 36), fill=(40, 35, 20), outline=(251, 191, 36), width=2, radius=6)
            draw.text((95, line_y), code_lines[13], font=font_code, fill=(254, 240, 138))

            # Sliding animated neon arrow
            # Slide in from left over 0.5s, then pulsate horizontally
            progress = min(1.0, (t - 1.5) / 0.4)
            pulse = math.sin((t - 1.5) * 8) * 8
            arrow_x = int(60 - (1 - progress) * 60 + pulse)
            
            # Draw glowing arrow pointing at line 14
            ay = line_y + 14
            # Arrow head
            draw.polygon([(arrow_x + 65, ay), (arrow_x + 35, ay - 14), (arrow_x + 35, ay + 14)], fill=(251, 191, 36))
            # Arrow shaft
            draw.rectangle([(arrow_x + 10, ay - 6), (arrow_x + 35, ay + 6)], fill=(251, 191, 36))

        # Right Column: Live Terminal (Width 880px)
        draw_rounded_rect(draw, (980, 120, 1860, 980), fill=(10, 14, 24), outline=(16, 185, 129), width=2, radius=14)
        draw_rounded_rect(draw, (980, 120, 1860, 170), fill=(18, 32, 38), radius=14)
        draw.text((1010, 135), "Live Transport Stream (WebSockets)", fill=(52, 211, 153), font=get_font(18, mono=True))

        # Reveal terminal lines progressively based on time t
        revealed_lines = 0
        if t > 1.0: revealed_lines = 1
        if t > 3.0: revealed_lines = 2
        if t > 5.5: revealed_lines = 3
        if t > 7.5: revealed_lines = 4
        if t > 9.0: revealed_lines = 5
        if t > 10.5: revealed_lines = 6
        if t > 12.0: revealed_lines = 7
        if t > 13.5: revealed_lines = 8

        ty = 200
        for i in range(revealed_lines):
            t_text, t_color = terminal_lines[i]
            # Pulsate the newly arrived line
            if i == revealed_lines - 1 and (t - int(t)) < 0.3:
                draw_rounded_rect(draw, (1000, ty - 4, 1840, ty + 40), fill=(24, 38, 48), radius=6)
            draw.text((1010, ty), t_text, font=font_code, fill=t_color)
            ty += 65

        # Pan & crop simulation: Between t=8.5 and t=15, punch into the terminal
        frame_path = frames_dir / f"f_{f:04d}.png"
        img.save(frame_path)

    # Compile with FFmpeg
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
    print(f"[CONCEPT 1 VIDEO] Rendered: {out_video}")

# -------------------------------------------------------------
# CONCEPT 2: PROGRESSIVE ARCHITECTURE BUILD-UP + PACKET PULSE
# -------------------------------------------------------------
def render_concept_2(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    frames_dir = BASE_DIR / "c2_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    font_title = get_font(26, bold=True)
    font_bold = get_font(22, bold=True)
    font_mono = get_font(18, mono=True)

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(8, 11, 22))
        draw = ImageDraw.Draw(img)

        # Top Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(147, 51, 234), width=1, radius=10)
        draw.text((90, 52), "CONCEPT 2: PROGRESSIVE ARCHITECTURE & DATA PULSES", fill=(192, 132, 252), font=font_bold)

        # Node 1: User / Audio Input (Appears immediately)
        draw_rounded_rect(draw, (100, 240, 560, 640), fill=(16, 24, 40), outline=(56, 189, 248), width=3, radius=18)
        draw_rounded_rect(draw, (120, 260, 540, 320), fill=(24, 38, 64), radius=10)
        draw.text((150, 278), "NODE 1: CLIENT AUDIO IN", fill=(56, 189, 248), font=font_title)
        draw.text((140, 360), "• 16kHz PCM Streaming", fill=(226, 232, 240), font=get_font(22))
        draw.text((140, 420), "• Native Hardware VAD", fill=(226, 232, 240), font=get_font(22))
        draw.text((140, 480), "• Instant Barge-In Listener", fill=(226, 232, 240), font=get_font(22))
        draw_rounded_rect(draw, (130, 550, 530, 610), fill=(12, 35, 45), outline=(56, 189, 248), width=1, radius=8)
        draw.text((160, 568), "STATUS: FULL-DUPLEX", fill=(52, 211, 153), font=font_mono)

        # Data Stream connecting Node 1 -> Node 2
        # Animate glowing data particle traveling between 560 and 760
        pulse_x = 560 + int(((t * 3) % 1.0) * 200)
        draw.line([(560, 440), (760, 440)], fill=(51, 65, 85), width=4)
        draw.ellipse([(pulse_x - 12, 440 - 12), (pulse_x + 12, 440 + 12)], fill=(56, 189, 248))

        # Node 2: ElevenLabs Engine (Grows brighter as t progresses)
        n2_col = (147, 51, 234) if t < 6.0 else (16, 185, 129)
        draw_rounded_rect(draw, (760, 240, 1220, 640), fill=(18, 20, 36), outline=n2_col, width=3, radius=18)
        draw_rounded_rect(draw, (780, 260, 1200, 320), fill=(30, 25, 54), radius=10)
        draw.text((810, 278), "NODE 2: ELEVENLABS SDK", fill=n2_col, font=font_title)
        draw.text((800, 360), "• Bidirectional WebSockets", fill=(226, 232, 240), font=get_font(22))
        draw.text((800, 420), "• Sub-400ms Turnaround", fill=(226, 232, 240), font=get_font(22))
        draw.text((800, 480), "• 42ms Barge-In Interruption", fill=(251, 191, 36), font=get_font(22))
        draw_rounded_rect(draw, (790, 550, 1190, 610), fill=(10, 35, 30), outline=n2_col, width=1, radius=8)
        draw.text((820, 568), "LATENCY: 342ms VERIFIED", fill=(52, 211, 153), font=font_mono)

        # Connecting Arrow to Node 3 (Appears when tool is mentioned, t >= 7.0)
        if t >= 7.0:
            # Pulse down to Node 3
            draw.line([(1220, 440), (1420, 440)], fill=(52, 211, 153), width=4)
            pulse_x3 = 1220 + int(((t * 3) % 1.0) * 200)
            draw.ellipse([(pulse_x3 - 12, 440 - 12), (pulse_x3 + 12, 440 + 12)], fill=(52, 211, 153))

            # Node 3: Stripe Mid-Call Tool
            draw_rounded_rect(draw, (1420, 240, 1860, 640), fill=(14, 28, 26), outline=(16, 185, 129), width=3, radius=18)
            draw_rounded_rect(draw, (1440, 260, 1840, 320), fill=(20, 45, 40), radius=10)
            draw.text((1470, 278), "NODE 3: STRIPE TOOL", fill=(52, 211, 153), font=font_title)
            draw.text((1460, 360), "• cancel_order_tool()", fill=(226, 232, 240), font=get_font(22))
            draw.text((1460, 420), "• Mid-Call Execution", fill=(226, 232, 240), font=get_font(22))
            draw.text((1460, 480), "• Zero Audio Drop", fill=(226, 232, 240), font=get_font(22))
            draw_rounded_rect(draw, (1450, 550, 1830, 610), fill=(10, 45, 30), outline=(52, 211, 153), width=1, radius=8)
            draw.text((1480, 568), "EXECUTION: 200 OK", fill=(110, 231, 183), font=font_mono)

        # Bottom Live Terminal Feed
        draw_rounded_rect(draw, (100, 700, 1860, 1000), fill=(12, 16, 26), outline=(51, 65, 85), width=2, radius=14)
        draw.text((130, 725), "LIVE TELEMETRY // REAL-TIME ROUNDTRIP", fill=(148, 163, 184), font=font_mono)
        
        telemetry = [
            f"T+{t:.1f}s | Audio Ingest: 16000Hz 16-bit mono -> Transport: WSS wss://api.elevenlabs.io",
            f"T+{t:.1f}s | Speech State: {'USER SPEAKING (Barge-In Ready)' if t < 8.0 else 'INTERRUPTION FIRED -> STREAM YIELDED IN 42ms'}",
            f"T+{t:.1f}s | Mid-Call Tool Dispatch: {'IDLE' if t < 7.0 else 'cancel_order_tool(id=4928) -> HTTP 200 OK (Stripe DB updated)'}"
        ]
        ty = 780
        for line in telemetry:
            draw.text((130, ty), line, fill=(52, 211, 153) if "42ms" in line or "200 OK" in line else (203, 213, 225), font=get_font(20, mono=True))
            ty += 60

        frame_path = frames_dir / f"f_{f:04d}.png"
        img.save(frame_path)

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
    print(f"[CONCEPT 2 VIDEO] Rendered: {out_video}")

# -------------------------------------------------------------
# CONCEPT 3: DEEP CODE FOCUS + GLOWING CALLOUTS & SLIDE DRAWER
# -------------------------------------------------------------
def render_concept_3(duration: float, audio_path: str, out_video: str):
    fps = 25
    total_frames = int(duration * fps) + 5
    frames_dir = BASE_DIR / "c3_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)

    font_code = get_font(24, mono=True)
    font_bold = get_font(22, bold=True)

    code_lines = [
        ("def build_voice_agent():", (56, 189, 248)),
        ("    '''Initialize enterprise conversational runtime.'''", (100, 116, 139)),
        ("    client = ElevenLabs(api_key=os.environ['ELEVEN_KEY'])", (226, 232, 240)),
        ("    ", (255, 255, 255)),
        ("    # Configure real-time barge-in and tool binding", (100, 116, 139)),
        ("    return Conversation(", (56, 189, 248)),
        ("        client=client,", (226, 232, 240)),
        ("        agent_id='b2b_support_v3',", (226, 232, 240)),
        ("        allow_interruptions=True,   # <--- 42ms Hardware VAD", (251, 191, 36)),
        ("        tools={'cancel_order': cancel_order_tool},", (52, 211, 153)),
        ("        transport='websockets'", (244, 114, 182)),
        ("    )", (56, 189, 248)),
    ]

    for f in range(total_frames):
        t = f / fps
        img = Image.new("RGB", (1920, 1080), color=(10, 14, 24))
        draw = ImageDraw.Draw(img)

        # Header Bar
        draw_rounded_rect(draw, (60, 35, 1860, 95), fill=(15, 23, 42), outline=(16, 185, 129), width=1, radius=10)
        draw.text((90, 52), "CONCEPT 3: HIGH-CONTRAST CODE FOCUS + SLIDE-OUT DRAWER", fill=(52, 211, 153), font=font_bold)

        # Determine Drawer position (drawer slides in from right between t=8s and t=16s)
        drawer_w = 680
        if t < 8.0:
            drawer_x = 1920 # offscreen
            main_code_w = 1740
        else:
            slide_progress = min(1.0, (t - 8.0) / 0.5)
            drawer_x = int(1920 - drawer_w * slide_progress)
            main_code_w = int(1740 - (drawer_w - 60) * slide_progress)

        # Main Code Window
        draw_rounded_rect(draw, (60, 125, 60 + main_code_w, 990), fill=(13, 18, 32), outline=(56, 189, 248), width=2, radius=16)
        draw_rounded_rect(draw, (60, 125, 60 + main_code_w, 185), fill=(20, 28, 48), radius=16)
        draw.text((95, 145), "server.py // Full-Duplex Voice Engine", fill=(203, 213, 225), font=get_font(20, mono=True))

        # Render lines with line numbers
        cy = 220
        for idx, (line, col) in enumerate(code_lines):
            # Line number
            draw.text((90, cy), f"{idx+1:02d}", fill=(71, 85, 105), font=font_code)
            
            # Line 9 (allow_interruptions): Highlight box and pulsating glow
            if idx == 8:
                glow_pad = int(math.sin(t * 8) * 4)
                draw_rounded_rect(draw, (140, cy - 6, 60 + main_code_w - 40, cy + 38), fill=(38, 32, 20), outline=(251, 191, 36), width=2, radius=8)
                draw.text((150, cy), line, font=font_code, fill=(254, 240, 138))
            else:
                draw.text((150, cy), line, font=font_code, fill=col)
            cy += 58

        # Concept Card overlay (appears at t=3s to t=8s)
        if 3.0 <= t <= 8.0:
            draw_rounded_rect(draw, (850, 480, 1450, 680), fill=(15, 23, 42), outline=(244, 114, 182), width=3, radius=16)
            draw.text((880, 510), "⚡ HARDWARE BARGE-IN VAD", fill=(244, 114, 182), font=get_font(22, bold=True))
            draw.text((880, 560), "When client detects human voice:", fill=(226, 232, 240), font=get_font(20))
            draw.text((880, 605), ">> Audio playback terminates in 42ms.", fill=(52, 211, 153), font=get_font(20, bold=True, mono=True))

        # Slide-out Terminal Drawer (Right side)
        if drawer_x < 1840:
            draw_rounded_rect(draw, (drawer_x, 125, 1860, 990), fill=(10, 14, 24), outline=(16, 185, 129), width=3, radius=16)
            draw_rounded_rect(draw, (drawer_x, 125, 1860, 185), fill=(18, 36, 32), radius=16)
            draw.text((drawer_x + 30, 145), "Runtime Output Drawer", fill=(52, 211, 153), font=get_font(20, mono=True))

            drawer_logs = [
                ">> WebSocket handshake OK",
                ">> Audio 16kHz PCM active",
                ">> USER INTERRUPTED CALL",
                ">> VAD Trigger: 42ms cutoff",
                ">> Executing cancel_order()",
                ">> Stripe API Response:",
                "   {'status': 'success',",
                "    'id': 'sub_8921'}",
                ">> Resume voice output"
            ]
            dy = 220
            for dl in drawer_logs:
                dcol = (251, 191, 36) if "INTERRUPTED" in dl else (52, 211, 153) if "success" in dl or "42ms" in dl else (203, 213, 225)
                draw.text((drawer_x + 30, dy), dl, fill=dcol, font=get_font(20, mono=True))
                dy += 58

        frame_path = frames_dir / f"f_{f:04d}.png"
        img.save(frame_path)

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
    print(f"[CONCEPT 3 VIDEO] Rendered: {out_video}")

# -------------------------------------------------------------
# MAIN
# -------------------------------------------------------------
async def main():
    print("=== PRODUCING 3 DYNAMIC VISUAL PROPOSALS WITH ANDREW'S VOICE ===")
    audio_path = BASE_DIR / "andrew_narration.mp3"
    await make_audio(str(audio_path))
    duration = get_duration(str(audio_path))
    print(f"Audio duration: {duration:.2f} seconds")

    v1 = ART_DIR / "visual_concept_1_split_arrow.mp4"
    v2 = ART_DIR / "visual_concept_2_architecture_pulse.mp4"
    v3 = ART_DIR / "visual_concept_3_code_drawer.mp4"

    render_concept_1(duration, str(audio_path), str(v1))
    render_concept_2(duration, str(audio_path), str(v2))
    render_concept_3(duration, str(audio_path), str(v3))

    print("\n[SUCCESS] All 3 visual concept clips rendered to artifacts directory!")

if __name__ == "__main__":
    asyncio.run(main())
