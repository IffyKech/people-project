import sqlite3 as sql
import os
import webbrowser
import configparser
import sys
from tkinter import messagebox
import src.applications.home.app as mainwindow
import src.server.app as server


# TODO: WORK ON CODE WORKFLOW, AND MAKING REQUESTS


def doesfileexist(filetofind):
    for file in os.listdir():
        if filetofind == file:
            return True
    return False


def createdatabase():
    database = sql.connect("contacts.sqlite3")

    databasecursor = database.cursor()
    databasecursor.execute("""CREATE TABLE Contacts(Firstname TEXT, Lastname TEXT, Location TEXT, Number TEXT,
     Email TEXT, FieldOfWork TEXT, Source TEXT, Occupation TEXT)""")

    database.commit()
    database.close()


def read_secrets():
    config = configparser.ConfigParser()
    config.read("config.ini")

    client_id = config["SECRETS"]["client_id"]
    client_secret = config["SECRETS"]["client_secret"]

    return client_id, client_secret


# def linkedinLogin():
#     """
#     Open the authentication page, then start the web server. Waits for the user to authenticate, then processes the
#     authentication in the webserver. Once complete, the server is shutdown and tk window is run.
#
#     :return:
#     """
#     request_auth_code()
#     app.app.run()
#     # wait for authentication
#     page_response = ""
#     while len(page_response) < 1:


def write_config():
    """
    Write the config file containing the PATHS section, including: src_path and applications_path,
    also with the SECRETS section, including: client_id, client_secret.

    :return:
    """
    config = configparser.ConfigParser()

    root_path = os.getcwd()
    src_path = root_path + r"\src"

    # raw string (ignores the string literal: \a)
    applications_path = src_path + r'\applications'

    config["PATHS"] = {"root_path": root_path,
                       "src_path": src_path,
                       "applications_path": applications_path}

    config["SECRETS"] = {"client_id": "7821200o7f56h2",
                         "client_secret": "HOvue2xKkF97PbmJ"}

    with open("config.ini", 'w') as cf:
        config.write(cf)


def rewrite_config_paths():
    """
    Rewrite the PATHS values in the config file. This is done incase the application's directory is moved.

    :return:
    """
    config = configparser.ConfigParser()

    # read the config file
    config.read("config.ini")

    root_path = os.getcwd()
    src_path = root_path + r"\src"
    applications_path = src_path + r'\applications'

    # set/change the current paths
    config.set("PATHS", "root_path", root_path)
    config.set("PATHS", "src_path", src_path)
    config.set("PATHS", "applications_path", applications_path)

    # rewrite the paths
    with open("config.ini", 'w') as cf:
        config.write(cf)


def get_paths():
    """
    Get the paths in the config file

    :return: array - array of paths in the config file
    """
    config = configparser.ConfigParser()
    config.read("config.ini")

    paths = []

    for key in config["PATHS"]:
        paths.append(config["PATHS"][key])

    return paths


def validate_paths():
    """
    Checks if the application's directory has been moved and the path is no longer the same. If so, rewrites the config
    paths to match the path of the current directory

    :return: boolean - True if the directory has not been moved, False if the directory has been moved
    """
    config = configparser.ConfigParser()
    config.read("config.ini")

    if config["PATHS"]["root_path"] == os.getcwd():
        return True

    return False


def validate_sys_paths(paths):
    """
    Check if ALL of the paths in the config file are in sys.path

    :param paths: Array - string array of paths in the config file
    :return: boolean - True if the paths are in sys.path, False if not all of the paths are in sys.path
    """
    paths_set = set(paths)
    sys_set = set(sys.path)

    if paths_set.issubset(sys_set):
        return True

    return False


def update_sys_path(paths):
    """
    Update sys.path to contain the paths in the application's directory

    :param paths: Array - string array of paths in config file
    :return:
    """
    for path in paths:
        if path not in sys.path:
            sys.path.insert(1, path)


def init():
    # if a config file doesn't exist
    if not doesfileexist("config.ini"):
        write_config()

    # if the config file does exist
    else:
        # check if the config paths are valid
        if not validate_paths():
            rewrite_config_paths()

    # check if paths are in sys.path
    paths = get_paths()
    if not validate_sys_paths(paths):
        update_sys_path(paths)

    # END OF init()


def request_auth_code():
    client_id, client_secret = read_secrets()
    redirect_uri = "http://127.0.0.1:5000/callback"
    webbrowser.open("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={}"
                    "&redirect_uri={}&state=97b2ff2e09&scope=r_liteprofile"
                    "%20r_emailaddress".format(client_id, redirect_uri), 1)


def main():
    init()
    # for path in sys.path:
    #     print(path)
    try:
        request_auth_code()
        server.app.run()

        """ THIS WILL NOT RUN UNTIL THE SERVER IS SHUTDOWN"""
        # if a token wasn't received (due to error)
        if server.token == "":
            messagebox.showerror("Authentication Error", "Error occurred during authentication\nPlease try again later")

        # if a token was received (accepted auth)
        else:
            # run the application
            mainwindow.main()

    except Exception as err:
        print(err)
        input()


if __name__ == "__main__":
    main()
