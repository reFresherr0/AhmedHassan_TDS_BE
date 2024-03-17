# Get package weight and shipping method from user
weight = float(input("Enter the package weight in pounds: "))
shipping_method = input("Enter the shipping method (ground, priority, or express): ")

# Calculate shipping cost based on weight and shipping method
if shipping_method == "ground":
    if weight <= 2:
        cost = 1.5 * weight + 2.5
    elif weight <= 6:
        cost = 3.0 * weight + 2.5
    elif weight <= 10:
        cost = 4.0 * weight + 2.5
    else:
        cost = 4.75 * weight + 2.5
elif shipping_method == "priority":
    if weight <= 2:
        cost = 3.0 * weight + 5.0
    elif weight <= 6:
        cost = 4.0 * weight + 5.0
    elif weight <= 10:
        cost = 5.0 * weight + 5.0
    else:
        cost = 6.0 * weight + 5.0
elif shipping_method == "express":
    if weight <= 2:
        cost = 4.5 * weight + 10.0
    elif weight <= 6:
        cost = 9.0 * weight + 10.0
    elif weight <= 10:
        cost = 12.0 * weight + 10.0
    else:
        cost = 14.0 * weight + 10.0
else:
    print("Invalid shipping method entered. Please enter 'ground', 'priority', or 'express'.")

# Display shipping cost to user
print("The shipping cost is $%.2f." % cost)
