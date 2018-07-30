#!/usr/bin/env python

import tweepy
import filters
import tweet
from auth import api

#Create streamer for constant
class MyStreamListener(tweepy.StreamListener):
    #This acts as the call back for the myStream object
    #we will write the tweet here
    def on_status(self, status):
        if "cubs" in status.text.lower():

            #checking if a reply
            if status.in_reply_to_screen_name != None:
                return

            #check for retweet
            if status.text[:2] == 'RT':
                return

            player = status.text.split('-')[0]

            bot = tweet.BotFunctionality()
            bot.ding(player)

    #Handle 420 errors - the more 420 errors longer locked out of stream
    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

#Create instance of MyStreamListener
myStreamListener = MyStreamListener()

#Create a stream object
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(follow=filters.userIds)
