import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

global CountryList
CountryList = []
#TODO Fix this as it does not work currently it fails to properly input the data and the data is not correctly in
def initialize():
    global CountryList
    #file = open("Backend\TempByAvgCountryClean.csv", "r", encoding="utf8")
    #country = ""
    #x = []
    #y = []
    #flag = True
    #for line in file:
    #    if flag:
    #        flag = False
    #        country = line.split(",")[2]
    #    if country != line.split(",")[2]:
    #        f = False
    #        for x in CountryList:
    #            if x["Country"] == country:
    #                f = True
    #        if not f:
    #            CountryList.append({"Country":country,"Years":x,"Temps":y})
    #        country = line.split(",")[2]
    #        x = [line.split(",")[0]]
    #        y = [line.split(",")[1]]
    #    x.append(line.split(",")[0])
    #    y.append(line.split(",")[1])
    #FIXME This temporarly clears the above part until it works and replaces it with some temporary sample data
    CountryList = [{"Country":"A","Years":[0,1,2,3,4,5,6],"Temps":[1,2,3,4,5,6,7]},{"Country":"B","Years":[0,1,2,3,4,5,6],"Temps":[1,2,3,4,5,6,7]},{"Country":"C","Years":[0,1,2,3,4,5,6],"Temps":[1,2,3,4,5,6,7]}]


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
            plt.savefig("Static\\Data.png")
            plt.clf()
            plt.close()
            return True