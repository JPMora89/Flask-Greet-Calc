# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_calc():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)
@app.route("/sub")
def sub_calc():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)
@app.route("/mult")
def mult_calc():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)
@app.route("/div")
def divide_calc():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)

Math_Operations = {
    "add": add,
    "subtract": sub,
    "multiply": mult,
    "divide": div
}

@app.route("/math/<operation>")
def calculation(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = Math_Operations[operation](a,b)

    return str(result)