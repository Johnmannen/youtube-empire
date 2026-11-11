---
name: research-and-pitch-scouting
description: Autonomously scouts high-RPM tech and developer topics, evaluates search intent and market demand, validates monetization/recurring affiliate opportunities (20-40% via PartnerStack), and tests executable Python sandbox scripts before generating structured pitch dossiers for the Overseer Dashboard. Use when the user asks to research new video ideas, scout trending tech topics, evaluate B2B/SaaS monetization viability, or update channel pitch proposals. Do not use for rendering MP4 videos or synthesizing audio.
---

# Dedicated Research & Pitch Scouting Skill

## Purpose
This skill serves as the dedicated intelligence and topic-scouting engine for autonomous YouTube channels. It isolates the entire research, demand analysis, affiliate evaluation, and sandbox code verification from the video rendering pipeline.

## Core Scouting Pillars

### 1. High-Value Tech Intent & RPM Filtering
- **Target Category:** Software engineering, AI orchestration, developer tools, and workflow automation.
- **Target RPM:** $18.00 – $35.00 (High-intent B2B/Developer audience).
- **Search Intent Analysis:** We identify acute bottlenecks that engineers actively search for (e.g. eliminating multi-second latency, avoiding expensive API bills, automating video localization).

### 2. SaaS Affiliate & Monetization Due Diligence
- **Primary Source:** Verified partner programs via PartnerStack or direct SaaS affiliate platforms.
- **Criteria:** 20% to 40% recurring lifetime or first-year commissions.
- **Requirement:** Must offer a low-friction entry point (e.g., generous free tier or free trial) so viewers can reproduce the video's tutorial immediately without upfront investment.

### 3. Strict Anti-Slop Sandbox Protocol
- **MANDATORY RULE:** No pitch may be promoted to the Overseer Dashboard without an executable, working proof-of-concept Python script tested in the local sandbox (`demos/`).
- If an API or library is broken, undocumented, or throws unresolvable errors during sandbox testing, the topic is rejected immediately.

### 4. Dossier Packaging & Packaging Output
For each approved topic, this skill generates a complete Pitch Dossier:
1. **Primary Title:** Strictly `< 60 characters` for mobile devices.
2. **Alternative A/B Title:** Focus on high CTR / pain-point relief.
3. **Thumbnail Concept:** Follows the Hybrid 1+3 standard (Left: Red pain point, Right: Green 3-node architecture, Bottom: Live status badge, Max 2-4 words).
4. **Scene Outline:** 5-to-7 scenes following the Scene Director format.
5. **Spoken CTA Plan:** Outro script including verbal affiliate mention, GitHub repository link, Like & Subscribe, and End Screen next-video bridge.

## File Outputs
- Updates `docs/dashboard_state.json` under the `pitches` key.
- Updates pitch cards and modal dossiers in `docs/index.html`.
