#!/usr/bin/python3
""" Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
 - /: display “Hello HBNB!”
 - /hbnb: display “HBNB”
 - /c/<text>: display “C ” \
         followed by the value of the text variable \
         (replace underscore _ symbols with a space )
 - /python/(<text>): display “Python ”, \
         followed by the value of the text variable \
         (replace underscore _ symbols with a space )
         The default value of text is “is cool”
 - /number/<n>: display “n is a number” only if n is an integer
 - /number_template/<n>: display a HTML page only if n is an integer
 - You must use the option strict_slashes=False in your route definition """

from flask import Flask, abort, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """ minimal flask app"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def name(text):
    """ returns C and name """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ returns Python is cool on default, else text string """
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """returns only integers"""
    try:
        num = int(n)
        return "{} is a number".format(num)
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def return_page(n):
    """returns HTML page if number is int"""
    try:
        number = int(n)
        return render_template('5-number.html', number=number)
    except ValueError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
