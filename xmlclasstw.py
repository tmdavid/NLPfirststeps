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
        topictext = "new topic"

        head = ET.SubElement(root, 'tweet')
        topic = ET.SubElement(head, 'topic')
        topic.set('topic', topictext)


        author = ET.SubElement(topic, "author")
        tweet = ET.SubElement(topic, "text")
        time = ET.SubElement(topic, "time")
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
            print ("trying to insert an element to our XML")
            '''
            head = ET.SubElement(root, 'tweet')
            topic = ET.SubElement(head, 'topic')
            topic.set('topic', topictext)
            '''
            topictext = "david"
            head = ET.SubElement(root, 'tweet')
            topic = ET.SubElement(head, 'topic')
            topic.set('topic',topictext)

            newNodeName = ET.SubElement(topic, 'author')
            newNodeName.text = tweet.get('author')

            newNodeName = ET.SubElement(topic,'text')
            newNodeName.text = tweet.get('tweet')

            newNodeName = ET.SubElement(topic,'time')
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
        search = "tweet/topic[@topic='" + topic +"']"
        tweets = root.findall(search) #("tweet/topic[@topic='david']") #[@topic='NPL']")
        print(search)
        print 'tweets found: ', len(tweets)
        for e in tweets:
            print e.find('author').text

        return