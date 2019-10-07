#Contractor Project Main App
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os

client = MongoClient()
#
db = client.Fabrics
fabrics = db.fabrics

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage"""
    return render_template('home_index.html', fabrics=fabrics.find())

@app.route('/fabrics/new')
def playlists_new():
    """Create a new playlist."""
    return render_template('playlists_new.html', playlist={}, title='New Fabric')

#CREATE -------------------------------------------------------
@app.route('/fabrics', methods=['POST'])
def fabrics_submit():
    """Submit a new fabric."""
    fabric ={
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'price': request.form.get('price'),
        'description': request.form.get('description')
    }
    fabric_id = fabrics.insert_one(fabric).inserted_id
    return redirect(url_for('fabrics_show', fabric_id=fabric_id))
    pass
#READ ---------------------------------------------------------
@app.route('/fabrics/<fabric_id>')
def fabrics_show(fabric_id):
    """Show single fabric item"""
    fabric = fabrics.find_one({'_id': ObjectId(fabric_id)})
    return render_template('fabrics_show.html', fabric=fabric)
    pass
#UPDATE -------------------------------------------------------
#DESTROY ------------------------------------------------------

if __name__=='__main__':
    app.run(debug=True)
