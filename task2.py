# File: web_scraper_books.py

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books(base_url="http://books.toscrape.com/"):
    print("Fetching data from:", base_url)
    books = []
    for page in range(1, 6):  # Scrape first 5 pages for demo
        url = f"{base_url}catalogue/page-{page}.html"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve page {page}")
            continue
        
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='product_pod')

        for article in articles:
            title = article.h3.a['title']
            price = article.find('p', class_='price_color').text.strip()
            availability = article.find('p', class_='instock availability').text.strip()
            books.append({
                'Title': title,
                'Price': price,
                'Availability': availability
            })
    
    df = pd.DataFrame(books)
    df.to_csv("books_data.csv", index=False)
    print("Scraping completed! Data saved to books_data.csv")
    print(df.head())

if __name__ == "__main__":
    scrape_books()
