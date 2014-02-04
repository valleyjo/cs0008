#Email: amv49@pitt.edu
#Name: Alex Vallejo
#ID: 3578411
#Description: This program is a budget calculator. It will help you calculate
#             your monthly budget by asking you estimated values for monthly
#             spending.

# print a welcome message
print("Author: Alex Vallejo <amv49@pitt.edu>")
print("\nThis is a budget calculator program. It will help you calculate\
         \nyour monthly budget")

# Get the user's name
name = input("\nEnter your name: ")

# Display a personalized greeting
print("\nHello " + name + "\n")

print("You may enter non-integers for the following inputs.")
print("EXAMPLE => Food: $525.67")
print("EXAMPLE => Regular hours: 160.5\n")

# Values entered as dollar amounts
hourly_rate = float(input("Hourly rate: $"))       # hourly rate
overtime_rate = float(input("Overtime rate: $"))   # overtime rate per hour
regular_hours = float(input("Regular hours: "))    # number of reguar hours worked
overtime_hours = float(input("Overtime hours: "))  # number of overtime hours worked
rent = float(input("Rent: $"))                     # cost of rent
food = float(input("Food: $"))                     # cost of food
entertainment = float(input("Entertainment: $"))   # cost of entertainment
car = float(input("Car: $"))                       # cost of car

print("\nPlease enter the following values as percentages in decimal form.")
print("EXAMPLE => Electric bill: .02\n")

# Values entered as percentages
electric_p = float(input("Electric bill: "))  # cost of electric bill
water_p = float(input("Water bill: "))        # cost of water bill
sewer_p = float(input("Sewer bill: "))        # cost of sewer bill
gas_p = float(input("Gas bill: "))            # cost of gas bill


# Print the name, value and type of each variable
print("\nVariables Details:")
print("Name: hourly_rate  Value: ", hourly_rate, "Type: ", type(hourly_rate))
print("Name: overtime_rate  Value: ", overtime_rate, "Type: ", type(overtime_rate))
print("Name: regular_hours  Value: ", regular_hours, "Type: ", type(regular_hours))
print("Name: overtime_hours  Value: ", overtime_hours, "Type: ", type(overtime_hours))
print("Name: rent  Value: ", rent, "Type: ", type(rent))
print("Name: electric_p  Value: ", electric_p, "Type: ", type(electric_p))
print("Name: water_p  Value: ", water_p, "Type: ", type(water_p))
print("Name: sewer_p  Value: ", sewer_p, "Type: ", type(sewer_p))
print("Name: gas_p  Value: ", gas_p, "Type: ", type(gas_p))
print("Name: food  Value: ", food, "Type: ", type(food))
print("Name: entertainment  Value: ", entertainment, "Type: ", type(entertainment))
print("Name: car  Value: ", car, "Type: ", type(car))
