is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cool day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#  Exercise
price = 1000000
is_credit_good = True

if is_credit_good:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment: $ {down_payment}")

# ---------------------------------------

# Logical Operators

has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
        print("Eligible for loan")
        # wont print becuase True and False

# ---------------------------------------
print("---------------------------------------")
# Comparison Operators

temperature = 30
if temperature > 30:
    print("It's a hot a day")
else:
    print("It's not a hot day")

# Exercise

name = input("Name:")
namelen = len(name)
if namelen < 3:
    print("Name must be at least 3 characters")
elif namelen > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")


