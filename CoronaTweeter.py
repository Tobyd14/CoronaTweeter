import requests
from bs4 import BeautifulSoup


URL= 'https://www.worldometers.info/coronavirus/'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup= BeautifulSoup(page.content, 'html.parser')

title = soup.find_all(class_='sorting_1')

print(title)