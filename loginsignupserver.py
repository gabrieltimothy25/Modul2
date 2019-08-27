from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, abort, url_for
import os
import mysql.connector
from werkzeug.utils import secure_filename 
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Th_697203',
    database='HtmlDB'
)

@app.route('/')
def home():
    return render_template('formbaru.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method=='POST':
        data = request.form
        kursor = db.cursor()
        qry = 'insert into Users (Email, Password) values (%s, %s)'
        val = (data['email'], data['password'])
        kursor.execute(qry, val)
        db.commit()
        return "<p>Sign Up berhasil. Silahkan login kembali <a href='http://localhost:1234'>di sini.</a></p>"
@app.route('/login', methods=['POST'])
def login():
    if request.method=='POST':
        formdata = (json.dumps(request.form))
        formdata2 = json.loads(formdata)
        kursor = db.cursor()
        kursor.execute('describe Users')
        hasil = kursor.fetchall()
        namaKolom =[]
        for i in hasil:
            namaKolom.append(i[0])
        kursor.execute('select * from Users')
        hasil = kursor.fetchall()
        data = []
        for i in hasil:
            x = {
                namaKolom[0]: i[0],
                namaKolom[1]: i[1],
                namaKolom[2]: i[2],
            }
            data.append(x)
        for d in data:
            if formdata2["email"] == d["Email"] and formdata2["password"] == d["Password"]:
                return render_template('welcome.html')
            elif formdata2["email"] == d["Email"] and formdata2["password"] != d["Password"]:
                return ("<p>Mohon Maaf, password anda salah. Silahkan <a href='http://localhost:1234'>coba lagi.</a></p>")
            else:
                return("<p>Mohon Maaf, email anda belum terdaftar. Silahkan daftar dan <a href='http://localhost:1234'>coba lagi.</a></p>")
if __name__ == '__main__':
    app.run(
        debug = True,
        host = '0.0.0.0',
        port=1234  
    )