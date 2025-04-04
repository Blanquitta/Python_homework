#2
import csv
import traceback

def read_employees():
    # Dictionary to store the data
    data = {}
    # List to store the rows
    rows = []
    
    try:
        # 
        with open('../csv/employees.csv', mode='r') as file:
            # Read the CSV file
            csv_reader = csv.reader(file)
            
            # Loop through the rows
            for index, row in enumerate(csv_reader):
                if index == 0:
                    # Store the first row as column headers 
                    data["fields"] = row
                else:
                    # Add each row to the list
                    rows.append(row)
            
            # Add the row
            data["rows"] = rows
            return data
            
    

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
        
    
    
    # Return the dictionary
    

# Call the function and store the result in a global variable
employees = read_employees()
print(employees)

# #3

def column_index(heading):
    return employees['fields'].index(heading)
employee_id_column = column_index('employee_id')
print('Task2:\n', f'Employee_id_column: {employee_id_column}')

# #4

def first_name(row_number):
    #  employee dataset
    
    
    # Get the column index for "First Name"
    first_name_col_index = column_index("first_name")
    return employees["rows"][row_number][first_name_col_index]
    # Retrieve the value 
   

print(first_name(1)) 

 #5 
def employee_find(employee_id):
     
    
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches=list(filter(employee_match, employees["rows"]))
    return(matches)
# print(employee_match) 
   
        

      #6 
    
def employee_find_2(employee_id):
        matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
        return matches



# # # #7 
def sort_by_last_name():


# Define the index for the last name in the row
# 
# # Sort the list of rows in place 
    employees['rows'].sort(key=lambda row: row[column_index('last_name')])
    return employees['rows']


# Call the function
sort_by_last_name() 


#  # #8

 



# #  create an employee dictionary excluding 'employee_id'
def employee_dict(row):
#     # Exclude 'employee_id' from the dictionary
 employee_data = employees['fields']
 return dict(zip(employee_data[1:],row[1:]))

print(employee_dict(employees['rows'][0]))


     
#  #9
 

employees = [
    
]

# Function to create an employee dictionary excluding 'employee_id'
def employee_dict(row):
    # Exclude 'employee_id' from the dictionary
    employee_data = {key: value for key, value in row.items() if key != "employee_id"}
    return employee_data

# #10
import os 
def get_this_value():
  
  return os.getenv('THISVALUE')
  
  
#   #11
  import os

secret = "shazam"

def set_secret(new_secret):
    global secret
    secret = new_secret

import custom_module

# Define the set_that_secret function
def set_that_secret(new_secret):
    # Call the custom_module's set_secret function
    custom_module.set_secret(new_secret)

# Call the set_that_secret function with a new string of your choice
set_that_secret( )
print(custom_module.secret)

# #12 
import csv

def read_minutes():
    # Create dictionaries to store minutes data
    minutes1 = {"fields": [], "rows": []}
    minutes2 = {"fields": [], "rows": []}

    # Read the first CSV file (../csvminutes.csv)
    with open("../csvminutes.csv", mode="r") as file1:
        reader1 = csv.reader(file1)
        minutes1["fields"] = next(reader1)  # First row is the header (fields)
        minutes1["rows"] = [tuple(row) for row in reader1]  # Convert each row to a tuple

with open("../cvsminutess2.cvs", mode="r") as file2:
        reader2 = csv.reader(file2)
        minutes2["fields"] = next(reader2)  # First row is the header (fields)
        minutes2["rows"] = [tuple(row) for row in reader2]  # Convert each row to a tuple

    # Return both dictionaries
        print(read_minutes)

# Call the function and print the result
minutes1, minutes2 = read_minutes()
print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

# #13
def create_minute_set():


    # Example dictionaries minutes1 and minutes2 (ensure these exist in the code beforehand)
    minutes1 = {
        "fields": ["Time", "Note"],
        "rows": [("10:00", "Discussion about project"), ("10:15", "Review updates")]
    }
    minutes2 = {
        "fields": ["Time", "Comment"],
        "rows": [("11:00", "Plan next steps"), ("11:30", "Assign tasks")]
    }

    # Create sets from the rows of minutes1 and minutes2
    set1 = set(minutes1["rows"])  # Convert rows of minutes1 to a set
    set2 = set(minutes2["rows"])  # Convert rows of minutes2 to a set

    # Combine both sets into one single set
    combined_set = set1.union(set2)

    # Return the combined set
    return combined_set

# Call the function and print the result
result = create_minutes_set()
print(result)

# #14

from datetime import datetime

def create_minute_list():
    # Example minutes set containing recorder name and date strings
    minutes_set = {
        ["Alice", "March 25 25"],
        ["Bob", "April 01 25"]
    }

    # Convert minutes_set into a list
    minutes_list = list(minutes_set)
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d %y")), minutes_list))

    # Return the final list of tuples
    return converted_list

    # Call the function and print the result
    result = create_minute_list()
    print(result)

    # #15
import csv
from datetime import datetime

def write_sort_list():
    # Example fields from minutes1
    fields = ["Name", "Date"]

    # Example list to be sorted
    minutes_list = [
        ("Alice", datetime(2025, 3, 25)),
        ("Bob", datetime(2025, 4, 1))
    ]
import csv
from datetime import datetime

def write_sort_list():
    # Example fields from minutes1
    fields = ["Name", "Date"]

    # Example list to be sorted
    minutes_list = [
        ("Alice", datetime(2025, 3, 25)),
        ("Bob", datetime(2025, 4, 1))
    ]
write_sort_list()

print("Sorted list has been written to './minutes.csv'")





