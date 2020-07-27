names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[2])
print(names[-1])
print(names[2:])
print(names[2:4])
print(names[:])

# write a program to find the largest number in a list
numbers1 = [1,3,2,1,15,10,3,9]
max = 0
for num in numbers1:
    if num > max:
        max = num

print(max)

# --------------------------------------

print("---------------------------------")

# 2D Lists
# a list within a list

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

print("---------------------------------")

# List Methods

numbers = [5, 2, 1, 5, 7, 4]
numbers.append(20)
print(numbers)
numbers.insert(0, 10)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(50 in numbers)
print(numbers.count(5))
print(numbers.sort())  # no return value so it just returns none as an object
print(numbers)
numbers2 = numbers.copy()
numbers.append(19)
print(numbers2)

print("---------------------------------")

# Write a program to remove duplicates in a list
uniques = []
for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)