course = 'Python for Beginners'

print(len(course))  # number of char using len or number of items in a list
print(course.upper())
print(course)  # doesnt modify original string but makes another one
print(course.lower())
print(course.find('o'))  # return index of first appearance of char
                         # returns -1 if cant find anything
print(course.find('Beginners'))  # 11 because thats where the word starts

print(course.replace('Beginners', 'Absolute Beginners'))

# if you wanna know if the string contains the word python

print('Python' in course)  # returns boolean


# len and print are general purpose functions but upper
# is specific to objects like upper which is specific to strings
# and they are then called as methods


