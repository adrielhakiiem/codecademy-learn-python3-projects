hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

for price in prices:
  total_price += price 

print("This is the total price: " + str(total_price))
print("\n")

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))
print("\n")

new_prices = [price - 5 for price in prices]
print("This is the new prices for each haircut: " + str(new_prices))
print("\n")

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += (prices[i] * last_week[i])

print("Total Revenue: " + str(total_revenue)) 
print("\n")

average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: " + str(average_daily_revenue))
print("\n")

cuts_under_30 = [hairstyles[i] for i in  range(len(hairstyles[i])) if new_prices[i] < 30]

print("These are the cuts under 30: "+ str(cuts_under_30))
