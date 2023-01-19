# Getting Ready for Physics Class! 

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

# f_to_c, a function that takes fahrenheit as argument and converts it to celcius 
def f_to_c(f_temp):
    # celcius = (fahrenheit - 32) * 5/9
    c_temp = (f_temp - 32) * 5/9
    return c_temp

f100_in_celcius = f_to_c(100) # runs 

# c_to_f, a function that takes celcius as argument and converts it to fahrenheit 
def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32 
    return f_temp

c0_in_fahrenheit = c_to_f(0) # runs 

# get_force, a function that takes a product of mass and acceleration
def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration) # output = 226800 

print("The GE train supplies " + str(train_force) + " Newtons of force.") # runs 

# get_energy, a function that takes a product of mass and c squared 
c = 3*10**8 
def get_energy(mass, c):
    return mass * (c**2)

bomb_energy = get_energy(bomb_mass, c) 

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.") # runs 

# get_work, a function that that takes mass, acceleration, distance

# work = force(get_force) * distance 
def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
