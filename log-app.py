from flask import Flask
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Configure logging to write messages to a file
logging.basicConfig(filename='flask_app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def home():
    app.logger.info('Accessed home page')
    return 'Hello, welcome to the homepage!'

@app.route('/about')
def about():
    app.logger.info('Accessed about page')
    return 'This is the about page.'

@app.route('/add_sample')
def add_sample():
    # Additional sample logs
    app.logger.debug('This is a debug message')
    app.logger.info('This is an info message')
    app.logger.warning('This is a warning message')
    app.logger.error('This is an error message')
    app.logger.critical('This is a critical message')
    return '***Sample Logs Added***'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


