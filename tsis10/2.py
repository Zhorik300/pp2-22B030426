import sqlite3

# connect to database
conn = sqlite3.connect('snake.db')
cur = conn.cursor()

# create user table
cur.execute('''CREATE TABLE IF NOT EXISTS user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               level INTEGER DEFAULT 1
            )''')

# create user_score table
cur.execute('''CREATE TABLE IF NOT EXISTS user_score (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INTEGER NOT NULL,
               score INTEGER NOT NULL,
               level INTEGER NOT NULL,
               FOREIGN KEY (user_id) REFERENCES user(id)
            )''')

# function to check if a user exists in the database
def user_exists(username):
    cur.execute('''SELECT id FROM user WHERE username = ?''', (username,))
    return cur.fetchone() is not None

# function to create a new user
def create_user(username):
    if user_exists(username):
        print("User already exists.")
    else:
        cur.execute('''INSERT INTO user (username) VALUES (?)''', (username,))
        print("User created successfully.")

# function to show the current level of a user
def show_level(username):
    if not user_exists(username):
        print("User does not exist.")
    else:
        cur.execute('''SELECT level FROM user WHERE username = ?''', (username,))
        level = cur.fetchone()[0]
        print("Current level:", level)

# function to save user score to the database
def save_score(username, score, level):
    if not user_exists(username):
        print("User does not exist.")
    else:
        cur.execute('''SELECT id FROM user WHERE username = ?''', (username,))
        user_id = cur.fetchone()[0]
        cur.execute('''INSERT INTO user_score (user_id, score, level) VALUES (?, ?, ?)''', (user_id, score, level))
        print("Score saved successfully.")

# sample usage of the above functions
username = input("Enter your username: ")
create_user(username)

show_level(username)

level = 3
score = 500
save_score(username, score, level)

# close the database connection
conn.commit()
conn.close()