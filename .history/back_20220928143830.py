from flask import Flask
from pickle import GET
from flask import json, request, render_template

dados = []

app = Flask(__name__)

@app.route('/', methods = ["GET"])
def info():

    return render_template("cardapio.html")


@app.route("/projetoCafeteria", methods = ["GET", "POST"])
def getDados():
    
    global dados

    if request.method.lower() == "post":
        dado = {
            "id" : len(dados) + 1,
            "name" : request.form['name'],
            "price" :  request.form['price'],
            "image": request.form['image'],
            "description" : request.form['description']
        }
        dados.append(dado)
        return json.dumps(dado)
        

    return json.dumps(dados)

"""
@app.route('/autenticar', methods = ["GET", "POST"])
def autenticar():

    name = request.args.get("name")
    price = request.args.get("pricess")
    description = request.args.get("description")

    return "name: {} \n preço: {} \n descrição: {}".format(name, price, description) """

if __name__ == '__main__':
    app.run()