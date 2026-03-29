import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, None, 21, 23],
    'Marks': [85, 90, None, 88]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df.fillna(0, inplace=True)

df['Total'] = df['Marks'] + 5

df.rename(columns={'Marks': 'Score'}, inplace=True)

print("\nModified Data:")
print(df)