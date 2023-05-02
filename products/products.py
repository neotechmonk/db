import sqlite3


class Product:
    def __init__(self):
        self.con = sqlite3.connect("test.db")  # create a new DB if one doesnt exit
