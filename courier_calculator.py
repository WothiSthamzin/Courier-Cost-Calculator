# ============= TASK =============

# Design a program for a courier company that calculates the cost of sending a parcel
# The cost needs to factor in the user input
# Distance: The total distance of the delivery in kilometres. Use the distance input to calculate the Freight cost below.
# Use variables, each with two options based on the user's choice:


# Freight Cost Constants
LAND_FREIGHT_COST = 0.25  # Cost per km for land freight
AIR_FREIGHT_COST = 0.36   # Cost per km for air freight

# Insurance Cost Constants
FULL_INSURANCE_COST = 50.00
PARTIAL_INSURANCE_COST = 25.00

# Gift Wrap Cost Constant
GIFT_WRAP_COST = 15.00

# Priority Delivery Cost Constants
PRIORITY_DELIVERY_COST = 100.00
STANDARD_DELIVERY_COST = 20.00

# Packaging Cost Constants
POSTAGE_BOX_COST = 150.00
PARCEL_SLEEVE_COST = 100.00

# Get distance from user
distance_km = int(input(" Hi. How far, in kilometres, from our office do want your Parcel delivered? "))
print("The distance is:",user_input1,"km")
print(" ")

delivery = input("Do you prefer Air Freight or Land Freight? ").strip().lower()
if delivery == 'land freight':
    freight = user_input1 * LAND_FREIGHT_COST
    print("Your parcel delivery will cost R0.25c per km, by Land Freight.")
else:
    freight = user_input1 * AIR_FREIGHT_COST
    print("Your parcel delivery will cost R0.36c per km, by Air Freight.")

# ==================

# Get approval for Full or Partial Insurance
parcel_insurance = input("Would you like Full Insurance for your Parcel: True or False ?").strip().capitalize()
if user_input2 == "True":
    insurance = FULL_INSURANCE_COST
    print("An additional R50.00 will added to Delivery Cost")
else:
    insurance = PARTIAL_INSURANCE_COST
    print("An additional Partial Insurance cost of R25.00 will added to Delivery Cost")

# ==================


# Get approval for Gift Cover
gift_cover = input("Would you like a Gift Cover for your Parcel? True or False ? ").strip().capitalize()
if user_input3 == "True":
    gift = GIFT_WRAP_COST
    print("An additional R15.00 will be added to your Parcel Delivery Cost")
else:
    gift = 0.00
    print("No Gift Cover charge will be added to your Parcel Delivery cost.")
    print(" ")


# ==================

# Get approval for Priority or Standard Delivery
priority_delivery = input("Would you like Priority Delivery for your Parcel: True or False?").strip().capitalize()
if user_input4 == "True":
    priority = PRIORITY_DELIVERY_COST
    print("An additional R100.00 will be added to your Parcel Delivery Cost.")
else:
    priority = STANDARD_DELIVERY_COST
    print("A Standard Delivery charge of R20.00 will be added to your Parcel Delivery Cost.")

# ==================

# Get approval for Postage Box or Parcel Sleeve
postage_box = input("Would you like a Postage Box for your Parcel: True or False ?").strip().capitalize()
if user_input5 == "True":
    parcel = POSTAGE_BOX_COST
    print("An additional R150.00 will be added to your Parcel Delivery Cost.")
else:
    parcel = PARCEL_SLEEVE_COST
    print("An additional R100.00 for a Parcel Sleeve will be added to your Parcel Delivery Cost.")

# ==================

# Total Cost for Delivery with Add-Ons
total_cost = freight + insurance + gift + priority + parcel
print("Your Total Delivery Cost will be: R", round(total_cost,2))

