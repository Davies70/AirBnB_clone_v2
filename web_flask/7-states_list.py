#!/usr/bin/python3
''' a script that starts a Flask web application '''

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def dict_states():
    ''' returns HTML page wit states and id '''
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def end_session(exc):
    ''' ends session after each request '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
