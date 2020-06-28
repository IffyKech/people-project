import sqlite3 as sql
import os
import webbrowser
import configparser

# import time


# TODO: CREATE MORE MODULES (interface, funcs e.t.c) TO CLEAN UP CODE




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
    with open("src/secrets.txt", 'r') as f:
        client_id = f.readline().strip("\n")
        client_secret = f.readline()
        return client_id, client_secret


def request_auth_code():
    client_id, client_secret = read_secrets()
    redirect_uri = "http://127.0.0.1:5000/callback"
    webbrowser.open("https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={}"
                    "&redirect_uri={}&state=97b2ff2e09&scope=r_liteprofile"
                    "%20r_emailaddress".format(client_id, redirect_uri), 1)


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


# def get_path(path_to_get):
#     """
#     Get the path of a directory indicated by argument. Reads the JSON file of paths and returns the value(path) of the
#     key(path_to_get).
#
#     :param path_to_get: string - key of the JSON object pointing to the path of the key
#     :return: string - path of the directory
#     """


def write_config():
    """
    Write the config file containing the PATHS section, including: src_path and applications_path,
    also with the SECRETS section, including: client_id, client_secret.

    :return:
    """
    config = configparser.ConfigParser()

    root_path = os.getcwd()
    src_path = root_path + "\src"

    # raw string (ignores the string literal: \a)
    applications_path = src_path + r'\applications'

    config["PATHS"] = {"root_path" : root_path,
                       "src_path" : src_path,
                       "applications_path": applications_path}

    config["SECRETS"] = {"client_id": "7821200o7f56h2",
                         "client_secret": "HOvue2xKkF97PbmJ"}

    with open("config.ini", 'w') as cf:
        config.write(cf)

def init():
    # if a config file doesn't exist
    if not doesfileexist("config.ini"):
        write_config()

    #if the config file does exist
    else:
        config = configparser.ConfigParser()

        config.read("config.ini")

        # if the config root path is not the same path as the current directory
        



def main():
    init()
    # try:
    #     request_auth_code()
    #     app.app.run()
    #     main_window = tk.Tk()
    #     MainWindow(main_window)
    #     main_window.mainloop()
    #
    # except Exception as err:
    #     print(err)
    #     input()



if __name__ == "__main__":
    main()

