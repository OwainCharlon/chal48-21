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
db = client.chal48_passion_froid
col = db.picture

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


@app.route("/delete/<path>", methods=["GET", "POST"])
def delete(path):
    col.delete_one( { "path" : path } )
    message = 'Image has been deleted !'
    return render_template("index.html", message=message)

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

    response = request.json
    search = []

    filtersDic = {
            'name' :                '{ "name" : {"$regex": \'.*{}.*\' }}',
            'type' :                '{ "type" : {"$regex": \'.*{}.*\' }}',
            'credits' :             '{ "credits" : {"$regex": \'.*{}.*\' }}',
            'with_product' :        '{ "with_product" : {"$eq" :  {} }}', 
            'with_humans' :         '{ "with_humans" :  {"$eq" :  {} }}', 
            'institutional' :       '{ "institutional" : {"$eq" :  {} }}',
            'format' :              '{ "format" : {"$eq" :   {} }}', 
            'tags' :                '{ "tags" :         {"$in" :  {} }}', 
        }

    if 'filters' in response:
        for key, value in response['filters'].items():
            if key in filtersDic:
                newFilter = filtersDic[key].replace ( '{}', str(value) )
                search.append( ast.literal_eval( newFilter ))
            else:
                search = []

    if len(search):
        response = [ a for a in col.find({ "$and" : search }, {"_id" : 1}) ]

    else :
        response = { "output": {
                "type" : "notify",
                "description" : "no entities found"
            }
        }
            
    return response


if __name__ == "__main__":
    app.run(debug=True)