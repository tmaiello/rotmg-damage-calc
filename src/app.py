__author__ = "Tyler Maiello"

import flask
from functions import damage_calc, item, base_characters
from flask import jsonify
import json
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>RotMG Damage Calc</h1><p>This App is my take on a damage calculator for RotMG since the popular one a lot of people used is on flash.</p>"

# Damage endpoint, should take in character obj {stats} + equipment
@app.route('/damage', methods=['GET'])
def damage_endpoint():
    inputs = flask.request.get_json()

    # Getting character and items from JSON
    char_obj = base_characters.return_maxed_stats(inputs["character"])
    item_1_obj = json_item_to_item_object(inputs['item_1'])
    item_2_obj = json_item_to_item_object(inputs['item_2'])
    item_3_obj = json_item_to_item_object(inputs['item_3'])
    item_4_obj = json_item_to_item_object(inputs['item_4'])

    # Inserting items into character object
    # TODO: modularize process
    char_obj.slot_1 = item_1_obj.__dict__
    char_obj.slot_2 = item_2_obj.__dict__
    char_obj.slot_3 = item_3_obj.__dict__
    char_obj.slot_4 = item_4_obj.__dict__

    #TODO: need to add stats from all items besides weapons into calculation
    
    return damage_calc.damage_solve(char_obj)

# General function to convert any object JSON to an Item Object. Modularized in case change in formatting
def json_item_to_item_object(item_obj):
    print(f"Converting object: \n{item_obj}\nfrom JSON to Item Object")
    return item.Item(item_obj["life"],item_obj["mana"],item_obj["att"],item_obj["defense"],item_obj["spd"],item_obj["dex"],item_obj["vit"],item_obj["wis"],item_obj["slot_type"],item_obj["num_projectiles"],item_obj["min_damage"],item_obj["max_damage"])


if __name__ == '__main__':
    app.run()