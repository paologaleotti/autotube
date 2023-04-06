import praw
import random
from config import settings


def initialize_wrapper():
    reddit = praw.Reddit(client_id=settings.reddit.auth.client_id,
                         client_secret=settings.reddit.auth.client_secret,
                         user_agent=settings.reddit.auth.user_agent)
    return reddit


def retrieve_video_posts(limit: int, max_duration: int):
    reddit = initialize_wrapper()

    pool = settings.reddit.subreddits
    subreddit = reddit.subreddit(random.choice(pool))

    print("getting content from:", pool)

    posts = subreddit.hot(limit=100)

    filtered_posts = [post for post in posts
                      if post.is_video
                      and post.media['reddit_video']['duration'] <= max_duration]

    videos = random.sample(population=filtered_posts, k=limit)

    return videos
