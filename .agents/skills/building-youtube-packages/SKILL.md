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
- **Official Voice Actor & Pronunciation Rules:** `edge-tts` with voice `en-US-AndrewMultilingualNeural` (fallback: `en-US-ChristopherNeural`, Rate: `+0%` default). **Aldrig uttalat `B2B`:** Om `B2B` måste sägas i manuset ska det alltid skrivas ut som **`business to business`** i TTS-texten.
- **Outro-regel (Inga löften om nästa video):** Lova aldrig vilket ämne som kommer i "nästa video" (planerna kan ändras). Uppmana istället till att utforska övriga videor på kanalen tillsammans med **Like & Subscribe** och exakt länk i fäst kommentar & beskrivning.
- **Visual Production Engine:** Concept 4 Hybrid (24-26pt mobile code, sliding neon arrow pointers, floating concept badges, progressive architecture pulses, and smooth split-screen live terminal sync)
- **Thumbnail Standard (2026 CTR Poster Blueprint — Uppdaterad efter Steg 1 & Dual-Format-regel):**
  - **Dubbla format per avsnitt (TVINGANDE — Long 16:9 + Short 9:16):** Varje gång en thumbnail produceras ska det alltid skapas **två separata thumbnails i rätt format** — aldrig bara en beskuren/utdragen 16:9-bild:
    1. **Long-form Thumbnail (16:9, `1280×720`):** `thumb_<id>.png` (horisontell affischlayout, nedre högra hörnet fritt för YouTubes tidsstämpel).
    2. **Short-form Thumbnail (9:16, `1080×1920`):** `thumb_short_<id>.png` (vertikal affischlayout anpassad för Shorts-flödet, med säker topp-/bottenmarginal för YouTube Shorts UI).
    Båda formaten ska finnas synliga och nedladdningsbara på kontrollpanelen (`docs/index.html`).
  - **Ingen skärmbild av videon:** Thumbnails får aldrig se ut som en video-stillbild eller slarvig skärmdump. De ska vara **säljande affischer** som fokuserar på slutproduktens konkreta resultat enligt **Rule of Three** (ren mörk bakgrund + konkret resultat/bevis-grafik + max 2–4 ords hook).
  - **Kanalens Grundavatar:** Använd kanalens standard-avatar (man med hörlurar, mörk hoodie) för igenkänning, men **generera alltid en ny pose, nytt uttryck, nya props och ny färgton/ljussättning per avsnitt** — aldrig copy-paste av exakt samma foto. Endast ett par hörlurar på öronen (aldrig dubbla hörlurar runt halsen).
  - **Tydlig resultattext (aldrig vag eller kryptisk):** Använd konkreta, omedelbart begripliga ord och siffror (t.ex. `PDF → PODCAST / IN 60 SEC`, `ENGLISH TO / ANY LANGUAGE / IN 500 MS`) med en stark **neongrön/färgad highlight-pill** bakom vinnarordet/siffran. Inga kryptiska förkortningar (`EN`, `ANY VOICE`).
  - **Pil-regel vid radbrytning (TVINGANDE):** En pil (`→`) får **aldrig** stå ensam i slutet av en rad vid radbrytning. Om måltermen hamnar på nästa rad ska pilen ersättas med ett förbindelseord (t.ex. `TO`). Pilar används enbart när de pekar direkt på nästa ord på samma linje.
  - **Säker innermarginal & noll överlapp:** All text i UI-kort och ramar måste ha minst **16 px fri luft** till närmaste kantlinje, och text/vågformer/grafik får aldrig överlappa varandra. Håll nedre högra hörnet fritt för YouTubes tidsstämpel.
  - **200 ms-sidofältstest:** Varje thumbnail måste vara omedelbart läsbar även nedskalad till `168×94 px` (YouTube Suggested Sidebar).
- **Title Length Limit:** Strict limit `< 60 characters` for primary mobile CTR title
- **Target Video Duration:** 3:30 to 6:00+ minutes for technical tutorials (combining technical rigor with zero fluff)
- **Weekly Cadence:** 3 packages/week (Monday, Wednesday, Friday)
- **Target Long-form RPM:** $18.00 – $35.00

### 9:16 Shorts Master Guidelines (Strict Channel Standard — Uppdaterad efter Steg 2):
1. **Längd & Format (30–60 sekunder, "Lär dig på under en minut"):**
   - Shorts ska vara **30–60 sekunder** långa och fungera som en komplett, snabb *"Lär dig det här på under en minut"*-lektion med tydlig länk/pekning vidare till den djupare långvideon.
   - **Visuell motor (Fejkad äkta skärminspelning):** Rendera via Playwright/HTML/CSS (eller Remotion) med flytande fönster, rörlig muspekare, klick-ripple, skrivande kod tecken för tecken, live-terminal och subtil royaltyfri bakgrundsmusik under rösten.
