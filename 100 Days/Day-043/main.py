from bs4 import BeautifulSoup
import requests

response = requests.get("https://realpython.github.io/fake-jobs/")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
print(soup.title)