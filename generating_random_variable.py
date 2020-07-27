import random

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)  # choses random from our list
print(leader)

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))  # between 10-20

print("----" * 5)


# Exercise
# create a program to roll a 2 sided dice
class Dice:
    def __init__(self):
        pass

    def roll(self):
        rand_tuple = {random.randint(1, 6): random.randint(1, 6)}
        return rand_tuple


"""
Mosh's version

Class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second    # python recognizes this as a tuple no need of ()
        
"""

dice1 = Dice()
print(dice1.roll())
