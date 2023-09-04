import json


def get_credentials():
    """
    If credentials exists they are get from file
    :return: object
    """
    try:
        with open("credentials.txt", "r") as file:
            credentials = json.load(file)
        return credentials
    except FileNotFoundError:
        print("Error: File 'credentials.txt' not found.")
        return None
