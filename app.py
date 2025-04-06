from flask import Flask, request, redirect
import redis
import string
import random

app = Flask(__name__)

# Connect to Redis
r = redis.Redis(host='redis', port=6379, db=0)

def generate_short_url():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json.get('url')
    if not long_url:
        return {'error': 'URL is required'}, 400
    
    short_url = generate_short_url()
    r.set(short_url, long_url)
    return {'short_url': f'http://localhost:5000/{short_url}'}

@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = r.get(short_url)
    if long_url:
        return redirect(long_url.decode('utf-8'))
    return {'error': 'URL not found'}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
