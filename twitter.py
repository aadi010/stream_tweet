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
    def __init__(self, output_file=sys.stdout):
        super(listener,self).__init__()
        self.output_file = output_file
        
    def on_data(self, data):
        print(data, file=self.output_file)
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

    def find_userID_from_userName(self, user_name):
        api = API(self.auth, parser=JSONParser())
        result = api.lookup_users(screen_names= [user_name])
        if len(result) == 1:
            return result[0]["id"]
        else: 
            print("Multiple Users with username")
            sys.exit()

    def stream_tweets_userID(self,userID):
        output = open('tweets_userID.txt', 'w')
        twitterStream = Stream(self.auth, listener(output_file=output))
        try:
            twitterStream.filter(follow=[userID])
        except KeyboardInterrupt:
            print("Stopped.")
        finally:
            twitterStream.disconnect()
            output.close()

    def stream_tweets_hashTag(self,hashTag):
        output = open('tweets_hashTag.txt', 'w')
        twitterStream = Stream(self.auth, listener(output_file=output))
        try:
            twitterStream.filter(track=[hashTag], is_async=True)
        except KeyboardInterrupt:
            print("Stopped.")
        finally:
            twitterStream.disconnect()
            output.close()
        

