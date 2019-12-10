from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from twitter import StreamTweets
from dotenv import load_dotenv
load_dotenv()
import os

consumer_key = os.getenv('consumer_key')
consumer_secret = os.getenv('consumer_secret')
access_token = os.getenv('access_token')
access_token_secret = os.getenv('access_token_secret')

app = Flask(__name__)
api = Api(app)

#GET API to stream tweets based on a HashTag
class Twitter_Stream_HashTag(Resource):
    def get(self, hashTag):
        stream_tweets.stream_tweets_hashTag(str(hashTag))

#GET API to stream tweets for  UserName
class Twitter_Stream_UserName(Resource):
    def get(self, userName):
        userID = stream_tweets.find_userID_from_userName(str(userName))
        stream_tweets.stream_tweets_userID(str(userID))

#API endpoints
api.add_resource(Twitter_Stream_HashTag, '/tweets/hashTag=<hashTag>') 
api.add_resource(Twitter_Stream_UserName, '/tweets/userName=<userName>')


if __name__ == '__main__':
    stream_tweets = StreamTweets(consumer_key, consumer_secret, access_token, access_token_secret)
    app.run(port='5002')