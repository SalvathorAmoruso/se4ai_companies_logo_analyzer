import json
import os

import requests
import mlflow
import mlflow.pyfunc

from src.constants.constants import SEARCH_ENGINE_SERVER, ROOT_DIR
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
        if response["status"] == "ERROR":
            print(response["message"])

        print(response["results"])

        if response["results"]:
            for result in response["results"]:
                # Foreach result store metric distance in ml flow
                mlflow.log_metric("distance", value=result["distance"])
                pass

            # Store file with results in json in a folder
            with open(os.path.join(ROOT_DIR + "/src/models/similarity_model_results", "results.json"), 'w') as file:
                json.dump(response["results"], file)

            mlflow.log_artifact(ROOT_DIR + "/src/models/similarity_model_results/results.json")

    mlflow.end_run()
