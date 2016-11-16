import tweepy
from tweepy import OAuthHandler

consumer_key = 'CONSUMER-KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS-TOKEN'
access_secret = 'ACCESS-SECRET'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
  def on_data(self,data):
    try:
      with open('python.json','a') as f:
        f.write(data)
        return True
    except BaseException as e:
      print("Error on data : %s" % str(e))
    return True
  def on_error(self, status):
    print(status)
    return True
  
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])
