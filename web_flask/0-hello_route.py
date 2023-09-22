#!/usr/bin/python3

"""
    This module defines the simplest flask app possible
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ This function defines the response
        to a http request for the root of our website
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
