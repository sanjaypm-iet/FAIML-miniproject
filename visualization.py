from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

client = MongoClient("mongodb://localhost:27017/")
db = client["HousePriceDB"]
collection = db["houses"]

data = list(collection.find())
df = pd.DataFrame(data)
df = df.drop("_id", axis=1)

yes_no_columns = ["mainroad", "guestroom", "basement",
                  "hotwaterheating", "airconditioning", "prefarea"]

for col in yes_no_columns:
    df[col] = df[col].map({"yes": 1, "no": 0})

df = pd.get_dummies(df, columns=["furnishingstatus"], drop_first=True)

X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.show()