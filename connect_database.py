## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT NAME From restaurants where NEIGHBORHOOD_ID = 1")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_restaurants = db_cursor.fetchall()


print(list_restaurants)

liste = []

for i in list_restaurants:
      liste.append(i[0])

print(liste)

db_connection.close()



f = open('index.html',"w")
f.write("""<html>
  <head>
   <title>A super simple python CGI server</title>
 </head>
 <body>

 <p>
   Here is a list of all restaurants in Kreuzberg: </br>
   1. {} <br>
   2. {}

 </p>
 <body>
 """.format(liste[0],liste[1]))
