# Adds the ability to import an HTML file and assign variables in the file to variables from your code
from flask import render_template
#handles python using html
from flask import Flask
#So flask can make HTTP requests to itself
from flask import request
#So flask can handle accepting variables from the html
from flask import jsonify
#so we can link to the sources
import webbrowser
#lets you write the html in python and add it to the render template (thank you chatgpt for telling me this import exists)
from markupsafe import Markup
#import the backend.py
from backend import *

#defines the variable app to be a flask application
app = Flask(__name__)

#The Text In app Route is the part that goes after the basic url so for example https://baseURL/AppRouteText/ can be used so you have multiple pages

#Homepage, automatically creates buttons based on the items from the list that is taken in from the backend
@app.route("/")
def home():
    initialize()
    a = ""
    i = 0
    l = getAllStrings()
    for s in l:
        a = a +  "<script type=text/javascript> $(function(){$(\"#" + s.replace(" ","").replace("&","").replace("-","") + "\").click(function (event) {const text = '/getName/' + document.getElementById(\""+ s.replace(" ","").replace("&","").replace("-","") +"\").value;$.getJSON((text), {},function(data) { });return false;}); }); </script><input type = \"button\" id = \""+ s.replace(" ","").replace("&","").replace("-","") + "\" value = \"" + s +"\" />"
        i = i + 1   
        if i == 7: #TODO find some math here to make it always look nice
            a = a + "<br>"
            i = 0
        
    return render_template(
        "LinkPage.html",
        Buttons = a
    )


#Accepts data from the linkpage
@app.route('/getName/<name>')
def getName(name):
    global country
    country = name
    return "/CountryData/"


#Loads the Country Template with the vars from the backend
@app.route("/CountryData/")
def Country():
    global country
    
    #TODO tell backend to update the image "Data.png"
    try:
        ReturnGraph(country)
        #Call the image as an if statement so it doesnt execute the rest of the code while waiting for the thing to make the image
        return render_template(
            "CountryTemplate.html",
            Country = country,
            avg = format(getAvg(country),".2f")
        )
    except:
        return home()

#Loads the info page
@app.route("/info/")
def info():
    return render_template(
        "Info.html"
    )


#data sources
#e1
@app.route("/DataSource1/")
def DataSource1():
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data')
    return render_template(
        "Info.html"
    )