from .main import db

from sqlalchemy.sql.expression import text

genres = db.Table('genres',
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True),
    db.Column('legacy_id', db.Integer, db.ForeignKey('legacy.id'), primary_key=True)
)

class Legacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    plot = db.Column(db.String, nullable=False)
    genres = db.relationship('Genre', secondary=genres, lazy='subquery', backref=db.backref('legacies', lazy='subquery', cascade="all, delete"))
    image = db.Column(db.String, nullable=False)
    pushed = db.Column(db.Boolean, server_default='FALSE')
    link = db.Column(db.String, nullable=False)
    date = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date = db.Column(db.TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class LegacyPage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page = db.Column(db.Integer, nullable=False)

    def create_legacy_page_row(self):
        legacy_page = LegacyPage.query.first()

        if legacy_page == None:
            page = LegacyPage(page=248)
            db.session.add(page)
            db.session.commit()
