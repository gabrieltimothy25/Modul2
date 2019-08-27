from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, abort, url_for
import os
import mysql.connector
from werkzeug.utils import secure_filename 
import json
import pymongo

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['HtmlDB']
col = db['Users']
data = list(col.find())

@app.route('/')
def home():
    return render_template('formbaru.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method=='POST':
        data = request.form
        newdata = json.dumps(data)
        newdata2 = json.loads(newdata)
        col.insert_one({'Email': newdata2['email'],
                        'Password': newdata2['password']})
        return "<p>Sign Up berhasil. Silahkan login kembali <a href='http://localhost:1234'>di sini.</a></p>"
@app.route('/login', methods=['POST'])
def login():
    if request.method=='POST':
        data = request.form
        newdata = json.dumps(data)
        newdata2 = json.loads(newdata)
        dbdata = list(col.find())
        for d in dbdata:
            d["_id"] = str(d["_id"])
            d2 = json.dumps(d)
            d3 = json.loads(d2)
            if newdata2["email"] == d3["Email"] and newdata2["password"] == d3["Password"]:
                return render_template('welcome.html')
            elif newdata2["email"] == d3["Email"] and newdata2["password"] != d3["Password"]:
                return ("<p>Mohon Maaf, password anda salah. Silahkan <a href='http://localhost:1234'>coba lagi.</a></p>")
        else:
            return("<p>Mohon Maaf, email anda belum terdaftar. Silahkan daftar dan <a href='http://localhost:1234'>coba lagi.</a></p>")
if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port=1234  
    )