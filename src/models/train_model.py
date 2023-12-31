import requests

from src.utils.credentials.credentials import get_credentials
from src.constants.constants import SEARCH_ENGINE_SERVER


def train():
    """
    Start a training on the server
    :return:
    """

    credentials = get_credentials()
    if credentials is None:
        print("Error: credentials not found")
        return None

    response = requests.post(
        SEARCH_ENGINE_SERVER + "/api/projects/" + str(credentials["project_id"]) + "/train",
        json={
            "api_key": credentials["api_key"]
        }
    )

    response = response.json()
    if response["status"] == "ERROR":
        print(response["message"])

    print(response["message"])


def apply_train():
    """
    Apply the training done by remote model
    :return:
    """

    credentials = get_credentials()
    if credentials is None:
        print("Error: credentials not found")
        return None

    response = requests.post(
        SEARCH_ENGINE_SERVER + "/api/projects/" + str(credentials["project_id"]) + "/apply-training",
        json={
            "api_key": credentials["api_key"]
        }
    )

    response = response.json()
    if response["status"] == "ERROR":
        print(response["message"])

    print(response["message"])