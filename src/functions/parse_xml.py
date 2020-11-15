__author__ = "Tyler Maiello"

import csv 
import requests 
import xml.etree.ElementTree as ET

# loads equips.xml from RotMG Production
def load_equips(): 
    # set url of xml
    url = 'https://static.drips.pw/rotmg/production/current/xml/Equip.xml'
    # creating HTTP response object from given url 
    resp = requests.get(url) 
    # saving the xml file 
    with open('rotmg.xml', 'wb') as f: 
        f.write(resp.content)

# general parsing tool that obtains all <Object> in XML as list
def parse_xml(xmlfile): 
    # create element tree object 
    tree = ET.parse(xmlfile) 
    # get root element 
    root = tree.getroot()
    # create empty list for rotmg items 
    rotmg_items = [] 
    # iterate through all <Object>'s in XML 
    for item in root.findall('./Object'): 
        # empty items dictionary 
        items = {} 
        # iterate child elements of item 
        for child in item:
            items['type'] = (item.attrib.get('type'))
            items['id'] = (item.attrib.get('id'))
            if child.tag == 'SlotType':
                items[child.tag] = child.text
            if child.tag == 'Projectile':
                for proj in child.findall('./'):
                    items[proj.tag] = proj.text
        # append items dictionary to rotmg items list 
        rotmg_items.append(items) 
    # return rotmg items list 
    return rotmg_items 

# parsing tool that projects on valid "SlotType"
def get_equipable_items(xmlfile): 
    # create element tree object 
    tree = ET.parse(xmlfile) 
    # get root element 
    root = tree.getroot()
    # create empty list for rotmg items 
    rotmg_items = [] 
    # iterate through all <Object>'s in XML 
    for item in root.findall('./Object'): 
        # empty items dictionary 
        items = {} 
        # iterate child elements of item 
        for child in item:
            if child.tag == 'SlotType' and child.text != None:
                items['Type'] = (item.attrib.get('type'))
                items['Id'] = (item.attrib.get('id'))
                items[child.tag] = child.text
            if child.tag == 'RateOfFire':
                items[child.tag] = child.text
            if child.tag == 'Projectile':
                for proj in child.findall('./'):
                    items[proj.tag] = proj.text
            if child.tag == 'ActivateOnEquip' and child.text != None:
                for aoe in child.attrib.get('stat'):
                    items[child.attrib.get('stat')] = child.attrib.get('amount')
        # append items dictionary to rotmg items list 
        rotmg_items.append(items) 
    # return rotmg items list 
    return rotmg_items 

# saves the parsed XML data to CSV
def save_to_CSV(rotmgitems, filename): 
    # specifying the fields for csv file 
    fields = ['Type', 'Id', 'SlotType', 'RateOfFire', 'ObjectId',
    'LifetimeMS', 'MaxDamage', 'Speed', 'MinDamage', 'MultiHit',
    'Amplitude', 'Frequency', 'ArmorPiercing','PassesCover', 'Parametric',
    'ConditionEffect', 'Size', 'ParticleTrail', 'FaceDir','Wavy',
    'Boomerang','Magnitude','Damage', '0', '1', '3', '4', '20', '21', '22', '26', '27', '28']
    # writing to csv file 
    with open(filename, 'w') as csvfile: 
        # creating a csv dict writer object 
        writer = csv.DictWriter(csvfile, fieldnames = fields) 
        # writing headers (field names) 
        writer.writeheader() 
        # writing data rows 
        writer.writerows(rotmgitems) 

# Main for testing

def main(): 
    # load equip.xml from web to update existing xml file 
    load_equips() 
    # parse xml file -> project on SlotType != None
    rotmg_items = get_equipable_items('rotmg.xml') 
    # store rotmg items in a csv file 
    save_to_CSV(rotmg_items, 'rotmg.csv') 


if __name__ == "__main__": 
    main() 