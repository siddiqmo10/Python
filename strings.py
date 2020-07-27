course = 'Python for Beginners'
# when to use '' or ""

# imagine typing Python's we need "" instead of ''
course = "Python's Course for Beginners"
course = 'Python for "Beginners"'

course = """
Hi John, 

Here is our first email to you.

Thank you,
The support team

"""

course = 'Python for Beginners'
another = course[:]
print(course[0])

# this feature is on python and not many other languages
print(course[-1])  # it prints the last char
print(course[0:3]) # print from 0 to 3 but exclude the char at 3, 0: print till the end
print(course[:3])  # will asume 0:3
print(another)   # we can copy or clone a string

name = 'Jennifer'
print(name[1:-1])  # ennife exclude the last char and star from 1

# --------------------------------------------------------------
