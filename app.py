#Contractor Project Main App
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from bson.objectid import ObjectId
import os

client = MongoClient()
#db = client.get_default_database()
db = client.Fabrics
fabrics = db.fabrics
reviews = db.reviews

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage"""
    return render_template('home_index.html', fabrics=fabrics.find())

@app.route('/fabrics/new')
def fabrics_new():
    """Create a new playlist."""
    return render_template('fabrics_new.html', fabric={}, name='New Fabric')

#CREATE -------------------------------------------------------
@app.route('/fabrics', methods=['POST'])
def fabrics_submit():
    """Submit a new fabric."""
    fabric ={
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'price': request.form.get('price'),
        'source': request.form.get('source')
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
@app.route('/fabrics/<fabric_id>/edit')
def fabrics_edit(fabric_id):
    """ Show edit form for fabric sell page """
    fabric = fabrics.find_one({'_id': ObjectId(fabric_id)})
    return render_template('fabrics_edit.html', fabric=fabric, title='Edit Fabric Info')

@app.route('/fabrics/<fabric_id>', methods=['POST'])
def fabrics_update(fabric_id):
    updated_fabric = {
        'name': request.form.get('name'),
        'description': request.form.get('description'),
        'price': request.form.get('price'),
        'source': request.form.get('source')
    }
    fabrics.update_one(
        {'_id': ObjectId(fabric_id)},
        {'$set': updated_fabric})
    return redirect(url_for('fabrics_show', fabric_id=fabric_id))
#DESTROY / Delete ---------------------------------------------
@app.route('/fabrics/<fabric_id>/delete', methods=['POST'])
def fabrics_delete(fabric_id):
    """Delete one fabric listing."""
    fabrics.delete_one({'_id': ObjectId(fabric_id)})
    return redirect(url_for('index'))

#====================Review==================
# @app.route('/fabrics/reviews', methods=['POST'])
# def comments_new():
#     """Submit a new review."""
#     review = {
#         'title': request.form.get('title'),
#         'content': request.form.get('content'),
#         'review_id': ObjectId(request.form.get('review_id'))
#     }
#     print(review)
#     review_id = reviews.insert_one(comment).inserted_id
#     return redirect(url_for('playlists_show', playlist_id=request.form.get('playlist_id')))
# #Delete a Comment ----------------------------------------
# @app.route('/playlists/comments/<comment_id>', methods=['POST'])
# def comments_delete(comment_id):
#     """Action to delete a comment."""
#     comment = comments.find_one({'_id': ObjectId(comment_id)})
#     comments.delete_one({'_id': ObjectId(comment_id)})
#     return redirect(url_for('playlists_show', playlist_id=comment.get('playlist_id')))

if __name__=='__main__':
    app.run(debug=True)
