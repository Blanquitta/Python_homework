# Write your code here.
# 1 Print "Hello, World!"
print("Hello, World!")
#2
def greet(name):
    return f"Hello, {name}!"
print(greet("Lilian"))
#3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
           return a + b 
        elif operation == "subtract":
            return a - b

        elif operation =="mutiply":
            return a * b
        elif operation == "divide": 
         try:       
            return a/b
         except: 
             return "you can divide by zero"
        elif operation == "modulo":
            return a % b
        elif operation == "int divide": 
            try:
             return a // b 
            except:
               return "you can divede by zero"
        elif operation == "power" :
            return a ** b
        else: print("can not do that operation")
    except TypeError:
        return f"you can't {operation} by those values "
    
  #4  
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        elif data_type == "int":
            return int(value)
        else:
            raise ValueError("Invalid data type requested")
    except (ValueError, TypeError):
        return "You cannot convert value into a type"

#  Result
print(data_type_conversion("235", "int"))   
print(data_type_conversion("235.47", "float"))   
print(data_type_conversion("hi", "nosense"))  # Output: You cannot convert value into a type

#5 
def grade(*args):
    try:
        # Convert all arguments to a list 
        scores = [int(arg) for arg in args]
        
        if not scores:  # If no valid scores were provided
            return "No scores provided"
        
        # Get the average of the scores
        average = sum(scores) / len(scores)
        
        # Determine the grade based on the average
        if average >= 90:
            return "A"
        elif average >= 80-89:
            return "B"
        elif average >= 70-79:
            return "C"
        elif average >= 60-69:
            return "D"
        else:
            return "F"
    except (ValueError, TypeError):  #  invalid input
        return "invalid data was provided"

# Print scores
print(grade(82, 85, 88))           # Output: B
print(grade(100, 95))              # Output: A
print(grade(65,70, 62))            # Output: C
print(grade ("nosense", 80, 85))   # Output: invalid data was provided

# 6 Range and Loop repetitions

def repeat_string(string, count):
    repeated_string = ""
    for _ in range(count):
            repeated_string += string
    return repeated_string
my_string = "Hello"
repetitions = 3 #Times repeteaded
result = repeat_string(my_string, repetitions)
print(result)

#7 

def student_scores(position, **kwargs):
        if not kwargs:
            return "No scores provided."

        if position == "best":
            return max(kwargs.values())
        elif position == "mean":
            return sum(kwargs.values()) / len(kwargs)
        else:
            return "Invalid position argument. Use 'best' or 'mean'."

print(result)