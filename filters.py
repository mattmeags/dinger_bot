#!/usr/bin/env python

import tweepy
from auth import api

terms = ['Home Run', 'Homer', 'Dinger', 'Grand Slam']

handles = ['MLBHR']

print api.user_timeline

#stores user objects, you may not need this
userObjArray = []

#stores account IDs
userIds = []

for i in handles:
    userObjArray.append(api.get_user(i))
    userIds.append(str(api.get_user(i).id))
