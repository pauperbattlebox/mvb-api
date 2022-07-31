from application import create_app


def test_index():

    flask_app = create_app()

    with flask_app.test_client() as test_client:

        # test_client.config.from_pyfile("config.py")

        response = test_client.get("/")

        assert response.status_code == 200
        assert b"Cardsphere community-built project" in response.data
