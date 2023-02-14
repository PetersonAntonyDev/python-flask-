from pickle import GET
from flask import Flask, request, render_template, flash
import datetime

id = {1}
task = {False}

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def API():
    
    global id
    global task
 
    return (id, task)

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