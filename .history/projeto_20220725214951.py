from pickle import GET
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world(methods = ["GET"]):
    return "<p>Hello, World!</p> <h1>OLA MUNDO</h1>"

app.run()