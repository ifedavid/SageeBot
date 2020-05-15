from TweetQuotes import Tweets
from ReplyToMentions import MentionsReply
import time
import multiprocessing



def Tweet():
    Tweets()

def ReplyMentions():
    MentionsReply()


p1 = multiprocessing.process(target=Tweet())
p2 = multiprocessing.process(targer=ReplyMentions())


p1.start()
p2.start()
p1.join()
p2.join()




