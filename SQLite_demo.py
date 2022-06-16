"""
Stephen Nielsen

SQLite demo
"""

"""
Set up
"""

# import SQLite
import sqlite3

# link the database
data = sqlite3.connect("data.db")

# create cursor
cursor = data.cursor()

"""
# create table
cursor.execute('''CREATE TABLE Employees (id, name, job_description)''')

# insert data
cursor.execute("INSERT INTO Employees VALUES ('001', 'Jim', 'Mechanic')")
cursor.execute("INSERT INTO Employees VALUES ('002', 'Steve', 'Electrician')")
"""

"""
Define possible actions
"""

# confirm action
def confirm():
    user_input = input("Do you want to continue?")

    if (user_input[0].lower() == "y"):
        data.commit()
        print("Data commited")

# insert data
def insert():

    # gather data
    print("Enter the data for each column:")
    id = input("id: ")
    name = input("name: ")
    job_description = input("job_description: ")

    # input data
    cursor.execute(f"INSERT INTO Employees VALUES ('{id}', '{name}', '{job_description}')")
    
    #commit data
    confirm()


# modify data
def modify():
    pass

# delete data
def delete():
    pass

# retrieve data
def retrieve():

    # gather data
    col = input("Which column would you like to search by?: ")
    return_type = input("which column do you want to see?: ")
    param = input("What would you like to search for?: ")

    # search
    return_data = cursor.execute(f"SELECT {return_type} FROM Employees WHERE {col}={param}")

    # retrun data
    print("This is what was found:")
    print(return_data)




"""
Start gathering input
"""

while (True):
    print("-----")
    print("The table 'Employees' has three columns: id, name, and job_description.")
    user_input = input("What would you like to do with the data? (options: insert, modify, delete, retrieve, exit program)")

    user_input_simple = user_input[0].lower()

    if (user_input_simple == "i"): # insert
        insert()
    elif (user_input_simple == "m"): # modify
        modify()
    elif (user_input_simple == "d"): # delete
        delete()
    elif (user_input_simple == "r"): # retrieve.
        retrieve()
    else: # exit program
        print("Exiting program")
        break






"""
# retrieve data
return_data = cursor.execute("SELECT name FROM Employees WHERE id=002")

# commit changes
data.commit()

# print data
print(*return_data)


# close connection
data.close
"""


