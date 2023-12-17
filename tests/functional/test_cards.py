import requests


def test_index(test_client):

    response = test_client.get("/")

    assert response.status_code == 200
    assert b"Cardsphere community-built project" in response.data


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


def test_card_search_no_params(test_client):

    response = test_client.get("/api/v1/cards/search")

    assert response.status_code == 400
    assert b"Please enter at least one query parameter" in response.data


def test_card_search_name(test_client):

    response = test_client.get("/api/v1/cards/search?name=leyline")

    assert response.status_code == 200
    assert b"Leyline of Anticipation" in response.data


def test_card_search_name_and_edition(test_client):

    response = test_client.get("/api/v1/cards/search?name=leyline&edition=Gatecrash")

    assert response.status_code == 200
    assert b"Leyline Phantom" in response.data
    assert b"Gatecrash" in response.data


def test_card_search_name_and_coll_num(test_client):

    response = test_client.get("/api/v1/cards/search?name=leyline&collector_number=41")

    assert response.status_code == 200
    assert b"Leyline Phantom" in response.data
    assert b"41" in response.data


def test_card_search_name_and_is_foil(test_client):

    response = test_client.get("/api/v1/cards/search?name=leyline&is_foil=false")

    assert response.status_code == 200
    assert b"Leyline Phantom" in response.data
    assert b"false" in response.data


def test_card_search_name_and_mtgjson_code(test_client):

    response = test_client.get("/api/v1/cards/search?name=leyline&mtgjson_code=GTC")

    assert response.status_code == 200
    assert b"Leyline Phantom" in response.data
    assert b"GTC" in response.data


def test_card_search_all_params(test_client):

    response = test_client.get(
        "/api/v1/cards/search?name=leyline&edition=Gatecrash&collector_number=41&is_foil=false&mtgjson_code=GTC"
    )

    assert response.status_code == 200
    assert b"Leyline Phantom" in response.data
    assert b"GTC" in response.data
    assert b"false" in response.data
    assert b"Gatecrash" in response.data
    assert b"41" in response.data


def test_404(test_client):

    response = test_client.get("/api")

    assert response.status_code == 404
    assert b"404 Not Found" in response.data
