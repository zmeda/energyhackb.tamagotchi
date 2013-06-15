'''
Created on Jun 15, 2013

@author: joe
'''

import httplib
import xml.etree.ElementTree as ET

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
    print "--",  result
    
    return result

exampleRequest = '''<smeterengine>
<scale>DAY</scale>
<city>BERLIN</city>
<district>
<time_period begin="2013-06-14 00:00:00" end="2013-06-15 00:00:00" time_zone='CET'/>
</district>
</smeterengine>'''

def main():
    
    testReply = queryVattenfall(exampleRequest)
    print testReply
    
    root = ET.fromstring(testReply)
    for usage in root.iter('usage'):
        print usage.text
    
    


if __name__ == '__main__':
    main()