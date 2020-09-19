from server import app, db
from server.models import ProductScrape
from flask import request, json

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
    ProductScrape(part_id=2, vendor_id='1A', scraped_url='https://www.company.com', raw_text='specs specs more specs').save()
    scraped_specs = ProductScrape.objects.all()
    return 'Scrape OK'

