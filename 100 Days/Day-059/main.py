from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Blog Website"

@app.route("/about")
def about():
    return "About Page"

if __name__ == "__main__":
    app.run(debug=True) 