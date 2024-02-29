import requests
import pprint
import sqlite3

# sets url and headers for later on picking the api
url = "https://matchilling-tronald-dump-v1.p.rapidapi.com/random/quote"

headers = {
    "content-type": "application/octet-stream",
    "Accept": "application/hal+json",
    "X-RapidAPI-Key": "c7ccb727bemsh820f82fd14a46dbp1bb1e7jsn2847a6613051",
    "X-RapidAPI-Host": "matchilling-tronald-dump-v1.p.rapidapi.com"
}
list_of_quotes = []


def quote_picker(number_of_quotes=3):
    for i in range(number_of_quotes):
        response = requests.get(url, headers=headers)

        print(response)

        pprint.pprint(response.json())
        quote = response.json()['value']

        list_of_quotes.append(quote)


def quote_spitter():
    for quote in list_of_quotes:
        print(quote)


def database_maker():
    conn = sqlite3.connect('Tronald_Dump_Lulz.db')
    c = conn.cursor()

    c.execute('''
	          CREATE TABLE IF NOT EXISTS dummy_trumpy
	          ([quote_id] INTEGER PRIMARY KEY, [quote] TEXT)
	          ''')
    for quote in list_of_quotes:
        quote = quote.replace("'", "")
        quote = quote.replace('"', '')
        index = list_of_quotes.index(quote),

        c.execute(f'INSERT INTO dummy_trumpy  (quote_id, quote) VALUES (?,?)',
				    ( list_of_quotes.index(quote), quote))

        #c.executemany(sql_insert,quote)


    conn.commit()
    conn.close()

def main():
    number_of_quotes = int(input('How many quotes would you like to add to our database?'))
    quote_picker(number_of_quotes)
    quote_spitter()
    database_maker()

main()

