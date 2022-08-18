
from flask import Flask, render_template, request
from api_validation import validate
import db

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
    erro = ''
    # api de teste
    body = request.get_json()
    isvalid = validate.user(body)

    if isvalid == True:

        try:
            erro = cadastra_usuario(body)
            return "Salvo com sucesso"
        except:
            return erro
    else:

        return isvalid


app.route("/api/formulario_empresa", methods=["POST"])
def formulario_empresa():
    erro = ''
    # api de teste
    body = request.get_json()
    isvalid = validate.company(body)

    if isvalid == True:

        try:
            erro = db.cadastra_empresa(body)
            return "Salvo com sucesso"
        except:
            return erro
    else:

        return isvalid


app.route("/api/formulario_vaga", methods=["POST"])
def formulario_vaga():
    erro = ''
    # api de teste
    body = request.get_json()
    isvalid = validate.vaga(body)

    if isvalid == True:

        try:
            erro = db.cadastra_vaga(body)
            return "Salvo com sucesso"
        except:
            return erro
    else:

        return isvalid
