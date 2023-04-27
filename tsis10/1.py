import sqlite3
import csv

# define database name
DB_NAME = 'phonebook.db'

# create a connection to the database
conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

# create a table for the phonebook
cur.execute('''CREATE TABLE IF NOT EXISTS PhoneBook
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                phone TEXT,
                email TEXT,
                address TEXT,
                city TEXT,
                state TEXT,
                zip TEXT)''')

# function for inserting data from CSV file
def insert_from_csv(file_name):
    with open(file_name, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cur.execute('''INSERT INTO PhoneBook (first_name, last_name, phone, email, address, city, state, zip)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                        (row['First Name'], row['Last Name'], row['Phone'], row['Email'], row['Address'], row['City'], row['State'], row['Zip']))
            conn.commit()
    print("Data from CSV file inserted successfully")

# function for inserting data from console
def insert_from_console():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    city = input("Enter City: ")
    state = input("Enter State: ")
    zip = input("Enter Zip: ")

    cur.execute('''INSERT INTO PhoneBook (first_name, last_name, phone, email, address, city, state, zip)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                (first_name, last_name, phone, email, address, city, state, zip))
    conn.commit()
    print("Data inserted successfully")

# function for updating data in the table
def update_data():
    user_choice = input("Enter 1 to update first name or 2 to update phone: ")
    if user_choice == "1":
        user_id = input("Enter ID: ")
        new_first_name = input("Enter new First Name: ")
        cur.execute('''UPDATE PhoneBook SET first_name = ? WHERE id = ?''', (new_first_name, user_id))
        conn.commit()
        print("First Name updated successfully")
    elif user_choice == "2":
        user_id = input("Enter ID: ")
        new_phone = input("Enter new Phone: ")
        cur.execute('''UPDATE PhoneBook SET phone = ? WHERE id = ?''', (new_phone, user_id))
        conn.commit()
        print("Phone updated successfully")
    else:
        print("Invalid choice")

# function for querying data from the table
def query_data():
    user_choice = input("Enter 1 to query by first name, 2 to query by last name, or 3 to query by phone: ")
    if user_choice == "1":
        first_name = input("Enter First Name: ")
        cur.execute('''SELECT * FROM PhoneBook WHERE first_name = ?''', (first_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    elif user_choice == "2":
        last_name = input("Enter Last Name: ")
        cur.execute('''SELECT * FROM PhoneBook WHERE last_name = ?''', (last_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    elif user_choice == "3":
        phone = input