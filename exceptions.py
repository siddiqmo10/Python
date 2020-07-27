
# exit code 0 means it occurred with no error
# 0 means success anything else means error

try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0")
except ValueError:
    print("Invalid Value")

# this try and except will print error message and the program wont crash
