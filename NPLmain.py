__author__ = 'User'

import dataExtractor as dE
import xmlclasstw as xc
import twitterAPI as tAPI

import time

# @tmdavid
# NPL first steps???
#

dataE = dE.dataExtraction()
xmlTest = xc.dataToXml()
twitAPI = tAPI.twitterAPI()
stream = tAPI.listener(1,100)

print("there we go")

#dataE.dataFrom(1)

#xmlTest.createXML()

def main():

    print '1. Retrieve DataStream On topic'
    print '2. Get User Info'
    print '3. GTFO'
    todo = int(raw_input())
    #xmlTest.addToXml()
    if (todo == 2):
        print 'Which user?\n'
        username2check = raw_input()
        twitAPI.initTwitter(username2check)
        #twitAPI.saySomething()
        twitAPI.retrieveData()
        main()
    elif (todo == 1):
        while (True):
            print 'getting data from:', stream.keyword_list
            stream.getDatabyTopic()
    elif (todo == 3):
        exit('bye bye!')
    return



if __name__ == '__main__':
  main()