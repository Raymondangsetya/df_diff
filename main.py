from module.function import report_diff

import pandas as pd

# Creating a mock-up DataFrame for the 'new' data
new_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'age': [25, 30, 28, 35, 29],
    'city': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']
}

new = pd.DataFrame(new_data)

# Creating a mock-up DataFrame for the 'old' data
old_data = {
    'id': [1, 2, 3, 6, 7],
    'name': ['Alice', 'Bob', 'Charlie', 'Fiona', 'George'],
    'age': [25, 30, 25, 22, 29],
    'city': ['Indonesia', 'London', 'Paris', 'Sydney', 'Madrid']
}

old = pd.DataFrame(old_data)

# Print the mock-up DataFrames for verification
print("New DataFrame:")
print(new)
print("\nOld DataFrame:")
print(old)

key = "id"
Report=list()

Report = report_diff(new=new,old=old,key=key,report=Report)
print(Report)
# Convert the list to a DataFrame
report_df = pd.DataFrame(Report, columns=['Report'])  # Change 'Column_Name' to an appropriate column name for your report

# make a csv file
report_df.to_csv('report.csv', index=False)