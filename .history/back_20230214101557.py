from flask import Flask
from pickle import GET
from flask import json, request, render_template

app = Flask(__name__)
dados = 0
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
    idFood = request.form['id']
    for foods in food:
        if idFood == food["id"]:
            dados.remove(food)
            return json.dumps(food)
    return {"message":"Doesn't exist"}, 404
        

if __name__ == '__main__':
    app.run()