import converters
from converters import kg_to_lbs
from utils import find_max
import ecommerce.shipping  # name of packcage.module
# or for easier code
from ecommerce.shipping import calculate_shipping
# if you have multiple function from a module
from ecommerce import shipping

kg_to_lbs(70)  # when import a method then don't need to prefix it
converters.kg_to_lbs(70)

# Exercise
# create a function to find max in converters.py

numbers = [10, 3, 6, 2]

print(find_max(numbers))

print("----------------------")

# packages



ecommerce.shipping.calculate_shipping()
# instead of above we can use
calculate_shipping()
calculate_shipping()

# since we imported from shipping
shipping.calculate_shipping()
