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

    #xmlTest.addToXml()
    #xmlTest.getTweetsByTopic('david')
    #twitAPI.initTwitter()

    #twitAPI.saySomething()
    #twitAPI.retrieveData()
    while (1<2):
        print 'getting data from:', stream.keyword_list
        stream.getDatabyTopic()

    return



if __name__ == '__main__':
  main()