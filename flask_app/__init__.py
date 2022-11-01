from flask import Flask
DATABASE = "recipes"
app = Flask(__name__)
app.secret_key = "keepitsecret"