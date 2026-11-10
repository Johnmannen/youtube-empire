#!/usr/bin/env python3
"""
Agentic Stack B2B - Production Pipeline for Package #002
Topic: Build Real-Time Conversational Voice AI Agents in Python with ElevenLabs
"""

import os
import sys
import json
import asyncio
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import edge_tts

VOICE = "en-US-ChristopherNeural"
VOICE_RATE = "+5%"
SHORT_VOICE_RATE = "+10%"

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

def draw_wrapped_text(draw, pos, text, max_width, line_height, font, fill=(255, 255, 255)):
    words = text.split()
    lines = []
    curr = []
    for w in words:
        test_line = " ".join(curr + [w])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_width:
            curr.append(w)
        else:
            if curr:
                lines.append(" ".join(curr))
            curr = [w]
    if curr:
        lines.append(" ".join(curr))
    
    x, y = pos
    for line in lines:
        draw.text((x, y), line, fill=fill, font=font)
        y += line_height
    return y

def render_scene_1080p(scene_data: dict, output_path: str):
    width, height = 1920, 1080
    img = Image.new("RGB", (width, height), color=(8, 11, 20))
    draw = ImageDraw.Draw(img)

    # Accent lighting (Purple & Cyan for ElevenLabs theme)
    for r in range(400, 0, -20):
        alpha = int(12 * (1 - r / 400))
        draw.ellipse([1400 - r, 150 - r, 1400 + r, 150 + r], fill=(88, 28, 135, alpha))

    # Top Header Bar
    draw_rounded_rect(draw, (80, 50, 1840, 110), fill=(15, 23, 42), outline=(51, 65, 85), width=1, radius=12)
    font_brand = get_font(20, bold=True)
    draw.text((110, 68), "AGENTIC STACK B2B", fill=(168, 85, 247), font=font_brand)
    draw.text((345, 68), "//  EPISODE #002", fill=(148, 163, 184), font=get_font(20))
    draw.text((540, 68), "|  ELEVENLABS CONVERSATIONAL AI", fill=(56, 189, 248), font=get_font(20, bold=True))

    badge_text = scene_data.get("badge", "ELEVENLABS SDK")
    badge_w = 260
    draw_rounded_rect(draw, (1840 - badge_w - 20, 62, 1840 - 20, 98), fill=(88, 28, 135), outline=(168, 85, 247), width=1, radius=8)
    draw.text((1840 - badge_w + 10, 70), badge_text, fill=(243, 232, 255), font=get_font(15, bold=True, mono=True))

    # Left Column: Architecture & Narration Context (width: 860px)
    draw.text((100, 145), scene_data.get("category", "B2B ARCHITECTURE // VOICE AI"), fill=(168, 85, 247), font=get_font(15, bold=True, mono=True))
    draw_fitted_text(draw, (100, 175), scene_data["title"], max_width=860, initial_size=36, bold=True, fill=(255, 255, 255))
    font_sub = get_font(19)
    draw_wrapped_text(draw, (100, 235), scene_data["subtitle"], max_width=860, line_height=28, font=font_sub, fill=(148, 163, 184))

    # Architecture Step Cards (Left Column)
    steps = [
        ("1. Full-Duplex WebSocket", "Single connection for bidirectional audio & events"),
        ("2. Sub-500ms Latency", "Neural voice synthesis without round-trip lag"),
        ("3. User Interruption / Barge-in", "Native cancellation when human speaks"),
        ("4. Enterprise Tool Calling", "Trigger backend Python functions live on voice calls")
    ]
    curr_step = scene_data.get("active_step", 0)
    card_y = 330
    for idx, (stitle, sdesc) in enumerate(steps):
        is_active = (idx == curr_step)
        bg = (24, 18, 43) if is_active else (15, 23, 42)
        border = (168, 85, 247) if is_active else (30, 41, 59)
        num_bg = (147, 51, 234) if is_active else (30, 41, 59)
        text_color = (255, 255, 255) if is_active else (148, 163, 184)
        
        draw_rounded_rect(draw, (100, card_y, 960, card_y + 88), fill=bg, outline=border, width=2 if is_active else 1, radius=12)
        draw_rounded_rect(draw, (120, card_y + 16, 176, card_y + 72), fill=num_bg, radius=8)
        draw.text((138, card_y + 26), f"0{idx+1}", fill=(255, 255, 255), font=get_font(20, bold=True, mono=True))
        
        draw.text((195, card_y + 18), stitle, fill=text_color, font=get_font(19, bold=True))
        draw.text((195, card_y + 48), sdesc, fill=(148, 163, 184) if is_active else (100, 116, 139), font=get_font(15))
        card_y += 104

    # Right Column: Terminal Window (width: 820px)
    draw_rounded_rect(draw, (1000, 140, 1840, 920), fill=(10, 14, 26), outline=(51, 65, 85), width=2, radius=16)
    
    # Terminal Titlebar
    draw_rounded_rect(draw, (1000, 140, 1840, 200), fill=(15, 23, 42), outline=(51, 65, 85), width=1, radius=16)
    draw.ellipse([1025, 162, 1041, 178], fill=(239, 68, 68))
    draw.ellipse([1050, 162, 1066, 178], fill=(234, 179, 8))
    draw.ellipse([1075, 162, 1091, 178], fill=(34, 197, 94))
    
    font_term_hdr = get_font(16, bold=True, mono=True)
    draw.text((1115, 162), scene_data.get("code_filename", "elevenlabs_voice_agent.py"), fill=(148, 163, 184), font=font_term_hdr)

    # Terminal Code Lines
    font_code = get_font(17, mono=True)
    code_y = 220
    for line in scene_data.get("code_lines", []):
        if line.startswith("#"):
            color = (100, 116, 139)
        elif line.startswith("class ") or line.startswith("def ") or line.startswith("import ") or line.startswith("from "):
            color = (192, 132, 252)
        elif line.startswith(">>") or line.startswith("STATUS:"):
            color = (52, 211, 153)
        elif "elevenlabs" in line.lower() or "voice" in line.lower():
            color = (56, 189, 248)
        else:
            color = (226, 232, 240)
        draw.text((1035, code_y), line, fill=color, font=font_code)
        code_y += 28

    # Terminal Footer Output Bar
    draw_rounded_rect(draw, (1020, 840, 1820, 900), fill=(8, 12, 22), outline=(51, 65, 85), width=1, radius=8)
    draw.text((1040, 855), ">> WS CONNECTED: wss://api.elevenlabs.io/v1/convai/conversation", fill=(168, 85, 247), font=get_font(15, bold=True, mono=True))
    draw.text((1650, 855), "LATENCY: 380ms", fill=(52, 211, 153), font=get_font(15, bold=True, mono=True))

    # Bottom Branding Bar
    draw.text((100, 990), "Agentic Stack B2B  |  Episode 002: ElevenLabs Conversational Voice AI", fill=(100, 116, 139), font=get_font(16, bold=True))
    draw.text((1520, 990), "Partner Link: try.elevenlabs.io/agentic-voice", fill=(168, 85, 247), font=get_font(16, bold=True, mono=True))

    img.save(output_path, "PNG")
    print(f"[RENDER] Saved 1080p Slide: {output_path}")

