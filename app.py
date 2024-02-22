from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def home():
    return 'Hello, welcome to the homepage!'

@app.route('/about')
def about():
    return 'This is the about page.'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
