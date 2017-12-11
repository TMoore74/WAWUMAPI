import json
import urllib
import time

API_PARAM = {"APIKEY" : "YOUR_API_KEY", "LINE" : 167, "BUSSTOP" : 3072, "BUSID" : "01"}

def getBusStopTimeSeries(ile_do_przodu=3):
    URL = "https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId=%s&busstopNr=%s&line=%s&apikey=%s" % (API_PARAM["BUSSTOP"], API_PARAM["BUSID"],API_PARAM["LINE"],API_PARAM["APIKEY"])
    # request
    response = urllib.urlopen(URL)
    # get data from json
    data = json.loads(response.read()) 
    # pobranie czasu
    TIME = time.strftime("%H"),time.strftime("%M")
    czas = []
    for item in data["result"]:
        # wciagniecie czasu na tablice
        czas=item["values"][5]["value"].split(":")
        if ile_do_przodu > 0:
            if int(czas[0]) >= int(TIME[0]):
                if int(czas[1]) >= int(TIME[1]):
                    print "%s:%s" %(czas[0],czas[1])
                    ile_do_przodu-=1
    
    

getBusStopTimeSeries()
