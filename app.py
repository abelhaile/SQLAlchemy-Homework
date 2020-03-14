from datetime import datetime
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

app = Flask(__name__)

# Data_into_pandas= pd.DataFrame(last_12_months, columns=['date','prcp'])
# Data_into_pandas.set_index("date", inplace=True)
# Data_into_pandas= list(np.ravel(Data_into_pandas))[0]

@app.route("/")
def API():
    return("home Work return ")

@app.route("/api/v1.0/precipitation")
def precp():
    return("preceptation ")

@app.route("/api/v1.0/stations")
def station():
    station_json= engine.execute('SELECT * FROM Station').fetchall()
    station_json=list(np.ravel(station_json))
    print(station_json)
    return jsonify(station_json)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs_json= engine.execute('SELECT * FROM measurements').fetchall()
    tobs_json=list(np.ravel(tobs_json))
    print(tobs_json)
    return jsonify("tobs_json")

@app.route("/api/v1.0/<start>")
def start(start):
    return(start)
    print(start)

@app.route("/api/v1.0/<start>/<end>")
def end(start,end):
    return(start+end)
    print(start+end)
if __name__=='__main__':
    app.run(debug=True)