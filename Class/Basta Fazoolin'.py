# -- FIRST CLASS -- #
class Menu:

  # METHODS 
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return "Hello and welcome! This is the {a} menu, have a look! We serve from {b} to {c}.".format(a = self.name, b = self.start_time, c = self.end_time)

  # Returns the total price of a purchase consisting of all the items in purchased_items 
  def calculate_bill(self, purchased_items):
    bill = 0 
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
      else:
        print("Sorry, we don't seem to offer that meal over here! ")
    return bill


# MENU 
brunch_items = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}

early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 
  'espresso': 3.00
}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00
}

kids_items = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}

arepas_menu = {
  'arepa pabellon': 7.00, 
  'pernil arepa': 8.50, 
  'guayanes arepa': 8.00, 
  'jamon arepa': 7.50
}

# Declaration 
brunch = Menu("brunch", brunch_items, 1100, 1600)
early_bird = Menu("early_bird", early_bird_items, 1500, 1800)
dinner = Menu("dinner", dinner_items, 1700, 2300)
kids = Menu("kids", kids_items, 1100, 2100)
arepa = Menu("arepa", arepas_menu, 1000, 2000)

# -- SECOND CLASS -- #
class Franchise:

  # METHODS 
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus 

  def __repr__(self):
    return "This is the franchise on the {a}".format(a = self.address)

  def available_menus(self, time):
    available_menu = [] 
    for menu in self.menus:
      if time >= menu.start_time and time < menu.end_time:
        available_menu.append(menu)
    return available_menu


flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Muberry Street", [brunch, early_bird, dinner, kids])
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# -- THIRD CLASS -- #
class Business:

  # METHODS 
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
take_a_arepa = Business("Take a' Arepa", [arepas_place])

print(take_a_arepa)
