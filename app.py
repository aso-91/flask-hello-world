# ---- Flask Hello World ---- #
# import the Flask class from the flask package

from flask import Flask

# create the application object
app = Flask(__name__)

# use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")

# define the view using a function, which returns a string
def hello_world():
    return "Hello World!"

# start the development server using the run() method
if __name__ == "__main__":
    app.run()

# This launches the development server that's listening on port 5000.
# Open a web browser and navigate to http://127.0.0.1:5000/.

#  http://127.0.0.1:5000 and http://localhost:5000 are equivalent.


#_______________________ What's going on here? ____________________
# Let's first look at the code without the view function:

# 1. We imported the Flask class
from flask import Flask

# 2. Next, an instance of the Flask class was created
app = Flask(__name__)

# 3. Finally, we used the run() method , to run it locally
if __name__ == "__main__":
    app.run()


#******* Check page 42 for links to Decorators..!!

from datetime import datetime

def not_during_night(func):
    def wrapper():
        if 7 >= datetime.now().hour > 22:
            func()
        else:
            pass # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("whee")


say_whee = not_during_night(say_whee)

@not_during_night
def say_whee():
    print("whee")

# @not_during_night is just an easier way of saying say_whee = not_during_night(say_whee).
# It’s how you apply a decorator to a function.