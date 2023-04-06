from render_video import combine_clips
import time


def core():
    CLIPS_DIR = "clips"

    combine_clips(clips_dir=CLIPS_DIR)


if __name__ == '__main__':
    start_time = time.time()

    core()

    elapsed_time = time.time() - start_time
    print(f"[CLIPCOMBINER] DONE in {elapsed_time:.2f} seconds.")
