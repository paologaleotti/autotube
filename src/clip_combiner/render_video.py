import os

from moviepy.editor import VideoFileClip, concatenate_videoclips

from shared.config import settings
from shared.logger import log


def combine_clips(clips_dir, out_dir):
    try:
        height = settings.out_video.height
        width = settings.out_video.width
        bg_color = settings.out_video.bg_color
        fps = settings.out_video.fps
        out_file = os.path.join(out_dir, "combined.mp4")

        clips = []

        for filename in os.listdir(clips_dir):
            if filename.endswith(".mp4") and filename.startswith("out"):
                log.info(f"Adding clip: {filename}")

                clip_path = os.path.join(clips_dir, filename)
                clip = VideoFileClip(clip_path)

                resized_clip = clip.resize(height=height)
                padded_clip = resized_clip.set_position(("center", "center")).\
                    on_color(size=(width, height), color=tuple(bg_color))
                clips.append(padded_clip)

        final_clip = concatenate_videoclips(clips, method="compose")

        log.info(f"Using output settings: {width}*{height}@{fps}fps")
        log.info("Rendering...")

        final_clip.write_videofile(out_file, fps=fps)
        log.info(f"Output file: {os.path.abspath(out_file)}")

    except BaseException as e:
        log.critical(e)
        raise e
