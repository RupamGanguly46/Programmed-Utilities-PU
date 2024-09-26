import pandas as pd
import requests
from bs4 import BeautifulSoup

print("Searching for quotes...")

scraped_list = []

url = "https://quotes.toscrape.com"
response = requests.get(url)

try:
    while True:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_="text").text
            author = quote.find('small', class_="author").text
            scraped_list.append({"quote":text,"author":author})

        next = soup.find('li',class_='next')
        url += next.find('a')['href']

        response = requests.get(url)
        print("Next Page")
except:
    print("Finished all pages...")

df = pd.DataFrame(scraped_list)
print(df)

df.to_csv()

