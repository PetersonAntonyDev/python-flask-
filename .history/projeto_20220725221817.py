from pickle import GET
from flask import Flask, request, render_template, flash
import datetime



app = Flask(__name__)

@app.route("/Start", methods = ["GET"])
def hello_world():
    
    {
        "id": 1,
        "Task": False,
        "hours": datetime.date,
        
    }

    
    return render_template("index.html")


@app.route("/Tasks", methods = ["POST"])
def hello_world():
 
    return render_template("index.html")
app.run()