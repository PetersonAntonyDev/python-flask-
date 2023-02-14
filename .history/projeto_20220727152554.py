from asyncio import tasks
from pickle import GET
from flask import Flask, request, render_template, flash
import datetime


tasks = [{
    "id": 1,
    "task": False
}]

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def getTasks():
    
    global tasks
 
    return tasks

@app.route("/Tasks", methods = ["POST"])
def add():
    
    return 

@app.route("/Tasks", methods = ["PATH"])
def refresh():
 
    return 

@app.route("/Tasks", methods = ["DELETE"])
def delete():
 
    return 

app.run()