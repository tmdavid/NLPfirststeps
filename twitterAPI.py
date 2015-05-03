__author__ = 'User'

import twitter
import time
from tweepy import Stream
from tweepy import OAuthHandler
import os
from tweepy.streaming import StreamListener
import hiddenkeys as hk
import json
import urllib3.contrib.pyopenssl
import scipy
import re
import operator


urllib3.contrib.pyopenssl.inject_into_urllib3()

'''
CONS_KEY = 'J0RgdVza5oh0jl3YbaDaldwvX'
CONS_KEY_SECR = 'SJGXtGGEeTY6lue872W0wuwZJmopD65UMfAjFeognzKR0cRUrI'
ACCESS_TOKEN = '251285470-uLNlT7PLZW5UqlyacbouPksYgxc9r4aJdUXw9Xyt'
ACCES_TOKEN_SECR = 'qYMx3Z5kzCfF6EoONVo810hmOzQQVVtnJYYjHogeM3jK7'
'''

class twitterAPI():

    api = ''
    username = ''
    user = ''
    userID = ''
    userstatuses = 0
    statuscount = 0
    hashtagsUsed = {}

    def initTwitter(self, username):
        self.api = twitter.Api(consumer_key=hk.CONS_KEY, consumer_secret=hk.CONS_KEY_SECR, access_token_key=hk.ACCESS_TOKEN,
                               access_token_secret=hk.ACCES_TOKEN_SECR)
        print 'Credentials verify' + str(self.api.VerifyCredentials())
        self.username = username
        self.getUserID()
        userstatuses = 0
        statuscount = 0
        hashtagsUsed = {}



    def saySomething(self, tosay):
        status = self.api.PostUpdate(tosay)
        print status.text

    def getUserID(self):

        userJson = self.api.GetUser(None,self.username)
        print 'user info: ' + str(userJson)
        self.userID = int(userJson._id)
        self.userstatuses = int(userJson._statuses_count)
        print self.userstatuses

    def extract_hash_tags(self, s):
        return set([re.sub(r"(\W+)$", "", j, flags = re.UNICODE) for j in set([i for i in s.split() if i.startswith("#")])])

    #since_id needs to be added after saving everything to JSON or XML
    def retrieveData(self):
        newstatuses = self.api.GetUserTimeline(self.userID, count = 100)
        #print [s.text + '\n' for s in statuses]
        filename = str(self.username) + '.json'
        userFile = open(filename, 'a')
        timelinedone = False
        while (timelinedone == False):
            if(newstatuses.__len__()<1):
                timelinedone = True
            else:
                lowestID = newstatuses[newstatuses.__len__()-1]._id
                self.statuscount = self.statuscount + newstatuses.__len__()
                print self.statuscount
            for status in newstatuses:
                hashtags = self.extract_hash_tags(status._text)
                for hashtag in hashtags:
                    if (self.hashtagsUsed.has_key(hashtag)==1):
                        self.hashtagsUsed[hashtag] += 1
                    else:
                        self.hashtagsUsed.setdefault(hashtag,1)

                userFile.write(status.__str__())

                userFile.write('\n')

            newstatuses = self.api.GetUserTimeline(self.userID, count = 50, max_id=lowestID-1)

        userFile.close()
        print self.api.GetUser(self.userID).name
        sorted_x = sorted(self.hashtagsUsed.items(), key=operator.itemgetter(1), reverse= True)
        #print sorted_x
        tophashtags = '@'+self.username+ ' your top 3 hashtags are: '
        i = 0
        for tweetHT in sorted_x:
            if(i<3):
                tophashtags = tophashtags +' ' +str(tweetHT[0])
                i += 1
            else: break

        print tophashtags
        self.saySomething(tophashtags)
        return 1

'''
tweepy for stream
'''
class listener(StreamListener):

    auth = ''
    keyword_list = ''

    def __init__(self, start_time, time_limit):
        #print 'gonna listen'
        self.limit = time_limit
        self.time = time.time()
        self.auth = OAuthHandler(hk.CONS_KEY, hk.CONS_KEY_SECR) #OAuth object
        self.auth.set_access_token(hk.ACCESS_TOKEN, hk.ACCES_TOKEN_SECR)
        self.keyword_list = ['#CiU', '#ERC', '#CUP','#ERC', '#Cs', '#PP']  # track list



    def on_data(self, data):

        while (time.time() - self.time) < self.limit :

            print time.time()-self.time, self.limit
            try:

                saveFile = open('politics.json', 'a')
                printeddata = json.loads(data)
                #if (printeddata['lang'] == "es" or printeddata['lang'] == "ca"):
                print printeddata['text']
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



