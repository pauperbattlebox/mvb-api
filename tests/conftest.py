import pytest

from application import create_app
from application.extensions import limiter
from application.models import Cards, Sets


@pytest.fixture(scope="module")
def new_card():

    new_card = Cards(cs_id=1, name="Abundance", edition="10E", is_foil=False)

    return new_card


@pytest.fixture(scope="module")
def new_set():

    new_set = Sets(cs_id=772, cs_name="Avacyn Restored", mtgjson_code="AVR")

    return new_set


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()

    flask_app.config.from_object("application.config.TestConfig")

    with flask_app.test_client() as testing_client:
        limiter.enabled = False
        with flask_app.app_context():
            yield testing_client
