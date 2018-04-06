#!/usr/bin/env python

import tweepy
from auth import api

#Create streamer for constant
class MyStreamListener(tweepy.StreamListener):
    #This acts as the call back for the myStream object
    #we will write the tweet here
    def on_status(self, status):
        print(status.text)
        print('========')

    #Handle 420 errors - the more 420 errors longer locked out of stream
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

#Create instance of MyStreamListener
myStreamListener = MyStreamListener()

#Create a stream object
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#TODO We will put words synamous for dinger in the track parameter array
#TODO Add a follow parameter so we only track tweets of people we want - other wise this streams ALL the tweets!
myStream.filter(track=['python'], async=True)
