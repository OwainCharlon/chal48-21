# Imports
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
import os
import pymongo

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

client = pymongo.MongoClient("mongodb+srv://user1:2NvZYRipodUWsipy@cluster1.swpth.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
#db = client.nomdb
#col = db.nomColonne

@app.route("/home", methods=["GET"])
def homepage():

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)