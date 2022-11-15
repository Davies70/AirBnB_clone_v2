#!/usr/bin/python3
''' a script that starts a Flask web application '''

from models import storage
from models.state import State


def dict_states():
    ''' returns HTML page wit states and id '''
    states = storage.all(State)
    for state in states:
        print(state)
