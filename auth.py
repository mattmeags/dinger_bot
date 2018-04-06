#!/usr/bin/env python

import tweepy
from secrets import *

#create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

#api instance
api = tweepy.API(auth)

#TODO This was for learning feel free to delete
#user = api.get_user('mattmeags')

# print user.screen_name
# print user.followers_count
# for friend in user.friends():
#     print friend.screen_name


#api.update_status('Hello Megan')
