from marshmallow import Schema, fields
from application.models import Sets, Cards

class SetsSchema(Schema):

    cs_id = fields.Int()
    cs_name = fields.Str()
    # mtgjson_code = fields.Str()
    # map = fields.Str()

set_schema = SetsSchema()
sets_schema = SetsSchema(many=True)
