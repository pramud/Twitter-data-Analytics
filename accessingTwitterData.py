import tweepy
from tweepy import OAuthHandler

consumer_key = 'CONSUMER-KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS-TOKEN'
access_secret = 'ACCESS-SECRET'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
