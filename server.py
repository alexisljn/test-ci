"""This module does blah blah."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """This module does blah blah."""
    return "Hello Porld !"

@app.route('/<name_param>')
def name(name_param):
    """This function returns Hello <name_param>"""
    return "Hello {0}".format(name_param)

if __name__ == "__main__":
    app.run()
