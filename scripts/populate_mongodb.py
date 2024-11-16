import random
import pprint
from datetime import datetime, date
import urllib.parse

from faker import Faker
from faker.providers import person, company, date_time
import pymongo


username = urllib.parse.quote_plus('mongoadmin')
password = urllib.parse.quote_plus('mongoadmin')
client = pymongo.MongoClient("mongodb://%s:%s@localhost:27018" % (username, password), directConnection=True) 
db = client["PERFECT_STORE"]
collection = db["SCORES"]


PILLARS = [("Preço", 40), ("Ponto Extra", 20), ("Presença", 40)]

def _add_providers(faker, *providers):
    for provider in providers:
        faker.add_provider(provider)
    return faker

fake = Faker("pt_BR")
fake = _add_providers(fake, person, company, date_time)


def generate_data_perfect_store():
    data = {}
    data["point_of_sale"] = fake.company()
    data["name_promoter"] = fake.name()
    data["date"] = fake.date_between(start_date=date(2024, 6, 1)).strftime("%Y-%m-%d")
    data["pillars"] = [{"name": pillar_score[0], "max_score": pillar_score[1], "score_achieved": round(random.uniform(0, pillar_score[1]), 2)} for idx, pillar_score in enumerate(PILLARS)]
    data["update_date"] = datetime.now()
        
    pprint.pprint(data)
    return data

def insert_into_mongodb(data):
    collection.insert_one(data) 
   

if __name__ == "__main__":
    while True:
        data = generate_data_perfect_store()
        insert_into_mongodb(data)
