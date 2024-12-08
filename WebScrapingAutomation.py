import requests # imported to fetch web content (also possible with 'urllib' but opted for this due to its simplicity)
from bs4 import BeautifulSoup #importing BeautifulSoup for parsing the HTML page(s)

url = "https://books.toscrape.com/catalogue/sharp-objects_997/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

