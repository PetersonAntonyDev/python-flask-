from asyncio import tasks
from pickle import GET
from flask import Flask, request, render_template, flash
import datetime


tasks = {
    "id": 1,
    "task": False
}

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def API():
    
    global tasks
 
    return tasks

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