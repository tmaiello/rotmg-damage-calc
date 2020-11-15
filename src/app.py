__author__ = "Tyler Maiello"

import flask
from functions import damage_calc
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>RotMG Damage Calc</h1><p>This App is my take on a damage calculator for RotMG since the popular one a lot of people used is on flash.</p>"

# Damage endpoint, should take in character obj {stats} + equipment
@app.route('/damage', methods=['POST'])
def damage_calc():
    inputs = flask.request.get_json()


if __name__ == '__main__':
    app.run()