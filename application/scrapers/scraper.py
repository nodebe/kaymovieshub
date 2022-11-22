import os
import secrets
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

class Scraper:
    def __init__(self, page:int) -> None:
        print('Initializing scraper...')
        self.page = page
        self.base_url = os.environ.get('WEBSITE_URL')
        self.url = f"{self.base_url}/genre.php?catID=2&pg={self.page}"
        self.scraped_movie_list = []


    def start_scraper(self):
        print('Scraping initial...')
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')

        # Fetch the rows containing information we need
        rows = soup.find_all('div', class_='mainbox')
        print('Scraping individual...')
        for row in rows:
            link = row.find('a').get('href')
            self.scrape_individual(movie_url=f"{self.base_url}/{link}")
    
    
    def scrape_individual(self, movie_url):
        html = requests.get(movie_url).text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            # Fetch movie information
            print('Fetching movie info')
            movie_title = soup.find('span', attrs={'itemprop': 'name'}).text
            movie_plot = soup.find('textcolor1', attrs={'itemprop': 'description'}).text
            genres_format = soup.find_all('span', attrs={'itemprop': 'genre'})
            movies_genres = [genre.text for genre in genres_format]
            movie_image_source = soup.find('img', attrs={'itemprop': 'image'}).get('src').strip(' ').replace(' ', '%20')
            # save_image = self.image_saver(movie_image_source)

            # Format movie details
            movie = {
                'title': movie_title,
                'plot': movie_plot,
                'genres': movies_genres,
                'image': f"{self.base_url}{movie_image_source}",
                'link': movie_url.strip(' ').replace(" ", "%20")
            }

            self.scraped_movie_list.append(movie)

        except Exception as e:
            print(str(e))

    # def image_saver(self, image_link):
    #     image_id = f"{secrets.token_hex(32)}.jpg"
    #     image_content = requests.get(f"{self.base_url}/{image_link}").content

    #     with open(f'application/static/images/{image_id}', 'wb+') as image:
    #         image.write(image_content)

    #     return image_id
