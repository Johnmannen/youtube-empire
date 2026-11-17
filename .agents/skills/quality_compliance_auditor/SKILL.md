---
name: quality-compliance-auditor
description: Autonomous Quality & Compliance Auditor agent for YouTube video packages. Validates long-form 1080p video, 9:16 Shorts, audio sync, thumbnails, script flow, SEO metadata, and affiliate links against the Master Manifest and channel guidelines before deployment to the Overseer Dashboard.
---

# 🛡️ Quality & Compliance Auditor Skill

## Syfte & Roll
Denna skill ger agenten mandat och verktyg att agera som en **oberoende grindvakt (*Quality Gate*)** för alla YouTube-videopaket som produceras för kanalen *Agentic Stack B2B*. Inget paket får flyttas till produktionsstatus på kontrollpanelen förrän denna agent har kört en fullständig granskning och utfärdat status **GODKÄND (PASS)**.

---

## 1. Granskningsområden & Kriterier

### A. Långvideo (16:9, 1080p)
- [ ] **Thumbnail-Start (0.0 – 2.5s):** Videon inleds med den officiella miniatyrbilden i fullskärm.
- [ ] **Mjuk Övergång (2.5 – 3.0s):** En mjuk 0.5s crossfade/dissolve över till Scen 1 (inga hårda klipp).
- [ ] **Aggressiv Intro-Hook (0 – 15s):** Startar direkt i smärtpunkten/problemet utan långa hälsningsfraser eller logotyper.
- [ ] **Spellängd:** Minst 4:00 minuter (typiskt 6:00 – 10:00+ minuter). Innehållet får aldrig kapas artificiellt på bekostnad av pedagogiken.
- [ ] **Visuell Dynamik & Highlighting:** Kodrader och arkitekturboxar belyses/highlightas i takt med berättarrösten. När specifika rader nämns ska en synkroniserad blickledare (glödande fokusram eller pil) omedelbart leda tittarens fokus dit utan söktid.
- [ ] **Scenövergångar:** 0.4–0.5s mjuk övertoning (crossfade) mellan alla scener.
- [ ] **Muntliga CTAs:** Berättarrösten uppmanar organiskt till *Like & Subscribe*, hänvisar till källkoden på GitHub, och nämner gratis provperiod via partnerlänken.
- [ ] **Grafisk Kvalitet:** Noll opaka färgblock över text, noll trasiga `□`-tecken (rena vektorpilar och ASCII), noll hackig 5-sekunders zoompan.

### B. Kortvideo / Reel (9:16, 1080x1920)
- [ ] **Result-First Hook (0.0 – 2.0s):** Bildruta 1 visar eller spelar upp slutresultatet direkt för att bryta swipe-beteendet.
- [ ] **Sömlös Ljudloop:** Sista meningen avslutas så att den flyter grammatiskt och melodiskt rakt in i videons första mening.
- [ ] **Mobil Safe Zones:** All text, grafik och kod hålls inom säkra zoner (topp: y=180–430, botten: y=1620–1840) så att inget döljs bakom YouTubes ikoner eller titelfält.
- [ ] **Funnel-CTA:** Tydlig banner och tal som leder tittaren till 6-minutersvideon på kanalen.
- [ ] **Shorts-längd:** Strikt mellan 15 och 20 sekunder.

### C. Text, Metadata & Affiliate-verifiering
- [ ] **Titlar:** Säljande och klickvänliga titlar (< 60 tecken för mobil CTR). Separat titel för Short med `#shorts #ai`.
- [ ] **Beskrivningar:** Fullständiga beskrivningar för både lång- och kortvideo. De första 2 raderna sammanfattar värdet.
- [ ] **Affiliate-länkar:** Strikt kontroll mot masterregistret:
  - Ep #003: `https://try.elevenlabs.io/agentic-dubbing`
  - Ep #002: `https://try.elevenlabs.io/agentic-voice`
  - Ep #004: `https://try.elevenlabs.io/agentic-telephony`
  - Ep #005: `https://try.elevenlabs.io/agentic-reader`
  - Ep #006: `https://try.elevenlabs.io/agentic-translator`
  - Ep #007: `https://try.elevenlabs.io/agentic-sfx`
  - Ep #008: `https://try.elevenlabs.io/agentic-onboarding`
  - Ep #009: `https://try.elevenlabs.io/agentic-onboarding`
  - Ep #010: `https://try.elevenlabs.io/agentic-onboarding`
