import requests
from logger import log
from config import PIXABAY_API_KEY, OUT_DIR

def fetch_pixabay(query, per_page=3):
    if not PIXABAY_API_KEY:
        log("⚠️ [MEDIA] Thiếu Pixabay API key.")
        return []
    res = requests.get("https://pixabay.com/api/videos/",
                       params={"key": PIXABAY_API_KEY, "q": query, "per_page": per_page}).json()
    urls = [v["videos"]["medium"]["url"] for v in res.get("hits", [])]
    log(f"✅ [MEDIA] {len(urls)} video tìm thấy.")
    return urls

def download_file(url, dest):
    try:
        r = requests.get(url, stream=True)
        with open(dest, "wb") as f:
            for chunk in r.iter_content(8192):
                f.write(chunk)
        log(f"⬇️ [MEDIA] {dest}")
        return str(dest)
    except Exception as e:
        log(f"❌ [MEDIA] Download lỗi: {e}")
        return None
