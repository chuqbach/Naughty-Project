from dataclasses import dataclass
from faker import Faker


@dataclass
class Manga:
    author: str
    title: str


class Generator:
    def __init__(self):
        self.fake: Faker = Faker()

    def generate(self):
        data = {
            "author": self.fake.name(),
            "address": self.fake.address()
        }
        return data
