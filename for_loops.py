for item in 'Phyton':
    print(item)

# item cant be printed outside of for loop
print("---------------")

for item in ['Mosh', 'Josh', 'Sarah']:
    print(item)

print("---------------")

for item in [1,2,3,4]:
    print(item)

print("---------------")

for item in range(5, 10):
    print(item)
print("---------------")

# increment by 2
for item in range(5,10, 2):
    print(item)

print("---------------")
print("Exercise")

# calculate total price of cart
total = 0
prices = [10, 20, 30]
for item in prices:
    total += item
print(total)