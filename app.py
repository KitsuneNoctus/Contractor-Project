#Contractor Project Main App
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os

client = MongoClient()
db = client.Fabrics
fabrics = db.fabrics

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage"""
    return render_template('home_index.html', fabrics=fabrics.find())

#CREATE -------------------------------------------------------
#READ ---------------------------------------------------------
@app.read('/fabrics/<fabric_id>')
def fabrics_show(fabric_id):
    """Show single fabric item"""
    fabric = fabrics.find_one({'_id': ObjectId(fabric_id)})
    return render_template('fabrics_show.html', fabric=fabric)
    pass
#UPDATE -------------------------------------------------------
#DESTROY ------------------------------------------------------

if __name__=='__main__':
    app.run(debug=True)
