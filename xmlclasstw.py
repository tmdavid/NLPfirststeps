__author__ = 'User'

import _elementtree as ET
import tweet as tWclass


class dataToXml():
    xmlName = ' '

    tw = {'author': '', 'tweet': '', 'time':''}

    def __init__(self):

        return

    def createTree(self):
        root = ET.Element("root")
        root.text = "Full data collection for nlp from twitter"
        topic = "new topic"
        head = ET.SubElement(root, "topic")
        head.text = topic
        author = ET.SubElement(head, "author")
        tweet = ET.SubElement(head, "tweet")
        time = ET.SubElement(head, "time")
        return root

    def createXML(self):
        xmlName = "twitter.xml"
        xmlRoot = self.createTree()
        tree = ET.ElementTree(xmlRoot)
        tree.write(xmlName)

        return xmlName

    def getTweets(self):

        #tweet = self.tw

        tw = tWclass.createTwit("daviddincognit","primer tweet","21-03-2015 19:55")

        return tw

    def addToXml(self):
        tree = ET.parse("twitter.xml")
        root = tree.getroot()
        tweet = self.getTweets()

        numberOfElements = len(root)
        try:
            print ("trying to insert a fuckin element to an xml tree")

            topic = "NPL"
            head = ET.SubElement(root, "topic")
            head.text = topic


            newNodeName = ET.SubElement(head, 'author')
            newNodeName.text = tweet.get('author')

            newNodeName = ET.SubElement(head,'tweet')
            newNodeName.text = tweet.get('tweet')

            newNodeName = ET.SubElement(head,'time')
            newNodeName.text = tweet.get('time')

            #root.insert(numberOfElements, head)

            tree.write('twitter.xml')

        except :
            print ("Couldnt Insert the tweet:")
            print (tweet)



    def readXML(self):

        xmltree = ET.parse("twitter.xml")

        return xmltree

    def getTweetsByTopic(self, topic):

        allData = dataToXml()
        alltweets = allData.readXML()
        root = alltweets.getroot()
        tweets = root.findall('topic')
        for e in tweets:
            print (e.text)


        return