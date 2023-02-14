from pickle import GET
from flask import Flask, request, render_template, flash
import datetime



app = Flask(__name__)

@app.route("/Start", methods = ["GET"])
def API():
    
    request.get_json
    {
        "id": 1,
        "Task": False,
        "hours": datetime.date,  
    }
 
    return "<p>HELLO<p>"


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