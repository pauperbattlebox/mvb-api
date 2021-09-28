from marshmallow import Schema, fields
from application.models import Sets, Cards

class SetsSchema(Schema):

    cs_id = fields.Int()
    cs_name = fields.Str()
    # mtgjson_code = fields.Str()
    # map = fields.Str()

set_schema = SetsSchema()
sets_schema = SetsSchema(many=True)

class CardsSchema(Schema):

    cs_id = fields.Int()
    url = fields.Str()
    name = fields.Str()
    #variant = fields.Str()
    edition = fields.Str()
    is_foil = fields.Boolean()
    mtgjson_id = fields.Str()
    scryfall_id = fields.Str()
    collector_number = fields.Str()

card_schema = CardsSchema()
cards_schema = CardsSchema(many=True)
