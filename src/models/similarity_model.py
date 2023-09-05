import requests

from src.constants.constants import SEARCH_ENGINE_SERVER
from src.utils.credentials.credentials import get_credentials


def get_similar_items():
    """
    get similar items to passed with params
    """

    credentials = get_credentials()
    if credentials is None:
        print("Error: credentials not found")
        return None

    print("SENDING REQUEST...")

    response = requests.get(
        SEARCH_ENGINE_SERVER + "/api/projects/search",
        params={
            "api_key": credentials["api_key"],
            "project_id": str(credentials["project_id"]),
            "limit": str(3),
            "image_url": "https://blog.giallozafferano.it/allacciateilgrembiule/"
                         "wp-content/uploads/2021/01/patatine-fritte-fatte-in-casa.jpg",
            "html": 0,
        }
    )

    response = response.json()
    if response["STATUS"] == "ERROR":
        print(response["message"])

    print(response["results"])
