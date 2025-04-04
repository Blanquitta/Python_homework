# 1
import traceback

try:
    # 
    with open("diary.txt", "a") as diary_file:
        # Initial prompt
        user_input = input("What happened today? ")

        # Keep prompting 
        while user_input.lower() != "done for now":
            diary_file.write(user_input + "\n")  # Write 
            user_input = input("What else? ")

        # Write final "done for now" 
        diary_file.write("done for now\n")
    print("Your entries have been saved.")
    ...

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



# except Exception as e:
#     # Handle exceptions and print traceback information
#     print("An error occurred:")
#     traceback.print_exc()

#2






