__author__ = 'User'

import _elementtree as ET

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
        root = ET.Element("Data")
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

        tw = {'author': 'david', 'tweet': 'supercool #bs', 'time':'10:12'}

        return tw

    def addToXml(self):
        tree = ET.parse("twitter.xml")
        tweet = self.getTweets()




        return