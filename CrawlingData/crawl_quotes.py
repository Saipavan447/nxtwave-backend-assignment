import requests
import json 
from bs4 import BeautifulSoup

page = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')
quote_data = soup.find_all('div',class_='col-md-8')
for quotes in quote_data:
    quote= quotes.find('span',class_="text")
    author=quotes.find('small',class_="author")
    tags=quotes.find('div',class_="tags")
    info=[quote,author,tags]
    print(info)