
#Task 3
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("./csv/employees.csv")

# Create a list of full names using list comprehension
full_names = [row['first_name'] + " " + row['last_name'] for index, row in df.iterrows()]
print("All employee names:")
print(full_names)

# Create a list of names that contain the letter 'e'
names_with_e = [name for name in full_names if 'e' in name.lower()]
print("\nEmployee names containing the letter 'e':")
print(names_with_e)



