from flask import Flask, render_template, redirect
from flask_pymongo import pymongo
# From the separate python file in this directory, import the code that is used to scrape mars information
import scrape_mars
app = Flask(__name__)
# Use flask_pymongo to set up mongo connection
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
# set database 
db=client.mars_db
# This route will query the Mongo DB and get the mars info and then render them to an html file
@app.route("/")
def home():
    mars_results = db.mars_results.find()
    return render_template("index.html", mars_results=mars_results)
# This route will read the web scraping file
@app.route("/scrape")
def scraper():
# drop any data that is already in database
   db.mars_results.drop()
   mars_data = scrape_mars.scrape()
   db.mars_results.insert_one(mars_data)
    # Use Flask's redirect function to send us to a different route once this task has completed.
   return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)