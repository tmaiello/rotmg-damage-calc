__author__ = "Tyler Maiello"

import flask
from functions import damage_calc, character, item, parse_xml, base_characters
from flask import jsonify
import json
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>RotMG Damage Calc</h1><p>This App is my take on a damage calculator for RotMG since the popular one a lot of people used is on flash.</p>"

# Damage endpoint, should take in character obj {stats} + equipment
@app.route('/damage', methods=['POST'])
def damage_endpoint():
    inputs = flask.request.get_json()
    # print(inputs)
    item_1_obj = item.Item(0,0,0,0,0,0,0,0,1,1,220,275)
    # item_2_obj = item.Item(0,0,0,0,0,0,0,0,1)
    # item_3_obj = item.Item(0,0,0,0,0,0,0,0,1)
    # item_4_obj = item.Item(0,0,0,0,0,0,0,0,1)
    char_obj = base_characters.return_maxed_stats("warrior")
    print(item_1_obj.__dict__)
    char_obj.slot_1 = item_1_obj.__dict__
    # print(jsonify(char_obj))
    print(json.dumps(char_obj.__dict__))
    return damage_calc.damage_solve(char_obj)



if __name__ == '__main__':
    app.run()