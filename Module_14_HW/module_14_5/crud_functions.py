import sqlite3

# connection = sqlite3.connect('product_base.db')
# cursor = connection.cursor()


def initiate_db():
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()
    connection = sqlite3.connect('user_base.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
        )
        ''')
    connection.commit()
    connection.close()


def add_values():
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    for i in range(1, 8):
        cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
                       (f'Продукт{str(i)}', f'Описание{i}', i*50))
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('product_base.db')
    cursor = connection.cursor()
    all_prod = cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    connection.close()
    return all_prod


def add_user(username, email, age):
    if not is_included(username):
        connection = sqlite3.connect('user_base.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))
        connection.commit()
        connection.close()


def is_included(username):
    connection = sqlite3.connect('user_base.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if cursor.fetchone() is None:
        return False
    else:
        return True


# connection.commit()
# connection.close()
