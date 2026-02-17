# Len's slice
# You work at Len’s Slice, a new pizza joint in the neighborhood. 
#You are going to use your knowledge of Python lists to organize some of your sales data.

# Create a list called toppings that holds pizza toppings
toppings = ['pepproni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# to keep track of how much each kind of pizza slice costs, create a list called prices
prices = [2,6,1,3,2,7,2]

# count the number of occurences of '2' in the prices list, and store the result in a variable called 'num_two_dollar_slices'
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# find the length of the toppings list and store it in a variable called num_pizzas
num_pizzas = len(toppings)
print(num_pizzas)

# Print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas.
print("We sell", num_pizzas, "different kinds of pizza!")

#create a two-dimensional list called pizza_and_prices 
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], 
                    [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]
print(pizza_and_prices)

#sort pizza and prices so that the pizzas are in the order of increasing price
pizza_and_prices.sort()
print(pizza_and_prices)

#store the first element of pizza_and_prices in a variable called cheapest_pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)


# A man walks into the pizza store and shouts “I will have your MOST EXPENSIVE pizza!”
# Get the last item of the pizza_and_prices list and store it in a variable called priciest_pizza.
priciest_pizza = pizza_and_prices[6]
print(priciest_pizza)

# It looks like the most expensive pizza from the previous step was our very last "anchovies" slice. 
# Remove it from our pizza_and_prices list since the man bought the last slice.
pizza_and_prices.remove([7, 'anchovies'])
print(pizza_and_prices)

# add a new topping called peppers to pizza and prices [2.5, 'peppers']
# be mindful to place in order of the pizza and prices
pizza_and_prices.insert(4, [2.5, 'peppers'])
print(pizza_and_prices)

# slice the pizza_and_prices list and store the 3 lowest cost pizzas in a list called three_cheapest
three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)

