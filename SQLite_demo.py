"""
Stephen Nielsen

SQLite demo
"""

# import SQLite
from pickletools import read_string1
import sqlite3

# link the database
data = sqlite3.connect("data.db")

# create cursor
cursor = data.cursor()

"""
# create table
cursor.execute('''CREATE TABLE Employees (id, name, job_description)''')

# insert data
cursor.execute("INSERT INTO Employees VALUES (001, 'Jim', 'Mechanic')")
cursor.execute("INSERT INTO Employees VALUES (002, 'Steve', 'Electrician')")
"""

# retrieve data
return_data = cursor.execute("SELECT name FROM Employees WHERE id=002")

# commit changes
data.commit()

# print data
print(*return_data)


# close connection
data.close



