from time import sleep
from decoration.log_decoration import log_decoration
from faker import Faker
import json


@log_decoration
def generate_fake_data() -> dict:
    """Generate a dictionary of fake user data."""
    fake = Faker()
    sleep(0.002)
    return {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "job": fake.job(),
        "phone_number": fake.phone_number(),
        "ssn": fake.ssn(),
        "username": fake.user_name()
    }


if __name__ == "__main__":
    dict1 = generate_fake_data()
    print(json.dumps(dict1, indent=4))