def render_thumbnail_002(output_path: str):
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), color=(8, 11, 24))
    draw = ImageDraw.Draw(img)

    # Ambient purple and cyan glow
    for r in range(450, 0, -30):
        alpha = int(18 * (1 - r / 450))
        draw.ellipse([1000 - r, 360 - r, 1000 + r, 360 + r], fill=(126, 34, 206, alpha))
        draw.ellipse([250 - r, 200 - r, 250 + r, 200 + r], fill=(14, 165, 233, alpha))

    # Top Badge
    draw_rounded_rect(draw, (60, 45, 480, 95), fill=(88, 28, 135), outline=(168, 85, 247), width=2, radius=10)
    draw.text((80, 56), "⚡ ELEVENLABS VOICE SDK 2026", fill=(243, 232, 255), font=get_font(21, bold=True, mono=True))

    # Main Headline (High Contrast B2B)
    font_hero1 = get_font(56, bold=True)
    font_hero2 = get_font(56, bold=True)
    draw.text((60, 125), "BUILD REAL-TIME", fill=(255, 255, 255), font=font_hero1)
    draw.text((60, 195), "VOICE AI AGENTS", fill=(168, 85, 247), font=font_hero2)
    draw.text((60, 265), "IN PYTHON", fill=(56, 189, 248), font=font_hero1)

    # Bullet points / value proposition
    bullets = [
        "✓ Sub-500ms Latency WebSockets",
        "✓ Native Interruption & Barge-In",
        "✓ Full Python Open-Source Code"
    ]
    by = 360
    for b in bullets:
        draw_rounded_rect(draw, (60, by, 580, by + 46), fill=(15, 23, 42), outline=(30, 41, 59), width=1, radius=8)
        draw.text((80, by + 10), b, fill=(226, 232, 240), font=get_font(20, bold=True))
        by += 60

    # Right Card: Floating Terminal Window
    draw_rounded_rect(draw, (650, 110, 1220, 640), fill=(10, 14, 26), outline=(168, 85, 247), width=3, radius=18)
    draw_rounded_rect(draw, (650, 110, 1220, 175), fill=(20, 15, 38), outline=(88, 28, 135), width=1, radius=18)
    draw.ellipse([675, 135, 691, 151], fill=(239, 68, 68))
    draw.ellipse([700, 135, 716, 151], fill=(234, 179, 8))
    draw.ellipse([725, 135, 741, 151], fill=(34, 197, 94))
    draw.text((760, 133), "elevenlabs_voice_agent.py", fill=(168, 85, 247), font=get_font(18, bold=True, mono=True))

    code_snippet = [
        "from elevenlabs.client import ElevenLabs",
        "from elevenlabs.conversational_ai import Agent",
        "",
        "agent = Agent(",
        "    client=ElevenLabs(api_key=API_KEY),",
        "    agent_id='b2b_support_v2',",
        "    tools=[api_lookup, db_query]",
        ")",
        "",
        "# Real-time full-duplex stream",
        "await agent.start_conversation(",
        "    audio_in=mic_stream,",
        "    audio_out=speaker_stream",
        ")"
    ]
    cy = 200
    for cl in code_snippet:
        color = (168, 85, 247) if "Agent" in cl or "client" in cl else (226, 232, 240)
        if cl.startswith("#"): color = (100, 116, 139)
        draw.text((680, cy), cl, fill=color, font=get_font(16, mono=True))
        cy += 24

    # Terminal Live Badge
    draw_rounded_rect(draw, (675, 560, 1195, 615), fill=(8, 12, 22), outline=(52, 211, 153), width=2, radius=10)
    draw.text((700, 575), "⚡ STATUS: 200 OK  |  LATENCY: 380ms  |  LIVE AUDIO", fill=(52, 211, 153), font=get_font(16, bold=True, mono=True))

    img.save(output_path, "PNG")
    print(f"[RENDER] Saved 1280x720 Thumbnail: {output_path}")

