"""This module does blah blah."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """This module does blah blah."""
    return "Hello Porld !"

if __name__ == "__main__":
    app.run()
