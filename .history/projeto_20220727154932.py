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

@app.route("/tasks", methods = ["POST"])
def addTasks():
    global tasks

    task = {
        "id": request.form['id'],
        "task": request.form['task']
    }

    tasks.append(task)

    return json.dumps(tasks)

@app.route("/tasks", methods = ["PATH"])
def refreshTasks():

    global tasks

    task = {
        "id": request.form['id'],
        "task": request.form['task']
    }

    

    return json.dumps(tasks)

@app.route("/tasks", methods = ["DELETE"])
def deleteTasks():
    global tasks

    task = {
        "id": request.form['id'],
        "task": request.form['task']
    }

    tasks.remove(task)

    return json.dumps(tasks)

app.run()