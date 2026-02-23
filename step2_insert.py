from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create database
db = client["HousePriceDB"]

# Create collection
collection = db["houses"]

# Load JSON file
with open("housing.json") as file:
    data = json.load(file)

# Insert data
collection.insert_many(data)

print("Data successfully inserted into MongoDB!")