#!/usr/bin/env python3.5

import tweepy
from tweepy import OAuthHandler
import textblob
import re
import json
import time
import codecs
import csv

*

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

word_list = ['#booz','#wasted','#alcohol','#beer','#whiskey']

for a in word_list:
        tweets = api.search(q = a, count = 100)
        for tweet in tweets:
            #tweet.text = tweet.text.replace('RT',' ')
            tweet.text = tweet.text.replace('\n','\r\n')
            tweet.text = tweet.text.replace('&amp;', '&')
            f.write(str(tweet.text))
            f.write(",Alcohol")
            f.write("\n\n")
        time.sleep(60)
