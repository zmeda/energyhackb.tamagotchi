'''
Created on Jun 15, 2013

@author: joe
'''

import httplib
import xml.etree.ElementTree as ET
from random import choice

#from basicPlot import plotData

url = "www.vattenfall.de"
api = "/SmeterEngine/networkcontrol"


def queryVattenfall(xmlRequest):
    
    
    webservice = httplib.HTTPS(url)
    webservice.putrequest("POST", api)
    webservice.putheader("Host", url)
    webservice.putheader("User-Agent","Python post")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(xmlRequest))
    webservice.endheaders()
    webservice.send(xmlRequest)
    statuscode, statusmessage, header = webservice.getreply()
    print statuscode, statusmessage, header
    result = webservice.getfile().read()
    
    return result

exampleRequest = '''<smeterengine>
<scale>DAY</scale>
<city>BERLIN</city>
<district>
<time_period begin="2013-06-14 00:00:00" end="2013-06-15 00:00:00" time_zone='CET'/>
</district>
</smeterengine>'''

lastDays = '''<smeterengine>
<scale>DAY</scale>
<city>BERLIN</city>
<district>
<time_period begin="2013-06-04 00:00:00" end="2013-06-15 00:00:00" time_zone='CET'/>
</district>
</smeterengine>'''


def findStats():
    xmlReply = queryVattenfall(lastDays)
    #xmlRoot = 
    
    
    

def main():
    
    findStats()
    
    testReply = queryVattenfall(exampleRequest)
    print testReply
    
    root = ET.fromstring(testReply)
    
    usageValues = [float(element.text) for element in root.iter("usage") if float(element.text) > 1.0]
    generationValues = [float(element.text) for element in root.iter("generation") if float(element.text) > 1.0]
    
    maxValue = max(usageValues)
    minValue = min(usageValues)
    threshold = (maxValue - minValue) * 0.1
    upperThreshold = maxValue - threshold
    lowerThreshold = minValue + threshold
    result = 0
    value = choice(usageValues)
    if (value > upperThreshold):
        result = 3
    elif (value < lowerThreshold):
        result = 1
    else:
        result = 2
    
    print maxValue, minValue, upperThreshold, lowerThreshold, value, result 
    
    print usageValues
    print generationValues
    
    #plotData(usageValues, generationValues)
    
    
    


if __name__ == '__main__':
    main()