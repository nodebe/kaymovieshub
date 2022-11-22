import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

from .scrapers.routes import scrapers
from .twitter_bot.routes import twitter_route

app.register_blueprint(scrapers, url_prefix='/v1/scrape')
app.register_blueprint(twitter_route, url_prefix='/v1/tweet')

# Configure database
from .models import LegacyPage

# Initialise Database
db.init_app(app)
with app.app_context():
    db.create_all()
    LegacyPage().create_legacy_page_row()

# Create necessary folder
def create_folder():
    try:
        os.makedirs('application/static/img')
    except Exception as e:
        print('Static folder Created!')

@app.route('/')
def index():
    return """<h2>Welcome to Kay Movies Hub!</h2> 
            <p>We are on twitter <a href='https://twitter.com/kaymovieshub'>@KayMoviesHub</a></p>
            """

create_folder()