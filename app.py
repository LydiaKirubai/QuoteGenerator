from flask import Flask, render_template, request
import json, random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/quote', methods=['POST'])
def show_quote():
    with open("quotes.json") as f:
        quotes = json.load(f)
    quote = random.choice(quotes)
    return render_template("index.html", quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
