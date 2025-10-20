import requests
from bs4 import BeautifulSoup
import pandas as pd
import time, random
from sqlalchemy import create_engine

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url,timeout=10)

#print(response.status_code)  # should be 200
html = response.text

soup = BeautifulSoup(html, "lxml")
books = soup.find_all("article", class_="product_pod")

all_books = []

for page in range(1, 6):  # scrape first 5 pages
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        all_books.append({"title": title, "price": price})

    time.sleep(random.uniform(1, 3))  # be kind to the website

df = pd.DataFrame(all_books)

engine = create_engine("sqlite:///books.db")
df.to_sql("books", engine, if_exists="replace", index=False)
