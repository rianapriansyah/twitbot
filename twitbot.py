import tweepy
from time import sleep
import json

json_file = open('config.json',) 

config = json.load(json_file)

consumer_key = config.get('consumer_key')
consumer_secret = config.get('consumer_secret')
access_token = config.get('access_token')
access_token_secret = config.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)




