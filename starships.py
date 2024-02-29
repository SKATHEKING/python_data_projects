import requests
import pprint
import pymongo

client = pymongo.MongoClient()

db = client['starwars']

# does singular api call
response = requests.get('https://swapi.dev/api/starships/?page=1')


# does api call
def do_call(url):
    response = requests.get(url).json()
    pprint.pprint(response)
    return response


# prints status code for api call as well as results
def api_call_check():
    print(response)
    pprint.pprint(response.text)


# loops through all pages and does api call whilst printing their values

def api_call_all():
    url = 'https://swapi.dev/api/starships/?page=1'
    response = requests.get(url)
    ships_info = []
    count = 0
    while response.json()['next'] != None:

        for ship in response.json()['results']:
            ships_info.append(ship)

        response = requests.get(response.json()['next'])

    try:
        if response.json()['next'] == None:

            for ship in response.json()['results']:
                ships_info.append(ship)

    except:
        print("ERROR")
    finally:
        for i in ships_info:
            count += 1
        print(count)
        pprint.pprint(ships_info)
        return ships_info


# call all pilots apis from within the json api
def all_pilot_api_call(ship):
    ships = api_call_all()
    list_of_pilots = []

    try:
        #for ship in ships:
       if ship['pilots'] != [] and ship['pilots'] != None:
             for pilots in ship['pilots']:
                if pilots:
                     pilot_data = do_call(pilots)
                     print(pilot_data['name'])
                     list_of_pilots.append(pilot_data['name'])

                    # pprint.pprint(do_call(pilot))
       else:
        print('No pilots were found')
        print(list_of_pilots)

    except:
        print('It was no possible to find any ships')

    pprint.pprint(list_of_pilots)
    return list_of_pilots


# adds starship database to collection
def add_collection(ship):
    ship_collection = db['starships']
    ship_collection.insert_one(ship)

def add_all_ships():
    db['starships'].insert_many(api_call_all())

# removes collection if it exists
def remove_collection(collection='starships'):
    try:
        if db[collection]:
            db[collection].drop()
            print("Removed " + collection)
    except:
        print('Unable to drop collection')


# checks if collection is there if not it creates collection
def create_collection_starship(collection='starships'):
    if db.starships:
        remove_collection()

    db.create_collection(collection)
    print(f'{collection} created successfully')


# inserts into collection all pilots with their corresponding ids
def insert_into_collection():
    client = pymongo.MongoClient()
    db = client["starwars"]
    create_collection_starship(collection='starships')
    #add_all_ships()
    for ship in api_call_all():
            if ship['pilots']:
                pilot_ids_list = []
                for pilot in all_pilot_api_call(ship):
                    pilot_id = db.characters.find_one({'name': pilot }, {'_id': 1})
                    pilot_ids_list.append(pilot_id)
                    ship['pilots'] = pilot_ids_list
            add_collection(ship)


# api_call_check()
# print(api_call_all())
# all_pilot_api_call()
# do_call('https://swapi.dev/api/people/39/')
insert_into_collection()
# add_collection()
# remove_collection()
# api_call_all()
#add_all_ships()