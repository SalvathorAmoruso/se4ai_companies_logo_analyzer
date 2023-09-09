import requests
from src.constants.constants import SEARCH_ENGINE_SERVER
from data.processed.companies import companies


def test_resources_add(request):
    """
    Test resources add to the "test project"
    """
    for c in companies:
        response = requests.post(
            SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/resources/add",
            json={
                "api_key": request.config.cache.get('api_key', 0), "name": c["name"], "external_resource_id": c["company_id"],
                "images_url": [c["logo"]]
            }
        )
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['status'] == "OK"
        assert response_json['resource_id'] is not None


def test_resources_images_added(request):
    """
    Test resources add to the "test project"
    """
    for c in companies:
        response = requests.get(
            SEARCH_ENGINE_SERVER + f"/api/projects/{request.config.cache.get('project_id', 0)}/resources/{c['company_id']}/images",
        )
        assert response.status_code == 200
        response_json = response.json()
        assert response_json['status'] == "OK"
        assert response_json['images'] is not None
        assert response_json['images'][0]['url'] == c["logo"]
