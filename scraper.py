import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Website to scrape
url = "https://books.toscrape.com/"

# Get webpage
response = requests.get(url)

# Read HTML
soup = BeautifulSoup(response.text, "html.parser")

# Store books
books = []

# Extract book information
for book in soup.select("article.product_pod"):

    title = book.h3.a["title"]
    price = book.select_one(".price_color").text
    rating = book.select_one("p.star-rating")["class"][1]
    link = book.h3.a["href"]

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "URL": link
    })

# Convert to DataFrame
df = pd.DataFrame(books)

# Create data folder automatically
os.makedirs("data", exist_ok=True)

# Save CSV file
df.to_csv("data/books.csv", index=False)

print("Scraping completed!")
print("Books collected:", len(df))
print("Dataset saved as data/books.csv")