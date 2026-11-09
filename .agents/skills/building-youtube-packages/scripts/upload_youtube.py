#!/usr/bin/env python3
"""
Phase 2 YouTube Data API v3 Upload Script
Uploads long-form and Short video packages autonomously to YouTube Studio.
"""
import os
import sys
import json
import argparse

def get_authenticated_service(client_secrets_file: str):
    try:
        import google_auth_oauthlib.flow
        import googleapiclient.discovery
    except ImportError:
        print("[ERROR] google-api-python-client or google-auth-oauthlib is not installed.")
        print("Run: pip install google-api-python-client google-auth-oauthlib")
        sys.exit(1)

    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes=scopes
    )
    credentials = flow.run_local_server(port=0)
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

def upload_video(youtube, video_path: str, title: str, description: str, tags: list, category_id: str = "28", privacy_status: str = "private"):
    from googleapiclient.http import MediaFileUpload
    
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"Video file not found: {video_path}")

    body = {
        "snippet": {
            "title": title[:100],
            "description": description,
            "tags": tags,
            "categoryId": category_id  # 28 = Science & Technology
        },
        "status": {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": False
        }
    }
    
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    
    print(f"[API] Uploading {video_path}...")
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"[API] Uploaded {int(status.progress() * 100)}%")
            
    print(f"[SUCCESS] Video uploaded successfully! Video ID: {response.get('id')}")
    return response.get('id')

def main():
    parser = argparse.ArgumentParser(description="Upload YouTube Video Package via Data API v3")
    parser.add_argument("--package", default="docs/dashboard_state.json", help="Path to dashboard state JSON")
    parser.add_argument("--client-secret", default="client_secret.json", help="Path to Google Cloud OAuth client secret")
    parser.add_argument("--type", choices=["long", "short"], default="long", help="Upload long-form or short")
    parser.add_argument("--privacy", choices=["private", "unlisted", "public"], default="private", help="Video visibility")
    args = parser.parse_args()

    if not os.path.exists(args.client_secret):
        print(f"[NOTICE] OAuth client secret file '{args.client_secret}' not detected.")
        print("To enable Phase 2 autonomous upload:")
        print("1. Create an OAuth 2.0 Client ID in Google Cloud Console with YouTube Data API v3 enabled.")
        print(f"2. Save the JSON file as '{args.client_secret}'.")
        print("3. Re-run this script to authenticate and upload automatically.")
        sys.exit(0)

    with open(args.package, "r", encoding="utf-8") as f:
        data = json.load(f)

    pkg = data.get("current_package", {})
    video_file = pkg.get("long_video_file") if args.type == "long" else pkg.get("short_video_file")
    title = pkg.get("title") if args.type == "long" else f"{pkg.get('title')} #Shorts"
    
    service = get_authenticated_service(args.client_secret)
    upload_video(
        youtube=service,
        video_path=video_file,
        title=title,
        description=pkg.get("description", ""),
        tags=pkg.get("tags", []),
        category_id=pkg.get("category_id", "28"),
        privacy_status=args.privacy
    )

if __name__ == "__main__":
    main()
