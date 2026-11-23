# Agentic Stack — Autonomous YouTube Production Factory (2026 Master Standard)

> **End-to-end AI-driven YouTube production & compliance pipeline for the [Agentic Stack YouTube Channel](https://www.youtube.com/@AgenticStackB2B) with verified open-source code in [Agentic-Stack-Library](https://github.com/Johnmannen/Agentic-Stack-Library).**

[![System Status](https://img.shields.io/badge/System_Status-ONLINE-10b981?style=for-the-badge&logo=googlecloud)](https://johnmannen.github.io/youtube-empire/)
[![YouTube Compliance](https://img.shields.io/badge/YouTube_2026_Compliance-100%25_Approved-06b6d4?style=for-the-badge&logo=youtube)](https://johnmannen.github.io/youtube-empire/)
[![Open Source Library](https://img.shields.io/badge/GitHub-Agentic_Stack_Library-38bdf8?style=for-the-badge&logo=github)](https://github.com/Johnmannen/Agentic-Stack-Library)

---

## 🌐 Live Kontrollpanel (Overseer Dashboard) & Öppet Kodbibliotek
- **Live Kontrollpanel (GitHub Pages):** 👉 **[https://johnmannen.github.io/youtube-empire/](https://johnmannen.github.io/youtube-empire/)** *(eller `docs/index.html` lokalt)*
- **Publikt Källkodsrepo (som alla videor länkar till):** 👉 **[https://github.com/Johnmannen/Agentic-Stack-Library](https://github.com/Johnmannen/Agentic-Stack-Library)**

---

## 🎯 Kanalstandard & Produktionsregler (2026 Master Blueprint)
- **Kanalnamn:** Agentic Stack B2B *(uttalas alltid `business to business` i tal — aldrig förkortat `B2B`)*
- **Officiell Speakerröst:** **Endast `Andrew` (`en-US-AndrewMultilingualNeural`)** via `edge-tts`. **Totalförbud mot fallback-röster** (som `ChristopherNeural`); vid tillfälligt API-fel görs alltid retry med `Andrew`. Andra röster (t.ex. spansk kvinnlig tolkröst eller podcast-gäst) får enbart förekomma på dedikerade live-demosegment som visar hur systemet fungerar.
- **Långvideo (16:9, `1920×1080`, `>= 4:00 min`):**
  - **Helt stilla Thumbnail-intro (`0.00s–1.80s`):** Andrews röst startar direkt på `0.00s` medan 16:9-thumbnailen ligger **100 % stilla (ingen zoom-in/tillbakahopp)**, följt av en mjuk `0.5s` crossfade (`1.80s–2.30s`) in i Scen 1.
  - **100 % Audio-Visual Speaker-Sync:** Grafiken skiftar vy/fokus vid varje nytt tankeskifte i manuset, med enhetlig glödande fokusram runt aktiv kod och nedtonade, stilla bakgrundskort.
  - **Outro-regel:** Lovar aldrig vilket ämne som kommer i "nästa video" — hänvisar till övriga videor på kanalen, exakt GitHub-länk och gratis provperiod i fäst kommentar & beskrivning samt **Like & Subscribe**.
- **YouTube Shorts (9:16, `1080×1920`, `30–60s`):**
  - **0–4s Live Result Proof:** Visar och spelar upp slutprodukten live i ljud och bild inom de första 4 sekunderna.
  - **Konsekvent rubrik med långvideon:** Övre rubrik och thumbnail-budskap matchar alltid långvideons breda värdeerbjudande (t.ex. `ENGLISH TO ANY LANGUAGE`, aldrig insnävat till ett enda språk).
  - **4-korts CTA-slutskärm:** Lyfter fram 1) Långvideon på kanalen, 2) Exakt GitHub-undermapp i `Agentic-Stack-Library`, 3) Gratis provperiod via affiliatelänk i fäst kommentar & beskrivning, samt 4) **Like & Subscribe**.
  - **YouTube Stream Hygiene:** Alltid `pix_fmt=yuv420p`, `color_range=tv`, `color_space=bt709`, `+faststart` och **0 `ICC Profile` side_data** (förhindrar uppladdningsfel `2888402`).
- **Dubbla Thumbnails per Avsnitt (16:9 Long + 9:16 Short):**
  - `docs/assets/thumb_<id>.png` (`1280×720` 16:9 horisontell poster med varierad avatar-pose/handposition per avsnitt).
  - `docs/assets/thumb_short_<id>.png` (`1080×1920` äkta vertikal 9:16-poster där avataren i nedre halvan **tittar och pekar uppåt** mot rubriken och bevisgrafiken — aldrig en slarvigt beskuren 16:9-bild).
- **Obligatorisk GitHub & README-synk:**
  - Vid varje ny video måste både avsnittets egen mapp (`<id>-<slug>/README.md` + körbar kod) **och** rot-`README.md` i `Johnmannen/Agentic-Stack-Library` (samt denna `README.md`) uppdateras och verifieras maskinellt via `audit_package.py`.

---

## 📚 Producerade Videopaket & Verifierade Länkar

| Avsnitt | Titel | Kodrepo (`Agentic-Stack-Library`) | Verifierad Affiliate-länk | Status |
|:---:|:---|:---|:---|:---:|
| **#001** | Build Autonomous AI Agent Skills in Python (Zero-Cost Blueprint) | [`001-autonomous-agent-skills`](https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/001-autonomous-agent-skills) | `https://try.elevenlabs.io/agentic-voice` | ✅ Publicerad |
| **#002** | Build Real-Time Voice AI Agents in Python (Sub-400ms WebSockets) | [`002-elevenlabs-voice-agent`](https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/002-elevenlabs-voice-agent) | `https://try.elevenlabs.io/agentic-voice` | ✅ Publicerad |
| **#003** | How to Clone Voices and Dub Videos in Python (29+ Languages) | [`003-voice-cloning-video-dubbing`](https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/003-voice-cloning-video-dubbing) | `https://try.elevenlabs.io/agentic-dubbing` | ✅ Publicerad |
| **#004** | Build an AI Voice Phone Agent in Python (ElevenLabs + Twilio) | [`004-voice-phone-agent`](https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/004-voice-phone-agent) | `https://try.elevenlabs.io/agentic-telephony` | ✅ Publicerad |
| **#005** | Turn Any Text Document into Audio Podcasts in Python (Audio Native) | [`005-doc-to-podcast`](https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/005-doc-to-podcast) | `https://try.elevenlabs.io/agentic-reader` | ✅ Publicerad |
| **#006** | Build an AI Real-Time Voice Translator in Python (Sub-500ms S2S) | [`006-realtime-voice-translator`](https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/006-realtime-voice-translator) | `https://try.elevenlabs.io/agentic-translator` | ✅ Publicerad |
| **#007** | Generate Dynamic AI Game Audio & NPC Voices in Python (SFX API) | [`007-dynamic-game-audio-sfx`](https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/007-dynamic-game-audio-sfx) | `https://try.elevenlabs.io/agentic-sfx` | ✅ Klar i Kontrollpanel |
| **#008** | Run 9 Local Autonomous AI Agents on Any Old Desktop PC (Google Antigravity + Python, 0 GPU) | [`antigravity-desktop-agentcore`](https://github.com/Johnmannen/antigravity-desktop-agentcore) | 100% Free MIT Open Source | ✅ Klar för uppladdning (`UPLOAD_PACKAGE_008`) |

### Kommande Pitch-kö (`#009` – `#011`)
- **Pitch `#009` (Automated B2B Onboarding Voice & Video Engine):** `https://try.elevenlabs.io/agentic-onboarding`
- **Pitch `#010` (Multi-Character AI Audiobook Studio):** `https://try.elevenlabs.io/agentic-onboarding`
- **Pitch `#011` (AI Voice Compliance & Call QA Auditor — Scribe):** `https://try.elevenlabs.io/agentic-onboarding`

---

## 🛠️ Viktiga Skript & Kvalitetsgrindar
```bash
# 1. Uppdatera kontrollpanelen (docs/dashboard_state.json & docs/index.html) för ett avsnitt:
python scripts/auto_deploy_package.py --package-id 006

# 2. Kör den 30+ punkters maskinella kvalitets-, ström-, röst- & GitHub README-revisionen:
python .agents/skills/quality_compliance_auditor/scripts/audit_package.py --package-id 006 --dir docs/assets
```
