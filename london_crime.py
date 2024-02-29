import pandas as pd
from pymongo import MongoClient
from pprint import pprint
import csv

# establishing database connection as well as database defined names
mongoClient = MongoClient()
print(mongoClient.list_database_names())
db = "mongodb://localhost:27017"
database_crime = mongoClient['london_crime']
crime_collection = database_crime['crime']

# stores csv into variable so it can be read and utilised during project, as well as initiating an empty list which will be populated
data = pd.read_csv(r'C:\Users\mateu\Documents\pythonProject\london_crime_by_lsoa.csv')
csv_string = "london_crime_by_lsoa.csv"
crime_list = []


# creates database which can be utilised for viewing and further analysis through mongoDB Compass
def create_crime_db():
    with open(csv_string, 'r') as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            crime_list.append(row)
            # print(row)

    database = database_crime
    collection = crime_collection
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


def filter_crime_by_borough(borough='Sutton'):
    crime_in_borough_selected = []
    cursor = crime_collection.find({})
    for crime in cursor:

         if crime['borough'] == borough:
             print(borough)
             crime_in_borough_selected.append(crime)
             print(crime)
         else:
             continue
             #print(f'crime not in {borough}')


def filter_crime_by_year(year=2012):
    crime_in_year_selected = []

    cursor = crime_collection.find({})
    for crime in cursor:

        if crime['year'] == year:
            print(year)
            crime_in_year_selected.append(crime)
            print(crime)
        else:
            continue
            # print(f'crime not in {borough}')


def filter_crime_by_month(month=3):
    crime_in_month_selected = []
    cursor = crime_collection.find({})
    for crime in cursor:

        if crime['month'] == month:
            print(month)
            crime_in_month_selected.append(crime)
            print(crime)
        else:
            continue
            # print(f'crime not in {borough}')


# creates a crime database which we will use to fully analyse and filter as well as visualise the mentioned data in csv
# create_crime_db()

filter_crime_by_borough()
filter_crime_by_year()
filter_crime_by_month()