2. **0–4 sekunders Live Result Proof ("Show, Don't Just Tell" — TVINGANDE):**
   - `Andrew` (`en-US-AndrewMultilingualNeural`) är alltid kanalens basröst, **men** inom de **första 0–4 sekunderna** (plus/minus 1–2s beroende på innehåll) måste tittaren direkt **höra eller se slutprodukten hända live** i själva öppningen — inte bara höra Andrew prata *om* den:
     - *Podcast-avsnitt:* Andrew inleder, och en **andra röst (t.ex. `Ava`)** tar direkt över nästa fras medan spelaren på skärmen lyser upp `GUEST` live.
     - *Översättningsavsnitt:* Andrew börjar på engelska och rösten/grafiken slår direkt om till målspråket (t.ex. spanska/japanska).
     - *Ljudeffekt-/spelavsnitt:* Ljudeffekten smäller direkt i öppningen.
3. **Högkontrast-rubrik & Ord-synkade Undertexter i säker mobilzon:**
   - Fast, högkontrast badge i övre säkra zonen (med exakt längdangivelse, t.ex. `LEARN IN 42 SEC`) och dynamiska ord-för-ord-undertexter i nedre mittzonen (`margin` ≥ 10px mellan ord så förstorat aktivt ord aldrig nuddar nästa ord).
4. **Sömlös loop & Exakt CTA (Like & Subscribe + Direktlänk):**
   - Skriptet designas så att sista meningen grammatiskt och rytmiskt flyter tillbaka till första meningen (driver APV > 100%).
   - **Obligatorisk CTA (gäller både Shorts och Long):** Varje video måste innehålla en tydlig uppmaning till **Like & Subscribe** samt exakt hänvisning till **var** den klickbara länken till just det här avsnittets GitHub-repo ligger (*"in the pinned comment or video description below"* – aldrig bara "sök på GitHub").
4. **Funnel-koppling till Långvideon:**
   - Slutsekunderna har en tydlig visuell och auditiv hänvisning till kanalen och källkoden (*"Watch the full step-by-step breakdown & grab the GitHub code on our channel"*).
5. **Shorts-längd & Musik:** Strikt mellan 15 och 20 sekunder för maximal retention. Inga kommersiella musikspår (100% Creator Pool).
6. **Dedikerad Shorts-metadata:**
   - Egen slagkraftig titel med `#shorts #ai`.
   - Egen kort beskrivning anpassad för mobilflödet med funnel-länk och partnerlänk.
   - Egen kort fäst kommentar.

### 16:9 Långvideo Master Guidelines (Strict Channel Standard — Uppdaterad efter Steg 3):
1. **Omedelbar Röst från `0.00s` & Mjuk Thumbnail-Transition (0.0 – 2.2s):**
   - **Aldrig död tystnad i början:** Berättarrösten (`Andrew`) **måste** börja tala direkt från `0.00s` medan den skarpa 1080p-thumbnailen visas (`0.00s–1.35s` med subtil zoom) och därefter gör en mjuk övertoning (`1.35s–2.20s` crossfade) in till Scen 1.
2. **Audio-Visual Speaker-Sync (TVINGANDE — `ERROR` vid osynk):**
   - **Tal måste alltid synka med det visuella.** Grafiken ska följa speakern steg för steg och byta vy/kort/fokus vid varje nytt tankeskifte i manuset (max ~8–12 sekunder per oförändrad vy). Det är förbjudet att låta en statisk eller gammal grafik ligga kvar medan rösten pratar vidare om nya argument. Om tal och bild inte synkar ska granskande agent rapportera **`ERROR`**. Enda undantaget är när en video uttryckligen demonstrerar hur ett fel uppstår.
3. **Speaker mot Resultat i Öppningen (< 5s):**
   - Direkt efter öppningsmeningen visar och spelar videon upp slutprodukten live (t.ex. `Andrew` växlar till gäst-rösten `Ava` med pulserande spelare).
3. **Arkitektur-teaser inom 15 sekunder:**
   - Visa snabbt terminalen, systemöversikten eller koden så att tittaren ser exakt vad de kommer att behärska vid videons slut.
