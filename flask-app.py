from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/*')
def not_found():
    return redirect(url_for('home'))

