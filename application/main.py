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

