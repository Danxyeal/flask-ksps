from server import app, db
from server.models import ProductScrape
from flask import request, jsonify

@app.route('/')
@app.route('/index')
def index():
    return 'Hello Flask'

'''
@app.route('*')
def not_found():
    return redirect(url_for('home'))
    '''

@app.route('/scrape')
def scrape():
    ProductScrape(part_id=5, vendor_id='1A', scraped_url='https://www.company.com', raw_text='specs specs more specs').save()
    return 'OK'

@app.route('/products')
def products():
    return jsonify(ProductScrape.objects.all())
