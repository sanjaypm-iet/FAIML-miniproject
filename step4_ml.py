from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["HousePriceDB"]
collection = db["houses"]

# Retrieve data
data = list(collection.find())
df = pd.DataFrame(data)
df = df.drop("_id", axis=1)

# Convert Yes/No columns to 1/0
yes_no_columns = ["mainroad", "guestroom", "basement",
                  "hotwaterheating", "airconditioning", "prefarea"]

for col in yes_no_columns:
    df[col] = df[col].map({"yes": 1, "no": 0})

# Convert furnishingstatus into numbers
df = pd.get_dummies(df, columns=["furnishingstatus"], drop_first=True)

# Define features and target
X = df.drop("price", axis=1)
y = df["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))