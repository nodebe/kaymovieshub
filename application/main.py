import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from scrapers.routes import scrapers

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

app.register_blueprint(scrapers, url_prefix='/v1/scrape')

# Configure database
from models import *

# Initialise Database
db.init_app(app)
with app.app_context():
    db.create_all