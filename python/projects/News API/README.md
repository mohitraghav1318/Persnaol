# News API Python Script

This Python script fetches the latest news articles based on user input using the [News API](https://newsapi.org/). It retrieves and displays the top 10 recent news articles related to the user's query.

---

## Features

- Accepts a search query from the user for the type of news they are interested in.
- Fetches news articles from the News API matching the query.
- Displays the top 10 articles with their title, description, and a link to read more.
- Handles cases where no articles are found.

---

## Requirements

- Python 3.x
- `requests` library

You can install the required library using:

pip install requests


---

## How to Use

1. Clone or download this repository.
2. Open the script file.
3. Replace the API key with your own News API key in the `api` variable.
4. Run the script:

python main.py



5. Enter the type of news you want to search for when prompted.
6. View the top 10 related news articles.

---

## Example Usage


---

## Notes

- Make sure you have an active internet connection.
- You need a valid News API key. You can get one for free at [https://newsapi.org/](https://newsapi.org/).
- The API currently fetches news articles from August 1, 2025, onward due to API limitations.
- Make sure to check the date because it will only works if you are searching in ONE MONTN from the mention date.
---

## License

This project is open source and available under the MIT License.

---

Feel free to modify and expand this script for your needs!

