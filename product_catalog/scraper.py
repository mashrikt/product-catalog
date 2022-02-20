import re

import requests
from bs4 import BeautifulSoup


class EbayScraper:

    def __init__(self, url):
        self.url = url
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def get_product_details(self):
        title = self.soup.find('h1', {'id': 'itemTitle'}).find(text=True, recursive=False)
        try:
            rating = self.soup.find('span', {'class': 'reviews-star-rating'})['title'].split(',')[0]
        except (TypeError, KeyError):
            rating = ''
        return title, rating

    def get_image_data(self):
        image = self.soup.find('div', {'id': 'mainImgHldr'}).find('img', {'id': 'icImg'})
        url = image['src']
        # replace pattern s-l300. to s-l2000. to fetch the highest qulity image
        url = re.sub('s-l\d+\.', 's-l2000.', url)
        return url, image['alt']
