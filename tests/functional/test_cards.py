def test_index(test_client):

    response = test_client.get("/")

    assert response.status_code == 200
    assert b"Cardsphere community-built project" in response.data


def test_cards_post(test_client):

    response = test_client.post("/api/v1/cards/cs/1")

    assert response.status_code == 405

def test_cache(test_client):

    response = test_client.get("/api/v1/cache")

    assert b"last_updated" in response.data
