from pickle import GET
from flask import Flask, request, render_template, flash
import datetime



app = Flask(__name__)

@app.route("/", methods = ["GET"])
def API():
    
    {
        "id": 1,
        "Task": False,
        "hours": datetime.date,  
    }
 
    return render_template("index.html")


@app.route("/Tasks", methods = ["POST"])
def ADD():
    
    return API

@app.route("/Tasks", methods = ["PATH"])
def Refresh():
 
    return API

@app.route("/Tasks", methods = ["DELETE"])
def DEL():
 
    return API

app.run()