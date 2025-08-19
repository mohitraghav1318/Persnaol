from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    articles = []
    query = ""

    if request.method == 'POST':
        query = request.form.get('query')
        api = "017bd4f88c71408095f3c574dc57b104"  # Your actual API key
        url = f"https://newsapi.org/v2/everything?q={query}&from=2025-08-10&sortBy=publishedAt&apiKey={api}"

        r = requests.get(url)
        data = r.json()
        articles = data.get("articles", [])

    return render_template('index.html', articles=articles[:10], query=query)

@app.route('/index.html', methods=['GET', 'POST'])
def index():
    return home()

@app.route('/about.html', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
