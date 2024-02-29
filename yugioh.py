import requests
from pprint import pprint
from pymongo import MongoClient
import json




mongoClient = MongoClient()
db = "mongodb://localhost:27017"
database = mongoClient['yu-gi-oh']
collection = database['cards']



cards_list = []
data = ''

# does singular api call whilst also creating database for yu gi oh cards in mongodb

def do_call():
    # does singular api call
    response = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php')
    print(response)
    #pprint(response.text)
    pprint(response.json())

    data_dict = response.json()
    for card in data_dict['data']:
        cards_list.append(card)

    database = mongoClient['yu-gi-oh']
    collection = database['cards']

    dblist = mongoClient.list_database_names()

    if database in dblist:
        print("The database exists.")
        print('Able to proceed with operation')
    if collection in database.list_collection_names():
        try:
            if collection:
                collection.drop()
                print("Removed " + collection)
        except:
            print('Unable to drop collection')
            collection = database['cards']
            print('Collection created')

    collection.insert_many(cards_list)

do_call()
