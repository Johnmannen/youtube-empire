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

    total_views = data.get("total_views", 373)
    video_count = data.get("video_count", 4)
    total_comments = data.get("total_comments", 4)
    total_likes = data.get("total_likes", 6)
    subscribers = data.get("subscribers", 1)
    top_video = data.get("top_video", {})
    video_breakdown = data.get("video_breakdown", "")
    last_synced = data.get("last_synced", "")
    videos = data.get("videos", [])

    print(f"Fetched {len(videos)} videos. Total views across all videos: {total_views}")

    # 1. Update docs/dashboard_state.json
    state_file = os.path.join("docs", "dashboard_state.json")
    if os.path.exists(state_file):
        try:
            with open(state_file, "r", encoding="utf-8") as f:
                state = json.load(f)
            
            if "channel_metrics" not in state:
                state["channel_metrics"] = {}
            state["channel_metrics"]["total_views"] = total_views
            state["channel_metrics"]["total_comments"] = total_comments
            state["channel_metrics"]["total_likes"] = total_likes
            state["channel_metrics"]["subscribers"] = subscribers
            state["channel_metrics"]["video_count"] = video_count
            state["channel_metrics"]["top_video"] = top_video
            state["channel_metrics"]["video_breakdown"] = video_breakdown
            state["channel_metrics"]["videos"] = videos
            state["channel_metrics"]["last_synced"] = last_synced

            if "kpis" in state:
                state["kpis"]["views_30d"] = f"{total_views} visningar ({video_count} videor totalt)"
                state["kpis"]["videos_produced"] = f"4 ({video_count} publicerade live på kanalen)"

            with open(state_file, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2, ensure_ascii=False)
            print("Updated docs/dashboard_state.json successfully.")
        except Exception as e:
            print(f"Failed to update dashboard_state.json: {e}")

    # 2. Update docs/index.html KPI elements in static markup
    index_file = os.path.join("docs", "index.html")
    if os.path.exists(index_file):
        try:
            with open(index_file, "r", encoding="utf-8") as f:
                html = f.read()
            
            # Update kpiTotalViews
            html = re.sub(
                r'(id="kpiTotalViews">)[^<]+(</span>)',
                rf'\g<1>{total_views}\g<2>',
                html
            )

            # Update kpiVideoBreakdown
            html = re.sub(
                r'(id="kpiVideoBreakdown">)[^<]+(</p>)',
                rf'\g<1>{video_breakdown}\g<2>',
                html
            )

            # Update kpiApiStatus
            html = re.sub(
                r'(id="kpiApiStatus">)[^<]+(</p>)',
                rf'\g<1>● YouTube Data API Live ({video_count} videor)\g<2>',
                html
            )

            # Update kpiCommentCount
            html = re.sub(
                r'(id="kpiCommentCount">)[^<]+(</p>)',
                rf'\g<1>{total_comments} kommentarer registrerade\g<2>',
                html
            )

            # Update kpiTopVideoTitle
            top_title_label = top_video.get("label", "Short #002.1")
            top_title_full = top_video.get("title", "Build Real-Time Voice AI Agents in Python")
            top_views_val = top_video.get("views", total_views)

            html = re.sub(
                r'(id="kpiTopVideoTitle">)[^<]+(</div>)',
                rf'\g<1>{top_title_label}\g<2>',
                html
            )

            # Update kpiTopVideoSubtitle
            html = re.sub(
                r'(id="kpiTopVideoSubtitle">)[^<]+(</p>)',
                rf'\g<1>{top_title_full}\g<2>',
                html
            )

            # Update kpiTopVideoViews
            html = re.sub(
                r'(id="kpiTopVideoViews">)[^<]+(</span>)',
                rf'\g<1>{top_views_val} visn.\g<2>',
                html
            )

            # Update kpiChannelTotalFooter
            html = re.sub(
                r'(id="kpiChannelTotalFooter">)[^<]+(</p>)',
                rf'\g<1>Totalt {total_views} visningar över samtliga {video_count} videor\g<2>',
                html
            )

            with open(index_file, "w", encoding="utf-8") as f:
                f.write(html)
            print("Updated KPI markup in docs/index.html successfully.")
        except Exception as e:
            print(f"Failed to update index.html: {e}")

if __name__ == "__main__":
    sync_metrics()
