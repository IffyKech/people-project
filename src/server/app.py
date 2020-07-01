from flask import Flask, request
import requests
import configparser

app = Flask(__name__)

# access token when auth is accepted
token = ""
token_duration = 0

# TODO: ADDRESS CONNECTION CHECKPOINTS WITH TRY STATEMENT FOR WHOLE FUNCTION
# TODO: LOOK INTO WRITING ACCESS TOKEN INTO CONFIG AS WELL AS DURATION


def read_secrets():
    config = configparser.ConfigParser()
    config.read("config.ini")

    client_id = config["SECRETS"]["client_id"]
    client_secret = config["SECRETS"]["client_secret"]

    return client_id, client_secret


# shutdown the server when the authentication is processed
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/callback", methods=["GET"])
def callback():
    global token
    global token_duration

    # if the application is rejected
    if "error" in request.args:
        # TODO: CONNECTION CHECKPOINT
        return "<html><head></head><body><h1>401 Unauthorized</h1></body></html>"

    # if the application is accepted
    else:
        # authorization code from member approval
        auth_code = request.args["code"]

        # check for original authorization request
        auth_state = request.args["state"]

        # if a different state code was used (not the original auth request)
        if auth_state != "97b2ff2e09":
            # TODO: CONNECTION CHECKPOINT
            return "<html><head></head><body><h1>401 Unauthorized</h1></body></html>"

        # if the authorization request is authentic
        else:
            client_id, client_secret = read_secrets()
            redirect_uri = "http://127.0.0.1:5000/callback"
            body = {"grant_type": "authorization_code",
                    "code": auth_code,
                    "redirect_uri": redirect_uri,
                    "client_id": client_id,
                    "client_secret": client_secret
                    }
            config = {"Content-Type": "application/x-www-form-urlencoded"}

            # used to check if a token hasn't been received yet
            # set to 0 when app is run, changes when a token is received,
            if token_duration == 0:
                # TODO: CONNECTION CHECKPOINT
                response = requests.post("https://www.linkedin.com/oauth/v2/accessToken",
                                         data=body,
                                         headers=config)

                if response.status_code == 404 or response.status_code == 204:
                    # TODO: CONNECTION CHECKPOINT
                    return response.raise_for_status()

                else:
                    token_response = response.json()
                    token = token_response["access_token"]
                    token_duration = token_response["expires_in"]
                    # TODO: CONNECTION CHECKPOINT
                    return "<html><head></head><body><h1>Login Successful</h1></body></html>", shutdown()

            # if a token has already been received
            else:  # TODO: CONNECTION CHECKPOINT
                return "<html><head></head><body><h1>Already Logged In</h1></body></html>"


@app.route("/shutdown", methods=["POST"])
def shutdown_server():
    shutdown()
    return "Server shut down"


if __name__ == "__main__":
    app.run()
