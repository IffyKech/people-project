from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/callback", methods=["GET"])
def callback():
    url = request.args["code"]
    return url

if __name__ == "__main__":
    app.run()
