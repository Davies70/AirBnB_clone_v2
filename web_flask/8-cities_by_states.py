#!/usr/bin/python3
''' Flask app running on host=0.0.0.0, port=5000 '''
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_by_states():
    ''' display city by states '''
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def end_session(error):
    ''' closes session after each query '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
