#!/usr/bin/env python

import tweepy
from auth import api

class BotFunctionality:

    def ding(self, player):
        baseTweet = 'Dinger: ' + player
        baseTweetLen = len(baseTweet)
        lastTweet = api.user_timeline('dinger_bot')[0].text
        lastTweetLen = len(lastTweet)

        # Check if the same player hit the dinger
        if lastTweet == baseTweet or lastTweet[baseTweetLen] == baseTweet :
            # Player going on to atleast 3 dingers!!
            if lastTweet[lastTweetLen - 1] == ")" :
                dingerCount = int(lastTweet[lastTweetLen - 2])
                dingerCount += 1
                tweet = baseTweet + "(" + dingerCount +")"
            # Player's second dinger
            else:
                tweet = baseTweet + " (2)"
        # A different player   
        else:
            tweet = baseTweet

        api.update_status(tweet)
