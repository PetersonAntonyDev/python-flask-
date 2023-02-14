from pickle import GET
from flask import Flask, request, render_template, flash
import datetime



app = Flask(__name__)

@app.route("/", methods = ["GET"])
def API():
    
    {
        "id": 1,
        "Task": False,
    }
 
    return render_template("index.html", "style.css", "script.js")


@app.route("/Tasks", methods = ["POST"])
def ADD():
    
    return 

@app.route("/Tasks", methods = ["PATH"])
def Refresh():
 
    return 

@app.route("/Tasks", methods = ["DELETE"])
def DEL():
 
    return 

app.run()