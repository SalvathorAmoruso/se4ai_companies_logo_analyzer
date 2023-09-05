import requests
import mlflow
import mlflow.pyfunc

from src.constants.constants import SEARCH_ENGINE_SERVER
from src.utils.credentials.credentials import get_credentials


def get_similar_items(url):
    """
    get similar items to passed with params
    """

    credentials = get_credentials()
    if credentials is None:
        print("Error: credentials not found")
        return None

    print("SENDING REQUEST...")

    # Initialize MLflow run
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    with mlflow.start_run():

        response = requests.get(
            SEARCH_ENGINE_SERVER + "/api/projects/search",
            params={
                "api_key": credentials["api_key"],
                "project_id": str(credentials["project_id"]),
                "limit": str(3),
                "image_url": url,
                "html": 0,
            }
        )

        # Log relevant information to MLflow
        mlflow.log_param("url", url)
        mlflow.log_param("limit", 3)

        response = response.json()
        if response["STATUS"] == "ERROR":
            print(response["message"])

        print(response["results"])

        if response["results"]:
            for result in response["results"]:

                resource = result["resource"]

                mlflow.log_metric("distance", value=result["distance"])
                """
                mlflow.log_param(resource["external_resource_id"]+"_distance", result["distance"])
                mlflow.log_param(resource["external_resource_id"]+"_name", resource["name"])
                mlflow.log_param(resource["external_resource_id"]+"_image_url", result["image_url"])
                mlflow.log_artifact(resource["external_resource_id"]+"_image_url", result["image_url"])
                """


    mlflow.end_run()
