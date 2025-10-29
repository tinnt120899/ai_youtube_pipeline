import time
from pathlib import Path
from gtts import gTTS
from logger import log
from config import ELEVEN_API_KEY, OUT_DIR

try:
    from elevenlabs import generate, save, set_api_key
except:
    generate = save = set_api_key = None

def tts_gtts(text, lang="en"):
    outpath = OUT_DIR / f"voice_{int(time.time())}.mp3"
    gTTS(text=text, lang=lang).save(str(outpath))
    log(f"✅ [TTS] via gTTS: {outpath}")
    return outpath

def tts_elevenlabs(text, voice="Rachel"):
    if not ELEVEN_API_KEY:
        log("⚠️ [TTS] Thiếu ELEVEN_API_KEY → fallback gTTS.")
        return tts_gtts(text)
    outpath = OUT_DIR / f"voice_{int(time.time())}.mp3"
    set_api_key(ELEVEN_API_KEY)
    audio = generate(text=text, voice=voice, model="eleven_multilingual_v2")
    save(audio, outpath)
    log(f"✅ [TTS] via ElevenLabs: {outpath}")
    return outpath
