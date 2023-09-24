#!/usr/bin/python3
"""This module defines a flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Render html page with State, City,
        and Amenity data
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def end_connection(error):
    """Hook method, runs at end of request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
