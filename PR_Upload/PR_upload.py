from flask import Flask, send_from_directory, jsonify, render_template, abort, redirect, request
import plotly, json, os
import plotly.graph_objects as go
import chart_studio.plotly as py
import numpy as np
import pandas as pd
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt

app=Flask(__name__)
app.config['UPLOAD FOLDER'] = './static/upload'

@app.route('/')
def home():
    return render_template('uploadcsv.html')

@app.route('/plotly', methods=['POST'])
def plotlyhehe():
    request.method == 'POST'
    myFile = request.files['MyFile']
    fn = secure_filename(myFile.filename)
    myFile.save(os.path.join(app.config['UPLOAD FOLDER'], fn))
    df = pd.read_csv(os.path.join(app.config['UPLOAD FOLDER'], fn))
    x = list(df['x'])
    y = list(df['y'])
    trace = go.Scatter(
        x=x, 
        y=y)
    data = [trace]
    graphJson = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('visualsatu.html', x = graphJson)


@app.route('/matplotlib', methods=['POST'])
def matplotlibhehe():
    request.method == 'POST'
    myFile = request.files['MyFile']
    fn = secure_filename(myFile.filename)
    myFile.save(os.path.join(app.config['UPLOAD FOLDER'], fn))
    df = pd.read_csv(os.path.join(app.config['UPLOAD FOLDER'], fn))
    x = list(df['x'])
    y = list(df['y'])
    plt.plot(x,y, linestyle='-', marker='o', color='red')
    plt.title('Plotting Data Using Matplotlib', fontdict={'fontsize':30})
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.savefig('./static/upload/graphs.png')
    return render_template('visualdua.html')

if __name__ == '__main__':
    app.run(debug=True,
    host= 'localhost',
    port= 4400)