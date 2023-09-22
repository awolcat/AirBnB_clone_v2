#!/usr/bin/python3

"""
    This module defines a simple flask app
    with two route definitions
"""
from flask import Flask
from markupsafe import escape
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


@app.route('/c/<text>')
def variable(text):
    """Capture text from a request
        on the c route
    """
    text = escape(text)
    text = text.replace('_', ' ')
    return f'C {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
