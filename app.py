from flask import Flask
from flask import request

app = Flask(__name__)


@app.get("/")
def hello():
    return "GET method by flask Hello, Flask!"


@app.route("/user/conf", methods=["POST"])
def hello_var():
    print(f"request method {request.method}")
    print(f"request form {request.form}")
    return f"request method {request.method}"
