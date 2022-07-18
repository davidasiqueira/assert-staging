#from crypt import methods
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///assert.db3'
db = SQLAlchemy(app)

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
    print(body)
    return "200"

    