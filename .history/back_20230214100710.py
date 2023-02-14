from flask import Flask
from pickle import GET
from flask import json, request, render_template

app = Flask(__name__)
dados = 0;
food = {
            "id" : len(dados) + 1,
            "name" : request.form['name'],
            "price" :  request.form['price'],
            "image": request.form['image'],
            "description" : request.form['description']
        }

@app.route('/', methods = ["GET"])
def info():

    return render_template("cardapio.html")


@app.route("/projetoCafeteria", methods = ["GET", "POST"])
def getDados():

    if request.method.lower() == "post": 
        dados.append(food)
        return json.dumps(food)

    return json.dumps(dados)

@app.route("/projetoCafeteria/<id>", methods = ["DELETE"])
def deleteFood(id):
    request.form['id']
    del food[]
        

if __name__ == '__main__':
    app.run()