import os

from moviepy.editor import VideoFileClip, concatenate_videoclips

from shared.config import settings


def combine_clips(clips_dir):

    height = settings.out_video.height
    width = settings.out_video.width
    bg_color = settings.out_video.bg_color
    fps = settings.out_video.fps

    clips = []

    for filename in os.listdir(clips_dir):
        if filename.endswith(".mp4") and filename.startswith("out"):
            clip_path = os.path.join(clips_dir, filename)
            clip = VideoFileClip(clip_path)

            resized_clip = clip.resize(height=height)
            padded_clip = resized_clip.set_position(("center", "center")).\
                on_color(size=(width, height), color=tuple(bg_color))
            clips.append(padded_clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("merged.mp4", fps=fps)
