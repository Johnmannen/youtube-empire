---
name: building-youtube-packages
description: Researches high-RPM B2B software topics, writes verified technical tutorial scripts, synthesizes neural voiceovers with edge-tts, renders 1080p MP4 videos and 9:16 Shorts via FFmpeg, generates thumbnails, and updates the Overseer Dashboard. Use when the user asks to produce a YouTube video package, run the daily content pipeline, build the Overseer Dashboard, or upload via the YouTube Data API. Do not use for unrelated web scraping or personal vlog editing.
---

# Autonomous YouTube B2B Production Skill (Agentic Stack B2B)

## Purpose
Executes an end-to-end, zero-cost cloud production pipeline that creates complete, monetization-compliant YouTube video packages for the **Agentic Stack B2B** channel. Produces Long-form 1080p MP4, 9:16 Short MP4 (<20s), PNG Thumbnails, SEO Metadata with affiliate links, and synchronizes the Overseer Dashboard.

## Channel & Production Specifications
- **Channel Name:** Agentic Stack B2B
- **Niche:** AI & Agentic Stack B2B (Python, Agentic Workflows, LLM & API Integrations)
- **Voice Actor:** `edge-tts` with voice `en-US-ChristopherNeural` (Rate: `+5%`)
- **Operational Mode:** PITCH-MODE (3 curated high-RPM topic proposals displayed on the dashboard for one-click production approval)
- **Weekly Cadence:** 3 packages/week (Monday, Wednesday, Friday)
- **Target Long-form RPM:** $18.00 – $35.00
- **Shorts Strategy:** Duration < 20 seconds, aggressive 2-second visual & audio hook, exactly 0 commercial music tracks to retain 100% Creator Pool allocation (45% net).
- **Compliance Rules (YouTube 2026):**
  - Strict Anti-Slop Protocol: All Python scripts must be executed and verified in the sandbox before script writing.
  - Transparent Metadata: Category `28` (Science & Technology), `altered_content: false` (no synthetic humans or simulated real-world news).
  - FTC Affiliate Disclosures included in descriptions and pinned comments.

## Workflow Checklist
- [ ] Step 1: Environment & Dependency Verification (`edge-tts`, `ffmpeg`, `pillow`, `matplotlib`)
- [ ] Step 2: Topic Scouting & Sandbox Code Verification (`demos/`)
- [ ] Step 3: Script & Metadata Generation (Long-form scenes + Short script <20s)
- [ ] Step 4: Neural Audio Synthesis (`edge-tts` with `en-US-ChristopherNeural`)
- [ ] Step 5: Visual Asset Generation (Slide diagrams, code syntax cards, high-contrast 1280x720 PNG thumbnail)
- [ ] Step 6: Video Assembly & Rendering via FFmpeg (1080p MP4 and 9:16 Short MP4)
- [ ] Step 7: Overseer Dashboard Update (`docs/dashboard_state.json` & `docs/index.html`)
- [ ] Step 8: Phase 2 Autonomous Upload (`scripts/upload_youtube.py`, optional)

## Script Usage

### Producing a Complete Video Package:
```bash
python .agents/skills/building-youtube-packages/scripts/produce_package.py --package-id 001 --output docs/assets/
```

### Direct Upload via YouTube Data API v3 (Phase 2):
```bash
python .agents/skills/building-youtube-packages/scripts/upload_youtube.py --package docs/dashboard_state.json --client-secret client_secret.json
```
