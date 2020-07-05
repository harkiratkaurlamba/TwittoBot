# python TwittoBot.py
import tweepy
from textblob import TextBlob

consumer_key = '4pvMrOiU6lMazDc4c4DkHHlHa'
consumer_secret = 'fr7BP2K8TBLtxMT7kY8IKPdrCeayMy1s2C42zqnOGhHABBdsxt'
access_token = '1278008765841719297-rEMnu0CbPYHImzdyRZCjY0cgk2YMS8'
access_token_secret = 'hm7Dm6PnA6vGIM5Nk7nNFH0KSEPAzqGD17687wgscwzK5'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
#api.update_status('Where to go if place of calmness and turmoil is same...yeah my brain')

FILE_NAME = 'D:\Python\Atom Files\last_seen.txt'
def read_last_seen(FILE_NAME):
    file_read= open(FILE_NAME,'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME,'w')
    file_read.write(str(last_seen_id))
    file_read.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME, tweet_mode= 'extended')
    for tweet in reversed(tweets):
        if '#doiworkok' in tweet.full_text.lower():
            print(str(tweet.id) + '-' + tweet.full_text)
            api.update_status('#yesyouworkok'+ tweet.user.screen_name +'  Blue heart', tweet.id)
            store_last_seen(FILE_NAME, tweet.id)

reply()
