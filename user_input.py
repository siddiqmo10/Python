# Ask a user their weight (in pounds), convert it to kilograms and print on the terminal


weight = input("What is your weight ? ")
# weight_kilo = float(weight) / 2.20462
weight_kilo = int(weight) * 0.45
print("Your weight in kilograms is :", weight_kilo)

# Solution by mosh

weight_lbs = input("Weight (lbs): ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

# i over complciated it will change to int instead of float