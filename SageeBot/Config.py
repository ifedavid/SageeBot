import tweepy
import logging
import os

TwitterConsumerKey = os.getenv("TwitterConsumerKey")
TwitterConsumerSecret = os.getenv("TwitterConsumerSecret")
TwitterAccessToken = os.getenv("TwitterAccessToken")
TwitterAccessTokenSecret = os.getenv("TwitterAccessTokenSecret")

logger = logging.getLogger()

def CreateApi():
    auth = tweepy.OAuthHandler("TwitterConsumerKey", "TwitterConsumerSecret")

    auth.set_access_token("TwitterAccessToken", "TwitterAccessTokenSecret")

    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error Creating API")
        raise e
    logger.info("API Created")
    return api




