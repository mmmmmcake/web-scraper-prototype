"""
main.py

A simple Python script to scrape quotes and their authors from http://quotes.toscrape.com.
The extracted data is printed to the console and saved to a CSV file.

Technologies used:
- requests: to fetch the HTML content
- BeautifulSoup (bs4): to parse and extract data from the HTML
- csv: to write the scraped data to a CSV file

This is a basic prototype meant for learning and experimenting with web scraping in Python.
"""


from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("http://quotes.toscrape.com")

# parse the web site html and store it in a variable
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# the quotes items are inside a span html element with the css class text
quotes = soup.find_all("span", attrs={"class": "text"})

# the authors items are inside a small html element with the css class author
authors = soup.find_all("small", attrs={"class":"author"})

# now we can do whatever we want with this data, store it in our "stage" db so it can be refined for example
# for this prototype I will simply store the data into csv file

# setup csv writer
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

# write header
writer.writerow(["QUOTES", "AUTHORS"])

# write file content and also print the content in the console
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])

# close csv file
file.close()


