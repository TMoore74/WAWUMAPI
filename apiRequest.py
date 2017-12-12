import json
import urllib
import time

API_PARAM = {"APIKEY" : "YOUR_API_KEY", "LINE" : 167, "BUSSTOP" : 3072, "BUSID" : "01"}

def getBusStopTimeSeries(ile_do_przodu=3):
    URL = "https://api.um.warszawa.pl/api/action/dbtimetable_get?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId=%s&busstopNr=%s&line=%s&apikey=%s" % (BUS_API_PARAM["BUSSTOP"], BUS_API_PARAM["BUSID"],BUS_API_PARAM["LINE"],BUS_API_PARAM["APIKEY"])
    # result
    result = {}
    try:
        # request
        response = urlopen(URL)
        # get data from json
        data = json.loads(response.read()) 
        # pobranie czasu
        TIME= strftime("%H"),strftime("%M")
        # zmienne wyjsciowe
        result["line"] = BUS_API_PARAM["LINE"]
        result["dir"] = data["result"][0]["values"][3]["value"]
        result["time"] = []
        # dodanie tablicy czasow odjazdow
        timeSeries = []
        for item in data["result"]:
            # wciagniecie czasu na tablice
            czas = item["values"][5]["value"].split(":")
            timeSeries.append((czas[0],czas[1]))
        # szukanie najblizszego danej godziny
        counter = 0
        for index in range(len(timeSeries)):
            if ile_do_przodu > 0:
                if int(timeSeries[index][0]) >= int(TIME[0]):
                    if int(timeSeries[index][1]) > int(TIME[1]):
                        result["time"].append("%s:%s" %(timeSeries[index][0],timeSeries[index][1]))
                        counter+=1 
                        ile_do_przodu-=1
        # jak nie znalazl w danej godzinie ustawiamy wieksza o 1 i minuty na 00
        if counter == 0:
            TIME = TIME[0]+1,00
        for index in range(len(timeSeries)):
            if ile_do_przodu > 0:
                if int(timeSeries[index][0]) >= int(TIME[0]):
                    if int(timeSeries[index][1]) > int(TIME[1]):
                        result["time"].append("%s:%s" %(timeSeries[index][0],timeSeries[index][1]))
                        ile_do_przodu-=1
    except Exception as e:
        raise e
    return result
