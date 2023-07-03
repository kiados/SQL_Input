import os
import sqlite3
from loguru import logger

class Database:

    db_name = "my_db.db"
    connect = None
    cursor = None

    def create_db_and_tables(self):

        if os.path.exists(self.db_name):
            logger.warning(f'Database {self.db_name} already exists!')
            os.remove(self.db_name)

        self.connect = sqlite3.connect("my_db.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users (userId INTEGER PRIMARY KEY, age INT)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Purchases (purchaseId INTEGER PRIMARY KEY, userId,'
                            ' itemId, date)')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Items (itemId INTEGER PRIMARY KEY, price)')

    def insert_test_data(self, users, items, purchases):

        for row in users:
            self.insert_row('users', row)

        for row in items:
            self.insert_row('items', row)

        for row in purchases:
            self.insert_row('purchases', row)

        return

    def insert_row(self, table, row):
            columns = ",".join([str(item) for item in row])
            values = ",".join([f'"{str(row[item])}"' for item in row])
            stmt = f'INSERT INTO {table}({columns}) VALUES({values})'
            self.cursor.execute(stmt)
            self.connect.commit()
