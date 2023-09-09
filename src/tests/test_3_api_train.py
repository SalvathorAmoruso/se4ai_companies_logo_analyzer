import requests
from src.constants.constants import SEARCH_ENGINE_SERVER
from data.processed.companies import companies
import time

def test_project_train(request):
    """
    Test project training
    """
    response = requests.post(
        SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/train",
        json={
            "api_key": request.config.cache.get('api_key', 0)
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status'] == "OK"


def test_project_train_finish(request):
    """
    Test if project train finished
    """
    response_json = None
    while response_json is None or response_json['project']['selected_features_indexes'] == '':
        time.sleep(2)
        response = requests.get(
            SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}",
            params={
                "api_key": request.config.cache.get('api_key', 0)
            }
        )
        response_json = response.json()
    assert response_json['project']['selected_features_indexes'] != ''


def test_project_apply_train(request):
    """
    Test if project training is applied on resource's features set
    """
    for c in companies:
        response = requests.post(
            SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/apply-training",
            json={
                "api_key": request.config.cache.get('api_key', 0)
            }
        )
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['status'] == "OK"
