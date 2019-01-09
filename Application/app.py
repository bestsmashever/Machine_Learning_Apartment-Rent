# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    flash)

from config import gkey
from jinja2 import Template
from forms import UserInput
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import requests as req

# Flask Setup
app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculation", methods=['GET', 'POST'])
def calculation():
    form = UserInput(request.form)
    if request.method == "POST":
        userinput = {
            'Address': form.address.data,
            'Bed': form.bed.data,
            'Bath': form.bath.data,
            'Avg SF': form.sf.data,
            "Concessions %": form.sf.data,
            # "Year Built": 
            "Walk in Closet": form.walk_in_closet.data,
            "Hardwood/Vinyl Floor": form.hardwood_vinyl_floor.data
        }
        global Address
        Address = form.address.data
        print(Address)
        flash("submit successful")
        return redirect("/")

    # load the pre-trained model
    
    # make prediction
    # lin_model.predict(userinput)

    return render_template("calculation.html", form=form)

@app.route("/scraping/", methods=['GET', 'POST'])
def scraping():
    #logic for scraping
    payload = {
        "units": "imperial",
        "origins": Address, 
        "destinations": "11410 Century Oaks Terrace, Austin, TX 78758|1100 Congress Ave, Austin, TX 78701",
        "key": "AIzaSyCQhKXIlYN6TQ3MHT4lujpN0lXAyB1Tvyo"
    }

    response = req.get("https://maps.googleapis.com/maps/api/distancematrix/json", params = payload).json()

    print(response['rows'][0]['elements'][0]['distance']['text'],
    response['rows'][0]['elements'][1]['distance']['text'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
