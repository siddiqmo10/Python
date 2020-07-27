# in dictionaries we can store key value pairs

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# each key should be unique we cant have age more than once
customer["name"] = "Jack Smith"
customer["birthdate"] = "Jan 2"
print(customer["name"])
print(customer.get("birthdate"))  # dosent throw error just returns none since no key exist
print(customer.get("birthdate", "Jan 1 1980"))  # replace none with a default value

print("------------------------------------------")

phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)