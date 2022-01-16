from .extensions import db
import datetime

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
    mtgjson_id = db.Column(db.String(100))
    scryfall_id = db.Column(db.String(100))
    collector_number = db.Column(db.String(10))
    matched_by_image = db.Column(db.Boolean)
    mtgjson_code = db.Column(db.String(10))
    prices = db.relationship('Prices', backref='cards', uselist=False)

class Sets(db.Model):
    __tablename__ = 'sets'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key = True)
    cs_id = db.Column(db.Integer, unique = True)
    cs_name = db.Column(db.String(100))
    mtgjson_code = db.Column(db.String(100))
    map = db.Column(db.String(50))

class Prices(db.Model):
    __tablename__ = 'prices'
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Float)
    updated = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
    