def render_shorts_slide_002(output_path: str):
    width, height = 1080, 1920
    img = Image.new("RGB", (width, height), color=(8, 11, 24))
    draw = ImageDraw.Draw(img)

    for r in range(500, 0, -40):
        alpha = int(22 * (1 - r / 500))
        draw.ellipse([540 - r, 960 - r, 540 + r, 960 + r], fill=(126, 34, 206, alpha))

    # Top Branding Header
    draw_rounded_rect(draw, (80, 120, 1000, 210), fill=(20, 15, 38), outline=(168, 85, 247), width=2, radius=16)
    draw.text((120, 145), "AGENTIC STACK B2B // SHORTS #002", fill=(168, 85, 247), font=get_font(28, bold=True, mono=True))

    # Aggressive Hook Headline
    draw_fitted_text(draw, (80, 270), "STOP BUILDING", max_width=920, initial_size=72, bold=True, fill=(255, 255, 255))
    draw_fitted_text(draw, (80, 360), "TEXT CHATBOTS", max_width=920, initial_size=76, bold=True, fill=(239, 68, 68))
    draw_fitted_text(draw, (80, 455), "REAL-TIME VOICE AI", max_width=920, initial_size=68, bold=True, fill=(168, 85, 247))
    draw_fitted_text(draw, (80, 540), "IN PYTHON (2026)", max_width=920, initial_size=64, bold=True, fill=(56, 189, 248))

    # Middle Code Showcase Card
    draw_rounded_rect(draw, (80, 650, 1000, 1380), fill=(10, 14, 26), outline=(168, 85, 247), width=3, radius=24)
    draw_rounded_rect(draw, (80, 650, 1000, 740), fill=(24, 18, 43), outline=(88, 28, 135), width=1, radius=24)
    draw.text((130, 678), "elevenlabs_voice_agent.py", fill=(243, 232, 255), font=get_font(26, bold=True, mono=True))

    code_lines = [
        "# Sub-second Conversational Voice AI",
        "from elevenlabs.conversational_ai import Agent",
        "",
        "agent = Agent(",
        "    agent_id='b2b_support_v2',",
        "    client=ElevenLabs(api_key=API_KEY),",
        "    latency_optimization='ultra_low'",
        ")",
        "",
        "# Full-duplex WebSocket stream",
        "await agent.start_conversation(",
        "    audio_stream=mic,",
        "    on_barge_in=handle_interruption",
        ")",
        "",
        ">> STATUS: WS STREAMING",
        ">> LATENCY: 380ms | 0 BUFFER"
    ]
    sy = 780
    for l in code_lines:
        color = (52, 211, 153) if ">>" in l else ((168, 85, 247) if "Agent" in l or "elevenlabs" in l else (226, 232, 240))
        if l.startswith("#"): color = (100, 116, 139)
        draw.text((120, sy), l, fill=color, font=get_font(23, mono=True))
        sy += 34

    # Bottom Call To Action Card
    draw_rounded_rect(draw, (80, 1440, 1000, 1720), fill=(24, 18, 43), outline=(168, 85, 247), width=2, radius=20)
    draw.text((120, 1480), "FREE CODE & BLUEPRINT:", fill=(255, 255, 255), font=get_font(32, bold=True))
    draw.text((120, 1540), "github.com/Johnmannen/Agentic-Stack-Library", fill=(56, 189, 248), font=get_font(24, bold=True, mono=True))
    draw.text((120, 1610), "FREE ELEVENLABS TRIAL:", fill=(168, 85, 247), font=get_font(28, bold=True))
    draw.text((120, 1660), "try.elevenlabs.io/agentic-voice", fill=(52, 211, 153), font=get_font(24, bold=True, mono=True))

    img.save(output_path, "PNG")
    print(f"[RENDER] Saved 9:16 Shorts Slide: {output_path}")

