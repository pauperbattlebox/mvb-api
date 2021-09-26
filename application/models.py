from .extensions import db

class Cards(db.Model):
    __tablename__ = 'cards'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    cs_id = db.Column(db.Integer, unique = True)
    url = db.Column(db.String(50))
    name = db.Column(db.String(100))
    variant = db.Column(db.String(500))
    edition = db.Column(db.String(500))
    is_foil = db.Column(db.Boolean)
    mtgjson_id = db.Column(db.String(100), unique = True)
    scryfall_id = db.Column(db.String(100), unique = True)
    collector_number = db.Column(db.String(10))

class Sets(db.Model):
    __tablename__ = 'sets'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    cs_id = db.Column(db.Integer, unique = True)
    cs_name = db.Column(db.String(100))
    mtgjson_code = db.Column(db.String(100))
    map = db.Column(db.String(50))
