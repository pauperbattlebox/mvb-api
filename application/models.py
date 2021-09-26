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
    alt_art = db.Column(db.Boolean)
    alt_art_etched = db.Column(db.Boolean)
    etched = db.Column(db.Boolean)
    borderless = db.Column(db.Boolean)
    extended_art = db.Column(db.Boolean)
    prerelease_promo = db.Column(db.Boolean)
    promo_pack = db.Column(db.Boolean)
    ampersand_promos = db.Column(db.Boolean)
    commander_decks = db.Column(db.Boolean)
    commander_deck_ext_art = db.Column(db.Boolean)
    showcase = db.Column(db.Boolean)
    godzilla = db.Column(db.Boolean)
    retro_frame = db.Column(db.Boolean)
    retro_frame_etched = db.Column(db.Boolean)
    map = db.Column(db.String(50))
