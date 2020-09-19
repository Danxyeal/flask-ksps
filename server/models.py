import flask
from server import db

class ProductScrape(db.Document):
    part_id = db.IntField(unique=True)
    vendor_id = db.StringField(max_length=30)
    scraped_url = db.StringField(max_length=200)
    raw_text = db.StringField(max_length=999)

