import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

global CountryList
CountryList = []
def initialize():
    global CountryList
    CountryList.clear()
    file = open("Backend\\GlobalTempsClean.csv", "r", encoding="utf8")
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
            if "\n" in country:
                country = country.replace("\n","")
            CountryList.append({"Country":country,"Years":xx,"Temps":yy})
            x.clear()
            y.clear()
            country = line.split(",")[2]
        x.append(float(line.split(",")[0]))
        y.append(float(line.split(",")[1]))
    xx = []
    for number in CountryList[len(CountryList) - 1].get("Years"):
        xx.append(number)
    xx.append(float(x[0]))
    CountryList[len(CountryList) - 1].update({"Years":xx})
    xx.clear()
    for number in CountryList[len(CountryList) - 1].get("Temps"):
        xx.append(float(number))
    xx.append(float(y[0]))
    CountryList[len(CountryList) - 1].update({"Temps":xx})

def getAllStrings():
    list = []
    global CountryList
    for country in CountryList:
        list.append(country["Country"])
    return list

def getAvg(country):
    data = 0
    count = 1
    for thing in CountryList:
        if thing["Country"] == country:
            for x in thing["Temps"]:
                data += x
                count += 1
    return data / count


def ReturnGraph(Country):
    for dictionary in CountryList:
        if dictionary["Country"] == Country:
            x = dictionary["Years"]
            y = dictionary["Temps"]
            plt.plot(x,y)
            xy = []
            count = 0
            for thing in x:
                if count % 24 == 0:
                    if thing == 2012:
                        xy.append(2013)
                    else:
                        xy.append(thing)
                count += 1
            yminimum = 0
            rangelist = []
            if min(y) < 0:
                yminimum = min(y)
            for number in range(math.floor(yminimum), math.ceil(max(y))):
                rangelist.append(number)
            plt.xticks(xy)
            plt.yticks(rangelist)
            plt.xlabel("Years")
            plt.ylabel("Temperatures")
            plt.title("Average Temperatures of " + Country)
            plt.savefig("Static\\Data.png")
            plt.clf()
            plt.close()
            return True