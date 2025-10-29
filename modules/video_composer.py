from moviepy import (
    AudioFileClip,
    VideoFileClip,
    concatenate_videoclips,
    CompositeVideoClip,
    TextClip,
    ColorClip,
)
from logger import log


def compose_video(script, audio_path, bg_files, out_file, resolution=(1080, 1920)):
    log("🎞️ [VIDEO] Đang dựng video...")

    # Load audio
    audio = AudioFileClip(str(audio_path))

    # Chuẩn bị text và chia thời lượng đều
    lines = [l.strip() for l in script.split("\n") if l.strip()]
    dur = audio.duration / max(1, len(lines))
    clips = []

    for i, text in enumerate(lines):
        # Video nền hoặc màu nền
        if bg_files:
            clip = VideoFileClip(bg_files[i % len(bg_files)]).subclip(0, min(10, dur))
        else:
            clip = ColorClip(size=resolution, color=(20, 20, 30), duration=dur)

        # Text clip (method="caption" đã đổi tên)
        try:
            txt = TextClip(
                text,
                fontsize=48,
                color="white",
                size=(int(resolution[0] * 0.8), None),
                method="caption",
            ).set_position(("center", 0.75), relative=True)
        except Exception:
            # Fallback nếu MoviePy không hỗ trợ 'caption'
            txt = TextClip(
                text,
                fontsize=48,
                color="white",
                size=(int(resolution[0] * 0.8), None),
            ).set_position(("center", 0.75), relative=True)

        clips.append(CompositeVideoClip([clip, txt.set_duration(dur)]))

    # Gộp clip + âm thanh
    final = concatenate_videoclips(clips).set_audio(audio)

    # Xuất video
    final.write_videofile(
        str(out_file),
        fps=24,
        codec="libx264",
        audio_codec="aac",
        verbose=False,
        logger=None,
    )

    log(f"✅ [VIDEO] Xuất file: {out_file}")
    return out_file
