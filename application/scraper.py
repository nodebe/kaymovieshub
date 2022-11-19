import os
import requests
from bs4 import BeautifulSoup

url = os.environ.get('WEBSITE_URL') + '/genre.php?catID=2&pg=248'

html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('div', class_='mainbox')

for row in rows:
    link = row.find('a').get('href')
    print(link)
# print(rows)

# with open('data.txt', 'w') as data_writer:
#     data_writer.write(rows)

# print('done')