from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Flask"

@app.route('/bye')
def bye_world():
    return "Bye Flask"

if __name__ == "__main__":
    app.run()