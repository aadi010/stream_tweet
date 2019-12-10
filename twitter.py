from tweepy import Stream, API
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy.parsers import JSONParser
import json
import os
import sys 
from dotenv import load_dotenv
load_dotenv()

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        if status == 420:
            return False
        print(status)

class StreamTweets():
    """
        Simple class to print tweets
    """
    def __init__(self, consumer_key, consumer_secret, access_token, 
                 access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = OAuthHandler(self.consumer_key, 
                                        self.consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)


def main():
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    access_token = os.getenv('access_token')
    access_token_secret = os.getenv('access_token_secret')
    stream_tweets = StreamTweets(consumer_key, consumer_secret, 
                              access_token, access_token_secret)

        

if __name__ == '__main__':
    main()