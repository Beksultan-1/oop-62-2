import sqlite3

connect = sqlite3.connect("movies.db")

cursor = connect.cursor()

cursor.execute('''
CREATE TABLE movies(
     name VARCHAR(20) NOT NULL,
     rating VARCHAR(10) NOT NULL,
     description TEXT  
)
''')