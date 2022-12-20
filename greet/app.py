from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome_screen():
    return "Welcome!"

@app.route("/welcome/home")
def welcome_home_screen():
    return "Welcome home!"

@app.route("/welcome/back")
def welcome_back():
    return "Welcome back!"
