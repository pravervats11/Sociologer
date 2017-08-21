#!/usr/bin/env python3.5

import tweepy
from tweepy import OAuthHandler
import json
import time

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

word_list = ["word_list"]

def get_tweets_category(word_list):
    for a in word_list:
        Tweets = []
        tweets = api.search(q = a, count = 100)
        for tweet in tweets:
            tweet.text = tweet.text.replace('&amp;', '&')
            Tweets.append(tweet.text)
        time.sleep(60)
        return Tweets
