from application.models import Cards


def get_card_by_cs_id(cs_id: int) -> Cards:

    card = Cards.query.filter(Cards.cs_id == cs_id).first_or_404()

    return card


def get_cards_by_mtgjson_id(mtgjson_id: str) -> Cards:

    cards = Cards.query.filter(Cards.mtgjson_id == mtgjson_id).all()

    return cards


def get_cards_by_scryfall_id(scryfall_id: str) -> Cards:

    cards = Cards.query.filter(Cards.scryfall_id == scryfall_id).all()

    return cards


def get_cards_by_attribue(args: dict) -> Cards:

    filtered_args = dict()

    for (k, v) in args.items():
        if v and k != "name" and k != "is_foil":
            filtered_args[k] = v

    cards = Cards.query

    if "name" in args and args["name"] != None:

        search_term = args["name"]
        search = f"%{search_term}%"
        cards = cards.filter(Cards.name.ilike(search))

    if "is_foil" in args and args["is_foil"] != None:
        cards = cards.filter(Cards.is_foil == args["is_foil"])

    cards = cards.filter_by(**filtered_args).limit(100)

    cards.all()

    return cards
