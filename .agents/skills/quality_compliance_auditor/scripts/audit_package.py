#!/usr/bin/env python3
"""
audit_package.py - Automated Quality & Compliance Audit Tool
Validates long video, short video, thumbnail, and metadata against the Master Manifest.
"""

import os
import sys
import json
import argparse
import subprocess
import re

AFFILIATE_REGISTRY = {
    "001": "https://try.elevenlabs.io/agentic-voice",
    "002": "https://try.elevenlabs.io/agentic-voice",
    "003": "https://try.elevenlabs.io/agentic-dubbing",
    "004": "https://try.elevenlabs.io/agentic-telephony",
    "005": "https://try.elevenlabs.io/agentic-reader"
}

GITHUB_URL = "https://github.com/Johnmannen/Agentic-Stack-Library"

def get_media_info(filepath):
    if not os.path.exists(filepath):
        return None
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration:stream=width,height,r_frame_rate,codec_name",
        "-of", "json", filepath
    ]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return json.loads(res.stdout)
    except Exception as e:
        print(f"Error probing {filepath}: {e}")
        return None

def extract_frame(video_path, time_str, out_png):
    cmd = ["ffmpeg", "-y", "-ss", time_str, "-i", video_path, "-vframes", "1", out_png]
    try:
        subprocess.run(cmd, capture_output=True, check=True)
        return os.path.exists(out_png)
    except Exception:
        return False

