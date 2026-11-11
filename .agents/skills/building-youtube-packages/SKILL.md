---
name: building-youtube-packages
description: Researches high-RPM B2B software topics, writes verified technical tutorial scripts, synthesizes neural voiceovers with edge-tts, renders 1080p MP4 videos and 9:16 Shorts via FFmpeg, generates thumbnails, and updates the Overseer Dashboard. Use when the user asks to produce a YouTube video package, run the daily content pipeline, build the Overseer Dashboard, or upload via the YouTube Data API. Do not use for unrelated web scraping or personal vlog editing.
---

# Autonomous YouTube B2B Production Skill (Agentic Stack B2B)

## Purpose
Executes an end-to-end, zero-cost cloud production pipeline that creates complete, monetization-compliant YouTube video packages for the **Agentic Stack B2B** channel. Produces Long-form 1080p MP4, 9:16 Short MP4 (<20s), PNG Thumbnails, SEO Metadata with affiliate links, and synchronizes the Overseer Dashboard.

## Channel & Production Specifications (Master Framework 2026)
- **Channel Name:** Agentic Stack B2B
- **Niche:** AI & Agentic Stack B2B (Python, Agentic Workflows, LLM & API Integrations)
- **Official Voice Actor:** `edge-tts` with voice `en-US-AndrewMultilingualNeural` (Rate: `+0%` default)
- **Visual Production Engine:** Concept 4 Hybrid (24-26pt mobile code, sliding neon arrow pointers, floating concept badges, progressive architecture pulses, and smooth split-screen live terminal sync)
- **Thumbnail Standard:** Hybrid Concept 1+3 (Split-screen contrast pain on left, 3-node connected network architecture on right, terminal status in bottom, max 2-3 words headline following Gycklarregeln)
- **Title Length Limit:** Strict limit `< 60 characters` for primary mobile CTR title
- **Target Video Duration:** 3:00 to 5:00 minutes for technical tutorials (combining depth with zero fluff)
- **Weekly Cadence:** 3 packages/week (Monday, Wednesday, Friday)
- **Target Long-form RPM:** $18.00 – $35.00
- **Shorts Strategy:** Duration < 20 seconds, aggressive 2-second visual & audio hook, exactly 0 commercial music tracks to retain 100% Creator Pool allocation.
- **Compliance Rules (YouTube 2026):**
  - Strict Anti-Slop Protocol: All Python scripts must be executed and verified in the sandbox before script writing.
  - Transparent Metadata: Category `28` (Science & Technology), `altered_content: false`.
  - FTC Affiliate Disclosures included in descriptions and pinned comments.
  - **Muntlig Hänvisning till Affiliate & Like/Subscribe:** Muntligt och organiskt integrerat i speakern vid delsegrar och outrot. Inga störande grafiska CTA-boxar.
  - **Post-Launch Review:** Granskningsagent körs vid 24h/48h för att mäta CTR och 0:30-retention med automatisk A/B-titelväxling vid behov.

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
