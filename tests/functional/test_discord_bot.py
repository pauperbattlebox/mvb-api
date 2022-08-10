import requests

def test_card_search_name(test_client):

    pass

def test_card_search_name_and_mtgjson_code(test_client):

    pass

def test_card_search_no_params(test_client):

    pass

def test_card_search_no_name(test_client):

    pass

def test_card_search_400(test_client):

    pass

def test_card_search_404(test_client):

    pass

def test_card_price(test_client):

    pass

def test_card_price_404(test_client):

    pass

def test_card_price_400(test_client):

    pass


# def test_card_search_no_params(test_client):
#
#     response = test_client.get("/api/v1/cards/search")
#
#     assert response.status_code == 400
#
#
# def test_card_search_name(test_client):
#
#     response = test_client.get("/api/v1/cards/search?name=leyline")
#
#     assert response.status_code == 200
#     assert b"Leyline of Anticipation" in response.data
