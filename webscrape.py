import requests
from bs4 import BeautifulSoup

page = requests.get('https://en.wikipedia.org/wiki/Matrix_multiplication').text

soup = BeautifulSoup(page, "html.parser")

print(soup.header)
print(soup.text[0:100])