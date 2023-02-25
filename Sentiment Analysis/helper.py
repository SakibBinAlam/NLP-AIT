import praw
import pandas as pd
#import reddit_api
from prediction import predict_sentiment

# Instance of Reddit
# reddit = praw.Reddit(
#     client_id     = reddit_api.client_id,
#     client_secret = reddit_api.client_secret,
#     user_agent    = reddit_api.user_agent
# )
user_agent = "Test_api"

# Instance of Reddit
reddit = praw.Reddit(
    client_id = "elZ2l3hn14eVEVT2l1OXhg",
    client_secret="q8cPy2rIr5Msw2k0gARsUGmTNIzrDA",
    user_agent=user_agent
    #check_for_async=False
)

# reddit = praw.Reddit(client_id='', 
#                      client_secret='', 
#                      user_agent='',
#                      check_for_async=False)

# subreddit to extract posts from
def fetch_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)

    titles = []
    scores = []

    for submission in subreddit.top(limit=50):
        titles.append(submission.title)
        scores.append(submission.score)
    
    return titles, scores