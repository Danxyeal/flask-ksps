from server import app, db

@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask'

@app.route('/*')
def not_found():
    return redirect(url_for('home'))

class Product(db.Document):
    part_id = db.IntField(unique=True)
    vendor_id = db.StringField()

