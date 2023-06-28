from flask import Blueprint, abort
from flask import current_app as app
from flask import jsonify

from application.repositories.set_repository import *

from application import cache, current_version, limiter
from application.models import Cards, Sets
from application.schemas import (
    cards_schema,
    set_with_cards_schema,
    sets_schema,
    sets_with_cards_schema,
)

sets = Blueprint("sets", __name__)


###GET ALL SETS
@sets.route(current_version + "/sets")
@limiter.limit("10/hour")
@cache.cached(timeout=86400)
def get_all_sets():
    
    q = get_all_sets_from_db()

    result = sets_schema.dump(q)

    return jsonify(result)


###GET SET BY CS ID
@sets.route(current_version + "/sets/cs/<cs_id>")
@limiter.limit("60/minute")
@cache.cached(timeout=86400)
def get_set_by_set_name(cs_id):

    q = Sets.query.filter(Sets.cs_id == cs_id).first_or_404()
    result = set_with_cards_schema.dump(q)

    d = (
        Cards.query.filter(
            Cards.edition == q.cs_name,
            Cards.mtgjson_code != None,
            Cards.mtgjson_code != q.mtgjson_code,
        )
        .with_entities(Cards.mtgjson_code)
        .distinct()
    )

    result["related_mtgjson_codes"] = sets_schema.dump(d)

    p = (
        Cards.query.filter(Cards.edition == result["cs_name"])
        .order_by(Cards.name.asc(), Cards.is_foil.asc())
        .all()
    )
    result["cards"] = cards_schema.dump(p)

    return jsonify(result)


####GET SET BY MTGJSON CODE
####THIS MATCHES *.json file
@sets.route(current_version + "/sets/mtgjson/<mtgjson_code>")
@limiter.limit("60/minute")
@cache.cached(timeout=86400)
def get_set_by_mtgjson_code(mtgjson_code):

    q = Sets.query.filter(Sets.mtgjson_code == mtgjson_code.upper()).all()

    if len(q) < 1:
        q = Cards.query.filter(Cards.mtgjson_code == mtgjson_code.upper()).all()

        result = cards_schema.dump(q)
        return jsonify(result)

    else:

        result = sets_with_cards_schema.dump(q)
        return jsonify(result)
