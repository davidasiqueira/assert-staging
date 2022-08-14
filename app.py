
from flask import Flask, render_template, request
from api_validation import validate
from db import manipulate_data

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/great", methods=["POST"])
def greet():

    name = request.form.get("name")

    return render_template("great.html", name=name)


@app.route("/api/formulario_candidato", methods=["POST"])
def formulario_candidato():
    #api de teste
    body = request.get_json()
    isvalid = validate.user(body)

    if isvalid:
        
        try:
            manipulate_data(body)
            return "Salvo com sucesso"
        except:
            return "Erro ao salvar"        
    
    return isvalid

    