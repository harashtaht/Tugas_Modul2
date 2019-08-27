from flask import Flask, render_template, url_for, redirect, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/cv')
def cv_temp():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug = True,
        host = 'localhost',
        port = 1400
    )