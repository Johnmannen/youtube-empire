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
* **Audio Tail / No Mid-Sentence Cutoff:** Kontrollera att sista `0.35s` av både långvideo och Short klingar ut i tystnad (`< -32 dB`) så att ingen mening någonsin klipps av.
* **Dynamic Highlight & Pointer Motion:** Verifiera via pixel-diff att kodrader och arkitekturstadier faktiskt rör sig / byter markering med pil och fokusram under scenen (inga frusna IDE-scener).
* **Shorts Preview Poster:** Verifiera att `docs/assets/short_preview_<id>.png` existerar och är kopplad via `poster=` i `docs/index.html`.
* **Thumbnail Visual Uniqueness:** Verifiera att varje avsnitts thumbnail skiljer sig visuellt från föregående avsnitt (`mean diff >= 12.0`) och saknar textklippning.
