weight = 41.5

# GROUND SHIPPING
# cost = (weight * price per pound) + flat charge 
# flat charge = 20.00
if weight <= 2:
  cost = (weight * 1.50) + 20.00
elif weight <= 6:
  cost = (weight * 3.00) + 20.00
elif weight <= 10:
  cost = (weight * 4.00) + 20.00
else:
  cost = (weight * 4.75) + 20.00

print("This is the cost for Ground Shipping:  $" + str(cost))
print("\n")

# PREMIUM GROUND SHIPPING
# cost2 = weight + flat charges 
cost2 = 125.00

print("This is the cost for Premium Ground Shipping:  $" + str(cost2))
print("\n")

# DRONE SHIPPING
# cost3 = weight * price per pound 
if weight <= 2:
  cost3 = (weight * 4.50) 
elif weight <= 6:
  cost3 = (weight * 9.00) 
elif weight <= 10:
  cost3 = (weight * 12.00) 
else:
  cost3 = (weight * 14.25) 

print("This is the cost for Drone Shipping:  $" + str(cost3))
