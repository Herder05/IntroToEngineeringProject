import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

global CountryList
CountryList = []
def initialize():
    global CountryList
    CountryList.clear()
    file = open("Backend\GlobalTempsSingleCountry.csv", "r", encoding="utf8")
    country = ""
    x = []
    y = []
    flag = True
    for line in file:
        if flag:
            flag = False
            country = line.split(",")[2]
        if country != line.split(",")[2]:
            xx = []
            yy = []
            for thing in x:
                xx.append(thing)
            for thing in y:
                yy.append(thing)
            CountryList.append({"Country":country[-2],"Years":xx,"Temps":yy})
            x.clear()
            y.clear()
            country = line.split(",")[2]
        x.append(int(line.split(",")[0]))
        y.append(int(line.split(",")[1]))
    xx = []
    for number in CountryList[len(CountryList) - 1].get("Years"):
        xx.append(number)
    xx.append(int(x[0]))
    CountryList[len(CountryList) - 1].update({"Years":xx})
    xx.clear()
    for number in CountryList[len(CountryList) - 1].get("Temps"):
        xx.append(int(number))
    xx.append(int(y[0]))
    CountryList[len(CountryList) - 1].update({"Temps":xx})

def getAllStrings():
    list = []
    global CountryList
    for country in CountryList:
        list.append(country["Country"])
    return list

def ReturnGraph(Country):
    for dictionary in CountryList:
        if dictionary["Country"] == Country:
            x = dictionary["Years"]
            y = dictionary["Temps"]
            plt.plot(x,y)
            plt.xticks(x)
            plt.xlabel("Years")
            plt.ylabel("Temperatures")
            plt.savefig("Static\\Data.png")
            plt.clf()
            plt.close()
            return True