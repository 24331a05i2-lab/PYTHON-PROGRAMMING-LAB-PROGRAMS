import pandas as pd
df = pd.read_csv("organizations-100.csv")
print("Head:\n", df.head())
print("\nTail:\n", df.tail())
print("\nInfo:")
df.info()
print("\nDescribe:\n", df.describe())