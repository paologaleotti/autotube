import multiprocessing
import time

from clip_generator import generate_clip
from content_retriever import retrieve_video_posts
from moviepy.editor import *

from shared.config import settings


def log_finished_clips(videos):
    print("GENERATED CLIPS:")
    for video in videos:
        print(f"|ID: {video.id} |SUB: {video.subreddit}")


def core():
    limit = settings.content.clips_limit
    max_duration = settings.content.max_clip_duration

    videos = retrieve_video_posts(limit, max_duration)

    with multiprocessing.Pool() as pool:
        pool.map(generate_clip, videos)

    log_finished_clips(videos)


if __name__ == '__main__':
    start_time = time.time()

    core()

    elapsed_time = time.time() - start_time
    print(f"[CLIPMAKER] DONE in {elapsed_time:.2f} seconds.")
