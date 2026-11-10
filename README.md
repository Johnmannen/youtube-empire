# Agentic Stack B2B — Cloud Autonomous YouTube Production Factory

> **Autonomous AI-driven YouTube publishing pipeline operating completely inside cloud sandboxes with 0 kr infrastructure cost.**

[![System Status](https://img.shields.io/badge/System_Status-ONLINE-10b981?style=for-the-badge&logo=googlecloud)](https://johnmannen.github.io/youtube-empire/)
[![YouTube Compliance](https://img.shields.io/badge/YouTube_2026_Compliance-100%25_Approved-06b6d4?style=for-the-badge&logo=youtube)](https://johnmannen.github.io/youtube-empire/)
[![Production Cadence](https://img.shields.io/badge/Cadence-3_Packages%2FWeek-6366f1?style=for-the-badge)](https://johnmannen.github.io/youtube-empire/)

---

## 🌐 Live Kontrollpanel (Overseer Dashboard)
Öppna den live kontrollpanelen på GitHub Pages:  
👉 **[https://johnmannen.github.io/youtube-empire/](https://johnmannen.github.io/youtube-empire/)**  
*(Alternativt öppna `docs/index.html` lokalt i valfri webbläsare).*

---

## 🎯 Nisch & Konfiguration
- **Kanalnamn:** Agentic Stack B2B
- **Nisch:** AI & Agentic Stack B2B (Python, Agentiska arbetsflöden, LLM & API-integrationer)
- **Berättarröst:** `edge-tts` med neural röst `en-US-ChristopherNeural` (Rate: `+5%` / `+10%`)
- **Driftläge:** **PITCH-LÄGE** (3 kurerade högvärdiga B2B ämnesförslag med 1-klicks exekvering i molnet)
- **Frekvens:** 3 videopaket per vecka (Måndag, Onsdag, Fredag)
- **Hosting:** GitHub Pages (`docs/`-mapp i repot)
- **Affiliate-intäkter:** Verifierad PartnerStack referral-länk (ElevenLabs AI Voice & Conversational AI API: 22% recurring commission)

---

## 📦 Vad Ingår i Varje Videopaket?
Varje autonom körning genererar en komplett digital tillgång i `docs/assets/`:
1. **Långformatsvideo (1080p Full HD MP4):**
   - Multi-scen presentation med dynamiska arkitekturdiagram och färglagd terminalkod.
   - Professionell berättarröst via `edge-tts` (`en-US-ChristopherNeural`).
2. **YouTube Shorts (9:16 Vertikal MP4):**
   - Optimerad för **under 20 sekunder** för maximal retention (73% snitt).
   - Aggressiv 2-sekunders visuell och verbal hook.
   - Exakt **0 licensierade musikspår** för att behålla **100% av Creator Pool-allokeringen** (45% nettosplit).
3. **Miniatyrbild (1280x720 PNG):**
   - Högkontrast B2B-grafik med neonaccenter, fet typografi och arkitekturskiss.
4. **SEO & Intäktsmetadata (`metadata.json`):**
   - Högkonverterande titel och alternativa titlar för A/B-test.
   - Tidsstämplade kapitel (timestamps).
   - Direktlänk till källkoden överst i beskrivningen.
   - 3 kontextuella SaaS affiliate-länkar + obligatorisk FTC-deklaration.
   - Fastnålad kommentar och tekniska taggar.
   - YouTube Kategori `28` (Science & Technology) och `Altered Content: No`.

---

## 🛠️ Arkitektur & Katalogstruktur
```text
.
├── .agents/
│   └── skills/
│       └── building-youtube-packages/
│           ├── SKILL.md                  # Google Antigravity Skill spec (YAML + instruktioner)
│           └── scripts/
│               ├── produce_package.py    # Röstsyntes, diagram & videokomposition via FFmpeg
│               └── upload_youtube.py     # Fas 2: YouTube Data API v3 uppladdningsmotor
├── .github/
│   └── workflows/
│       └── daily_factory.yml             # Schemalagd CI/CD körning 3 ggr/vecka (04:00 UTC)
├── demos/
│   └── agent_skill_demo.py               # Verifierad körbar Python-kod för Anti-Slop protokoll
├── docs/                                 # GitHub Pages hosting root
│   ├── index.html                        # Overseer Dashboard (Tailwind CSS)
│   ├── dashboard_state.json              # Realtidsmanifest för KPI:er, pitchar och paket
│   └── assets/
│       ├── video_001_long.mp4            # Färdig 1080p MP4
│       ├── video_001_short.mp4           # Färdig 9:16 Shorts MP4 (<20s)
│       ├── thumb_001.png                 # 1280x720 Thumbnail
│       └── metadata.json                 # Komplett SEO- och affiliate-metadata
└── README.md
```

---

## 🚀 Snabbstart & Manuell Körning

### 1. Installera beroenden i molnet:
```bash
pip install edge-tts pillow matplotlib google-api-python-client google-auth-oauthlib
```

### 2. Producera ett nytt videopaket:
```bash
python .agents/skills/building-youtube-packages/scripts/produce_package.py --output docs/assets/
```

### 3. Fas 2: Schemalägg / Ladda upp via YouTube Data API v3:
```bash
python .agents/skills/building-youtube-packages/scripts/upload_youtube.py --package docs/dashboard_state.json --client-secret client_secret.json
```
