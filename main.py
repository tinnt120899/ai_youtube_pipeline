import argparse, sys, time
from logger import log
from config import OUT_DIR
from modules.script_manager import select_script, read_script_from_file
from modules.tts_engine import tts_gtts, tts_elevenlabs
from modules.media_fetcher import fetch_pixabay, download_file
from modules.video_composer import compose_video
from modules.youtube_uploader import upload_to_youtube

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tts", default="gtts", choices=["gtts", "elevenlabs"])
    parser.add_argument("--upload", action="store_true")
    parser.add_argument("--privacy", default="unlisted")
    parser.add_argument("--lang", default="en")
    parser.add_argument("--prompt", default="nature")
    args = parser.parse_args()

    script_file = select_script()
    script = read_script_from_file(script_file)

    voice = tts_elevenlabs(script) if args.tts == "elevenlabs" else tts_gtts(script)
    if not voice:
        sys.exit("❌ Voice generation failed.")

    urls = fetch_pixabay(args.prompt)
    bg_files = [download_file(u, OUT_DIR / f"bg_{i}.mp4") for i, u in enumerate(urls) if u]

    video_path = OUT_DIR / f"video_{int(time.time())}.mp4"
    compose_video(script, voice, bg_files, video_path)

    if args.upload:
        upload_to_youtube(str(video_path), script_file.stem, script[:800], args.privacy)
    else:
        log(f"💾 Lưu video tại: {video_path}")
    log("🎬 Hoàn tất pipeline.")

if __name__ == "__main__":
    main()
