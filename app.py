#Contractor Project Main App
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage"""
    return render_template('home_index.html')

if __name__=='__main__':
    app.run(debug=True)
