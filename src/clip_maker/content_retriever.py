import itertools
import random
from concurrent.futures import ThreadPoolExecutor

import praw

from shared.config import settings
from shared.logger import log


def initialize_wrapper():
    reddit = praw.Reddit(client_id=settings.reddit.auth.client_id,
                         client_secret=settings.reddit.auth.client_secret,
                         user_agent=settings.reddit.auth.user_agent)
    return reddit


def retrieve_combined_posts(reddit, pool, max_duration):
    post_retrieve_limit = settings.reddit.post_retrieve_limit

    def retrieve_subreddit_posts(subreddit_name):
        log.info(f"Getting posts from r/{subreddit_name}...")

        subreddit = reddit.subreddit(subreddit_name)
        posts = [post for post in subreddit.hot(limit=post_retrieve_limit)
                 if post.is_video
                 and post.media.get('reddit_video')
                 and post.media['reddit_video']['duration'] <= max_duration]

        log.info(f"Retrieved {len(posts)} from {subreddit_name}")
        return posts

    with ThreadPoolExecutor() as executor:
        subreddit_posts = executor.map(retrieve_subreddit_posts, pool)

    log.info("Combining posts...")
    flatten_posts = list(itertools.chain.from_iterable(subreddit_posts))

    log.info(f"Shuffling {len(flatten_posts)} posts...")
    random.shuffle(flatten_posts)
    return flatten_posts


def retrieve_video_posts(limit: int, max_duration: int):
    reddit = initialize_wrapper()
    pool = settings.reddit.subreddits

    posts = retrieve_combined_posts(reddit, pool, max_duration)

    videos = random.sample(posts, k=limit)
    return videos
