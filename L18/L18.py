#! .venv/scripts/python

from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/time')
def time_out():
    return datetime.now().isoformat()

if __name__ == '__main__':
    app.run()