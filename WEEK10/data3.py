import pandas as pd

data = {'Name': ['A', 'B', None],
        'Age': [25, None, 23],
        'Marks': [90, 85, 85]}

df = pd.DataFrame(data)

# Fill missing values
df.fillna(0, inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Add new column
df['Total'] = df['Marks'] + 10

print(df)