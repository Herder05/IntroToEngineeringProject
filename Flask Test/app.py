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

#not entirely sure why or how this works HOWEVER if i touch it everything breaks :3
app = Flask(__name__)

#The Text In app Route is the part that goes after the basic url so for example https://baseURL/AppRouteText/ can be used so you have multiple pages

#Homepage, automatically creates buttons based on the items from the list that is taken in from the backend
@app.route("/")
def home():
    a = ""
    i = 0
    #TODO get list from backend here
    l = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua & Deps", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde", "Central African Rep", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo", "Congo Democratic Rep", "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland Republic", "Israel", "Italy", "Ivory Coast", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea North", "Korea South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar, Burma", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russian Federation", "Rwanda", "St Kitts & Nevis", "St Lucia", "Saint Vincent & the Grenadines", "Samoa", "San Marino", "Sao Tome & Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
    for s in l:
        a = a +  "<script type=text/javascript> $(function(){$(\"#" + s.replace(" ","").replace("&","") + "\").click(function (event) {const text = '/getName/' + document.getElementById(\""+ s.replace(" ","").replace("&","") +"\").value;$.getJSON((text), {},function(data) { });return false;}); }); </script><input type = \"button\" id = \""+ s.replace(" ","").replace("&","") + "\" value = \"" + s +"\" />"
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
    print(name)
    global country
    country = name
    return "/CountryData/"


#Loads the Country Template with the vars from the backend
@app.route("/CountryData/")
def Country():
    global country
    
    #TODO tell backend to update the image "Data.png"
    #Call the image as an if statement so it doesnt execute the rest of the code while waiting for the thing to make the image
    return render_template(
        "CountryTemplate.html",
        Country = country,
        avg = 0, #TODO Call backend for data
        avgInc = 0, #TODO Call Backend for data
        totalInc = 0  #TODO call backend for data
    )

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
#image Credits
@app.route("/ImageS1/")
def ImageS1():
    webbrowser.open_new_tab('http://google.com')
    return render_template(
        "Info.html"
    )
@app.route("/ImageS2/")
def ImageS2():
    webbrowser.open_new_tab('http://google.com')
    return render_template(
        "Info.html"
    )