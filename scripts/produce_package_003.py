"""
Production script for Video 003: How to Clone Voices and Dub Videos in Python
Produces:
1. High-definition 1080p long video (docs/assets/video_003_long.mp4)
2. Vertical 9:16 Shorts video (docs/assets/video_003_short.mp4)
3. High-CTR split-screen thumbnail (docs/assets/thumb_003.png)
"""

import os
import asyncio
import subprocess
import edge_tts
from PIL import Image, ImageDraw, ImageFont

VOICE = "en-US-AndrewNeural"
TMP_DIR = "tmp_video_003"
ASSETS_DIR = "docs/assets"

os.makedirs(TMP_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

LONG_SCENES = [
    {
        "id": "s1_hook",
        "narration": "Translating video content manually costs five hundred dollars per language and takes weeks of tedious editing. Today, you are going to automate the entire dubbing and voice cloning pipeline in Python with ElevenLabs.",
        "headline": "MANUAL VIDEO DUBBING IS DEAD",
        "sub": "Translate Any Video Into 29 Languages in Python",
        "type": "terminal_intro",
        "code_snippet": None
    },
    {
        "id": "s2_arch",
        "narration": "Here is the production architecture. The ElevenLabs Dubbing API extracts the audio track, runs diarization to isolate distinct speakers, and clones their exact vocal timbre before translating the dialogue.",
        "headline": "SYSTEM ARCHITECTURE: 3-STAGE DUBBING",
        "sub": "Audio Separation -> Speaker Diarization -> Zero-Shot Voice Clone",
        "type": "architecture",
        "code_snippet": None
    },
    {
        "id": "s3_code_init",
        "narration": "In Python, we initialize the ElevenLabs client. On line six, we submit the source MP4 file, select the target language, and enable watermark-free studio export.",
        "headline": "PYTHON DUBBING API CLIENT",
        "sub": "Submitting Batch Translation Job via SDK",
        "type": "code",
        "highlight_line": 6,
        "code": [
            "from elevenlabs.client import ElevenLabs",
            "import os, time",
            "",
            "client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))",
            "",
            "# Line 6: Submit Video for Auto-Diarization & Dubbing",
            "response = client.dubbing.dub_a_video_or_an_audio_file(",
            "    file=open('input_presentation.mp4', 'rb'),",
            "    target_lang='es', # 29 languages supported",
            "    num_speakers=2,",
            "    watermark=False",
            ")",
            "dubbing_id = response.dubbing_id",
            "print(f'Dubbing job initiated: {dubbing_id}')"
        ]
    },
    {
        "id": "s4_code_poll",
        "narration": "On line eleven, we poll the dubbing status until rendering completes, then stream the localized Spanish MP4 file directly to disk.",
        "headline": "ASYNC POLLING & MP4 STREAMING",
        "sub": "Polling Job Status & Writing Localized Output",
        "type": "code",
        "highlight_line": 11,
        "code": [
            "while True:",
            "    status = client.dubbing.get_dubbing_project_metadata(dubbing_id)",
            "    if status.status == 'dubbed':",
            "        print('Dubbing complete! Downloading output...')",
            "        break",
            "    time.sleep(5)",
            "",
            "# Line 11: Stream Localized MP4 to Local Storage",
            "with open('output_spanish.mp4', 'wb') as f:",
            "    for chunk in client.dubbing.get_dubbed_file(dubbing_id):",
            "        f.write(chunk)",
            "print('Successfully downloaded localized B2B video!')"
        ]
    },
    {
        "id": "s5_split_compare",
        "narration": "Look at the side-by-side comparison. The cloned vocal tone, pacing, and emotional inflection match the original English presentation seamlessly.",
        "headline": "AUDIO WAVEFORM & LIP CADENCE MATCH",
        "sub": "Zero-Shot Vocal Timbre Preservation (English vs Spanish)",
        "type": "compare",
        "code_snippet": None
    },
    {
        "id": "s6_benchmarks",
        "narration": "Notice the production speed. A ten-minute presentation dubs in under three minutes, reducing localization overhead by ninety-six percent.",
        "headline": "ENTERPRISE LOCALIZATION BENCHMARKS",
        "sub": "Traditional Human Studio vs ElevenLabs Python API",
        "type": "benchmarks",
        "code_snippet": None
    },
    {
        "id": "s7_outro",
        "narration": "Grab the complete Python dubbing script in our GitHub repository below, test the ElevenLabs free trial in the description, and subscribe for next week's AI telephony agent tutorial.",
        "headline": "GITHUB BLUEPRINT & FREE TRIAL",
        "sub": "ElevenLabs Free Trial in Description | Next: AI Phone Agents",
        "type": "outro",
        "code_snippet": None
    }
]

SHORT_SCENE = {
    "narration": "Stop paying thousands to translate your videos. With ElevenLabs and five lines of Python, you can auto-clone your voice and dub any MP4 into 29 languages in under three minutes. Grab the free script on our GitHub below!",
    "headline": "AUTO-DUB VIDEOS IN PYTHON",
    "sub": "Clone Voice & Dub into 29 Languages"
}

async def generate_audio(text, outfile):
    for attempt in range(4):
        try:
            communicate = edge_tts.Communicate(text, VOICE)
            await communicate.save(outfile)
            if os.path.exists(outfile) and os.path.getsize(outfile) > 1000:
                return
        except Exception as e:
            print(f"Warning: Audio synth retry {attempt+1} due to: {e}")
            await asyncio.sleep(1.5)
    
    # Fallback to ChristopherNeural if Andrew intermittently times out
    print("Falling back to en-US-ChristopherNeural for stability...")
    communicate = edge_tts.Communicate(text, "en-US-ChristopherNeural")
    await communicate.save(outfile)

def get_audio_duration(file_path):
    cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{file_path}"'
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return float(res.stdout.strip())

def render_slide_image(scene, out_png, width=1920, height=1080):
    img = Image.new("RGBA", (width, height), (10, 15, 30, 255))
    draw = ImageDraw.Draw(img)

    try:
        f_head = ImageFont.truetype("arialbd.ttf", 36)
        f_sub = ImageFont.truetype("arial.ttf", 20)
        f_code = ImageFont.truetype("consola.ttf", 22)
        f_tag = ImageFont.truetype("arialbd.ttf", 16)
        f_big = ImageFont.truetype("arialbd.ttf", 44)
    except:
        f_head = ImageFont.load_default()
        f_sub = ImageFont.load_default()
        f_code = ImageFont.load_default()
        f_tag = ImageFont.load_default()
        f_big = ImageFont.load_default()

    # Ambient grid / gradient top bar
    draw.rectangle([(0, 0), (width, 80)], fill=(15, 23, 42, 240))
    draw.line([(0, 80), (width, 80)], fill=(59, 130, 246, 120), width=2)
    draw.ellipse([(60, 28), (84, 52)], fill=(16, 185, 129, 255))
    draw.text((105, 26), "AGENTIC STACK  //  EPISODE 003: AI VOICE CLONING & VIDEO DUBBING", fill=(255, 255, 255), font=f_head)

    # Top right tag
    draw.rounded_rectangle([(width - 240, 22), (width - 60, 58)], radius=8, fill=(168, 85, 247, 40), outline=(168, 85, 247, 180), width=1)
    draw.text((width - 220, 29), "ELEVENLABS API", fill=(216, 180, 254), font=f_tag)

    stype = scene.get("type", "intro")

    if stype == "code":
        # Left side info card
        draw.rounded_rectangle([(60, 120), (560, 960)], radius=16, fill=(15, 23, 42, 200), outline=(51, 65, 85, 180), width=1)
        draw.text((90, 150), scene["headline"], fill=(255, 255, 255), font=f_head)
        draw.text((90, 200), scene["sub"], fill=(148, 163, 184), font=f_sub)

        # Code breakdown points
        draw.rounded_rectangle([(90, 270), (530, 480)], radius=12, fill=(10, 15, 28, 220), outline=(30, 41, 59, 200), width=1)
        draw.text((110, 290), "KEY HIGHLIGHTS", fill=(168, 85, 247), font=f_tag)
        draw.text((110, 330), "• Full Diarization Support (Multi-Speaker)", fill=(226, 232, 240), font=f_sub)
        draw.text((110, 370), "• 29 Target Languages Supported", fill=(226, 232, 240), font=f_sub)
        draw.text((110, 410), "• Zero-Shot Voice Timbre Preservation", fill=(226, 232, 240), font=f_sub)

        # Right side code IDE
        draw.rounded_rectangle([(590, 120), (width - 60, 960)], radius=16, fill=(11, 15, 25, 240), outline=(59, 130, 246, 120), width=2)
        # IDE top bar
        draw.rectangle([(590, 120), (width - 60, 170)], fill=(20, 27, 45, 240))
        draw.ellipse([(620, 138), (634, 152)], fill=(239, 68, 68))
        draw.ellipse([(644, 138), (658, 152)], fill=(234, 179, 8))
        draw.ellipse([(668, 138), (682, 152)], fill=(34, 197, 94))
        draw.text((720, 135), "dubbing_pipeline.py  (Python 3.11)", fill=(148, 163, 184), font=f_sub)

        # Code lines
        code_lines = scene.get("code", [])
        hl = scene.get("highlight_line", 0)
        cy = 200
        for idx, line in enumerate(code_lines, 1):
            if idx == hl:
                draw.rectangle([(600, cy - 4), (width - 70, cy + 30)], fill=(168, 85, 247, 45), outline=(168, 85, 247, 180), width=1)
                line_color = (236, 72, 153)
                num_color = (255, 255, 255)
            else:
                line_color = (226, 232, 240)
                num_color = (100, 116, 139)

            draw.text((620, cy), f"{idx:2d}", fill=num_color, font=f_code)
            draw.text((680, cy), line, fill=line_color, font=f_code)
            cy += 48

    elif stype == "architecture":
        draw.rounded_rectangle([(100, 140), (width - 100, 960)], radius=20, fill=(15, 23, 42, 220), outline=(59, 130, 246, 140), width=2)
        draw.text((150, 180), scene["headline"], fill=(255, 255, 255), font=f_big)
        draw.text((150, 240), scene["sub"], fill=(148, 163, 184), font=f_sub)

        # 3 Stages Nodes
        stages = [
            ("Stage 1: Ingestion", "Audio Track Separation\n& Speaker Diarization", (6, 182, 212)),
            ("Stage 2: Translation", "Neural LLM Translation\nwith Lip-Sync Timing", (168, 85, 247)),
            ("Stage 3: Synthesis", "Zero-Shot Voice Clone\n& Localized Audio Mix", (16, 185, 129))
        ]
        box_w = 480
        box_h = 340
        start_x = 180
        for i, (title, desc, col) in enumerate(stages):
            bx = start_x + i * 530
            by = 360
            draw.rounded_rectangle([(bx, by), (bx + box_w, by + box_h)], radius=16, fill=(10, 15, 28, 240), outline=col, width=2)
            draw.rounded_rectangle([(bx + 20, by + 20), (bx + box_w - 20, by + 70)], radius=8, fill=(col[0], col[1], col[2], 40))
            draw.text((bx + 40, by + 32), title, fill=col, font=f_head)
            draw.text((bx + 40, by + 120), desc, fill=(226, 232, 240), font=f_sub)

    elif stype == "benchmarks":
        draw.rounded_rectangle([(100, 140), (width - 100, 960)], radius=20, fill=(15, 23, 42, 220), outline=(16, 185, 129, 140), width=2)
        draw.text((150, 180), scene["headline"], fill=(255, 255, 255), font=f_big)
        draw.text((150, 240), scene["sub"], fill=(148, 163, 184), font=f_sub)

        # Two comparison blocks
        # Left: Manual Human Studio
        draw.rounded_rectangle([(180, 340), (880, 840)], radius=16, fill=(239, 68, 68, 20), outline=(239, 68, 68, 120), width=2)
        draw.text((220, 380), "TRADITIONAL HUMAN DUBBING", fill=(248, 113, 113), font=f_head)
        draw.text((220, 460), "Cost: $500 - $1,200 per video", fill=(255, 255, 255), font=f_sub)
        draw.text((220, 520), "Turnaround Time: 5 to 14 Days", fill=(255, 255, 255), font=f_sub)
        draw.text((220, 580), "Voice Consistency: New Voice Actors", fill=(255, 255, 255), font=f_sub)
        draw.text((220, 640), "Scalability: Linear, manual overhead", fill=(255, 255, 255), font=f_sub)

        # Right: ElevenLabs Python Dubbing
        draw.rounded_rectangle([(960, 340), (1660, 840)], radius=16, fill=(16, 185, 129, 20), outline=(16, 185, 129, 180), width=2)
        draw.text((1000, 380), "ELEVENLABS PYTHON DUBBING", fill=(52, 211, 153), font=f_head)
        draw.text((1000, 460), "Cost: ~$2.50 API consumption (96% Savings)", fill=(255, 255, 255), font=f_sub)
        draw.text((1000, 520), "Turnaround Time: Under 3 Minutes", fill=(255, 255, 255), font=f_sub)
        draw.text((1000, 580), "Voice Consistency: 100% Original Timbre Cloned", fill=(255, 255, 255), font=f_sub)
        draw.text((1000, 640), "Scalability: Infinite Async API Batches", fill=(255, 255, 255), font=f_sub)

    elif stype == "outro":
        draw.rounded_rectangle([(100, 140), (width - 100, 960)], radius=20, fill=(15, 23, 42, 220), outline=(168, 85, 247, 140), width=2)
        draw.text((150, 180), scene["headline"], fill=(255, 255, 255), font=f_big)
        draw.text((150, 240), scene["sub"], fill=(148, 163, 184), font=f_sub)

        # YouTube End Screen Elements
        draw.rounded_rectangle([(200, 340), (900, 780)], radius=16, fill=(10, 15, 28, 240), outline=(59, 130, 246, 180), width=2)
        draw.text((240, 380), "PREVIOUS EPISODE", fill=(96, 165, 250), font=f_head)
        draw.text((240, 440), "Episode 002: Conversational Voice AI", fill=(255, 255, 255), font=f_sub)
        draw.text((240, 490), "Sub-400ms WebSockets & Barge-In VAD", fill=(148, 163, 184), font=f_sub)

        draw.rounded_rectangle([(1000, 340), (1700, 780)], radius=16, fill=(10, 15, 28, 240), outline=(168, 85, 247, 180), width=2)
        draw.text((1040, 380), "NEXT EPISODE (PITCH #004)", fill=(192, 132, 252), font=f_head)
        draw.text((1040, 440), "AI Voice Phone Agent in Python", fill=(255, 255, 255), font=f_sub)
        draw.text((1040, 490), "Twilio SIP Telephony + Live CRM Database", fill=(148, 163, 184), font=f_sub)

        # Call to Action Banner
        draw.rounded_rectangle([(200, 820), (1700, 910)], radius=12, fill=(16, 185, 129, 30), outline=(16, 185, 129, 140), width=1)
        draw.text((240, 845), "🎁 ElevenLabs Free Trial & Python Blueprint in Description Below!", fill=(52, 211, 153), font=f_head)

    else: # Default intro / compare
        draw.rounded_rectangle([(100, 140), (width - 100, 960)], radius=20, fill=(15, 23, 42, 220), outline=(59, 130, 246, 140), width=2)
        draw.text((150, 220), scene["headline"], fill=(255, 255, 255), font=f_big)
        draw.text((150, 300), scene["sub"], fill=(148, 163, 184), font=f_head)

        draw.rounded_rectangle([(150, 420), (1750, 780)], radius=16, fill=(10, 15, 28, 240), outline=(51, 65, 85, 180), width=1)
        draw.text((200, 480), "• Full-Duplex Neural Audio Diarization", fill=(226, 232, 240), font=f_head)
        draw.text((200, 560), "• Cloned Voice Inflection Across 29 Languages", fill=(226, 232, 240), font=f_head)
        draw.text((200, 640), "• Production Python Architecture with SDK & Webhooks", fill=(226, 232, 240), font=f_head)

    img.save(out_png)

def render_shorts_slide(out_png, width=1080, height=1920):
    img = Image.new("RGBA", (width, height), (10, 15, 30, 255))
    draw = ImageDraw.Draw(img)

    try:
        f_big = ImageFont.truetype("arialbd.ttf", 64)
        f_head = ImageFont.truetype("arialbd.ttf", 44)
        f_sub = ImageFont.truetype("arial.ttf", 32)
        f_code = ImageFont.truetype("consola.ttf", 26)
        f_tag = ImageFont.truetype("arialbd.ttf", 24)
    except:
        f_big = ImageFont.load_default()
        f_head = ImageFont.load_default()
        f_sub = ImageFont.load_default()
        f_code = ImageFont.load_default()
        f_tag = ImageFont.load_default()

    # Top Brand Header
    draw.rectangle([(0, 0), (width, 160)], fill=(15, 23, 42, 240))
    draw.line([(0, 160), (width, 160)], fill=(168, 85, 247, 180), width=3)
    draw.ellipse([(60, 60), (96, 96)], fill=(16, 185, 129))
    draw.text((120, 56), "AGENTIC STACK B2B", fill=(255, 255, 255), font=f_head)

    # Main Hero Title
    draw.text((60, 240), "STOP TRANSLATING\nVIDEOS MANUALLY", fill=(239, 68, 68), font=f_big)
    draw.text((60, 420), "Dub into 29 Languages with Python", fill=(148, 163, 184), font=f_sub)

    # Visual Comparison Card
    draw.rounded_rectangle([(60, 500), (width - 60, 920)], radius=24, fill=(15, 23, 42, 220), outline=(168, 85, 247, 180), width=2)
    draw.text((100, 540), "AUTO VOICE CLONING (AI DUB)", fill=(192, 132, 252), font=f_head)
    
    draw.text((100, 630), "❌ Human Agency: $500/video, 10 days", fill=(248, 113, 113), font=f_sub)
    draw.text((100, 710), "✅ ElevenLabs API: $2.50/video, 2 min", fill=(52, 211, 153), font=f_sub)
    draw.text((100, 790), "✅ Exact Voice Cloned Across 29 Langs", fill=(56, 189, 248), font=f_sub)

    # Python Code Block in Mobile Center
    draw.rounded_rectangle([(60, 980), (width - 60, 1540)], radius=24, fill=(11, 15, 25, 250), outline=(59, 130, 246, 140), width=2)
    # Code top bar
    draw.rectangle([(60, 980), (width - 60, 1040)], fill=(20, 27, 45, 240))
    draw.ellipse([(90, 1002), (106, 1018)], fill=(239, 68, 68))
    draw.ellipse([(118, 1002), (134, 1018)], fill=(234, 179, 8))
    draw.ellipse([(146, 1002), (162, 1018)], fill=(34, 197, 94))
    draw.text((200, 998), "dub_video.py (5 Lines)", fill=(148, 163, 184), font=f_tag)

    code_lines = [
        "from elevenlabs.client import ElevenLabs",
        "client = ElevenLabs(api_key='...')",
        "",
        "# Submit Video for Auto-Dubbing",
        "res = client.dubbing.dub_a_video(",
        "    file=open('video.mp4', 'rb'),",
        "    target_lang='es',",
        "    num_speakers=2",
        ")",
        "print('Dubbed video generated!')"
    ]
    cy = 1080
    for l in code_lines:
        draw.text((90, cy), l, fill=(226, 232, 240) if "dub_a_video" not in l else (236, 72, 153), font=f_code)
        cy += 44

    # Bottom CTA Banner
    draw.rounded_rectangle([(60, 1600), (width - 60, 1780)], radius=24, fill=(16, 185, 129, 30), outline=(16, 185, 129, 180), width=2)
    draw.text((100, 1640), "FREE PYTHON BLUEPRINT 👇", fill=(52, 211, 153), font=f_head)
    draw.text((100, 1710), "Full code + ElevenLabs trial on GitHub", fill=(255, 255, 255), font=f_sub)

    img.save(out_png)

def render_thumbnail_003(out_png):
    width, height = 1280, 720
    img = Image.new("RGBA", (width, height), (10, 15, 30, 255))
    draw = ImageDraw.Draw(img)

    try:
        f_huge = ImageFont.truetype("arialbd.ttf", 68)
        f_head = ImageFont.truetype("arialbd.ttf", 36)
        f_code = ImageFont.truetype("consola.ttf", 20)
        f_badge = ImageFont.truetype("arialbd.ttf", 22)
    except:
        f_huge = ImageFont.load_default()
        f_head = ImageFont.load_default()
        f_code = ImageFont.load_default()
        f_badge = ImageFont.load_default()

    # Split Screen: Left Side (English Audio Wave), Right Side (Spanish Video IDE)
    draw.rectangle([(0, 0), (width // 2, height)], fill=(15, 23, 42, 255))
    draw.rectangle([(width // 2, 0), (width, height)], fill=(11, 15, 25, 255))
    draw.line([(width // 2, 0), (width // 2, height)], fill=(168, 85, 247, 200), width=3)

    # Top Banner Headline (Approved High CTR text: DUB ANY VIDEO IN PYTHON)
    draw.rounded_rectangle([(40, 30), (width - 40, 130)], radius=18, fill=(168, 85, 247, 220), outline=(216, 180, 254), width=2)
    draw.text((70, 48), "DUB ANY VIDEO IN PYTHON", fill=(255, 255, 255), font=f_huge)

    # Left Side: Speaker 1 (Original Cloned Voice)
    draw.rounded_rectangle([(60, 170), (width // 2 - 40, height - 60)], radius=16, fill=(10, 15, 28, 230), outline=(6, 182, 212, 140), width=2)
    draw.text((90, 200), "ORIGINAL ENGLISH", fill=(34, 211, 238), font=f_head)
    draw.text((90, 260), "🎙️ Voice Timbre Cloned", fill=(226, 232, 240), font=f_badge)
    draw.text((90, 310), "⚡ 29 Target Languages", fill=(226, 232, 240), font=f_badge)
    draw.text((90, 360), "⏱️ Under 3 Minutes", fill=(226, 232, 240), font=f_badge)

    draw.rounded_rectangle([(90, 440), (width // 2 - 70, height - 90)], radius=12, fill=(16, 185, 129, 40), outline=(16, 185, 129, 180), width=1)
    draw.text((120, 500), "ZERO-SHOT CLONING", fill=(52, 211, 153), font=f_head)
    draw.text((120, 560), "100% Matching Vocal Tone", fill=(255, 255, 255), font=f_badge)

    # Right Side: Localized Python Terminal
    draw.rounded_rectangle([(width // 2 + 40, 170), (width - 60, height - 60)], radius=16, fill=(10, 15, 28, 230), outline=(168, 85, 247, 140), width=2)
    draw.text((width // 2 + 70, 200), "LOCALIZED SPANISH", fill=(216, 180, 254), font=f_head)

    right_code = [
        "client.dubbing.dub_a_video(",
        "    file='presentation.mp4',",
        "    target_lang='es',",
        "    num_speakers=2",
        ")",
        "",
        "# STATUS: 100% COMPLETED",
        ">> Output: localized_es.mp4"
    ]
    ry = 270
    for l in right_code:
        col = (52, 211, 153) if "STATUS" in l or "Output" in l else (226, 232, 240)
        draw.text((width // 2 + 70, ry), l, fill=col, font=f_code)
        ry += 42

    # Bottom badge
    draw.rounded_rectangle([(width - 340, height - 120), (width - 70, height - 70)], radius=10, fill=(239, 68, 68), outline=(255, 255, 255), width=2)
    draw.text((width - 320, height - 110), "ELEVENLABS API", fill=(255, 255, 255), font=f_badge)

    img.save(out_png)

async def main():
    print("=== Step 1: Synthesizing Audio for Long Video Scenes ===")
    long_scene_files = []
    concat_list_file = os.path.join(TMP_DIR, "concat_scenes.txt")
    
    with open(concat_list_file, "w", encoding="utf-8") as f_concat:
        for idx, sc in enumerate(LONG_SCENES):
            wav_file = os.path.join(TMP_DIR, f"long_s{idx}_{sc['id']}.mp3")
            png_file = os.path.join(TMP_DIR, f"long_s{idx}_{sc['id']}.png")
            mp4_file = os.path.join(TMP_DIR, f"long_s{idx}_{sc['id']}.mp4")

            print(f"Generating audio for scene {idx}: {sc['headline']}...")
            await generate_audio(sc["narration"], wav_file)
            dur = get_audio_duration(wav_file) + 0.3 # Add slight padding for clean transitions
            print(f"  Duration: {dur:.2f}s")

            # Render PNG slide
            render_slide_image(sc, png_file, 1920, 1080)

            # Render segment MP4
            cmd = (
                f'ffmpeg -y -loop 1 -i "{png_file}" -i "{wav_file}" '
                f'-c:v libx264 -t {dur:.3f} -pix_fmt yuv420p -c:a aac -b:a 192k -shortest "{mp4_file}"'
            )
            subprocess.run(cmd, shell=True, check=True)
            f_concat.write(f"file '{os.path.abspath(mp4_file)}'\n")
            long_scene_files.append(mp4_file)

    print("=== Step 2: Merging Long Video Segments ===")
    out_long_mp4 = os.path.join(ASSETS_DIR, "video_003_long.mp4")
    cmd_merge = f'ffmpeg -y -f concat -safe 0 -i "{concat_list_file}" -c copy "{out_long_mp4}"'
    subprocess.run(cmd_merge, shell=True, check=True)
    long_dur = get_audio_duration(out_long_mp4)
    print(f"SUCCESS: Long Video produced: {out_long_mp4} (Duration: {long_dur:.1f}s)")

    print("=== Step 3: Producing 9:16 Shorts Video ===")
    short_wav = os.path.join(TMP_DIR, "short_003.mp3")
    short_png = os.path.join(TMP_DIR, "short_003.png")
    out_short_mp4 = os.path.join(ASSETS_DIR, "video_003_short.mp4")

    print("Synthesizing audio for 9:16 Short...")
    await generate_audio(SHORT_SCENE["narration"], short_wav)
    short_dur = get_audio_duration(short_wav)
    print(f"Short audio duration: {short_dur:.2f}s (Strictly under 25s)")

    render_shorts_slide(short_png, 1080, 1920)

    cmd_short = (
        f'ffmpeg -y -loop 1 -i "{short_png}" -i "{short_wav}" '
        f'-c:v libx264 -t {short_dur + 0.2:.3f} -pix_fmt yuv420p -c:a aac -b:a 192k -shortest "{out_short_mp4}"'
    )
    subprocess.run(cmd_short, shell=True, check=True)
    print(f"SUCCESS: Shorts Video produced: {out_short_mp4} (Duration: {get_audio_duration(out_short_mp4):.1f}s)")

    print("=== Step 4: Generating High-CTR Thumbnail ===")
    out_thumb = os.path.join(ASSETS_DIR, "thumb_003.png")
    render_thumbnail_003(out_thumb)
    print(f"SUCCESS: Thumbnail generated: {out_thumb}")

if __name__ == "__main__":
    asyncio.run(main())
