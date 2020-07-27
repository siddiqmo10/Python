def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user("John", "Smith")
greet_user(last_name="Smith", first_name="John")  # keyword argument irrespective of the order of the parameters
greet_user("Mary", last_name="Jane")  # when mixing always postional arg then keyword arg
print("Finish")

print("------------------------------------")


# return

def square(number):
    return number * number


print(square(3))

# be default python return none for every function
# if instead of return number * number we type print(number*number)
# and then we call it as print(square(3)) it will print 9 None

# reusable functions

print("------------------------------------")

def emoji(description):
    words = description.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "☹️"
    }

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


description = input(">")
print(emoji(description))