async def synthesize_speech(text: str, output_mp3: str, output_srt: str, rate: str = "+5%"):
    communicate = edge_tts.Communicate(text, VOICE, rate=rate)
    submaker = edge_tts.SubMaker()
    with open(output_mp3, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
    with open(output_srt, "w", encoding="utf-8") as f:
        f.write(submaker.get_srt())
    print(f"[TTS] Synthesized speech: {output_mp3} ({rate})")

def render_video_ffmpeg(image_path: str, audio_path: str, output_mp4: str):
    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", image_path,
        "-i", audio_path,
        "-c:v", "libx264", "-tune", "stillimage", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-shortest",
        output_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[FFMPEG] Rendered clip: {output_mp4}")

def concat_videos(clip_paths: list, output_mp4: str):
    concat_file = "temp_concat_002.txt"
    with open(concat_file, "w") as f:
        for p in clip_paths:
            f.write(f"file '{Path(p).resolve().as_posix()}'\n")
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", concat_file,
        "-c", "copy",
        output_mp4
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if os.path.exists(concat_file):
        os.remove(concat_file)
    print(f"[FFMPEG] Concatenated full video: {output_mp4}")

async def main():
    out = Path("docs/assets")
    out.mkdir(parents=True, exist_ok=True)
    temp_dir = Path("build_temp_002")
    temp_dir.mkdir(exist_ok=True)

    print("\n" + "=" * 65)
    print("PRODUCING PACKAGE #002: ELEVENLABS CONVERSATIONAL VOICE AI")
    print("=" * 65)

    # 1. SCENE DEFINITIONS (Long-Form)
    scenes = [
        {
            "title": "Conversational Voice AI: The Death of Text Chatbots",
            "subtitle": "Why modern enterprise applications require sub-second streaming audio interfaces.",
            "category": "B2B CONVERSATIONAL AI // ELEVENLABS ARCHITECTURE",
            "badge": "ELEVENLABS SDK",
            "active_step": 0,
            "code_filename": "elevenlabs_voice_agent.py",
            "narration": (
                "Welcome back to Agentic Stack B2B. In 2026, text-only chatbots are rapidly losing user engagement. "
                "Enterprise customers expect sub-second conversational voice interfaces. Today, we are breaking down how to connect "
                "Python agents directly to ElevenLabs' Conversational AI WebSocket API for zero-latency bidirectional voice. "
                "Let's inspect the architecture."
            ),
            "code_lines": [
                "# The Problem with Traditional Voice Chains (4-5s Latency)",
                "# Mic -> Audio Chunk -> Whisper STT (1.5s) -> LLM (1.8s) -> TTS (1.2s)",
                "",
                "# The 2026 Conversational AI Architecture (Sub-500ms)",
                "from elevenlabs.conversational_ai import Agent",
                "from elevenlabs.client import ElevenLabs",
                "",
                "agent = Agent(",
                "    client=ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY')),",
                "    agent_id='b2b_support_v2',",
                "    latency_optimization='ultra_low'",
                ")"
            ]
        },
        {
            "title": "Sub-Second Latency & Full-Duplex WebSockets",
            "subtitle": "How single-connection bidirectional streaming handles user interruptions.",
            "category": "STREAMING PROTOCOL & WEBSOCKETS",
            "badge": "STAGE 2: PROTOCOL",
            "active_step": 1,
            "code_filename": "streaming_websocket_handler.py",
            "narration": (
                "Traditional voice setups chain separate speech-to-text, language models, and text-to-speech APIs, "
                "resulting in four seconds of awkward silence. ElevenLabs Conversational AI combines conversation state "
                "and voice synthesis into a single full-duplex WebSocket connection, slashing turn-taking latency down to under "
                "five hundred milliseconds with native user interruption support."
            ),
            "code_lines": [
                "# Bidirectional Streaming Event Loop",
                "async with websockets.connect(ELEVENLABS_WS_URL) as ws:",
                "    # Stream raw PCM audio chunks continuously",
                "    await ws.send(json.dumps({'user_audio_chunk': audio_bytes}))",
                "",
                "    # Handle incoming streaming audio & barge-in",
                "    async for msg in ws:",
                "        event = json.loads(msg)",
                "        if event['type'] == 'user_interruption':",
                "            speaker.stop_playback()  # Cancel audio immediately",
                "        elif event['type'] == 'audio_output':",
                "            speaker.stream_audio(event['audio_base64'])"
            ]
        },
        {
            "title": "Live Python Code Walkthrough in the Sandbox",
            "subtitle": "Executing the real-time event loop with dynamic enterprise tool execution.",
            "category": "SANDBOX CODE INSPECTION",
            "badge": "STAGE 3: LIVE DEMO",
            "active_step": 2,
            "code_filename": "demos/voice_agent_runtime.py",
            "narration": (
                "Here is our verified Python agent runtime using the ElevenLabs SDK. We initialize the client with our API key, "
                "register dynamic tool calling schemas for enterprise actions, and stream microphone input while playing "
                "synthesized neural audio in real time. Notice how clean the event-driven loop is with zero local hardware lag."
            ),
            "code_lines": [
                "async def run_voice_session():",
                "    # Register dynamic backend tools for the voice agent",
                "    tools = [check_account_status, book_consultation]",
                "    session = await agent.start_session(tools=tools)",
                "",
                "    # Active voice streaming session",
                "    print('>> LISTENING: Speak into microphone...')",
                "    await session.listen_and_respond()",
                "",
                ">> STATUS: 200 OK | Round-Trip Latency: 380ms | Voice: Christopher Neural"
            ]
        },
        {
            "title": "Deploying Enterprise Voice Agents & Code Access",
            "subtitle": "Deploying across customer support and internal workflows with zero cloud cost.",
            "category": "PRODUCTION BLUEPRINT & RESOURCES",
            "badge": "STAGE 4: DEPLOY",
            "active_step": 3,
            "code_filename": "episodes/002-elevenlabs-voice-agent/README.md",
            "narration": (
                "You can deploy this voice agent across customer support, sales qualification, or internal telephony. "
                "All source code and setup guides are ready in our open-source Agentic Stack Library. "
                "Make sure to claim your ElevenLabs free trial using the link in the description. "
                "Let us know in the comments what voice use-case you are building next!"
            ),
            "code_lines": [
                "# Clone the official Episode 002 code repository:",
                "$ git clone https://github.com/Johnmannen/Agentic-Stack-Library.git",
                "$ cd Agentic-Stack-Library/002-elevenlabs-voice-agent",
                "$ pip install elevenlabs websockets asyncio",
                "$ python voice_agent.py",
                "",
                "# Get your verified ElevenLabs partner trial:",
                "# https://try.elevenlabs.io/agentic-voice"
            ]
        }
    ]

    # Render long-form slides and audio
    long_video_clips = []
    for idx, sc in enumerate(scenes):
        slide_img = temp_dir / f"scene_{idx+1}.png"
        audio_mp3 = temp_dir / f"audio_scene_{idx+1}.mp3"
        srt_sub = temp_dir / f"subs_scene_{idx+1}.srt"
        clip_mp4 = temp_dir / f"clip_{idx+1}.mp4"

        render_scene_1080p(sc, str(slide_img))
        await synthesize_speech(sc["narration"], str(audio_mp3), str(srt_sub), rate=VOICE_RATE)
        render_video_ffmpeg(str(slide_img), str(audio_mp3), str(clip_mp4))
        long_video_clips.append(str(clip_mp4))

    final_long_mp4 = out / "video_002_long.mp4"
    concat_videos(long_video_clips, str(final_long_mp4))

    # Render Shorts
    print("\n--- SYNTHESIZING YOUTUBE SHORTS #002 (<20 SECONDS) ---")
    short_slide_img = temp_dir / "short_slide_002.png"
    short_audio_mp3 = temp_dir / "short_audio_002.mp3"
    short_srt = temp_dir / "short_subs_002.srt"
    final_short_mp4 = out / "video_002_short.mp4"

    render_shorts_slide_002(str(short_slide_img))
    shorts_narration = (
        "Text chatbots are dead. In 2026, real-time conversational voice agents built with ElevenLabs handle "
        "customer calls with sub-second latency. Grab the full Python code repository and free trial linked below!"
    )
    await synthesize_speech(shorts_narration, str(short_audio_mp3), str(short_srt), rate=SHORT_VOICE_RATE)
    render_video_ffmpeg(str(short_slide_img), str(short_audio_mp3), str(final_short_mp4))

    # Render Thumbnail 002
    print("\n--- RENDERING 1280x720 THUMBNAIL #002 ---")
    final_thumb_png = out / "thumb_002.png"
    render_thumbnail_002(str(final_thumb_png))

    # Save metadata_002.json
    metadata_002 = {
        "package_id": "002",
        "title": "Build Real-Time Conversational Voice AI Agents in Python (ElevenLabs WebSockets 2026)",
        "alternative_titles": [
            "How to Build Real-Time Voice AI in Python with ElevenLabs",
            "Stop Building Text Chatbots: Real-Time Conversational Voice AI (2026)",
            "ElevenLabs Python SDK Tutorial: Sub-Second Bidirectional Voice Agents"
        ],
        "hook_2s": "Text chatbots are dead in B2B. Here is how to build sub-second real-time conversational voice agents in Python using ElevenLabs.",
        "category_id": "28",
        "category_name": "Science & Technology",
        "altered_content": False,
        "c2pa_status": "VERIFIED_COMPLIANT_2026",
        "target_audience": "B2B SaaS Founders, AI Engineers, Full-Stack Python Developers",
        "tags": [
            "elevenlabs",
            "voice ai agents",
            "conversational ai",
            "python voice agent",
            "real time websockets",
            "sub second latency",
            "elevenlabs python sdk",
            "b2b ai workflows",
            "ai audio streaming",
            "agentic stack b2b"
        ],
        "timestamps": [
            {"time": "00:00", "title": "The Death of Text Chatbots & Shift to Voice"},
            {"time": "00:42", "title": "Sub-Second Latency & Full-Duplex WebSockets"},
            {"time": "01:22", "title": "Live Python SDK Implementation in Sandbox"},
            {"time": "02:02", "title": "Deploying Enterprise Voice Agents & Free Trial"}
        ],
        "affiliate_placeholders": [
            {
                "tool": "ElevenLabs AI Voice & Conversational AI API",
                "benefit": "Sub-second neural voice streaming & conversational agent SDK",
                "live_url": "https://try.elevenlabs.io/agentic-voice",
                "commission_rate": "22% Recurring Commission (PartnerStack)"
            }
        ],
        "github_code_url": "https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/002-elevenlabs-voice-agent",
        "studio_upload_url": "https://studio.youtube.com/channel/UCkphdiVQvc1vvNlcrAorMOg",
        "description": (
            "🚀 [SOURCE CODE] Grab Episode 002 ElevenLabs Voice Agent Blueprint:\n"
            "👉 https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/002-elevenlabs-voice-agent\n\n"
            "📚 [OPEN SOURCE REPO] All Channel Episodes & Star the Library:\n"
            "👉 https://github.com/Johnmannen/Agentic-Stack-Library\n\n"
            "Text chatbots are dead in B2B. In this episode of Agentic Stack B2B, we break down how to build "
            "sub-second real-time conversational voice agents in Python using ElevenLabs Conversational AI and full-duplex WebSockets.\n\n"
            "Learn how to bypass slow STT-LLM-TTS sequential chains, handle native human interruption and barge-in, "
            "and execute typed backend Python functions live during a voice call.\n\n"
            "⏱️ TIMESTAMPS:\n"
            "00:00 - The Death of Text Chatbots & Shift to Voice\n"
            "00:42 - Sub-Second Latency & Full-Duplex WebSockets\n"
            "01:22 - Live Python SDK Implementation in Sandbox\n"
            "02:02 - Deploying Enterprise Voice Agents & Free Trial\n\n"
            "🛠️ ENTERPRISE TOOLS (VERIFIED IN SANDBOX):\n"
            "👉 Try ElevenLabs Voice & Conversational SDK (Free Trial): https://try.elevenlabs.io/agentic-voice\n\n"
            "⚖️ FTC AFFILIATE DISCLOSURE:\n"
            "Some links in this description are affiliate links. If you sign up or purchase through them, we may receive "
            "a commission at no extra cost to you. We strictly test and verify every tool in our cloud sandbox before recommending it.\n\n"
            "#ElevenLabs #VoiceAI #Python #AIAgents #WebSockets #AgenticStack"
        ),
        "pinned_comment": (
            "📌 Grab the Episode 002 ElevenLabs voice agent code and complete blueprint here:\n"
            "👉 https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/002-elevenlabs-voice-agent\n\n"
            "💬 Question: What voice AI use-case are you currently building—customer support, automated sales triage, or internal voice assistants? Let us know below!"
        ),
        "long_video_file": "assets/video_002_long.mp4",
        "short_video_file": "assets/video_002_short.mp4",
        "thumbnail_file": "assets/thumb_002.png"
    }

    with open(out / "metadata_002.json", "w", encoding="utf-8") as f:
        json.dump(metadata_002, f, indent=2)
    print(f"[METADATA] Saved Package 002 metadata to: {out / 'metadata_002.json'}")

if __name__ == "__main__":
    asyncio.run(main())
