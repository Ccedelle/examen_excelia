from helpers import addition
from bottle import route, run


@route("/add/<a>/<b>")
@route("/add/<a>/<b>/")
def add(a, b):
    return addition(a, b)


run(host="localhost", port=8080, reloader=True)
