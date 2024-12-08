import requests # imported to fetch web content (also possible with 'urllib' but opted for this due to its simplicity)
from bs4 import BeautifulSoup #importing BeautifulSoup for parsing the HTML page(s)

url = "https://books.toscrape.com/catalogue/sharp-objects_997/index.html"
response = requests.get(url) # "response" stores the servers response. The other part of the code is a GET request to fetch the HTML via the url defined above
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('h1').text.strip()  # this line finds and then extracts the title of the book by finding the first <h1> HTML tag in the url
price = soup.find('p',{'class': 'price_color'}).text.strip() ## TO DO: remove unwanted symbols before output

print(f"Title: {title}")
print(f"Price: {price}")


