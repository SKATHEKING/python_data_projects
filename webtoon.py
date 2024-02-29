import requests
import pprint
import pymongo
import csv


client = pymongo.MongoClient()

db = client['Webtoon']



def add_all_ships(character):
    db['Webtoon'].insert_one(character)

# removes collection if it exists
def remove_collection(collection='Characters'):
    try:
        if db[collection]:
            db[collection].drop()
            print("Removed " + collection)
    except:
        print('Unable to drop collection')


# checks if collection is there if not it creates collection
def create_collection_characters(collection='Characters'):
    if db.starships:
        remove_collection()

    db.create_collection(collection)
    print(f'{collection} created successfully')

def insert_into_collection():

    try:
        create_collection_characters()
        with open('file.csv', newline='') as f:
            reader = csv.reader(f)
        data = list(reader)
        for character in data:
            add_all_ships(character)

        print('Added all characters to database successfully')
    except:
        print('Unable to add characters to mongodb Database')




insert_into_collection()