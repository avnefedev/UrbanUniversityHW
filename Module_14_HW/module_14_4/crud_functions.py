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
    cursor.execute('SELECT * FROM Products')
    # connection.close()
    return cursor.fetchall()


# connection.commit()
# connection.close()
