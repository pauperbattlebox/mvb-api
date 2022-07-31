import pytest

from application.models import Cards, Sets


@pytest.fixture(scope="module")
def new_card():

    new_card = Cards(cs_id=1, name="Abundance", edition="10E", is_foil=False)

    return new_card


@pytest.fixture(scope="module")
def new_set():

    new_set = Sets(cs_id=772, cs_name="Avacyn Restored", mtgjson_code="AVR")

    return new_set
