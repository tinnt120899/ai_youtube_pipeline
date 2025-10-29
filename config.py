import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# API Keys
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY")
YOUTUBE_CLIENT_SECRETS = os.getenv("YOUTUBE_CLIENT_SECRETS", "client_secrets.json")
CHANNEL_TITLE = os.getenv("CHANNEL_TITLE", "AI Auto Channel")

# Paths
BASE_DIR = Path(__file__).parent
OUT_DIR = BASE_DIR / "outputs"
SCRIPTS_DIR = BASE_DIR / "scripts"
OUT_DIR.mkdir(exist_ok=True)
SCRIPTS_DIR.mkdir(exist_ok=True)

# YouTube Scopes
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
