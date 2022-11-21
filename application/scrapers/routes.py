from flask import Blueprint
from sqlalchemy import func

from application.main import db
from application.models import LegacyPage, Genre, Legacy

from .scraper import Scraper

scrapers = Blueprint('scrapers', __name__)

@scrapers.get('/scrape_legacy_movies')
def scrape_legacy_movies():
    get_page = LegacyPage.query.first()

    scraper = Scraper(get_page.page)
    scraper.start_scraper()


    get_page.page -= 1

    movies = scraper.scraped_movie_list
    for movie in movies:
        genres = movie['genres']
        del movie['genres']

        add_movie = Legacy(**movie)
        db.session.add(add_movie)
        db.session.commit()
        
        for genre in genres:
            if len(genre.strip(' ')) == 0:
                continue
            fetch_genre = Genre.query.filter(func.lower(Genre.name) == func.lower(genre)).first()
            if fetch_genre == None:
                fetch_genre = Genre(name=genre)
                db.session.add(fetch_genre)
            
            add_movie.genres.append(fetch_genre)
        
        db.session.commit()
        

    return {'data': 'All done!'}