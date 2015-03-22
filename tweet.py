__author__ = 'User'


tw = {'author': '', 'tweet': '', 'time':''}

def createTwit(aut,text,ti):

    tw.__setitem__("author", aut)
    tw.__setitem__('tweet',text)
    tw.__setitem__('time',ti)

    return tw



