from asyncio import tasks
import json
from pickle import GET
from flask import Flask, request, render_template, flash



tasks = [{
    "id": 0,
    "task": False
}]

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def getTasks():
    
    global tasks
 
    return json.dumps(tasks)

@app.route("/", methods = ["POST"])
def addTasks():
    global tasks

    task = {
        "id": request.form['id'],
        "task": request.form['task']
    }

    tasks.append(task)

    return json.dumps(tasks)

@app.route("/", methods = ["PATH"])
def refreshTasks():

    global tasks

    task = {
        "id": request.form['id'],
        "task": request.form['task']
    }

    tasks.all_tasks(tasks)

    return json.dumps(task)

@app.route("/", methods = ["DELETE"])
def deleteTasks():
    global tasks

    task = {
        "id": request.form['id'],
        "task": request.form['task']
    }

    tasks.remove(task)

    return json.dumps(tasks)

@app.route("/interface", methods = ["GET"])
def interface():
    
    return render_template("index.html")

app.run()