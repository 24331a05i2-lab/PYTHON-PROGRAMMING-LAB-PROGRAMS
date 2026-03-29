import pandas as pd
data = {'Name': ['A', 'B', 'C'],
        'Age': [25, 20, 23],
        'Marks': [90, 85, 88]}
df = pd.DataFrame(data)
print("Sorted by Age:\n", df.sort_values(by='Age'))
print("\nFirst two rows:\n", df[:2])
print("\nMarks column:\n", df['Marks'])
print("\nUsing iloc:\n", df.iloc[0:2, 0:2])