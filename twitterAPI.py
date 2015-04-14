__author__ = 'User'

import twitter
import tweepy
import time
from tweepy import Stream
from tweepy import OAuthHandler
import os
from tweepy.streaming import StreamListener
import hiddenkeys as hk
'''
CONS_KEY = 'J0RgdVza5oh0jl3YbaDaldwvX'
CONS_KEY_SECR = 'SJGXtGGEeTY6lue872W0wuwZJmopD65UMfAjFeognzKR0cRUrI'
ACCESS_TOKEN = '251285470-uLNlT7PLZW5UqlyacbouPksYgxc9r4aJdUXw9Xyt'
ACCES_TOKEN_SECR = 'qYMx3Z5kzCfF6EoONVo810hmOzQQVVtnJYYjHogeM3jK7'
'''

class twitterAPI():

    api = ''

    def initTwitter(self):
        self.api = twitter.Api(consumer_key=hk.CONS_KEY, consumer_secret=hk.CONS_KEY_SECR, access_token_key=hk.ACCESS_TOKEN,
                               access_token_secret=hk.ACCES_TOKEN_SECR)
        print self.api.VerifyCredentials()


    def saySomething(self):
        status = self.api.PostUpdate('checking')
        print status.text

    def retrieveData(self):
        user = 'daviddincognit'
        user = '167346791'
        statuses = self.api.GetUserTimeline(user)
        print [s.text for s in statuses]
        print [s._in_reply_to_user_id for s in statuses]
        print self.api.GetUser(user).name
        return 1


class listener(StreamListener):

    auth = ''
    keyword_list = ''

    def __init__(self, start_time, time_limit):
        #print 'gonna listen'
        self.limit = time_limit
        self.time = time.time()
        self.auth = OAuthHandler(hk.CONS_KEY, hk.CONS_KEY_SECR) #OAuth object
        self.auth.set_access_token(hk.ACCESS_TOKEN, hk.ACCES_TOKEN_SECR)
        self.keyword_list = ['madeon','coachella']  # track list



    def on_data(self, data):

        while (time.time() - self.time) < self.limit :

            print time.time()-self.time, self.limit
            try:
                saveFile = open('madeon.json', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
                return True

            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                #pass

        return False
        #exit()

    def on_error(self, status):
        print status
        print 'waiting 30 segs'
        time.sleep(30)
        return False

    def getDatabyTopic(self):
        #print self.keyword_list
        start_time =time.time()
        twitterStream = Stream(self.auth, listener(start_time, time_limit=self.limit)) #initialize Stream object with a time out limit
        twitterStream.filter(track=self.keyword_list)



