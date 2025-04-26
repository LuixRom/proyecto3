import sqlite3
import os


if not os.path.exists('/data/users.db'):
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


    for i in range(20000):
        cursor.execute('''
            INSERT INTO Users (firstname, lastname, phonenumber, email, age)
            VALUES (?, ?, ?, ?, ?)
        ''', (f'First{i}', f'Last{i}', f'12345{i}', f'user{i}@example.com', 20 + (i % 30)))

    conn.commit()
    conn.close()
    print("Base de datos creada y llena exitosamente.")
else:
    print("Base de datos ya existe, no se creó nuevamente.")
