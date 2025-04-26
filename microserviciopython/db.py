import sqlite3

conn = sqlite3.connect('/data/users.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    phonenumber TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Addresses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    address_line TEXT,
    city TEXT,
    country TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    description TEXT,
    amount REAL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Payments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    payment_method TEXT,
    paid INTEGER,
    FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE
);
''')

conn.commit()
conn.close()