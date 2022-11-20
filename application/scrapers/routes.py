from flask import Blueprint

scrapers = Blueprint('scrapers', __name__)

@scrapers.get('/scrape_legacy_movies')
def scrape_legacy_movies():
    pass