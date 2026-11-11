import re
from pathlib import Path

html_path = Path("docs/index.html")
html = html_path.read_text(encoding="utf-8")

# 1. Update Short video file and link
html = html.replace("assets/video_003_short.mp4", "assets/video_002_1_short.mp4")

# 2. Update Video Description to Episode 002.1
new_description = """🎁 [FREE TRIAL] Try ElevenLabs Conversational Voice AI SDK:
👉 https://elevenlabs.io/?via=agenticstack (Affiliate Partner Link)

🚀 [SOURCE CODE] Download Python Scripts & WebSocket Blueprint:
👉 https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/002-elevenlabs-voice-agent

📚 [OPEN SOURCE REPO] All Channel Episodes & Star the Library:
👉 https://github.com/Johnmannen/Agentic-Stack-Library

Text chatbots with four-second response lags are dead. When users speak, they expect an immediate, fluid conversation, not dead silence.

In this video, we build a production-ready conversational voice agent in Python using ElevenLabs full-duplex WebSockets with sub-400ms round-trip latency and 42ms hardware barge-in interruption.

⏱️ TIMESTAMPS:
00:00 - The Death of High-Latency Chatbots
00:27 - System Architecture: Bi-Directional WebSockets
00:58 - Python Setup: Persistent Client & API Key
01:23 - 42ms Hardware Barge-In Configuration
01:47 - Split-Screen Tool Calling: Mid-Call Stripe Refund
02:15 - Latency Benchmarks: HTTP vs WebSockets
02:40 - Outro, Free Trial & Source Code

🛠️ ENTERPRISE TOOLS (VERIFIED IN SANDBOX):
👉 Try ElevenLabs Conversational AI SDK (Free Trial): https://elevenlabs.io/?via=agenticstack

⚖️ FTC AFFILIATE DISCLOSURE:
Some links in this description are affiliate links. If you sign up or purchase through them, we may receive a commission at no extra cost to you. We strictly test and verify every tool in our cloud sandbox before recommending it.

#VoiceAI #ElevenLabs #Python #ConversationalAI #WebSockets #AIAgents #AgenticStack"""

# Replace the inner textarea for videoDescription
p_desc_start = html.find('id="videoDescription"')
if p_desc_start != -1:
    tag_close = html.find('>', p_desc_start) + 1
    textarea_end = html.find('</textarea>', tag_close)
    html = html[:tag_close] + new_description + html[textarea_end:]

# 3. Update Pinned Comment to Episode 002.1
new_pinned = """📌 Grab the ElevenLabs Conversational AI Free Trial:
👉 https://elevenlabs.io/?via=agenticstack

💻 Download the Python script & WebSocket templates on GitHub:
👉 https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/002-elevenlabs-voice-agent

💬 Question: What latency are you getting on your voice pipelines today? Let us know below!"""

p_pin_start = html.find('id="pinnedComment"')
if p_pin_start != -1:
    tag_close = html.find('>', p_pin_start) + 1
    pin_end = html.find('</p>', tag_close)
    html = html[:tag_close] + new_pinned + html[pin_end:]

# 4. Update Tags to Episode 002.1
new_tags = "elevenlabs, voice ai, python voice agent, conversational ai, websockets python, real time ai, sub second latency, barge in vad, agentic stack"
p_tags_start = html.find('id="videoTags"')
if p_tags_start != -1:
    tag_close = html.find('>', p_tags_start) + 1
    tags_end = html.find('</p>', tag_close)
    html = html[:tag_close] + new_tags + html[tags_end:]

html_path.write_text(html, encoding="utf-8")
print("Successfully corrected docs/index.html with 002.1 Shorts, Description, Pinned Comment, and Tags!")
