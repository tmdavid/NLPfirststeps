__author__ = 'User'

import dataExtractor as dE
import xmlclasstw as xc
import twitterAPI as tAPI

# @tmdavid
# NPL first steps???
#

dataE = dE.dataExtraction()
xmlTest = xc.dataToXml()
twitAPI = tAPI.twitterAPI()
stream = tAPI.listener(1,600)

print("there we go")

dataE.dataFrom(1)

#xmlTest.createXML()

def main():

    #xmlTest.addToXml()
    #xmlTest.getTweetsByTopic('david')
    twitAPI.initTwitter()

    #twitAPI.saySomething()
    twitAPI.retrieveData()
    stream.getDatabyTopic()

    return



if __name__ == '__main__':
  main()