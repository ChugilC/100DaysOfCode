from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get('https://api.npoint.io/c8b09e840161c9ca0f0d')
all_blogs = response.json()

@app.route('/')
def home():
    return render_template('index.html', posts=all_blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):    
    return render_template('post.html', posts=all_blogs, num=id)

if __name__ == "__main__":
    app.run(debug=True)