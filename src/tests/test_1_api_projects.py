import requests
from src.constants.constants import SEARCH_ENGINE_SERVER

project_test_name = 'My PyTest Project'
updated_project_test_name = 'My PyTest Project v2'


def test_create_project(request):
    """
    Test project creation
    """
    global _project_id_test, _project_api_test
    response = requests.post(
        SEARCH_ENGINE_SERVER + "/api/projects/create",
        json={
            "name": project_test_name, "selected_features_index": []
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status'] == "OK"
    assert response_json['project_id'] is not None
    assert response_json['api_key'] is not None
    request.config.cache.set('project_id', response_json['project_id'])
    request.config.cache.set('api_key', response_json['api_key'])


def test_project_exists(request):
    response = requests.get(
        SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}",
        params={
            "api_key": request.config.cache.get('api_key', 0)
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status'] == "OK"
    assert response_json['project'] is not None
    assert response_json['project']['name'] == project_test_name


def test_update_project(request):
    """
    Test project update
    """
    response = requests.post(
        SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/update",
        json={
            "name": updated_project_test_name, "selected_features_index": [],
            "api_key": request.config.cache.get('api_key', 0)
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status'] == "OK"


def test_project_edited(request):
    response = requests.get(
        SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/get",
        params={
            "api_key": request.config.cache.get('api_key', 0)
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status'] == "OK"
    assert response_json['project'] is not None
    assert response_json['project']['name'] == updated_project_test_name
