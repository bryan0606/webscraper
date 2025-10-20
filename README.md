\# 📚 Book Store Web Scraper



This project is a simple \*\*Python web scraper\*\* that extracts book data — including titles and prices — from the website \[Books to Scrape](https://books.toscrape.com). It’s built using \*\*BeautifulSoup\*\*, \*\*Requests\*\*, and \*\*SQLAlchemy\*\*, and saves the scraped data into a \*\*SQLite database\*\* for analysis or further use.



---



\## 🧠 Project Overview

The scraper automatically visits the first 5 pages of the Books to Scrape catalog, extracts book titles and prices, and stores the data in a local SQLite database (`books.db`). This project demonstrates basic web scraping, data extraction, and database integration — ideal for a beginner data engineering or data analysis portfolio.



---



\## ⚙️ Technologies Used

\- \*\*Python 3\*\*

\- \*\*Requests\*\* – for sending HTTP requests  

\- \*\*BeautifulSoup (bs4)\*\* – for parsing HTML content  

\- \*\*Pandas\*\* – for handling tabular data  

\- \*\*SQLAlchemy\*\* – for saving data into SQLite



---



\## 🧩 How to Run

Clone this repository, install dependencies, and execute the scraper script to collect book data:



```bash

git clone https://github.com/yourusername/book-scraper.git

cd book-scraper

pip install -r requirements.txt

python scraper.py



