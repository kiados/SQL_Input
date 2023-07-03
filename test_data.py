from datetime import datetime
from faker import Faker
from random import randint


def create_test_data(count=10000):
    test_data = {}
    test_users = []
    test_items = []
    test_purchases = []

    fake = Faker('ru_RU')

    for i in range(1, count+1):

        # create Users
        user = {'age': randint(18, 65)}
        test_users.append(user)

        # create Items
        item = {'price': randint(10, 1000)}
        test_items.append(item)

        # create Purchases
        purchase = {
            # 'table': 'purchases',
            'UserId': randint(1, count),
            'ItemId': randint(1, count),
            'date': str(fake.date_between(datetime(2021,1,1), datetime(2023,6,6)))
        }
        test_purchases.append(purchase)

    test_data['users'] = test_users
    test_data['items'] = test_items
    test_data['purchases'] = test_purchases

    return test_data