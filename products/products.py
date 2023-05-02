import sqlite3


class Product:
    def __init__(self):
        self.con = sqlite3.connect("test.db")  # create a new DB if one doesnt exit
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        # self.cur.execute("DROP TABLE products")
        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS products( 
                    date DATE PRIMARY KEY,
                    category TEXT, 
                    store TEXT, 
                    name TEXT, 
                    price REAL,
                    link TEXT        
        )"""
        )

    def insert(self, product):
        self.cur.execute(
            """INSERT OR IGNORE INTO products
                 VALUES(?,?,?,?,?,?)""",
            product,
        )
        self.con.commit()

    def read(self):
        self.cur.execute("""SELECT * FROM products""")
        rows = self.cur.fetchall()
        return rows
