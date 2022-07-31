from application import create_app


def test_index():

    flask_app = create_app()

    flask_app.config.from_pyfile("config.py")   

    with flask_app.test_client() as test_client:

        response = test_client.get("/")

        assert response.status_code == 200
        assert b"Cardsphere community-built project" in response.data
