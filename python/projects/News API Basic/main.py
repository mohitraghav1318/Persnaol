import requests  # pip install requests
# This script fetches news articles based on user input using the News API.
# Make sure to replace the API key with your own.
query = input("What type of news are you interested in today? \n")   
api = "017bd4f88c71408095f3c574dc57b104"  # Replace with your actual API key

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-01&sortBy=publishedAt&apiKey={api}"

print(url)

# Fetching the news articles
r =  requests.get(url)

# Check if the request was successful
data = r.json()
articles = data["articles"]

# Check if articles were found
if not articles:
    print("No articles found for your query.")
    exit()

# Displaying the articles
print(f"Here are the top 10 articles for your query: {query}")

# Loop through the articles and print their titles and URLs
for i, article in enumerate(articles [:10]):
    title = article["title"]
    description = article["description"]
    url = article["url"]
    print(f"{i+1}. {title}\n   Description: {description}\n  Read more: {url}\n  ")   

# End of the script
# Note: Ensure you have an active internet connection to fetch the news articles.





