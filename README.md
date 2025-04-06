# 🕷️ web-scraper-prototype

A simple Python prototype that scrapes quotes and authors from [quotes.toscrape.com](http://quotes.toscrape.com) using BeautifulSoup. This project demonstrates the basics of web scraping, data extraction, and saving content to a CSV file.

---

## 🚀 Features

- Retrieves HTML content from a website using `requests`
- Parses HTML with `BeautifulSoup`
- Extracts quotes and their corresponding authors
- Prints results in the console
- Saves results in a CSV file (`scraped_quotes.csv`)

---

## 📦 Requirements

- Python 3.x

---

## ▶️ Usage

1. Clone or download the repository.
2. Install the required packages using pip:

```bash
pip install beautifulsoup4 requests
```

3. Run the script:

```bash
python main.py
```

4. The script will:
   - Print quotes and authors to the console
   - Save them to a CSV file named `scraped_quotes.csv`

---

## 📁 Sample Output

### Console output:

```text
“The world as we have created it is a process of our thinking.” - Albert Einstein
“It is our choices, Harry, that show what we truly are...” - J.K. Rowling
...
```

### CSV file (`scraped_quotes.csv`):

| QUOTES                               | AUTHORS         |
| ------------------------------------ | --------------- |
| “The world as we have created it...” | Albert Einstein |
| “It is our choices, Harry...”        | J.K. Rowling    |
| ...                                  | ...             |

---

## 💡 Ideas for Improvement

- 🔄 Add support to scrape multiple web pages
- 📤 Export results to JSON
- 🗃️ Store data in a database
