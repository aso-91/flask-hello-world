# ---- Flask Hello World ---- #
# import the Flask class from the flask package

from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello World!?????"


# adding dynamic route                  (a1)
# @app.route("/test")
# def search():
#     return "Hello"
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

# ** (2)
# @app.route("/integer/<int:value>")
# def int_type(value):
#     print(value + 1)
#     return "correct"
#
# @app.route("/float/<float:value>")
# def float_type(value):
#     print(value + 1)
#     return "correct"

# dynamic route that accepts slashes
# @app.route("/path/<path:value>")
# def path_type(value):
#     print(value)
#     return "correct"

# dynamic route with explicit status codes              (3)
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name)
    else:
        return "Not found", 404


if __name__ == "__main__":
    app.run()
