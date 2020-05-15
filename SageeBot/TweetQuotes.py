import http.client
import json
import logging
import time
from Config import CreateApi
import os


logger = logging.getLogger()


def TweetQuote(api):
    conn = http.client.HTTPSConnection("quotes15.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "quotes15.p.rapidapi.com",
        'x-rapidapi-key': "adedf96f72mshff11965263c4628p18aecdjsn8edf0ae612cc"
        }

    conn.request("GET", "/quotes/random/?language_code=en", headers=headers)

    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")

    jsonFormat = json.loads(result)
    authorDetails = jsonFormat["originator"]
    quote = jsonFormat["content"]
    author = authorDetails["name"]


    quoteLength = len(quote)
    if quoteLength <= 200:
        api.update_status(quote + "\n\n" + author)

def Tweets():
    api = CreateApi()
    while True:
        TweetQuote(api)
        logger.info("Waiting...")
        time.sleep(43200)

if __name__ == "__main__":
    Tweets()