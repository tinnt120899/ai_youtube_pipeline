from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from logger import log
from config import SCOPES, YOUTUBE_CLIENT_SECRETS

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(YOUTUBE_CLIENT_SECRETS, SCOPES)
    creds = flow.run_console()
    return build("youtube", "v3", credentials=creds)

def upload_to_youtube(video_path, title, description, privacy="unlisted"):
    yt = get_authenticated_service()
    body = {"snippet": {"title": title, "description": description, "categoryId": "27"},
            "status": {"privacyStatus": privacy}}
    media = MediaFileUpload(video_path, chunksize=-1, resumable=True)
    req = yt.videos().insert(part="snippet,status", body=body, media_body=media)
    log("📤 [UPLOAD] Uploading...")
    while True:
        status, resp = req.next_chunk()
        if resp:
            log(f"✅ [UPLOAD] Done: https://youtu.be/{resp.get('id')}")
            break
        if status:
            log(f"⏫ Upload... {int(status.progress()*100)}%")
