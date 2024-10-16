# ============= TASK =============

# Design a program for a courier company that calculates the cost of sending a parcel
# The cost needs to factor in the user input
# Distance: The total distance of the delivery in kilometres. Use the distance input to calculate the Freight cost below.
# Use variables, each with two options based on the user's choice:

# Get distance from user
distance_km = int(input(" Hi. How far, in kilometres, from our office do want your Parcel delivered? "))
print("The distance is:",user_input1,"km")
print(" ")

# freight = user_input1<=150
# freight = user_input1>=150
delivery_land = user_input1*0.25
delivery_air = user_input1*0.36
freight = 0

delivery = input("Do you prefer Air Freight or Land Freight? ")
if delivery == 'Land Freight':
    freight = delivery_land
    print("Your parcel delivery will cost R0.25c per km, by Land Freight.")
    print(" ")
    print("That'll will be R",freight)
    print(" ")
else:
    freight = delivery_air
    print("Your parcel delivery will cost R0.36c per km, by Air Freight.")
    print(" ")
    print("That'll will be R",freight)
    print(" ")

# ==================

# insurance = 50.00
# insurance = 25.00
insurance = 0.0

# Get approval for Full or Partial Insurance
parcel_insurance = input("Would you like Full Insurance for your Parcel: True or False ?")
if user_input2=="True":
    insurance = 50.00
    print("An additional R50.00 will added to Delivery Cost")
    print(" ")
else:
    insurance = 25.00
    print("An additional Partial Insurance cost of R25.00 will added to Delivery Cost")
    print(" ")

# ==================


gift = 0.00

# Get approval for Gift Cover
gift_cover = input("Would you like a Gift Cover for your Parcel? True or False ? ")
if user_input3=="True":
    gift = 15.00
    print("An additional R15.00 will be added to your Parcel Delivery Cost")
    print(" ")
else:
    print("No Gift Cover charge will be added to your Parcel Delivery cost.")
    print(" ")

# ==================

# priority = 100.00
# priority = 20.00
priority = 0.00

# Get approval for Priority or Standard Delivery
priority_delivery = input("Would you like Priority Delivery for your Parcel: True or False?")
if user_input4=="True":
    priority = 100.00
    print("An additional R100.00 will be added to your Parcel Delivery Cost.")
    print(" ")
else:
    priority = 20.00
    print("A Standard Delivery charge of R20.00 will be added to your Parcel Delivery Cost.")
    print(" ")

# ==================

# parcel = 100.00
# parcel = 150.00
parcel = 0.00

# Get approval for Postage Box or Parcel Sleeve
postage_box = input("Would you like a Postage Box for your Parcel: True or False ?")
if user_input5=="True":
    parcel = 150.00
    print("An additional R150.00 will be added to your Parcel Delivery Cost.")
    print(" ")
else:
    parcel = 100.00
    print("An additional R100.00 for a Parcel Sleeve will be added to your Parcel Delivery Cost.")
    print(" ")

# ==================

# Total Cost for Delivery with Add-Ons
total_cost = freight + insurance + gift + priority + parcel
print("Your Total Delivery Cost will be: R", round(total_cost,2))

