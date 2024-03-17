age = int(input("Enter your age: "))
has_license = input("Do you have a driver's license? (yes/no): ")

if age >= 18 and has_license.lower() == "yes":
    print("You can drive.")
else:
    print("You cannot drive.")
