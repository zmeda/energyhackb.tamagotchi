'''
Created on Jun 15, 2013

@author: joe
'''

import httplib
import xml.etree.ElementTree as ET

from datetime import datetime
import datetime as dt


start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print start


url = "www.vattenfall.de"
api = "/SmeterEngine/networkcontrol"


def whatIsThePeakStatusInBerlinNow():
    
    ff = "%Y-%m-%d %H:%M:%S"

    end = datetime.now().strftime(ff)
    start = datetime.now() - dt.timedelta(minutes=15)
    start = start.strftime(ff)
    
    nowRequest = '''<smeterengine>
<scale>DAY</scale>
<city>BERLIN</city>
<district>
<time_period begin="%s" end="%s" time_zone='CET'/>
</district>
</smeterengine>''' % (start, end)
    
    result = queryVattenfall(nowRequest)
    print "--> ", result
    



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
    
    usageValues = [float(element.text) for element in root.iter("usage")]
    generationValues = [float(element.text) for element in root.iter("generation")]
    
    print usageValues
    print generationValues
    
    
    
    whatIsThePeakStatusInBerlinNow()


if __name__ == '__main__':
    main()