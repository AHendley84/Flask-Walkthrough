import os
# Import the Flask class.
from flask import Flask

# Create an instance of Flask and store it in a variable.
# The first argument of the Flask class is the name of the
# applications module: __name__
app = Flask(__name__)

# app.route decorator - Decorator is a way of wrapping functions
@app.route("/")
def index():
    return "Hello, World"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
    debug=True)