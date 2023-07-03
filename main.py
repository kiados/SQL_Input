from db import Database
from test_data import create_test_data


if __name__ == '__main__':
    test_data = create_test_data()
    db = Database()
    db.create_db_and_tables()
    db.insert_test_data(**test_data)

