import requests
from src.constants.constants import SEARCH_ENGINE_SERVER
from data.processed.companies import companies

def test_resources_delete(request):
    """
    Test resources deletion
    """
    for c in companies:
        response = requests.post(
            SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/resources/{c['company_id']}/delete",
            json={
                "api_key": request.config.cache.get('api_key', 0)
            }
        )
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['status'] == "OK"


def test_project_delete(request):
    """
    Test project deletion
    """
    response = requests.post(
        SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/delete",
        json={
            "api_key": request.config.cache.get('api_key', 0)
        }
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['status'] == "OK"


