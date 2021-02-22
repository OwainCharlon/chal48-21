# Imports
from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
import os
import pymongo

from config import DevelopmentConfig
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'pic/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

client = pymongo.MongoClient("mongodb+srv://user1:2NvZYRipodUWsipy@cluster1.swpth.mongodb.net/sample_airbnb?retryWrites=true&w=majority")
#db = client.nomdb
#col = db.nomColonne

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == 'POST':
        current_dir = os.getcwd()
        current_path = current_dir + "\\pictures\\"
        print( request.values.get('picture_type') )
        return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('homepage'))
    return render_template("upload.html")

@app.route("/search", methods=["GET"])
def search():
    #Recherche par Nom/Libelléimage -> regex du champ name
    #Recherche par type/image -> regex du champ type image
    #Ensemble de checkBox
    #Nom d'auteur ->regex 
    return


if __name__ == "__main__":
    app.run(debug=True)