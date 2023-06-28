def test_all_sets(test_client):

    response = test_client.get("/api/v1/sets")

    assert response.status_code == 200
    assert b"DCI Legend Membership" in response.data


def test_set_by_mtgjson_code(test_client):

    pass

def test_set_by_cs_id(test_client):

    pass