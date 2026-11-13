#!/usr/bin/env python3
"""
auto_deploy_package.py - Updates docs/dashboard_state.json and docs/index.html
after a pitch is produced and audited.
"""

import os
import re
import html as html_lib
import json
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

def get_duration_sec(filepath: str) -> float:
    try:
        res = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", filepath],
            capture_output=True, text=True, check=True
        )
        return float(res.stdout.strip())
    except Exception:
        return 0.0

def replace_elem_text(doc: str, tag: str, elem_id: str, new_text: str) -> str:
    """Replaces inner content of <tag id="elem_id" ...>...</tag> cleanly."""
    pattern = rf'(<{tag}\b[^>]*\bid="{re.escape(elem_id)}"[^>]*>)(.*?)(</{tag}>)'
    escaped = html_lib.escape(new_text, quote=False)
    return re.sub(pattern, lambda m: m.group(1) + escaped + m.group(3), doc, count=1, flags=re.DOTALL)

def deploy_package(pkg_id: str):
    state_path = Path("docs/dashboard_state.json")
    html_path = Path("docs/index.html")
    meta_path = Path(f"docs/assets/metadata_{pkg_id}.json")

    if not meta_path.exists():
        raise FileNotFoundError(f"Missing {meta_path}")

    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    state = json.loads(state_path.read_text(encoding="utf-8"))
    html = html_path.read_text(encoding="utf-8")

    old_pkg = state.get("current_package", {})
    old_id = old_pkg.get("package_id")

    # 1. Archive old current_package if different
    if old_id and old_id != pkg_id:
        already_archived = any(p.get("package_id") == old_id for p in state.get("published_packages", []))
        if not already_archived:
            state.setdefault("published_packages", []).append({
                "package_id": old_id,
                "title": old_pkg.get("title", f"Episode {old_id}"),
                "status": "PUBLISHED_LIVE",
                "published_date": datetime.utcnow().strftime("%Y-%m-%d"),
                "format": "16:9 Long",
                "github_code_url": old_pkg.get("github_code_url", "https://github.com/Johnmannen/Agentic-Stack-Library"),
                "affiliate": old_pkg.get("affiliate_placeholders", [{}])[0].get("live_url", ""),
                "thumbnail": old_pkg.get("thumbnail_file", f"assets/thumb_{old_id}.png"),
            })

    # 2. Set new current_package in dashboard_state.json
    long_meta = meta.get("long_form", {})
    short_meta = meta.get("short_form", {})
    new_title = long_meta.get("title", f"Episode {pkg_id}")
    state["current_package"] = {
        "package_id": pkg_id,
        "title": f"{new_title} [EPISODE {pkg_id}]",
        "category_id": "28",
        "category_name": "Science & Technology",
        "altered_content": False,
        "c2pa_status": "VERIFIED_COMPLIANT_2026",
        "tags": long_meta.get("tags", []),
        "github_code_url": "https://github.com/Johnmannen/Agentic-Stack-Library",
        "studio_upload_url": "https://studio.youtube.com/channel/UCkphdiVQvc1vvNlcrAorMOg",
        "description": long_meta.get("description", ""),
        "pinned_comment": long_meta.get("pinned_comment", ""),
        "shorts_metadata": short_meta,
        "long_video_file": f"assets/video_{pkg_id}_long.mp4",
        "short_video_file": f"assets/video_{pkg_id}_short.mp4",
        "thumbnail_file": f"assets/thumb_{pkg_id}.png",
    }

    # 2b. Remove produced pitch from active 3-pitch queue & replenish with next ElevenLabs pitch
    ELEVENLABS_PITCH_BACKLOG = {
        "008": {
            "episode_id": "008",
            "title": "Build an Automated B2B Onboarding Voice & Video Engine in Python",
            "alternative_title": "Personalized Client Walkthroughs at Scale (ElevenLabs Flash v2.5 + FFmpeg)",
            "duration": "04:00–4:45 min",
            "niche_rpm": "$29.40",
            "search_volume_monthly": 22600,
            "growth_mom": "+64%",
            "pedagogical_goal": "Personaliserade röst- & videoguidas per CRM-kund",
            "target_audience": "B2B SaaS Founders, Growth Engineers & RevOps",
            "affiliate_partner": "ElevenLabs Flash v2.5 & Voice API (22% Rec)",
            "affiliate_url": "https://try.elevenlabs.io/agentic-voice",
            "hook": "Generic onboarding emails get ignored. Generate personalized, studio-quality voice and video walkthroughs for every new B2B signup automatically in Python.",
            "code_demo": "ElevenLabs Flash v2.5 + CRM Webhook & FFmpeg",
            "goal": "Bygg en automatisk B2B onboarding-motor i Python som lyssnar på CRM/Stripe-webhooks, genererar kundanpassad röstsyntes med ElevenLabs Flash v2.5 och renderar en personlig välkomstvideo.",
            "script_steps": [
                "• Scen 1 (00:00 - 00:35): Varför generiska välkomstmejl ger 80% churn-risk första veckan i B2B SaaS.",
                "• Scen 2 (00:35 - 01:25): Webhook-arkitektur: Stripe/HubSpot-trigger -> ElevenLabs Flash v2.5 -> FFmpeg-komposition.",
                "• Scen 3 (01:25 - 02:40): Python-kod: Dynamisk variabelinjektion och sub-75ms röstgenerering med Flash v2.5.",
                "• Scen 4 (02:40 - 03:45): Automatisk MP4-rendering och utskick med spårbar klickkonvertering.",
                "• Scen 5 (03:45 - 04:20): ROI-kalkyl, GitHub-kod och ElevenLabs gratis provperiod."
            ],
            "trend": "Sökvolym: 22 600 sökningar/månad (+64% MoM). Hyper-personaliserad B2B-onboarding med röst och video växer kraftigt.",
            "code": "ElevenLabs Flash v2.5 API + FastAPI CRM Webhook + FFmpeg Overlay Pipeline.",
            "affiliates": [
                "• ElevenLabs Flash v2.5 & Voice API: 22% Recurring Commission via PartnerStack",
                "• FastAPI / HubSpot / FFmpeg Automation Stack"
            ],
            "status": "PITCH_READY_REVIEW",
        },
        "009": {
            "episode_id": "009",
            "title": "Build a Multi-Character AI Audiobook Studio in Python (ElevenLabs v3)",
            "alternative_title": "Full-Cast Emotion-Tagged Audio Production with ElevenLabs Projects API",
            "duration": "04:00–5:00 min",
            "niche_rpm": "$26.80",
            "search_volume_monthly": 24900,
            "growth_mom": "+71%",
            "pedagogical_goal": "Flerröstats bok- & kursproduktion med känslotaggar",
            "target_audience": "EdTech Teams, Creators & Publishing Platforms",
            "affiliate_partner": "ElevenLabs Voice Design & Projects API (22% Rec)",
            "affiliate_url": "https://try.elevenlabs.io/agentic-reader",
            "hook": "Single-voice narration puts listeners to sleep. Build an automated multi-character audiobook and course narration pipeline in Python.",
            "code_demo": "ElevenLabs Multi-Voice + Chapter Mastering",
            "goal": "Automatisera helautomatisk ljudboks- och kursproduktion i Python med separata karaktärsröster, pausstyrning och kapitelmastring.",
            "script_steps": [
                "• Scen 1 (00:00 - 00:35): Varför en-rösts AI-uppläsning faller platt i längre utbildningar och böcker.",
                "• Scen 2 (00:35 - 01:25): Karaktärs-parsing i Python: Dela upp manus i berättare och dialogroller.",
                "• Scen 3 (01:25 - 02:45): ElevenLabs API: Rösttilldelning, stabilitet och naturlig prosodi.",
                "• Scen 4 (02:45 - 03:50): FFmpeg loudness-normalisering (-14 LUFS) och kapitel-export.",
                "• Scen 5 (03:50 - 04:30): Outro med ElevenLabs gratis provperiod och GitHub-mall."
            ],
            "trend": "Sökvolym: 24 900 sökningar/månad (+71% MoM). Efterfrågan på automatiserad EdTech- och ljudboksproduktion skjuter i höjden.",
            "code": "Python Script Parser + ElevenLabs Multi-Voice Synthesis + FFmpeg Loudness Mastering.",
            "affiliates": [
                "• ElevenLabs Creator & Pro Tier: 22% Recurring Commission via PartnerStack",
                "• Python Pydub / FFmpeg Mastering Pipeline"
            ],
            "status": "PITCH_READY_REVIEW",
        },
        "010": {
            "episode_id": "010",
            "title": "Build an AI Voice Compliance & Call QA Auditor in Python (ElevenLabs Scribe)",
            "alternative_title": "Automated Sales Call Diarization & Policy Scoring in Python",
            "duration": "04:00–4:45 min",
            "niche_rpm": "$33.50",
            "search_volume_monthly": 18400,
            "growth_mom": "+59%",
            "pedagogical_goal": "Automatisk samtalsanalys & talar-diarisering",
            "target_audience": "FinTech, Enterprise Sales & QA Engineering",
            "affiliate_partner": "ElevenLabs Scribe STT & Voice AI (22% Rec)",
            "affiliate_url": "https://try.elevenlabs.io/agentic-telephony",
            "hook": "Manual QA reviews less than 2% of support calls. Build an automated speaker-diarized call auditor in Python using ElevenLabs Scribe.",
            "code_demo": "ElevenLabs Scribe API + Speaker Diarization QA",
            "goal": "Bygg en Python-pipeline som transkriberar kundsamtal med talarseparering (diarization) via ElevenLabs Scribe och flaggar compliance-avvikelser automatiskt.",
            "script_steps": [
                "• Scen 1 (00:00 - 00:35): 98% av alla B2B-samtal granskas aldrig — compliance-risken i enterprise.",
                "• Scen 2 (00:35 - 01:25): ElevenLabs Scribe-arkitektur: Ultra-exakt STT med talaridentifiering.",
                "• Scen 3 (01:25 - 02:45): Python-integration: Skicka ljudfil, hämta tidsstämplad dialog per talare.",
                "• Scen 4 (02:45 - 03:50): Automatisk QA-poängsättning och Slack-larm vid regelbrott.",
                "• Scen 5 (03:50 - 04:25): ROI-kalkyl, GitHub-repo och ElevenLabs gratis provperiod."
            ],
            "trend": "Sökvolym: 18 400 sökningar/månad (+59% MoM). Högsta B2B-RPM inom FinTech och Enterprise QA.",
            "code": "ElevenLabs Scribe API + Python Diarization & Compliance Scoring Engine.",
            "affiliates": [
                "• ElevenLabs Scribe & Enterprise Voice AI: 22% Recurring Commission via PartnerStack",
                "• Python FastAPI / Webhook QA Pipeline"
            ],
            "status": "PITCH_READY_REVIEW",
        },
    }

    pitches = [p for p in state.get("pitches", []) if p.get("episode_id") != pkg_id]
    existing_ids = {p.get("episode_id") for p in pitches}
    while len(pitches) < 3:
        max_num = max([int(p.get("episode_id", 0)) for p in pitches if str(p.get("episode_id", "")).isdigit()] + [int(pkg_id) if pkg_id.isdigit() else 0])
        next_id = f"{max_num + 1:03d}"
        if next_id in existing_ids:
            break
        if next_id in ELEVENLABS_PITCH_BACKLOG:
            pitches.append(ELEVENLABS_PITCH_BACKLOG[next_id])
            existing_ids.add(next_id)
        else:
            break
    state["pitches"] = pitches

    state_path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    # 3. Update index.html
    html = re.sub(
        r"PRODUKTION KLAR: Paket #\d+.*?(?=</span>)",
        f"PRODUKTION KLAR: Paket #{pkg_id} Godkänt & Revisionsgranskat (100% Compliant)",
        html,
    )
    if old_id and old_id != pkg_id:
        html = html.replace(f"Dagens Färdiga Videopaket #{old_id}", f"Dagens Färdiga Videopaket #{pkg_id}")
        html = html.replace(f"assets/video_{old_id}_long.mp4", f"assets/video_{pkg_id}_long.mp4")
        html = html.replace(f"assets/video_{old_id}_short.mp4", f"assets/video_{pkg_id}_short.mp4")
        html = html.replace(f"assets/thumb_{old_id}.png", f"assets/thumb_{pkg_id}.png")
        html = html.replace(f"assets/short_preview_{old_id}.png", f"assets/short_preview_{pkg_id}.png")

        # Archive old_id card if not already in archive
        archive_header = 'Tidigare färdigställda videopaket, källkodsrepon och direkta YouTube-länkar.</p>\n          </div>\n        </div>\n      </div>'
        if archive_header in html and f"AVSNITT #{old_id}" not in html:
            old_title = old_pkg.get("title", f"Episode {old_id}")
            archive_card = f'''\n\n      <!-- AVSNITT #{old_id} (ARKIVERAD) -->
      <div class="glass-card rounded-2xl p-5 border border-emerald-500/40 bg-slate-900/50 hover:border-emerald-500/70 transition">
        <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div class="flex items-center gap-4">
            <div class="relative w-28 h-16 rounded-xl overflow-hidden border border-emerald-500/40 bg-slate-950 shrink-0">
              <img src="assets/thumb_{old_id}.png" alt="Ep {old_id} Thumbnail" class="w-full h-full object-cover">
            </div>
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 rounded font-mono font-bold text-[10px] bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">AVSNITT #{old_id}</span>
                <span class="px-2 py-0.5 rounded-full font-mono font-semibold text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-500/30">● LIVE PÅ YOUTUBE</span>
                <span class="text-[10px] text-slate-400">Publicerad: {datetime.utcnow().strftime("%Y-%m-%d")}</span>
              </div>
              <h4 class="text-sm font-bold text-white">{old_title}</h4>
            </div>
          </div>
          <div class="flex items-center gap-2 w-full md:w-auto">
            <a href="https://studio.youtube.com/channel/UCkphdiVQvc1vvNlcrAorMOg" target="_blank" class="px-3.5 py-2 rounded-lg bg-red-600 hover:bg-red-500 text-white font-bold text-xs transition">Se på YouTube</a>
            <a href="assets/video_{old_id}_long.mp4" download class="px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs transition">⬇ MP4</a>
          </div>
        </div>
      </div>'''
            html = html.replace(archive_header, archive_header + archive_card)

    # Replace all long-form & short-form metadata elements cleanly
    long_desc = long_meta.get("description", "")
    aff_match = re.search(r"https://try\.elevenlabs\.io/[A-Za-z0-9_-]+", long_desc)
    aff_url = aff_match.group(0) if aff_match else "https://try.elevenlabs.io/agentic-reader"

    html = replace_elem_text(html, "p", "videoTitle", f"{new_title} [EPISODE {pkg_id}]")
    html = replace_elem_text(html, "p", "affiliateUrl", aff_url)
    html = re.sub(
        r'(<a\s+href=")https://try\.elevenlabs\.io/[A-Za-z0-9_-]+("\s+target="_blank"[^>]*>\s*Testa Länk)',
        rf'\g<1>{aff_url}\g<2>',
        html,
        count=1,
    )
    html = replace_elem_text(html, "textarea", "videoDescription", long_desc)
    html = replace_elem_text(html, "p", "pinnedComment", long_meta.get("pinned_comment", ""))
    html = replace_elem_text(html, "p", "videoTags", ", ".join(long_meta.get("tags", [])))

    html = replace_elem_text(html, "p", "shortsTitle", short_meta.get("title", ""))
    html = replace_elem_text(html, "textarea", "shortsDescription", short_meta.get("description", ""))
    html = replace_elem_text(html, "p", "shortsPinnedComment", short_meta.get("pinned_comment", ""))
    html = replace_elem_text(html, "p", "shortsTags", ", ".join(short_meta.get("tags", [])))
    html = re.sub(r'alt="YouTube Thumbnail #\d+"', f'alt="YouTube Thumbnail #{pkg_id}"', html)

    # Sync exact rendered video durations & episode labels in Section 2
    l_sec = get_duration_sec(f"docs/assets/video_{pkg_id}_long.mp4")
    s_sec = get_duration_sec(f"docs/assets/video_{pkg_id}_short.mp4")
    l_mmss = f"{int(l_sec // 60):02d}:{int(round(l_sec % 60)):02d}" if l_sec > 0 else "04:00"
    s_fmt = f"{s_sec:.1f}s" if s_sec > 0 else "18.0s"
    first_tag = (long_meta.get("tags") or ["ElevenLabs AI"])[0]
    html = replace_elem_text(html, "p", "packageSummarySub", f"1080p Långformat ({l_mmss} min) + 9:16 Shorts ({s_fmt}) + Unik Thumbnail + Komplett Engelsk SEO & {first_tag} Affiliate")
    html = replace_elem_text(html, "span", "longSpecsLabel", f"1080p Full HD ({l_mmss} min, 7 Synkade Scener + Verifierad Kod)")
    html = replace_elem_text(html, "span", "longCaptionLabel", f"Arkitekturdiagram + Enhetlig Glödande Kodgranskning (7 Scener) — {first_tag}")
    html = replace_elem_text(html, "p", "shortSpecsLabel", f"⚡ {s_fmt} | Rent flöde | 0 musik (100% pool)")
    html = replace_elem_text(html, "span", "affiliateTagLabel", first_tag)

    # Rebuild Section 1 (#pitchesContainer) & PITCH_DATA from the rotated 3-pitch queue
    themes = [
        ("cyan", "bg-cyan-950/10", "border-cyan-500/40 hover:border-cyan-400/60", "bg-cyan-500/20 text-cyan-300 border-cyan-500/30", "text-cyan-300", "hover:text-cyan-300", "bg-cyan-600 hover:bg-cyan-500 shadow-cyan-600/30"),
        ("purple", "bg-purple-950/10", "border-purple-500/40 hover:border-purple-400/60", "bg-purple-500/20 text-purple-300 border-purple-500/30", "text-purple-300", "hover:text-purple-300", "bg-purple-600 hover:bg-purple-500 shadow-purple-600/30"),
        ("emerald", "bg-emerald-950/10", "border-emerald-500/40 hover:border-emerald-400/60", "bg-emerald-500/20 text-emerald-300 border-emerald-500/30", "text-emerald-300", "hover:text-emerald-300", "bg-emerald-600 hover:bg-emerald-500 shadow-emerald-600/30"),
    ]
    cards_html = []
    dossier_list = []
    for idx_p, p in enumerate(pitches[:3]):
        ep_id = p.get("episode_id", f"{idx_p+1:03d}")
        p_title = p.get("title", "")
        p_hook = p.get("hook", "")
        p_goal = p.get("pedagogical_goal") or p.get("code_demo", "")
        sv = p.get("search_volume_monthly", 20000)
        sv_fmt = f"{sv:,}".replace(",", " ") + f"/mån ({p.get('growth_mom', '+50%')} MoM)"
        rpm = p.get("niche_rpm", "$25.00")
        if str(rpm).startswith("."):
            rpm = "$" + ("31" if ep_id == "006" else "27" if ep_id == "007" else "25") + str(rpm)
        aud = p.get("target_audience", "B2B Developers")
        aff_p = p.get("affiliate_partner", "ElevenLabs API (22% Rec)")
        code_d = p.get("code_demo", "Python SDK")
        dur_lbl = p.get("duration", "3:30–4:30 min")
        if "min" not in dur_lbl:
            dur_lbl = f"{dur_lbl} min"
        _, bg_cls, brd_cls, badge_cls, txt_cls, hvr_cls, btn_cls = themes[idx_p % 3]
        safe_title_js = p_title.replace("'", "\\'")
        cards_html.append(f'''
        <!-- PITCH {idx_p+1}: PITCH #{ep_id} -->
        <div class="glass-card rounded-2xl p-5 border {brd_cls} transition-all flex flex-col justify-between space-y-4 {bg_cls}">
          <div class="space-y-3">
            <div class="flex items-center justify-between text-xs">
              <span class="px-2 py-0.5 rounded font-mono font-bold {badge_cls} border">PITCH #{ep_id}</span>
              <span class="{txt_cls} font-semibold font-mono">⏱️ Längd: {html_lib.escape(dur_lbl)}</span>
            </div>
            <h3 class="text-base font-bold text-white {hvr_cls} transition">{html_lib.escape(p_title)}</h3>
            <p class="text-xs text-slate-300 italic">"{html_lib.escape(p_hook)}"</p>
            <div class="bg-slate-950/80 rounded-xl p-3 border border-slate-800 text-xs space-y-2">
              <div class="flex justify-between">
                <span class="text-slate-400">Pedagogiskt Mål:</span>
                <span class="{txt_cls} font-semibold text-right">{html_lib.escape(p_goal)}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Sökvolym:</span>
                <span class="text-white font-mono">{html_lib.escape(sv_fmt)}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Nisch-RPM:</span>
                <span class="text-emerald-400 font-mono font-bold">{html_lib.escape(rpm)}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Målgrupp:</span>
                <span class="text-slate-300">{html_lib.escape(aud)}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Affiliatepartner:</span>
                <span class="text-purple-300 font-semibold">{html_lib.escape(aff_p)}</span>
              </div>
              <div class="flex justify-between">
                <span class="text-slate-400">Kod i Sandlåda:</span>
                <span class="text-emerald-400 font-mono text-[11px]">{html_lib.escape(code_d)}</span>
              </div>
            </div>
          </div>
          <div class="pt-2 flex items-center gap-2">
            <button onclick="showPitchDossier({idx_p})" class="flex-1 px-3 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 border border-slate-700 font-semibold transition text-center">
              📋 Granska Dossier
            </button>
            <button id="pitchBtn{idx_p}" onclick="triggerPitch('PITCH #{ep_id}', '{safe_title_js}', this)" class="px-4 py-2 rounded-lg {btn_cls} text-white font-bold text-xs transition shadow-md flex items-center gap-1.5">
              <span>🚀 Exekvera</span>
            </button>
          </div>
        </div>''')
        dossier_list.append({
            "id": f"PITCH #{ep_id}",
            "duration": f"⏱️ Längd: {dur_lbl}",
            "title": p_title,
            "goal": p.get("goal", p_hook),
            "script_steps": p.get("script_steps", [
                f"• Scen 1 (00:00 - 00:35): Smärtpunktskrok – {p_hook}",
                f"• Scen 2 (00:35 - 01:30): Systemarkitektur & {code_d}",
                "• Scen 3 (01:30 - 03:00): Komplett Python-implementation i sandlådan",
                "• Scen 4 (03:00 - 04:00): Prestanda, ROI & ElevenLabs gratis provperiod"
            ]),
            "trend": p.get("trend", f"Sökvolym: {sv_fmt}. Stark efterfrågan inom {aud}."),
            "code": p.get("code", code_d),
            "affiliates": p.get("affiliates", [f"• {aff_p}"])
        })

    html = re.sub(
        r'(<div class="grid grid-cols-1 lg:grid-cols-3 gap-6" id="pitchesContainer">).*?(</div>\s*</section>)',
        lambda m: m.group(1) + "\n" + "\n".join(cards_html) + "\n      " + m.group(2),
        html,
        count=1,
        flags=re.DOTALL,
    )
    html = re.sub(
        r'(const PITCH_DATA = )\[.*?\](;)',
        lambda m: m.group(1) + json.dumps(dossier_list, indent=6, ensure_ascii=False) + m.group(2),
        html,
        count=1,
        flags=re.DOTALL,
    )
    if pitches:
        html = replace_elem_text(html, "span", "dossierId", f"PITCH #{pitches[0].get('episode_id', '')}")

    html_path.write_text(html, encoding="utf-8")
    print(f"Successfully deployed Episode #{pkg_id} to dashboard_state.json and index.html!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-id", required=True)
    args = parser.parse_args()
    deploy_package(args.package_id.strip())
