from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, Flask!"


@app.route("/<s>")
def hello_var(s):
    return f"Hello, fuck you {s}!"
