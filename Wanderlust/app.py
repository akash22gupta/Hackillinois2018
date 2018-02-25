from flask import Flask, render_template, flash, request, jsonify, session
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import json
import requests 
import sys
import pyrebase
import re 
 
# App config.

#DEBUG = True
app = Flask(__name__)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

'''
class ReusableForm(Form):
    origin = TextField('Origin:', validators=[validators.required()])
    pickup = TextField('Pickup:', validators=[validators.required()])
    dropoff = TextField('Dropoff:', validators=[validators.required()])
'''
@app.route("/", methods=['GET','POST'])
def index():
    di2 = []
    
    if request.method == 'GET':
        return render_template('index1.html')
    
    if request.method == 'POST':
        origin = request.form['origin']
        pickup = request.form['pickup']
        budget = request.form['budget']
        #r = requests.get('http://api.sandbox.amadeus.com/v1.2/cars/search-airport?location='+origin+'&pick_up='+pickup+'&drop_off='+dropoff+'&apikey=hqGqfssnxF76GvutLSZQTEyIYEP0ajA0')
        response = requests.get('https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search?origin='+origin+'&departure_date='+pickup+'&max_price='+budget+'&apikey=UKlVeBWn328d1N1rI5TjETI3fpUr7WyT')
        #print(type(response))
        #json_obj = response.json
    
        json_obj = json.loads(response.text)
        di1 = {}
        #di2 = {}
        j = 1
        for i in json_obj["results"]:
            di1['destination'] = i["destination"]
            di1['departure_date'] = i["departure_date"]
            di1['return_date'] = i["return_date"]
            di1['airline'] = i["airline"]
            di1['price'] = i["price"]
            resp_poi = requests.get('https://api.sandbox.amadeus.com/v1.2/hotels/search-airport?apikey=UKlVeBWn328d1N1rI5TjETI3fpUr7WyT&location=SFO&check_in=2018-02-26&check_out=2018-03-03&number_of_results=1')
            resp_poi_json = json.loads(resp_poi.text)
            di1['Hotel'] = resp_poi_json
            di2.append(di1)
            di1 = {}
            #j += 1
        #json_obj = json.loads(response.text)
        session['data'] = di2
        return render_template('index2.html', data=di2)

@app.route("/data", methods=['GET','POST'])
def data():
    di12 = []
    #loc = request.form[{{destination}}]
    #checkin = request.form['departure_date']
    #checkout = request.form['return_date']
    #print(loc,checkin,checkout)
    #print("loc is")
    #print(loc)
    response2 = requests.get('https://api.sandbox.amadeus.com/v1.2/hotels/search-airport?apikey=UKlVeBWn328d1N1rI5TjETI3fpUr7WyT&location=SFO&check_in=2018-02-26&check_out=2018-03-03')
    #response2 = requests.get('https://api.sandbox.amadeus.com/v1.2/hotels/search-airport?apikey=UKlVeBWn328d1N1rI5TjETI3fpUr7WyT&location='+loc+'&check_in='+checkin+'&check_out='+checkout)
    print(response2.text)
    print("doend")
    json_obj_2 = json.loads(response2.text)
    di11 = {}
    #di2 = {}
    j = 1
    for i in json_obj_2['results']:
        di11['property_name'] = i["property_name"]
        di11['total_price'] = i["total_price"]
        #resp_poi = requests.get('https://api.sandbox.amadeus.com/v1.2/hotels/search-airport?apikey=UKlVeBWn328d1N1rI5TjETI3fpUr7WyT&location=BOS&check_in=2018-02-25&check_out=2016-2-27&amenity=RESTAURANT&amenity=PARKING&number_of_results=2')
        #resp_poi_json = json.loads(resp_poi.text)
        #di1['Points Of Interest'] = resp_poi_json 
        di12.append(di11)
        di11 = {}
        #j += 1
    #json_obj = json.loads(response.text)
    #return render_template('index3.html', data=di12)
    return di2


if __name__ == "__main__":
    app.run(debug=True)