from flask import Flask, request
import requests
from src import secrets


app = Flask(__name__)

token = ""
token_duration = 0


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/callback", methods=["GET"])
def callback():
    global token
    global token_duration

    redirect_uri = "http://127.0.0.1:5000/callback"

    # authorization code from member approval
    auth_code = request.args["code"]

    # check for original authorization request
    auth_state = request.args["state"]
    if auth_state != "97b2ff2e09":
        return "<html><head></head><body><h1>401 Unauthorized</h1></body></html>"
    
    body = {"grant_type" : "authorization_code",
            "code" : auth_code,
            "redirect_uri" : redirect_uri,
            "client_id" : secrets.client_id,
            "client_secret" : secrets.client_secret
            }
    config = {"Content-Type" : "application/x-www-form-urlencoded"}

    # used to check if a token hasn't been received yet
    # set to 0 when app is run, changes when a token is received,
    if token_duration == 0:
        response = requests.post("https://www.linkedin.com/oauth/v2/accessToken",
                                 data = body,
                                 headers = config)

        if response.status_code == 404 or response.status_code == 204:
            return response.raise_for_status()

        else:
            token_response = response.json()
            token = token_response["access_token"]
            token_duration = token_response["expires_in"]
            return "<html><head></head><body><h1>Login Successful</h1></body></html>"

    # if a token has already been received
    else:
        return "<html><head></head><body><h1>Already Logged In</h1></body></html>"


if __name__ == "__main__":
    app.run()
