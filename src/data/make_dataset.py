import time

import requests

from data.processed.companies import companies
from src.utils.credentials.credentials import get_credentials
from src.constants.constants import SEARCH_ENGINE_SERVER


def send_company(company_id, name, logo_url):
    """
    Send a company information with the logo to the server
    :param company_id:
    :param name:
    :param logo_url:
    :return:
    """
    credentials = get_credentials()

    if credentials is None:
        print("Error: credentials not found")
        return None

    print("CARICO PRODOTTO...")

    response = requests.post(
        SEARCH_ENGINE_SERVER + "/api/projects/" + str(credentials["project_id"]) + "/resources/add",
        json={
            "api_key": credentials["api_key"],
            "name": name,
            "external_resource_id": company_id,
            "images_url": [logo_url]
        }
    )

    response = response.json()
    if response["status"] == "ERROR":
        print(response["message"])

    print("PRODOTTO " + name + " SINCRONIZZATO")


def synchronize_companies():
    """
    Send all local companies to the away project
    :return: bool
    """
    print(companies)

    for index, company in enumerate(companies):
        print(company["logo"])
        send_company(company["company_id"], company["name"], company["logo"])
        time.sleep(1.3)
