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

# 6 Range and Loop repetitionsl

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
def student_scores(option, **scores):
        if option == "best":
            # Find the student with the highest score
            best_student = max(scores, key=scores.get)
            return best_student
        elif option == "mean":
            # Calculate the average score
            if scores:
                average_score = sum(scores.values()) / len(scores)
                return average_score
            else:
                return 0  # Return 0 
        else:
            return "Invalid option. Use 'best' or 'mean'."

    # Example 
print(student_scores("best", Alice=90, Bob=75, Charlie=85)) 
print(student_scores("mean", Alice=90, Bob=75, Charlie=85))  


#8

                    
def titleize(input_string):
    # Define the list of exception words that should not be capitalized
    exceptions = {"a", "on", "an", "the", "of", "and", "is", "in"}

    # Split the input string into a list of words
    words = input_string.split()

    # Loop through the words with their index using enumerate
    for index, word in enumerate(words):
        if index == 0 or index == len(words) - 1:  # Always capitalize the first and last words
            words[index] = word.capitalize()
        elif word in exceptions:  # Lowercase the exceptions in the middle
            words[index] = word.lower()
        else:  # Capitalize all other words
            words[index] = word.capitalize()

    # Join the words back into a single string
    return " ".join(words)

# Example usage
text = "a quick brown fox jumps over the lazy dog in the park"  # Define 'text'  here
print(titleize(text))

#9

def hang_man(secret, guess):
    # Create a list to store the result
    result = []

    # Loop through each letter in the secret word
    for letter in secret:
        if letter in guess:  # If the letter is in the guess string
            result.append(letter)  # Keep the letter
        else:
            result.append("_")  # Replace with an underscore

    # Join the result list into a string and return it
    return "".join(result)

# Example usage
secret_word = "alphabet"
guess_letters = "ab"
print(hang_man(secret_word, guess_letters))

#10

def pig_latin(sentence):
    # Split the  sentence into words
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        # Rule 1: Starts with a vowel
        if word[0] in 'aeiou':
            pig_latin_word = word + 'ay'
        # Rule 3: Starts with 'qu'
        elif word[:2] == 'qu':
            pig_latin_word = word[2:] + 'quay'
        # Rule 2: Starts with consonants
        else:
            # Find the first vowel in the word
            for i, letter in enumerate(word):
                if letter in 'aeiou':
                    break
            pig_latin_word = word[i:] + word[:i] + 'ay'
        
        pig_latin_words.append(pig_latin_word)

    # Join the words into a sentence
    return ' '.join(pig_latin_words)

# Test 
english_sentence = "the quick brown fox jumps over the lazy dog"
pig_latin_sentence = pig_latin(english_sentence)
print(pig_latin_sentence)



                        

