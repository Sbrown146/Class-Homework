import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
import pandas as pd
from flask import Flask, jsonify

engine=create_engine("sqlite:///Resources/hawaii.sqlite")
Base=automap_base()
Base.prepare(engine, reflect=True)

Measurement=Base.classes.measurement
Station=Base.classes.station

app=Flask(__name__)

@app.route("/")
def welcome():
    """Populate list of all available api routes."""
    return(
        f"Make a Selection from the Following Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start_date><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Works
@app.route("/api/v1.0/precipitation")
def prcp():
    """Display all precipitation values"""
    session=Session(engine)
    results=session.query(Measurement.date, Measurement.prcp).all()

    all_prcp=[]
    for date, prcp in results:
        prcp_dict={}
        prcp_dict["Date"]=date
        prcp_dict["Precipitation"]=prcp
        all_prcp.append(prcp_dict)


    return jsonify(all_prcp)

# Works
@app.route("/api/v1.0/stations")
def station():
    """List of all station names"""
    session=Session(engine)
    results=session.query(Station.station).all()

    all_names=list(np.ravel(results))

    return jsonify(all_names)

# Works
@app.route("/api/v1.0/tobs")
def temp_obs():
    """List of temperpature observations over last year"""
    session=Session(engine)
    results=session.query(Measurement.tobs).filter(Measurement.date < '2017-08-24').filter(Measurement.date > '2016-08-22').all()

    #Fix to just display tobs, not both date and tobs
    all_names=list(np.ravel(results))

    return jsonify(all_names)

# Works  - No forward slash at the end or 404 error will occur.
@app.route("/api/v1.0/<start_date>")
def calc_temps(start_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    session=Session(engine)

    return str(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all())

# Works
@app.route("/api/v1.0/<start>/<end>")
def calc_temps_both(start, end):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """

    session=Session(engine)

    return str(session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all())


if __name__=='__main__':
    app.run(debug=True)