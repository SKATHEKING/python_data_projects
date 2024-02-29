import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import csv
import sys

# import tkinter module
from tkinter import *

# Following will import tkinter.ttk module and
# automatically override all the widgets
# which are present in tkinter module.
from tkinter.ttk import *

mongoClient = MongoClient()
db = "mongodb://localhost:27017"
database = mongoClient['skyrim_weapons']
collection = database['weapon_list']

data = pd.read_csv(r'C:\Users\mateu\Documents\pythonProject\Skyrim_Weapons.csv')

weapons = []
csv_string = "Skyrim_Weapons.csv"


def create_weapons_list(skyrim=weapons):
    with open(csv_string, 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            weapons.append(row)

        pprint(weapons)

    database = mongoClient['skyrim_weapons']
    collection = database['weapon_list']
    data.reset_index(inplace=True)
    data_dict = data.to_dict("records")
    dblist = mongoClient.list_database_names()

    if database in dblist:
        print("The database exists.")
        print('Able to proceed with operation')
    if collection in database.list_collection_names():
        try:
            if db[collection]:
                db[collection].drop()
                print("Removed " + collection)
        except:
            print('Unable to drop collection')
            collection = database['weapon_list']
            print('Collection created')

    collection.insert_many(data_dict)


def filter_weapon_by_category(category='Archery'):
    weapons_category = []
    cursor = collection.find({})
    for weapon in cursor:

        if weapon['Category'] == category:
            print(category)
            weapons_category.append(weapon)
            pprint(weapon)
        else:
            continue
            # print(f'crime not in {borough}')
    return weapons_category


def filter_weapon_by_damage(damage=20):
    weapons_damage = []
    cursor = collection.find({})
    for weapon in cursor:

        if weapon['Damage'] > damage:
            print(damage)
            weapons_damage.append(weapon)
            pprint(weapon)
        else:
            continue
            # print(f'crime not in {borough}')
    return weapons_damage


def filter_weapon_by_type(type='Bow'):
    weapons_type = []
    cursor = collection.find({})
    for weapon in cursor:

        if weapon['Type'] == type:
            print(type)
            weapons_type.append(weapon)
            pprint(weapon)
        else:
            continue
            # print(f'crime not in {borough}')

    return weapons_type


def filter_weapon_by_perk(perk='Dwarven'):
    weapons_perk = []
    cursor = collection.find({})
    for weapon in cursor:

        if weapon['Perk'] == perk:
            print(perk)
            weapons_perk.append(weapon)
            pprint(weapon)
        else:
            continue
            # print(f'crime not in {borough}')

    return weapons_perk


def which_button(button_press):
    print(button_press)
    return button_press

def create_gui():
    # Create Object
    root = Tk()
    root.title('Skyrim Weapons Filter')

    # Initialize tkinter window with dimensions 100x100
    root.geometry('500x500')

    btn_category = Button(root, text='Filter By Category',
                          command=filter_weapon_by_category)

    btn_damage = Button(root, text='Filter By Damage',
                        command=filter_weapon_by_damage)

    btn_type = Button(root, text='Filter By Type',
                      command=filter_weapon_by_type)

    btn_perk = Button(root, text='Filter By Perk',
                      command=filter_weapon_by_perk)

    console = Text(root)


    # Set the position of button on the top of window
    btn_category.pack(side='top')
    btn_damage.pack(side='top')
    btn_type.pack(side='top')
    btn_perk.pack(side='top')
    console.pack()

    root.mainloop()


def main():
    create_weapons_list()
    create_gui()


main()
