#!/usr/bin/python3

"""
    This module defines a simple flask app
    with two route definitions
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ This function defines the response
        to a http request for the root of our website
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """This functions defines the return value
        of our website at the route /hbnb
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
