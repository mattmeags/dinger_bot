#!/usr/bin/env python

import tweepy
from auth import api

class BotFunctionality:

    def ding(self):
        api.update_status('Dinger')