- [ ] **GitHub-länk:** Korrekt referens till `https://github.com/Johnmannen/Agentic-Stack-Library`.
- [ ] **Fäst Kommentar:** Separat anpassad kommentar för både lång- och kortvideo med korrekta länkar.
- [ ] **Tidsstämplar:** Korrekta kapitel från `00:00` i långvideons beskrivning.

---

## 2. Automatiserat Granskningsverktyg

Kör revisionsskriptet för att utföra maskinell analys av ett paket:
```bash
python .agents/skills/quality_compliance_auditor/scripts/audit_package.py --package-id 003 --dir docs/assets/review_003
```

Skriptet genererar automatiskt kontrollbilder från nyckelpunkter (thumbnail-start, övergångar, safe-zones) och skapar en sammanfattande granskningsrapport.


### Utökade Revisionskrav (Synkroniserade efter Episode #005-granskningen)
* **YouTube Upload Stream Hygiene (No `yuvj420p` / No `ICC Profile`):** Verifiera med `ffprobe` att både Long och Short har `pix_fmt=yuv420p` (`color_range=tv`, `color_space=bt709`) och **inte** innehåller `yuvj420p` (`color_range=pc`, `bt470bg`) eller `side_data_type=ICC Profile` (vilket orsakar YouTube-uppladdningsfel `2888402`).
* **Audio Tail / No Mid-Sentence Cutoff:** Kontrollera att sista `0.35s` av både långvideo och Short klingar ut i tystnad (`< -32 dB`) så att ingen mening någonsin klipps av.
* **Dynamic Highlight & Pointer Motion:** Verifiera via pixel-diff att kodrader och arkitekturstadier faktiskt rör sig / byter markering med pil och fokusram under scenen (inga frusna IDE-scener).
* **Dual-Format Thumbnails (Long 16:9 + Short 9:16), Konsekvent Rubrik & Pose-kontroll:** Verifiera att varje avsnitt har **både** en Long-form thumbnail (`thumb_<id>.png`, `1280×720`) **och** en separat Short-form thumbnail (`thumb_short_<id>.png`, `1080×1920`) i äkta vertikal 9:16-design där avataren i nedre delen **tittar/pekar uppåt mot rubriken** (aldrig en slarvigt beskuren 16:9-bild med avklippt hand/tumme i kanten eller blick åt sidan!). Verifiera att rubriken på thumbnail och i videons topp är **konsekvent mellan Long och Short** (t.ex. `ENGLISH TO ANY LANGUAGE`, aldrig begränsad till ett enda språk i Shorten), att Shorts-spelaren använder `poster="assets/thumb_short_<id>.png"`, samt att båda thumbnails visas och är nedladdningsbara på kontrollpanelen (`docs/index.html`).
* **Single Host Voice (`Andrew`) — Noll Fallback-röst (`ChristopherNeural` FÖRBJUDEN) & Statisk Thumbnail-Intro (`0.00s–2.00s`):** Verifiera att **100 % av speakerrösten är `Andrew` (`en-US-AndrewMultilingualNeural`)** och att inga segment någonsin faller tillbaka till `ChristopherNeural` eller annan standardröst vid TTS-retry (andra röster får endast förekomma på det specifika demo-segment där en funktion demonstreras, t.ex. spansk kvinnlig tolkröst). Verifiera även via bildrutediff (`0.00s` vs `1.20s`) att thumbnail-introt i långvideon är **100 % stilla (`mean diff == 0.0`, ingen inzoomning eller tillbakahopp!)** innan den mjuka övertoningen till Scen 1.
* **Thumbnail Visual Uniqueness & 2026 Poster Standard:** Verifiera att varje avsnitts thumbnail skiljer sig visuellt från föregående avsnitt (`mean diff >= 12.0`), saknar textklippning och överlapp mellan text/grafik, har minst `16 px` innermarginal i UI-kort, följer pil-regeln vid radbrytning (aldrig ensam pil i radslut utan förbindelseord som `TO`), samt inte använder copy-paste av exakt samma avatar-pose från tidigare avsnitt.
* **Intra-Scene Glow & Zoom Motion:** Verifiera att det faktiskt sker visuell rörelse *inom* aktiva highlight-block (lugn pulserande glöd på aktiv ram medan kameran efter mjuk inzoomning håller stilla, utan gungande zoom) genom att jämföra två bildrutor med 0.60 sekunders mellanrum inuti samma fokusfas (`mean diff > 0.08`).
* **Active vs Inactive Box Contrast:** Verifiera att endast den aktiva sektionen/boxen i flerstegsscener är ljus- och färgförstärkt medan inaktiva bakgrundsboxar är tydligt nedtonade och stilla (aktivt kort har högre luminans/kontrast än inaktiva kort, så att inget bakgrundsflimmer drar bort blicken).
* **Unified Multi-Line Framing & Padding:** Flera sammanhängande kodrader ska ramas in av **en sammanhållen fokusram** (ej staplade rader) med generös, symmetrisk luft ovanför och under texten samt dynamisk badge-padding utan överlappning.
* **Dashboard Metadata Sync (Long + Shorts):** Verifiera att samtliga 8 fält i `docs/index.html` (`videoTitle`, `affiliateUrl`, `pinnedComment`, `videoTags`, `shortsTitle`, `shortsDescription`, `shortsPinnedComment`, `shortsTags`) exakt matchar `metadata_<id>.json` för aktuellt avsnitt — inga gamla texter från tidigare avsnitt får ligga kvar.
* **Active Pitch Queue Rotated:** Verifiera att producerat avsnitt (`PITCH #<id>`) automatiskt har tagits bort från de 3 aktiva pitch-korten i `docs/dashboard_state.json` och `docs/index.html`, och att kön automatiskt fyllts på med en ny pitch så att alltid 3 oproducerade pitchar visas.
* **Shorts 30–60s & 0–4s Live Result Proof:** Verifiera att Shorts-videon är **30–60 sekunder** lång, använder "fejkad skärminspelning" (rörlig kod, pekare, terminal) med **Andrew som basröst**, och att **de första 0–4 sekunderna** (plus/minus 1–2s) faktiskt demonstrerar slutprodukten live i ljud/bild (t.ex. live röstväxling till co-host, språkomslag eller ljudeffekt). Verifiera även minst 10px ordmellanrum i dynamiska undertexter.
* **Audio-Visual Speaker-Sync (`ERROR` vid osynk — TVINGANDE):** Verifiera att tal och bild alltid synkar genom hela videon (inklusive direkt röststart från `0.00s` över thumbnail-transition och att grafiken följer speakern med visuellt skifte vid varje nytt tankeskifte/argument — inga statiska 15–35s sjok där rösten går vidare utan bildskifte). Om tal och visuellt innehåll inte synkar ska agenten utfärda **`ERROR` / `FAILED`** (enda undantaget är om videon uttryckligen demonstrerar hur ett fel görs).
* **Like & Subscribe + Exakt GitHub-hänvisning & Komplett README-Synk (Live HTTP 200 & Innehållskontroll) + Outro-regel:** Verifiera att både Shorts och Long-form avslutas med **Like & Subscribe**, anger att den klickbara direktlänken till rätt GitHub-repo finns i **pinned comment** och **video description**, att den specifika avsnittsmappen (`https://github.com/Johnmannen/Agentic-Stack-Library/tree/main/<id>-...`) är pushad till GitHub och svarar med **HTTP `200 OK`**, att avsnittets `README.md` innehåller arkitekturöversikt, quickstart och rätt affiliatelänk, **SAMT att rot-`README.md` i `Johnmannen/Agentic-Stack-Library` (och i `youtube-empire`) listar avsnitt `#<id>` i tabellen och under Quickstart Commands**! Verifiera även att videon **inte** lovar ett specifikt ämne för "nästa video" (hänvisar istället till andra videor på kanalen), och i tal alltid säger **`business to business`** (aldrig förkortat `B2B`).
