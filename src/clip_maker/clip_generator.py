import os

import requests
from moviepy.editor import AudioFileClip, VideoFileClip

from shared.logger import log

BASE_CLIPS_PATH = "clips"


def get_clip_path(prefix, post_id):
    os.makedirs(BASE_CLIPS_PATH, exist_ok=True)
    return os.path.join(BASE_CLIPS_PATH, f"{prefix}_{post_id}.mp4")


def generate_clip(post):
    try:
        log.info(f"Generating video for post {post.id}...")

        video_url = post.media["reddit_video"]["fallback_url"]
        audio_url = video_url[:video_url.find(
            "DASH_")] + "DASH_audio.mp4?source=fallback"

        video_path = get_clip_path("video", post.id)
        audio_path = get_clip_path("audio", post.id)
        output_path = get_clip_path("out", post.id)

        with open(video_path, "wb") as f:
            f.write(requests.get(video_url).content)

        with open(audio_path, "wb") as f:
            f.write(requests.get(audio_url).content)

        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)

        merged_clip = video.set_audio(audio)
        merged_clip.write_videofile(output_path, verbose=False, logger=None)

        os.remove(video_path)
        os.remove(audio_path)
    except BaseException as e:
        log.error(e)
