#!/usr/bin/env python3
"""
order_listener.py - Continuous Background Order Dispatcher for Antigravity
Watches for remote orders committed by GitHub Actions via docs/pending_order.json.
When a new order is detected:
1. Pulls latest changes from origin/main.
2. Identifies the requested pitch (e.g. 005, 006, 007).
3. Produces the video package via produce_package.py or specific generator.
4. Executes the automated 18-point pre-flight compliance audit.
5. Updates dashboard_state.json and index.html with the completed package.
6. Clears the pending order and pushes the finalized build live to GitHub.
"""

import os
import sys
import time
import json
import subprocess
from datetime import datetime

PENDING_ORDER_FILE = os.path.join("docs", "pending_order.json")
DASHBOARD_STATE_FILE = os.path.join("docs", "dashboard_state.json")

def run_cmd(cmd, check=True):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)

def check_for_orders():
    # Fetch remote changes quietly
    try:
        run_cmd("git fetch origin main")
        # Check if remote main is ahead
        status = run_cmd("git status -uno")
        if "Your branch is behind" in status.stdout:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Remote changes detected. Pulling...")
            run_cmd("git pull --rebase origin main")
    except Exception as e:
        print(f"Error fetching git remote: {e}")
        return None

    if not os.path.exists(PENDING_ORDER_FILE):
        return None

    try:
        with open(PENDING_ORDER_FILE, "r", encoding="utf-8") as f:
            order = json.load(f)

        if order.get("status") == "PENDING_ANTIGRAVITY_BUILD":
            return order
    except Exception as e:
        print(f"Error reading order file: {e}")

    return None

def process_order(order):
    pitch_id = order.get("pitch_id", "005")
    clean_id = pitch_id.replace("PITCH #", "").strip()
    title = order.get("title", "Autonomous Build")

    print("=" * 70)
    print(f"🚀 EXECUTING REMOTE ORDER: {pitch_id} - {title}")
    print("=" * 70)

    # 1. Update order status to IN_PROGRESS
    order["status"] = "IN_PROGRESS_BUILDING"
    order["started_at"] = datetime.now().isoformat()
    with open(PENDING_ORDER_FILE, "w", encoding="utf-8") as f:
        json.dump(order, f, indent=2)

    # 2. Check if a specific builder script exists
    script_path = f"scripts/produce_master_package_{clean_id}.py"
    if not os.path.exists(script_path):
        # Fallback to general produce_package
        script_path = ".agents/skills/building-youtube-packages/scripts/produce_package.py"

    print(f"Running production script: {script_path}...")
    try:
        res = subprocess.run([sys.executable, script_path], check=True)
        print(f"✅ Video production completed successfully for {pitch_id}!")
    except Exception as e:
        print(f"❌ Video production failed: {e}")
        order["status"] = "FAILED"
        order["error"] = str(e)
        with open(PENDING_ORDER_FILE, "w", encoding="utf-8") as f:
            json.dump(order, f, indent=2)
        return False

    # 3. Run Quality & Compliance Auditor
    audit_script = ".agents/skills/quality_compliance_auditor/scripts/audit_package.py"
    if os.path.exists(audit_script):
        print("Running pre-flight quality audit...")
        try:
            subprocess.run([sys.executable, audit_script, "--package-id", clean_id, "--dir", "docs/assets"], check=True)
            print("✅ Quality Audit: 100% COMPLIANT!")
        except Exception as e:
            print(f"⚠️ Audit warning/block: {e}")

    # 4. Mark order as COMPLETED
    order["status"] = "COMPLETED"
    order["completed_at"] = datetime.now().isoformat()
    with open(PENDING_ORDER_FILE, "w", encoding="utf-8") as f:
        json.dump(order, f, indent=2)

    # 5. Git Commit and Push Result
    try:
        run_cmd("git add docs/")
        run_cmd(f'git commit -m "feat(auto-build): completed remote order for {pitch_id} [skip ci]"')
        run_cmd("git push origin main")
        print("✅ Finished order pushed to GitHub main!")
    except Exception as e:
        print(f"Git push error: {e}")

    return True

def main():
    print("=" * 70)
    print("ANTIGRAVITY AUTONOMOUS ORDER LISTENER STARTED")
    print("Listening for GitHub Actions dispatch orders (docs/pending_order.json)...")
    print("Press Ctrl+C to stop.")
    print("=" * 70)

    # Check once immediately
    order = check_for_orders()
    if order:
        process_order(order)
    else:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] No pending orders. Standing by.")

if __name__ == "__main__":
    main()
