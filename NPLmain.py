__author__ = 'User'

import dataExtractor as dE
import xmlclasstw as xc

# @tmdavid
# NPL first steps???
#

dataE = dE.dataExtraction()
xmlTest = xc.dataToXml()

print("there we go")

dataE.dataFrom(2)

xmlTest.createXML(2)
