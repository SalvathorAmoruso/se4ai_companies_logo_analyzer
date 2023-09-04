import json

import requests
from constants.constants import SEARCH_ENGINE_SERVER


def create_project():
    """
    Allows to create logos company project on API server
    :return: Void
    """

    # Request to create
    response = requests.post(
        SEARCH_ENGINE_SERVER + "/api/projects/create",
        json={"name": "logos_company", "selected_features_indexes": []}
    )

    if response.status_code != 200:
        print("Error: Project not created")
        return 0

    response = response.json()
    if response["STATUS"] == "ERROR":
        print(response["message"])

    credentials = {
        "api_key": response["api_key"],
        "project_id": response["project_id"]
    }

    with open("credentials.txt", "w") as file:
        json.dump(credentials, file)

    print("Credentials saved to 'credentials.txt' file.")