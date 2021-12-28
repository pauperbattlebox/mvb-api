from marshmallow import Schema, fields
from application.models import Sets, Cards

class SetsSchema(Schema):

    cs_id = fields.Int()
    cs_name = fields.Str()
    mtgjson_code = fields.Str()
    related_mtgjson_codes = fields.List(fields.Str())

set_schema = SetsSchema()
sets_schema = SetsSchema(many=True)

class CardsSchema(Schema):

    cs_id = fields.Int()
    url = fields.Str()
    name = fields.Str()
    edition = fields.Str()
    is_foil = fields.Boolean()
    mtgjson_id = fields.Str()
    scryfall_id = fields.Str()
    collector_number = fields.Str()
    mtgjson_code = fields.Str()

card_schema = CardsSchema()
cards_schema = CardsSchema(many=True)

class SetsWithCardsSchema(SetsSchema):

    cards = fields.List(fields.Nested(CardsSchema()))

    class Meta:
        ordered = True

set_with_cards_schema = SetsWithCardsSchema()
sets_with_cards_schema = SetsWithCardsSchema(many=True)

class CardsWithRelatedPrintingsSchema(CardsSchema):

    related_printings = fields.List(fields.Nested(CardsSchema()))

    class Meta:
        ordered = True

card_with_related_printings_schema = CardsWithRelatedPrintingsSchema()
cards_with_related_printings_schema = CardsWithRelatedPrintingsSchema(many=True)
