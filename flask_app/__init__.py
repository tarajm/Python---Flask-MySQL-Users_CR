#__init__.py
from flask import Flask

app = Flask(__name__)
app.secret_key = "baboo"


#this creates a module for yoru flask app