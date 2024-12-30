from sre_constants import ANY
from time import sleep
from typing import Any
from decoration.log_decoration import log_decoration
from faker import Faker
import json


@log_decoration()
def generate_fake_data(count: int = 1) -> list:
    """Generate a list of dictionaries containing fake user data."""
    fake = Faker()
    return [
        {
            "name": fake.name(),
            "address": fake.address(),
            "email": fake.email(),
            "job": fake.job(),
            "phone_number": fake.phone_number(),
            "ssn": fake.ssn(),
            "username": fake.user_name()
        }
        for _ in range(count)
    ]


if __name__ == "__main__":
    list_dict = generate_fake_data(2)
    print(json.dumps(list_dict, indent=4))
