from application.models import Cards, Sets


def test_new_card(new_card):

    assert new_card.cs_id == 1
    assert new_card.name == "Abundance"
    assert new_card.edition == "10E"
    assert new_card.is_foil == False


def test_new_set(new_set):

    assert new_set.cs_id == 772
    assert new_set.cs_name == "Avacyn Restored"
    assert new_set.mtgjson_code == "AVR"
