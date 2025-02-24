from faker import Faker

class User:

    @staticmethod
    def create_data_user():
        fake = Faker()

        reg_data = {
            "email": fake.email(),
            "password": fake.password(),
            "name": fake.name()}
        return reg_data

    data_real = {
        "email": "testemail@yandex.ru",
        "password": "password"
    }

    data_fake = {
        "email": "testemail_wrong@yandex.ru",
        "password": "password"
    }

    data_double = {
        "email": "testemail@yandex.ru",
        "password": "password",
        "name": "name"
    }

    data_empty_email = {
        "email": "",
        "password": "password",
        "name": "name"
    }

    data_empty_password = {
        "email": "testemail@yandex.ru",
        "password": "",
        "name": "name"
    }

    data_empty_name = {
        "email": "testemail@yandex.ru",
        "password": "password",
        "name": ""
    }

    data_updated = {
        "email": "testemail@yandex.ru",
        "password": "password",
        "name": "new_name"
    }