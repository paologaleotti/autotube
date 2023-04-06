from concurrent.futures import ThreadPoolExecutor
import praw
import random
from config import settings


def initialize_wrapper():
    reddit = praw.Reddit(client_id=settings.reddit.auth.client_id,
                         client_secret=settings.reddit.auth.client_secret,
                         user_agent=settings.reddit.auth.user_agent)
    return reddit


def retrieve_mapped_posts(reddit, pool, max_duration):

    def retrieve_subreddit_posts(subreddit_name):
        subreddit = reddit.subreddit(subreddit_name)
        print("Getting posts from", subreddit_name)

        return [post for post in subreddit.hot(limit=150)
                if post.is_video
                and post.media.get('reddit_video')
                and post.media['reddit_video']['duration'] <= max_duration]

    with ThreadPoolExecutor() as executor:
        subreddit_posts = list(executor.map(retrieve_subreddit_posts, pool))

    return subreddit_posts


def retrieve_video_posts(limit: int, max_duration: int):
    reddit = initialize_wrapper()
    pool = settings.reddit.subreddits

    subreddit_mapped_posts = retrieve_mapped_posts(reddit, pool, max_duration)

    posts = []
    for _ in range(limit):
        random_sub = random.choice(subreddit_mapped_posts)
        post = random.choice(random_sub)
        print(f"selected post {post.id} from {post.subreddit}")

        posts.append(post)

    videos = random.sample(posts, k=limit)
    return videos
