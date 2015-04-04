__author__ = 'User'

import _elementtree as ET
import tweet as tWclass
'''
xml class to store data?
# build a tree structure
root = ET.Element("html")

head = ET.SubElement(root, "head")

title = ET.SubElement(head, "title")
title.text = "Page Title"

body = ET.SubElement(root, "body")
body.set("bgcolor", "#ffffff")

body.text = "Hello, World!"

# wrap it in an ElementTree instance, and save as XML
tree = ET.ElementTree(root)
tree.write("page.xhtml")
The ElementTree wrapper adds code to load XML files as trees of Element objects, and save them back again. You can use the parse function to quickly load an entire XML document into an ElementTree instance:

import elementtree.ElementTree as ET

tree = ET.parse("page.xhtml")

# the tree root is the toplevel html element
print tree.findtext("head/title")

# if you need the root element, use getroot
root = tree.getroot()

# ...manipulate tree...

tree.write("out.xml")
'''


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
        newNodeStr = 'topic'
        try:
            print ("trying to insert a fuckin element to an xml tree")

            topic = "new topic"
            head = ET.SubElement(root, "topic")
            head.text = topic

            insElement = ET.Element(newNodeStr)

            newNodeName = ET.SubElement(head, 'author')
            newNodeName.text = tweet.get('author')

            newNodeName = ET.SubElement(head,'tweet')
            newNodeName.text = tweet.get('tweet')

            newNodeName = ET.SubElement(head,'time')
            newNodeName.text = tweet.get('time')

            root.insert(numberOfElements, insElement)

            '''
            newNodeName = ET.Element('topic')
            newNodeName.text = 'new topic'
            insElement.append(newNodeName)
            newNodeName = ET.Element('author')
            newNodeName.text = tweet.get('author')
            insElement.append(newNodeName)
            newNodeName = ET.Element('tweet')
            newNodeName.text = tweet.get('tweet')
            insElement.append(newNodeName)
            newNodeName = ET.Element('time')
            newNodeName.text = tweet.get('time')
            insElement.append(newNodeName)
            root.insert(numberOfElements, insElement)
            '''

            tree.write('twitter.xml')

        except :
            print ("Couldnt Insert the tweet:")
            print (tweet)



    def readXML(self):

        xmltree = ET.parse("twitter.xml")


        return