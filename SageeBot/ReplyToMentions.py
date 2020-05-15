import time
import logging
import tweepy
import json
import http.client
from Config import CreateApi

logger = logging.getLogger()

def ConvertStringToList(string):
    li = list(string.split(" "))
    return li

def GetOriginDetails(firstname, lastname):
    conn = http.client.HTTPSConnection("namsor-origin.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "namsor-origin.p.rapidapi.com",
        'x-rapidapi-key': "adedf96f72mshff11965263c4628p18aecdjsn8edf0ae612cc"
        }

    conn.request("GET", "/json/origin/"+ firstname + "/"+ lastname +"", headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")
    jsonFormat = json.loads(result)
    continent = jsonFormat["topRegion"]
    subregion = jsonFormat["subRegion"]
    country = jsonFormat["countryName"]
    responseList = [continent, subregion, country]
    return responseList

def check_mentions(api, since_id):
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        tweetList =  ConvertStringToList(tweet.text)
        screeName = tweet.user.screen_name
        new_since_id = max(tweet.id, new_since_id)
        tweetLength = len(tweetList)

        if tweet.in_reply_to_status_id is not None:
            continue
        logger.info(f"Answering to {tweet.user.name}")

        if tweetLength < 3:
            message = "@%s Sorry, I didn't get that. It has to be your Firstname and Lastname separated by space." %screeName
            api.update_status(message, in_reply_to_status_id = tweet.id)
            continue


        originList = GetOriginDetails(tweetList[1], tweetList[2])
        m = "@"+screeName+" Hey! Your origin details are as follows:\n\n Continent - "+originList[0]+"\n Region - "+originList[1]+"\n Country - "+originList[2]

        api.update_status(
            m,
            in_reply_to_status_id = tweet.id
        )
    return new_since_id

def MentionsReply():
    api = CreateApi()
    since_id = 1
    while True:
        since_id = check_mentions(api, since_id)
        logger.info("Waiting...")
        print("waiting")
        time.sleep(30)

if __name__ == "__main__":
    MentionsReply()