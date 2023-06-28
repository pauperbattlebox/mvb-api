from application.models import Sets


def get_all_sets_from_db() -> Sets:

    q = Sets.query.with_entities(Sets.cs_id, Sets.cs_name, Sets.mtgjson_code).all()

    return q

def get_sets_from_db_by_mtgjson_code(mtgjson_code: str) -> Sets:

    q = Sets.query.filter(Sets.mtgjson_code == mtgjson_code.upper()).all()

    return q
