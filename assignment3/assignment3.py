#1
import pandas as pd 
 
#df = pd.read_csv("my_file.csv")


data ={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
# df = pd.DataFrame(data)
# print(df)
task1_data_frame = pd.DataFrame(data)

task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print(task1_with_salary)



task1_older = task1_with_salary.copy()

# Increment the 'Age' column by 1 for each entry
task1_older["Age"] = task1_older["Age"] + 1

# Print the modified DataFrame 
print(task1_older)

task1_older.to_csv("employees.csv", index=False)

print("DataFrame saved to employees.csv without an index!")

#2

task2_employees = pd.read_csv("employees.csv")

# Print the DataFrame 
print(task2_employees)
#mport pandas as pd
import json

#  Create the JSON file with additional employee data




# # Step 2: Load the JSON file into a new dataframe
json_employees = pd.read_json("additional_employees.json")

print("JSON Employees DataFrame:")
print(json_employees)



# # Step 4: Combine the data from the JSON file and the CSV file
more_employees = pd.concat([task2_employees , json_employees], ignore_index=True)

# # Verify the combined dataframe
print("\nCombined Employees DataFrame:")
print(more_employees)

# #3
first_three = more_employees.head(3)

# Print the  rows to 
print("\nFirst Three Rows:")
print(first_three)

last_two = more_employees.tail(2)
print("\nLast_Two Rows:")
print(last_two)

employee_shape = more_employees.shape

# Print the shape to verify
print("\nShape of the DataFrame:")
print(employee_shape)

print(more_employees.info())

# #4 


import numpy as np

# Create a dataframe from 'dirty_data.csv' 
dirty_data = pd.read_csv("dirty_data.csv")
print("Original Dirty Data:")
print(dirty_data)

# # Step 1: Create a copy of the dirty data
clean_data = dirty_data.copy()

# Step 2: Remove duplicate rows
#  clean_data.drop_duplicates()
print("\nAfter Removing Duplicates:")
print(clean_data)
clean_data.drop_duplicates(inplace=True)
# # Step 3: Convert 'age' to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("\nAfter Converting 'Age' to Numeric:")
print(clean_data)




# # Step 4: Convert 'salary' to numeric and replace placehold
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'].replace(['unknown', 'n/a'], np.nan), errors='coerce')
print("\nAfter Converting 'Salary' to Numeric and Replacing Placeholders:")
print(clean_data)

# # Step 5: Fill missing numeric values
clean_data['Age'].fillna(clean_data['Age'].mean(), inplace=True)
clean_data['Salary'].fillna(clean_data['Salary'].median(), inplace=True)
print("\nAfter Filling Missing Values (Age with Mean, Salary with Median):")
print(clean_data)

# # Step 6: Convert 'hire_date' to datetime
# data = {'Hire_Date': ['']}
# clean_data = pd.DataFrame(data)



clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("\nAfter Converting 'Hire Date' to  datetime:")
print(clean_data)

# #   Step 7: Strip extra whitespace and standardize 
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print("\nAfter Cleaning 'Name' and 'Department':")
print(clean_data)

