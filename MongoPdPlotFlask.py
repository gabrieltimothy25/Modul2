from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, abort, url_for
from werkzeug.utils import secure_filename 
import os
import pymongo
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly
import chart_studio.plotly as py
import plotly.graph_objects as go
import json

# Access MongoDB with pandas Dataframe
""" x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avengers']

df = pd.DataFrame(list(col.find()))
print(df) """



""" app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'
# route home
@app.route('/')
def home():
    return render_template('plotupload.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        myf = request.files['file']
        fn = secure_filename(myf.filename)
        myf.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        with open(fn, 'r') as f:
            data = []
            x = []
            y = []
            reader = csv.reader(f)
            for d in reader:
                data.append(d)
            data.pop(0)
            for d2 in data:
                x.append(d2[0])
                y.append(d2[1])
            x = np.array(x)
            y = np.array(y)
            plt.plot(x, y, marker='.',linestyle='--', color='black', linewidth=1 )
            plt.title('Hasil plot dari data file yang di-upload')
            plt.xlabel('Sumbu X')
            plt.ylabel('Sumbu Y')
            plt.grid(True)
            plt.savefig('file/result.png')
            return redirect('/file/' + 'result.png')

@app.route('/file/<path:path>')
def aksesFile(path):
    return send_from_directory('file', path)
if __name__ == '__main__':
    app.run(debug = True) """

# Flask Upload file CSV to be plotted using plotly
""" app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './file'
# route home
@app.route('/')
def home():
    return render_template('plotupload.html')

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        myf = request.files['file']
        fn = secure_filename(myf.filename)
        myf.save(os.path.join(app.config['UPLOAD_FOLDER'], fn))
        with open(fn, 'r') as f:
            data = []
            x = []
            y = []
            reader = csv.reader(f)
            for d in reader:
                data.append(d)
            data.pop(0)
            for d2 in data:
                x.append(d2[0])
                y.append(d2[1])
            x = np.array(x)
            y = np.array(y)
            plot = go.Scatter(x = x, y = y)
            plot = [plot]
            plotJSON = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)
            return render_template('plotresult.html', x=plotJSON)

# @app.route('/file/<path:path>')
# def aksesFile(path):
#     return send_from_directory('file', path)
if __name__ == '__main__':
    app.run(debug = True)
 """