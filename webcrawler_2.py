# web crawler basic

from bs4 import BeautifulSoup
import requests

def getHTMLdocument(url):
    response = requests.get(url)

    return response.text

url_to_scrape = "https://theguardian.com/uk"

html_document = getHTMLdocument(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser')

print(soup)
