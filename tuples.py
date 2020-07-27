# tuples cant be modified they are immutable

numbers = (1, 2, 3)
print(numbers[0])

print("--------------------")

# unpacking
coordinates = (1, 2, 3)

# if you want to use these values many times in a code

""" x = coordinates[0]
y = coordinates[1]
z = coordinates[2] """

# we can do this with unpacking
x, y, z = coordinates
print(z)
# we can do this on lists as well
