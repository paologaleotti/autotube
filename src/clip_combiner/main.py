import time
import os

from render_video import combine_clips

from shared.logger import log


def core():
    CLIPS_DIR = "clips"
    OUTPUT_DIR = "out"

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    combine_clips(clips_dir=CLIPS_DIR, out_dir=OUTPUT_DIR)


if __name__ == '__main__':
    start_time = time.time()
    log.info(f"[CLIPCOMBINER] STARTED process")

    core()

    elapsed_time = time.time() - start_time
    log.info(f"[CLIPCOMBINER] DONE in {elapsed_time:.2f} seconds.")
