from helpers import addition
from bottle import route, run
import sys


@route("/add/<a>/<b>")
@route("/add/<a>/<b>/")
def add(a, b):
    return addition(a, b) + "."


run(host="0.0.0.0", port=sys.argv[1], reloader=True)
