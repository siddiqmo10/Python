# list of coordinates (x, y)
"""for x in range(4):
    for y in range(3):
        print(f'({x}, {y})') """


# -----------------------------
# Exercise
numbers = [5, 2, 5, 2, 2]
numbers_L =[2, 2, 2, 2, 5]

for out in numbers:
    output = ''
    for inner in range(out):
        output += 'X'
    print(output)

print(" ")

for out in numbers_L:
    output = ''
    for inner in range(out):
        output += 'X'
    print(output)