#!/usr/bin/python3

"""
    This module defines a simple flask app
    with two route definitions
"""
from flask import Flask, render_template
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


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    """Capture text from a request
        url on the c route
    """
    text = escape(text)
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def default_var(text='is cool'):
    """Capture text from a request
        url on the python route
    """
    text = escape(text)
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def mustbe_int(n):
    """Capture part of the url
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render a template only if n is
        an integer
    """
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
