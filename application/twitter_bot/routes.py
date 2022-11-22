from flask import Blueprint

from application.main import db
from application.models import Legacy

from .twitter_class import TwitterObj

twitter_route = Blueprint('twitter_route', __name__)

@twitter_route.get('/legacy_kaymovieshub_push')
def legacy_kaymovieshub_push():
    ''' Gets the movie from the DB, generates a twitter image id and tweets'''

    get_movie = Legacy.query.filter_by(pushed=False).first()

    tweeter = push_movie(get_movie)

    get_movie.pushed = True
    db.session.commit()

    return {'data': tweeter}

def push_movie(movie):
    if movie == None:
        return {'msg': 'Nothing to push!'}
        
    title = movie.title[:50].upper()
    plot = movie.plot[:150] + '...' if len(movie.plot) > 150 else movie.plot
    link = movie.link

    genres = []
    for genre in movie.genres:
        genres.append(f"#{genre.name}")
    genres = ' '.join(genres)

    image_file = f"application/static/images/{movie.image}"

    text_format = f"""{title}\n\n{plot}\n\nLink: {link}\n\n{genres}"""

    tweet_obj = TwitterObj()

    image_id = tweet_obj.generate_image_id(image_file)

    tweet = tweet_obj.post_tweet(text=text_format, media_id=[image_id])

    return tweet

@twitter_route.get('/callback')
def callback():
    print('received')