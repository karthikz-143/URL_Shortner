from flask import Flask, request, jsonify, render_template, redirect
import hashlib

app = Flask(__name__)

# Dictionary to store URL mappings
url_mapping = {}
# List to store the history of shortened URLs
url_history = []

def shorten_url(long_url):
    # Generate a hash of the long URL
    hash_object = hashlib.md5(long_url.encode())
    short_url = hash_object.hexdigest()[:6]  # Taking first 6 characters of the hash for the short URL
    
    # Store the mapping of short URL to long URL
    url_mapping[short_url] = long_url
    # Update the history
    url_history.append({'short_url': short_url, 'long_url': long_url})
    
    return short_url

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = shorten_url(long_url)
    return jsonify({'short_url': short_url})

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_mapping.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found", 404

@app.route('/history')
def history():
    return jsonify(url_history)

if __name__ == '__main__':
    app.run(debug=True)
