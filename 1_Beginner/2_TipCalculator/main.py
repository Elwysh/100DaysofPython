# Calculate a tip in a restuarant 

print("Welcome to the US tip calculator.")

bill = float(input("What was the total bill?\n"))
percentage = float(input("How much would you like to tip? (in %)\n"))
people = int(input("How many people are splitting the bill?\n"))

result = str((bill + (bill * percentage / 100)) / people)
rounded = "{:.2f}".format(result)
# can also use round() but that is not gonna display 0 at the at if the result is 32.6 (if you want to round to 2 decimal places)

print("Each person should pay: " + rounded)
