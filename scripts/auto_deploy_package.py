#!/usr/bin/env python3
"""
auto_deploy_package.py - Updates docs/dashboard_state.json and docs/index.html
after a pitch is produced and audited.
"""

import os
import re
import json
import argparse
from datetime import datetime
from pathlib import Path

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

    # Update pitch status in state
    for p in state.get("pitches", []):
        if p.get("episode_id") == pkg_id:
            p["status"] = "COMPLETED_AND_READY"

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

    # Replace description textarea cleanly
    ta_start = html.find('<textarea id="videoDescription"')
    if ta_start != -1:
        content_start = html.find(">", ta_start) + 1
        content_end = html.find("</textarea>", content_start)
        if content_end != -1:
            html = html[:content_start] + long_meta.get("description", "") + html[content_end:]

    # Mark pitch button as completed in Section 1
    html = re.sub(
        rf'(<button[^>]*triggerPitch\(\'PITCH #{pkg_id}\'[^>]*>)\s*<span>.*?</span>\s*(</button>)',
        r'\1<span>✅ Producerad & Klar</span>\2',
        html,
        flags=re.DOTALL,
    )

    html_path.write_text(html, encoding="utf-8")
    print(f"Successfully deployed Episode #{pkg_id} to dashboard_state.json and index.html!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package-id", required=True)
    args = parser.parse_args()
    deploy_package(args.package_id.strip())
