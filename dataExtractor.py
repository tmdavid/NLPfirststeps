__author__ = 'User'


def twitter():
        print("info from twitter")


def facebook():
        print("info from facebook")

class dataExtraction():

    def __init__(self):
        return

    def dataFrom(self, where):
        switchDataFrom = {1: twitter, 2: facebook}
        switchDataFrom[where]()
        return