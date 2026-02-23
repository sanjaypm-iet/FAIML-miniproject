import pandas as pd

df = pd.read_csv("Housing.csv")

print(df.head())

df.to_json("housing.json", orient="records")

print("CSV successfully converted to JSON!")