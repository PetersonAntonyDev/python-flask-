from pickle import GET
from flask import Flask, request, render_template, flash



app = Flask(__name__)

@app.route("/")
def hello_world(methods = ["GET"]):
    return render_template("index.html")

app.run()