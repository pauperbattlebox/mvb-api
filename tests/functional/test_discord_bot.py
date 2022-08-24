import requests


def test_card_search_name(test_client):

    response = test_client.get("/api/v1/discord/cards/search?name=Black Lotus")

    assert response.status_code == 200
    assert b"cs_id" in response.data


def test_card_search_name_and_mtgjson_code(test_client):

    response = test_client.get(
        "/api/v1/discord/cards/search?name=Black Lotus&mtgjson_code=LEA"
    )

    assert response.status_code == 200
    assert b"cs_id" in response.data
    assert b"24536" in response.data


def test_card_search_no_params(test_client):

    response = test_client.get("/api/v1/discord/cards/search")

    assert response.status_code == 400
    assert b"name missing" in response.data


def test_card_search_no_name(test_client):

    response = test_client.get("/api/v1/discord/cards/search?name=")

    assert response.status_code == 400
    assert b"name missing" in response.data


def test_card_search_wrong_params(test_client):

    response = test_client.get("/api/v1/discord/cards/search?day=night")

    assert response.status_code == 400
    assert b"name missing" in response.data


def test_card_price(test_client):

    response = test_client.get("/api/v1/discord/cards/price/Black Lotus")

    assert response.status_code == 200
    assert b"Black Lotus" in response.data


def test_card_price_404(test_client):

    response = test_client.get("/api/v1/discord/cards/price/Josh, Bridge Four")

    assert response.status_code == 404
    assert b"404 Not Found" in response.data
