from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('/data/users.db')
    except sqlite3.Error as e:
        print(e)
    return conn

@app.route('/user', methods=['GET', 'POST'])
def users():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Users')
        users = [
            dict(id=row[0], firstname=row[1], lastname=row[2],
                 phonenumber=row[3], email=row[4], age=row[5])
            for row in cursor.fetchall()
        ]
        return jsonify(users), 200

    if request.method == "POST":
        data = request.json
        sql = '''INSERT INTO Users (firstname, lastname, phonenumber, email, age)
                 VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(sql, (
            data['firstname'], data['lastname'],
            data['phonenumber'], data['email'], data['age']
        ))
        conn.commit()
        return f"User created successfully", 201

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def user_by_id(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Users WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            user = dict(id=row[0], firstname=row[1], lastname=row[2],
                        phonenumber=row[3], email=row[4], age=row[5])
            return jsonify(user), 200
        return "User not found", 404

    if request.method == "PUT":
        data = request.json
        sql = '''UPDATE Users SET firstname=?, lastname=?, phonenumber=?, email=?, age=? WHERE id=?'''
        cursor.execute(sql, (
            data['firstname'], data['lastname'], data['phonenumber'],
            data['email'], data['age'], id
        ))
        conn.commit()
        return jsonify(data), 200

    if request.method == "DELETE":
        cursor.execute('DELETE FROM Users WHERE id=?', (id,))
        conn.commit()
        return f"User with id: {id} deleted successfully", 200

@app.route('/address', methods=['GET', 'POST'])
def addresses():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Addresses')
        addresses = [
            dict(id=row[0], user_id=row[1], address_line=row[2], city=row[3], country=row[4])
            for row in cursor.fetchall()
        ]
        return jsonify(addresses), 200

    if request.method == "POST":
        data = request.json
        sql = '''INSERT INTO Addresses (user_id, address_line, city, country)
                 VALUES (?, ?, ?, ?)'''
        cursor.execute(sql, (
            data['user_id'], data['address_line'], data['city'], data['country']
        ))
        conn.commit()
        return f"Address created successfully", 201

@app.route('/address/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def address_by_id(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Addresses WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            address = dict(id=row[0], user_id=row[1], address_line=row[2], city=row[3], country=row[4])
            return jsonify(address), 200
        return "Address not found", 404

    if request.method == "PUT":
        data = request.json
        sql = '''UPDATE Addresses SET user_id=?, address_line=?, city=?, country=? WHERE id=?'''
        cursor.execute(sql, (
            data['user_id'], data['address_line'], data['city'], data['country'], id
        ))
        conn.commit()
        return jsonify(data), 200

    if request.method == "DELETE":
        cursor.execute('DELETE FROM Addresses WHERE id=?', (id,))
        conn.commit()
        return f"Address with id: {id} deleted successfully", 200

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Orders')
        orders = [
            dict(id=row[0], user_id=row[1], description=row[2], amount=row[3])
            for row in cursor.fetchall()
        ]
        return jsonify(orders), 200

    if request.method == "POST":
        data = request.json
        sql = '''INSERT INTO Orders (user_id, description, amount)
                 VALUES (?, ?, ?)'''
        cursor.execute(sql, (
            data['user_id'], data['description'], data['amount']
        ))
        conn.commit()
        return f"Order created successfully", 201

@app.route('/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def order_by_id(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Orders WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            order = dict(id=row[0], user_id=row[1], description=row[2], amount=row[3])
            return jsonify(order), 200
        return "Order not found", 404

    if request.method == "PUT":
        data = request.json
        sql = '''UPDATE Orders SET user_id=?, description=?, amount=? WHERE id=?'''
        cursor.execute(sql, (
            data['user_id'], data['description'], data['amount'], id
        ))
        conn.commit()
        return jsonify(data), 200

    if request.method == "DELETE":
        cursor.execute('DELETE FROM Orders WHERE id=?', (id,))
        conn.commit()
        return f"Order with id: {id} deleted successfully", 200

@app.route('/payments', methods=['GET', 'POST'])
def payments():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Payments')
        payments = [
            dict(id=row[0], order_id=row[1], payment_method=row[2], paid=row[3])
            for row in cursor.fetchall()
        ]
        return jsonify(payments), 200

    if request.method == "POST":
        data = request.json
        sql = '''INSERT INTO Payments (order_id, payment_method, paid)
                 VALUES (?, ?, ?)'''
        cursor.execute(sql, (
            data['order_id'], data['payment_method'], data['paid']
        ))
        conn.commit()
        return f"Payment created successfully", 201

@app.route('/payments/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def payment_by_id(id):
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor.execute('SELECT * FROM Payments WHERE id = ?', (id,))
        row = cursor.fetchone()
        if row:
            payment = dict(id=row[0], order_id=row[1], payment_method=row[2], paid=row[3])
            return jsonify(payment), 200
        return "Payment not found", 404

    if request.method == "PUT":
        data = request.json
        sql = '''UPDATE Payments SET order_id=?, payment_method=?, paid=? WHERE id=?'''
        cursor.execute(sql, (
            data['order_id'], data['payment_method'], data['paid'], id
        ))
        conn.commit()
        return jsonify(data), 200

    if request.method == "DELETE":
        cursor.execute('DELETE FROM Payments WHERE id=?', (id,))
        conn.commit()
        return f"Payment with id: {id} deleted successfully", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
