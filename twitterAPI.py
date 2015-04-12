__author__ = 'User'

import twitter
import tweepy
import time
from tweepy import Stream
from tweepy import OAuthHandler
import os
from tweepy.streaming import StreamListener

CONS_KEY = 'J0RgdVza5oh0jl3YbaDaldwvX'
CONS_KEY_SECR = 'SJGXtGGEeTY6lue872W0wuwZJmopD65UMfAjFeognzKR0cRUrI'
ACCESS_TOKEN = '251285470-uLNlT7PLZW5UqlyacbouPksYgxc9r4aJdUXw9Xyt'
ACCES_TOKEN_SECR = 'qYMx3Z5kzCfF6EoONVo810hmOzQQVVtnJYYjHogeM3jK7'

auth = OAuthHandler(CONS_KEY, CONS_KEY_SECR) #OAuth object
auth.set_access_token(ACCESS_TOKEN, ACCES_TOKEN_SECR)
keyword_list = ['coachella']  # track list

class twitterAPI():

    api = ''

    def initTwitter(self):
        self.api = twitter.Api(consumer_key=CONS_KEY, consumer_secret=CONS_KEY_SECR, access_token_key=ACCESS_TOKEN,
                               access_token_secret=ACCES_TOKEN_SECR)
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

    def __init__(self, start_time, time_limit):
        print 'gonna listen'
        self.limit = time_limit
        self.time = time.time()

    def on_data(self, data):

        while (time.time() - self.time) < self.limit :

            print time.time()-self.time , self.limit
            try:
                saveFile = open('coachella.json', 'a')
                saveFile.write(data)
                saveFile.write('\n')
                saveFile.close()
                return True


            except BaseException, e:
                print 'failed ondata,', str(e)
                time.sleep(5)
                pass

        exit()

    def on_error(self, status):
        print status

    def getDatabyTopic(self):

        start_time =time.time()
        twitterStream = Stream(auth, listener(start_time, time_limit=self.limit)) #initialize Stream object with a time out limit
        twitterStream.filter(track=keyword_list, languages=['en'])