from cgitb import html
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "/index.html"

app.run()