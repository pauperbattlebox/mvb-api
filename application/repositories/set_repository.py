from application.models import Sets


def get_all_sets_from_db() -> Sets:

    q = Sets.query.with_entities(Sets.cs_id, Sets.cs_name, Sets.mtgjson_code).all()

    return q
