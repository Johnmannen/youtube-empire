"""
Sync Dashboard Metrics Script
Executed automatically by GitHub Actions every 6 hours or manually.
Reads true statistics from YouTube Data API v3 and updates docs/dashboard_state.json and docs/index.html KPI values.
"""

import os
import re
import json

def sync_metrics():
    # Attempt to import and fetch from fetch_live_data
    try:
        from fetch_live_data import fetch_live_channel_data
        data = fetch_live_channel_data()
    except Exception as e:
        print(f"Could not import or run live fetch: {e}")
        return

    total_views = data.get("total_views", 12)
    videos = data.get("videos", [])
    print(f"Fetched {len(videos)} videos. Total channel views: {total_views}")

    # Update dashboard_state.json if exists
    state_file = os.path.join("docs", "dashboard_state.json")
    if os.path.exists(state_file):
        try:
            with open(state_file, "r", encoding="utf-8") as f:
                state = json.load(f)
            
            if "channel_metrics" not in state:
                state["channel_metrics"] = {}
            state["channel_metrics"]["total_views"] = total_views
            state["channel_metrics"]["video_count"] = len(videos)
            state["channel_metrics"]["last_synced"] = data.get("timestamp", "")
            
            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            print("Updated docs/dashboard_state.json successfully.")
        except Exception as e:
            print(f"Failed to update dashboard_state.json: {e}")

    # Update docs/index.html KPI element
    index_file = os.path.join("docs", "index.html")
    if os.path.exists(index_file):
        try:
            with open(index_file, "r", encoding="utf-8") as f:
                html = f.read()
            
            # Replace id="kpiTotalViews">...</span>
            new_html = re.sub(
                r'(id="kpiTotalViews">)[^<]+(</span>)',
                rf'\g<1>{total_views}\g<2>',
                html
            )
            if new_html != html:
                with open(index_file, "w", encoding="utf-8") as f:
                    f.write(new_html)
                print("Updated kpiTotalViews in docs/index.html.")
            else:
                print("kpiTotalViews already up to date in docs/index.html.")
        except Exception as e:
            print(f"Failed to update index.html: {e}")

if __name__ == "__main__":
    sync_metrics()
