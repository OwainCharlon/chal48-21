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

@app.route("/home", methods=["GET", "POST"])
def homepage():

    if request.method == 'POST':
        current_dir = os.getcwd()
        current_path = current_dir + "\\pictures\\"
        
        print( request.values.get('picture_type') )

        
        return render_template("index.html")

    else:
        return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    
    current_dir = os.getcwd()
    current_path = current_dir + "\\pictures\\"

    img = request.files['picture']

    #To do fonction de rename
    #name = 
    img.save(current_path + 'test.jpg')

    #body = request.get_json()
    
    #if col.insert_one( body ):
    #    print('Saved')

    return 

@app.route("/search", methods=["GET"])
def search():

    #Recherche par Nom/Libelléimage -> regex du champ name

    #Recherche par type/image -> regex du champ type image

    #Ensemble de checkBox

    #Nom d'auteur ->regex 

    return

if __name__ == "__main__":
    app.run(debug=True)