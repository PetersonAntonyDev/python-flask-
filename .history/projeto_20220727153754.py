from asyncio import tasks
import json
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
 
    return json.dumps(tasks)

@app.route("/Tasks", methods = ["POST"])
def addTasks():
    def adc():
        adcTask = tasks
        adcTask.append(["id"], ["task"])
    

    return adc()

@app.route("/Tasks", methods = ["PATH"])
def refreshTasks():
 
    return 

@app.route("/Tasks", methods = ["DELETE"])
def deleteTasks():
    global tasks
    return json.dumps(tasks.remove(["id"]))

app.run()