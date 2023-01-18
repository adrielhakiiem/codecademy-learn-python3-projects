hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# sum up ALL the prices of haircuts 
total_price = 0

# loop through prices list and add each price to the variable total_price
for price in prices:
    total_price += price # runs 

# find average price 
average_price = total_price / len(prices) # runs 

print("Average Haircut Price: " + str(average_price))

# cut all prices by 5 dollars and add it into a new list called new_prices using list comprehension 
new_prices = [price - 5 for price in prices]

print(new_prices) # runs 

# checking how much revenue
total_revenue = 0

for i in range(0, len(hairstyles)):
    # product of prices and last_week and add it to total_revenue 
    total_revenue += prices[i] * last_week[i]

print("Total Revenue: " + str(total_revenue)) # runs 

# find the average daily revenue 
average_daily_revenue = total_revenue / 7 

print("The Average Daily Revenue is: " + str(average_daily_revenue)) # runs 

# create a list of cuts under the price of 30 to advertise shop using list comprehension (display name of hairstyles instead of the price) 
cuts_under_30 = [] 

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])) if new_prices[i] < 30]

print("These are the haircuts that are under $30: " + str(cuts_under_30))
