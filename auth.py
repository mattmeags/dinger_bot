#!/usr/bin/env python

import tweepy
from secrets import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#api instance
api = tweepy.API(auth)
