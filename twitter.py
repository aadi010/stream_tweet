from tweepy import Stream, API
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy.parsers import JSONParser
import json
import os
import sys 
import environ

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
    # stream_tweets = StreamTweets(consumer_key, consumer_secret, 
    #                           access_token, access_token_secret)
    pass
    
    

if __name__ == '__main__':
    main()