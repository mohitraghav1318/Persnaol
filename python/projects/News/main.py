from flask import Flask, render_template, request, redirect, url_for
import requests

from flask_mail import Mail, Message

app = Flask(__name__)
# Configure mail server settings - use your SMTP provider
app.config['MAIL_SERVER'] = 'smtp.gmail.com'      # example: Gmail SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mohitraghav911@gmail.com'       # your actual email
app.config['MAIL_PASSWORD'] = '@mahi1318'          # use App Password for Gmail or secure password
app.config['MAIL_DEFAULT_SENDER'] = 'mohitraghav911@gmail.com'

mail = Mail(app)
# Initialize Flask app


@app.route('/', methods=['GET', 'POST'])
def home():
    query = ""
    articles = []

    if request.method == 'POST':
        # Get the search query from form
        query = request.form.get('query')
        # Redirect to GET request with query in URL to persist state
        return redirect(url_for('home', query=query))

    # For GET requests, get query from URL parameters
    query = request.args.get('query', '')
    if query:
        api = "017bd4f88c71408095f3c574dc57b104"
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

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message(subject=f"New message from {name}",
                  recipients=['mohitraghav911@gmail.com'])
    msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    try:
        mail.send(msg)
    except Exception as e:
        print("Failed to send email:", e)
        return "Error sending email. Please try again."

    return render_template('thankyou.html', name=name)

@app.route('/thankyou.html', methods=['GET', 'POST'])
def thankyou():
    return render_template('thankyou.html')     


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