4. **Visuell dynamik och tidsstyrd highlighting (Synkroniserad blickledare):**
   - När berättarrösten nämner en specifik kodrad eller ett kodblock (t.ex. *"Look at lines seven through twelve"*), ska hela det aktuella blocket ramas in som **en sammanhållen ram** (inte separata staplade boxar per rad) med **symmetrisk och generös luft** (minst 10–12 px ovanför högsta versal/ascender och lika mycket under lägsta descender — text får aldrig snudda ramen).
   - **Levande glöd & puls (endast på aktiv sektion):** Aktiv fokusram och vektorpil ska ha en **mjuk, lugn andas-liknande neon-glöd** (cykel `>= 2.0s`, mjuk amplitud `0.55–0.95`, aldrig hård/snabb blinkning) som flyttar vidare när berättarrösten byter fokus.
   - **Stilla & nedtonade bakgrundsboxar:** I scener med flera kort/boxar får **endast** den box som talaren pratar om just nu ha ljus-/färgförstärkning och glöd. Inaktiva bakgrundsboxar måste vara **helt stilla, nedtonade (muted)** med minst `2px` mörk kantlinje (utan stark accentfärg) och renderas via förlustfri mellankodning (`qp 0`) + `lanczos`-skalning vid zoom, så att bakgrundsboxar aldrig blinkar, flimrar eller konkurrerar om uppmärksamheten.
   - **Sektions-zoom (Zoom In -> Håll stilla -> Zoom Out):** När berättarrösten börjar prata om en specifik kodsektion eller arkitekturbox zoomar kameran mjukt in (`~0.65s` ease-in till `1.05x`), **håller kameran helt stilla** under hela förklaringen (ingen kontinuerlig gungande in/ut-rörelse!) och zoomar mjukt tillbaka till `1.00x` (`~0.65s` ease-out) när sektionen är färdigpratad.
   - **Badge-marginaler:** Alla pill-badges och etiketter måste beräkna bredd/höjd dynamiskt från textens bounding box med generös padding så att text aldrig klipps eller snuddar ramar.
5. **Mjuka övergångar mellan alla scener:**
   - 0.4–0.5 sekunders mjuk crossfade/dissolve mellan varje scen. Inga abrupta bildklipp.
6. **Organiska muntliga hänvisningar (Oral CTA):**
   - Hänvisning till affiliate-verktyg och källkod vid delsegrar.
   - Tydlig, organisk uppmaning att gilla och prenumerera (*Like & Subscribe*) under sista scenen och outrot.
   - Hänvisning till ElevenLabs gratis provperiod via partnerlänken i beskrivningen och fästa kommentaren.
7. **Spellängd och pedagogisk stringens:**
   - Minst 4:00 minuter. Innehållet får ta den tid som krävs för maximal pedagogisk tydlighet (t.ex. 6–10+ minuter). Ingen artificiell komprimering.
8. **Compliance & Kvalitetskontroll (YouTube 2026):**
   - Anti-Slop: All kod körs och verifieras i sandboxen.
   - Kategori `28` (Science & Technology), `altered_content: false`.
   - Fullständiga FTC-disclaimers i beskrivning och fastnålad kommentar.
   - Obligatorisk granskning av Informations- och Kvalitetskontrollanten innan uppladdning till kontrollpanelen.

## Workflow Checklist
- [ ] Step 1: Environment & Dependency Verification (`edge-tts`, `ffmpeg`, `pillow`, `matplotlib`)
- [ ] Step 2: Topic Scouting & Sandbox Code Verification (`demos/`)
- [ ] Step 3: Script & Metadata Generation (Long-form scenes with dynamic visuals + Short script with seamless loop and result-first hook)
- [ ] Step 4: Neural Audio Synthesis (`edge-tts` with `en-US-AndrewMultilingualNeural`)
- [ ] Step 5: Visual Asset Generation (High-contrast 9:16 mobile badges, 1080p slide diagrams, code syntax cards, 1280x720 Long thumbnail + 1080x1920 Short thumbnail)
- [ ] Step 6: Video Assembly & Rendering via FFmpeg (1080p MP4 and 9:16 Short MP4)
- [ ] Step 7: Local Verification & User Approval in Chat
- [ ] Step 8: Overseer Dashboard Update (`docs/dashboard_state.json` & `docs/index.html`) upon approval — **samtliga 8 fält** (Långvideo titel, affiliatelänk, beskrivning, fäst kommentar, taggar OCH Shorts titel, beskrivning, fäst kommentar, taggar) samt **både Long-thumbnail (16:9) och Short-thumbnail (9:16)** måste synkas via `scripts/auto_deploy_package.py`, och den producerade pitchen (`PITCH #<id>`) **tas automatiskt bort** ur pitch-kön och ersätts med en ny pitch så att alltid 3 kommande pitchar visas.

## Script Usage

### Producing a Complete Video Package:
```bash
python .agents/skills/building-youtube-packages/scripts/produce_package.py --package-id 003 --output docs/assets/
```
