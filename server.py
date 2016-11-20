import json
from flask import Flask, render_template
from flask import url_for

with open('accel.json') as json_data:
    d = json.load(json_data)

app = Flask(__name__, static_url_path='/static/')

@app.route('/')
def home():
    return json.dumps(d)


if __name__ == '__main__':
    app.run()