import requests
import pprint
import sqlite3

url = "https://www.boredapi.com/api/activity"


list_of_activities = []


def quote_picker(number_of_quotes=1):
    for i in range(number_of_quotes):
        response = requests.get(url)

        print(response)

        pprint.pprint(response.json())
        quote = response.json()['activity']

        list_of_activities.append(quote)


def quote_spitter():
    for quote in list_of_activities:
        print(quote)


def database_maker():
    conn = sqlite3.connect('Tronald_Dump_Lulz.db')
    c = conn.cursor()

    c.execute('''
	          CREATE TABLE IF NOT EXISTS dummy_trumpy
	          ([quote_id] INTEGER PRIMARY KEY, [quote] TEXT)
	          ''')
    for quote in list_of_activities:
        quote = quote.replace("'", "")
        quote = quote.replace('"', '')
        index = list_of_activities.index(quote),

        c.execute(f'INSERT INTO dummy_trumpy  (quote_id, quote) VALUES (?,?)',
				    ( list_of_activities.index(quote), quote))

        #c.executemany(sql_insert,quote)


    conn.commit()
    conn.close()

number_of_quotes = int(input('How many quotes would you like to add to our database?'))
quote_picker(number_of_quotes)
quote_spitter()
#database_maker()
