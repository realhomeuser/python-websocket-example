# coding: utf-8
from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shutdown')
def shutdown():
    return render_template('shutdown.html')