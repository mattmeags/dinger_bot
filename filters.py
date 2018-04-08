#!/usr/bin/env python

import tweepy
from auth import api

terms = ['Home Run', 'Homer', 'Dinger', 'Grand Slam']

#TODO make call to get twitter use ID and import
handles = ['mattmeags', 'Littles_League']

userObjArray = []

for i in handles:
    print api.get_user(i)
    userObjArry.appnd(api.get_user(i))
