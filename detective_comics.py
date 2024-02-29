import csv
import pprint
import mysql.connector as msql
from mysql.connector import Error

comics = []
def create_comic_list(comics = comics):
  with open("dc-comics.csv", 'r') as file:
      csvreader = csv.reader(file)

      for row in csvreader:
          comics.append(row)

      pprint.pprint(comics)
      print(comics[0])

def create_database():

    try:
        conn = msql.connect(host='127.0.0.1', user='root',
                            password='root')  # give ur username, password
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE Detective_Comics")
            print("Database is created")
    except Error as e:
        print("Error while connecting to MySQL", e)

    try:
        conn = msql.connect(host='localhost', database='Detective_Comics', user='root', password='root')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS comic_book_characters;')
            print('Creating table....')
            # in the below line please pass the create table statement which you want #to create
            cursor.execute(
                "CREATE TABLE comic_book_characters(page_id int,first_name varchar(255),urlslug varchar(255),ID varchar(255),Align varchar(255),eye varchar(255),Hair varchar(255),Sex varchar(255),Alive varchar(255),Appearances varchar(255),First_appearance varchar(255),Year varchar(255),web varchar(255))")
            print("Table is created....")
            # loop through the data frame
            for i, row in comics.iterrows():
                # here %S means string values
                sql = "INSERT INTO Detective_Comics.comic_book_characters VALUES (%i,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                # the connection is not auto committed by default, so we must commit to save our changes
                conn.commit()

                sql = "SELECT * FROM employee.employee_data"
                cursor.execute(sql)
                # Fetch all the records
                result = cursor.fetchall()
                for i in result:
                    print(i)
    except Error as e:
        print("Error while connecting to MySQL", e)



def main():
  create_comic_list()
  create_database()

main()