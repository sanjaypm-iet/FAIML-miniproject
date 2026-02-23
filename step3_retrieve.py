from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["HousePriceDB"]
collection = db["houses"]

# Retrieve data
data = list(collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

# Remove MongoDB automatic _id column
df = df.drop("_id", axis=1)

print("Data retrieved from MongoDB:")
print(df.head())