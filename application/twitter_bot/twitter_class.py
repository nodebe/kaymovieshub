import os
import secrets

import requests
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
        self.base_url = os.environ.get('WEBSITE_URL')
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
    
    def image_saver(self, image_link):
        print('downloading image')
        image_id = f"{secrets.token_hex(32)}.jpg"
        image_content = requests.get(f"{image_link}").content

        with open(f'application/static/images/{image_id}', 'wb+') as image:
            image.write(image_content)
        print('image saved!')
        return image_id

        