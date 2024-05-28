from flask import Flask, request, redirect, render_template, url_for, flash, jsonify
import json
import os
import string
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load URLs from file if it exists, else create an empty file
if os.path.exists('urls.json'):
    try:
        with open('urls.json', 'r') as url_file:
            urls = json.load(url_file)
    except json.JSONDecodeError:
        # Handle empty or invalid JSON file
        urls = {}
else:
    urls = {}

def save_urls():
    with open('urls.json', 'w') as url_file:
        json.dump(urls, url_file)

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(characters) for _ in range(length))
        if short_id not in urls:
            return short_id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['original_url']
    short_id = request.form['short_id']

    if not short_id:
        short_id = generate_short_id()
    elif short_id in urls:
        flash('Short ID already exists. Please choose another one.')
        return redirect(url_for('index'))

    urls[short_id] = original_url
    save_urls()

    short_url = request.host_url + short_id
    # flash(f'Short URL created: {short_url}')
    return redirect(url_for('index', short_url=short_url))

@app.route('/<short_id>')
def redirect_short_url(short_id):
    if short_id in urls:
        return redirect(urls[short_id])
    else:
        flash('Invalid URL')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
