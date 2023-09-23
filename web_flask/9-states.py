#!/usr/bin/python3
"""This module defines a flask app
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def all_states():
    """This method/route returns all states"""
    states = storage.all(State)
    return render_template('9-states.html', state=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def play_with_states(id):
    """This method will display all states
        or a specific state given a valid state id
        together with its associated cities
    """
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state=state, mode='id')
    return render_template('9-states.html', state=states, mode='none')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
