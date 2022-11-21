import os
from dotenv import load_dotenv
import tweepy

load_dotenv()

access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')
consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_KEY_SECRET')

class TwitterObj:

    def __init__(self):
        self.authenthicate = tweepy.OAuth1UserHandler(
            consumer_key, consumer_secret, access_token, access_token_secret
        )

    def post_tweet(self, text, media_id=None):
        auth = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

        tweet = auth.create_tweet(
            media_ids = media_id,
            text = text
        )

        return tweet
    
    def generate_image_id(self, image_file_name):
        auth = tweepy.API(auth=self.authenthicate)

        image_id = auth.simple_upload(image_file_name)

        return image_id.media_id_string

        