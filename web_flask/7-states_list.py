#!/usr/bin/python3
"""This module defines a flask app
    for AirBnB Clone
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """This view function/route will return a list
        of all State objects in our database
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def new_connection(error):
    """This function [decorated with app.teardown_appcontext]
        defines what happens after each request, specifically
        after the end of an app context.
        In this case, the current database connection is returned
        to the connection pool until the session is invoked again
        with a query
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
