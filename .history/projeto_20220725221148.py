from pickle import GET
from flask import Flask, request, render_template, flash



app = Flask(__name__)

@app.route("/", methods = ["GET"])
def hello_world():
    
    {
        "id": 1,
        "name": "And So It Begins",
        "author": "Artificial.Music",
        
    }

    
    return render_template("index.html")

app.run()