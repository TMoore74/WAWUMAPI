# Wrapper na API api.um.warszawa.pl

Trzeba skonfigurować tablice API_PARAM swoim APIKEY i podaniem danych przystanków.
Potrzebne dane można uzyskać po zarejestrowaniu się na stronie:

https://api.um.warszawa.pl/#

## Jak pobrać ID przystanku - parametr busstop

https://api.um.warszawa.pl/api/action/dbtimetable_get?id=b27f4c17-5c50-4a5b-89dd-236b282bc499&name=Siekierkowska&apikey=APIKEY

Podając nazwę przystanku, jak są polskie znaki trzeba je zakodować

## Drugie zapytanie pokaże jakie przystanki się tam znajdują i jakie linie zatrzymują się na nim

https://api.um.warszawa.pl/api/action/dbtimetable_get?id=88cd555f-6f31-43ca-9de4-66c479ad5942&busstopId=3072&busstopNr=01&apikey=API_KEY


## Przykład wykorzystania

Przystanek Siekierkowska **Id=3072**, w obie strony **01 i 02** dla linii **167 i 108**

```
  lines = [167,108]
  busstop = ["01","02"]

  for line in lines:
      API_PARAM["LINE"] = line
      for bstop in busstop:
          API_PARAM["BUSID"] = bstop
          print getBusStopTimeSeries()
  ```
