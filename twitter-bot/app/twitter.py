import tweepy
from os import environ
from .classes import Tweet

API_KEY = environ.get("API_KEY")
API_SECRET = environ.get("API_KEY_SECRET")
ACCESS_TOKEN = environ.get("ACCESS_TOKEN")
ACCESS_SECRET = environ.get("ACCESS_TOKEN_SECRET")

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
api.verify_credentials()

def getMentions() -> list[Tweet]:
    mentions = api.mentions_timeline(
        count = 50
    )
    results = []
    for mention in mentions:
        results.append(Tweet(mention.id, mention.text, mention.in_reply_to_status_id))

    return results

def getRecentTweets() -> list[Tweet]:
    timeline = api.user_timeline(
        count=80,
        tweet_mode="extended",
        exclude_replies=False,
        include_rts=False
    )
    results = []
    for tweet in timeline:
        results.append(Tweet(tweet.id, tweet.full_text, tweet.in_reply_to_status_id))

    return results

def postTweet(text, replyId):
    return api.update_status(
        status = text,
        in_reply_to_status_id = replyId,
        auto_populate_reply_metadata = True
    )