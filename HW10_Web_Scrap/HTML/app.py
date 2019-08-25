from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app=Flask(__name__)

mongo=PyMongo(app, uri="mongodb://localhost:27017/onto_mars")

@app.route("/")
def index():
    mars=mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():

    mars=mongo.db.mars
    mars_info=scrape_mars.Mars_News()
    mars_info=scrape_mars.Mars_Image()
    mars_info=scrape_mars.Mars_Weather()
    mars_info=scrape_mars.Mars_Facts()
    mars_info=scrape_mars.Mars_Hem()
    mars.update({}, mars_info, upsert=True)

    # return redirect("/")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)