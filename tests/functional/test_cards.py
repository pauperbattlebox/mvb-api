import requests

def test_index(test_client):

    response = test_client.get("/")

    assert response.status_code == 200
    assert b"Cardsphere community-built project" in response.data


def test_cards_post(test_client):

    response = test_client.post("/api/v1/cards/cs/1")

    assert response.status_code == 405

def test_cache(test_client):

    response = test_client.get("/api/v1/cache")

    assert response.status_code == 200
    assert b"last_updated" in response.data

def test_all_cards(test_client):

    response = test_client.get("/api/v1/cards")
    redirect = requests.get("https://cdn.multiversebridge.com/all_ids.json")

    assert response.status_code == 302
    assert "9cb62c63-8fba-51a5-a8c6-aa788c13d6a5" in redirect.text

def test_mtgjson():

    response = requests.get("https://cdn.multiversebridge.com/mtgjson_build.json")

    print(response.text)

    assert response.status_code == 200
    assert "15947b20-8c8e-42ed-9599-8b180a382d21" in response.text
