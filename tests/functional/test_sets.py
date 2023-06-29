def test_all_sets(test_client):

    response = test_client.get("/api/v1/sets")

    assert response.status_code == 200
    assert b"DCI Legend Membership" in response.data


def test_set_by_mtgjson_code(test_client):

    response = test_client.get("/api/v1/sets/mtgjson/8ED")

    assert response.status_code == 200
    assert b"0d73fa6f-f730-551d-a15a-09b4b1857f5d" in response.data
    assert b"Intrepid Hero" in response.data


def test_set_by_cs_id(test_client):

    response = test_client.get("/api/v1/sets/cs/965")

    assert response.status_code == 200
    assert b"Archenemy: Nicol Bolas" in response.data


def test_set_by_cs_id_not_found(test_client):

    response = test_client.get("/api/v1/sets/cs/1")

    assert response.status_code == 404
