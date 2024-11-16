from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://mongoadmin:mongoadmin@localhost:27018", directConnection=True)
db = client["PERFECT_STORE"]
collection = db["SCORES"]

data = collection.update_many(
    {"date": "2024-06-20", "pillars.name": "Preço"},
    {"$set": {"pillars.$.score_achieved": 0, "update_date": datetime.now()}}
)

print(data.modified_count)


data = collection.delete_many(
    {"date": "2024-06-02"}
)

try:
    print(data.modified_count)
except:
    pass