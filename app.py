#from crypt import methods
from flask import Flask, render_template, request
from app import app
import os

app = Flask(__name__)

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/great", methods=["POST"])
def greet():

    name = request.form.get("name")

    return render_template("great.html", name=name)


