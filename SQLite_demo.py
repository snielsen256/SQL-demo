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
    user_input = input("Do you want to continue?: ")

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
    
    # commit data
    confirm()


# modify data
def modify():
    # gather data
    id_original = input("Which entry would you like to modify? (Enter id): ")
    value_original = input("What value you like to modify?: ")
    value_new = input("What would you like to set it to?: ")

    # apply 
    
    cursor.execute(f"UPDATE Employees SET '{value_original}'='{value_new}' WHERE id='{id_original}'")

    # commit data
    confirm()



# delete data
def delete():
    # gather data
    id_row = input("Which entry would you like to delete? (Enter id): ")

    # apply
    cursor.execute(f"DELETE FROM Employees WHERE id='{id_row}'")

    # commit data
    confirm()

# retrieve data
def retrieve():

    # gather data
    col = input("Which column would you like to search?: ")
    param = input(f"What {col} are you looking for?: ")

    # search
    cursor.execute(f"SELECT * FROM Employees WHERE {col}='{param}'")

    # return data
    print("This is what was found:")
    print(cursor.fetchall())




"""
Start gathering input
"""

while (True):
    print("-----")
    print("The table 'Employees' has three columns: id, name, and job_description.")
    user_input = input("What would you like to do with the data? (options: insert, modify, delete, retrieve, exit program): ")

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




