from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
print(soup.title)