def audit_package(pkg_id, base_dir):
    print("=" * 70)
    print(f"RUNNING QUALITY & COMPLIANCE AUDIT: PACKAGE #{pkg_id}")
    print(f"Target directory: {base_dir}")
    print("=" * 70)

    report = {
        "package_id": pkg_id,
        "base_dir": base_dir,
        "checks": [],
        "passed_all": True
    }

    def add_check(category, name, passed, details):
        report["checks"].append({
            "category": category,
            "name": name,
            "passed": passed,
            "details": details
        })
        if not passed:
            report["passed_all"] = False
        status_symbol = "[PASS]" if passed else "[FAIL]"
        print(f"{status_symbol} {category} -> {name}: {details}")

    # 1. LONG VIDEO CHECKS
    long_candidates = [
        os.path.join(base_dir, f"video_{pkg_id}_long_master.mp4"),
        os.path.join(base_dir, f"video_{pkg_id}_long_remaster.mp4"),
        os.path.join(base_dir, f"video_{pkg_id}_long.mp4")
    ]
    long_file = next((f for f in long_candidates if os.path.exists(f)), None)

    if not long_file:
        add_check("Long Video", "File Existence", False, "Long video MP4 file not found.")
    else:
        info = get_media_info(long_file)
        if not info:
            add_check("Long Video", "Probing", False, "Failed to read media format.")
        else:
            duration = float(info.get("format", {}).get("duration", 0))
            streams = info.get("streams", [])
            v_stream = next((s for s in streams if "width" in s and s["width"] is not None), {})
            width = v_stream.get("width", 0)
            height = v_stream.get("height", 0)

            # Check duration >= 4 minutes (240s)
            add_check("Long Video", "Duration Target", duration >= 240, f"Duration: {duration/60:.2f} mins (Target: >= 4.0 mins)")

            # Check resolution 1920x1080
            add_check("Long Video", "1080p Standard", width == 1920 and height == 1080, f"Resolution: {width}x{height}")

            # Check frames for thumbnail intro and transition
            audit_dir = os.path.join(base_dir, "audit_frames")
            os.makedirs(audit_dir, exist_ok=True)
            
            f_thumb = os.path.join(audit_dir, "frame_01_thumbnail.png")
            f_trans = os.path.join(audit_dir, "frame_02_transition.png")
            f_scene1 = os.path.join(audit_dir, "frame_03_scene1.png")

            ok_thumb = extract_frame(long_file, "00:00:01", f_thumb)
            ok_trans = extract_frame(long_file, "00:00:02.8", f_trans)
            ok_scene = extract_frame(long_file, "00:00:05", f_scene1)

            add_check("Long Video", "Thumbnail Intro Frame", ok_thumb, f"Extracted: {f_thumb}")
            add_check("Long Video", "Scene Transition Frame", ok_trans, f"Extracted: {f_trans}")

    # 2. SHORT VIDEO CHECKS
    short_candidates = [
        os.path.join(base_dir, f"video_{pkg_id}_short_master.mp4"),
        os.path.join(base_dir, f"video_{pkg_id}_short_remaster.mp4"),
        os.path.join(base_dir, f"video_{pkg_id}_short.mp4")
    ]
    short_file = next((f for f in short_candidates if os.path.exists(f)), None)

    if not short_file:
        add_check("Short Video", "File Existence", False, "Short video MP4 file not found.")
    else:
        s_info = get_media_info(short_file)
        if s_info:
            s_dur = float(s_info.get("format", {}).get("duration", 0))
            s_streams = s_info.get("streams", [])
            s_v_stream = next((s for s in s_streams if "width" in s and s["width"] is not None), {})
            s_w = s_v_stream.get("width", 0)
            s_h = s_v_stream.get("height", 0)

            add_check("Short Video", "Duration Target (15-20s)", 14.5 <= s_dur <= 21.0, f"Duration: {s_dur:.2f}s")
            add_check("Short Video", "9:16 Vertical Standard", s_w == 1080 and s_h == 1920, f"Resolution: {s_w}x{s_h}")

            audit_dir = os.path.join(base_dir, "audit_frames")
            f_short = os.path.join(audit_dir, "frame_short_01.png")
            extract_frame(short_file, "00:00:03", f_short)
            add_check("Short Video", "Safe Zone Frame", os.path.exists(f_short), f"Extracted: {f_short}")

    # 3. METADATA & AFFILIATE AUDIT
    expected_affiliate = AFFILIATE_REGISTRY.get(pkg_id)
    metadata_candidates = [
        os.path.join(base_dir, f"metadata_{pkg_id}.json"),
        os.path.join("docs", "dashboard_state.json")
    ]
    meta_found = False
    for mf in metadata_candidates:
        if os.path.exists(mf):
            try:
                with open(mf, "r", encoding="utf-8") as f:
                    content = f.read()
                meta_found = True
                
                # Check affiliate link
                has_aff = expected_affiliate in content if expected_affiliate else True
                add_check("Metadata", "Verified Affiliate URL", has_aff, f"Looking for: {expected_affiliate}")

                # Check GitHub repo
                has_git = GITHUB_URL in content
                add_check("Metadata", "GitHub Blueprint URL", has_git, f"Looking for: {GITHUB_URL}")

                # Check Timestamps 00:00
                has_ts = "00:00" in content or "0:00" in content
                add_check("Metadata", "Timestamps Standard", has_ts, "Checks chapter timestamps starting at 00:00")
                break
            except Exception as e:
                print(f"Error reading metadata {mf}: {e}")

    if not meta_found:
        add_check("Metadata", "Metadata File", False, "No metadata file found to audit.")

    # 4. GENERATE AUDIT REPORT FILE
    report_file = os.path.join(base_dir, f"AUDIT_REPORT_{pkg_id}.md")
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# Quality & Compliance Audit Report: Package #{pkg_id}\n\n")
        f.write(f"**Overall Status:** {'PASS' if report['passed_all'] else 'FAIL'}\n\n")
        f.write("| Category | Check Name | Status | Details |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for c in report["checks"]:
            st = "PASS" if c["passed"] else "FAIL"
            f.write(f"| {c['category']} | {c['name']} | **{st}** | {c['details']} |\n")

    print("\n" + "=" * 70)
    print(f"OVERALL AUDIT VERDICT: {'PASSED [OK]' if report['passed_all'] else 'FAILED [BLOCKING]'}")
    print(f"Detailed Report written to: {report_file}")
    print("=" * 70)

    return report["passed_all"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit YouTube Package")
    parser.add_argument("--package-id", default="003", help="Package ID (e.g. 003)")
    parser.add_argument("--dir", default="docs/assets/review_003", help="Directory containing package assets")
    args = parser.parse_args()

    success = audit_package(args.package_id, args.dir)
    sys.exit(0 if success else 1)
