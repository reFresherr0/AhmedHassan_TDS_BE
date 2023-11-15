age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ")

if age >= 18 and citizenship.lower() == "yes":
    print("You are eligible to vote in national elections.")
elif age >= 16 and citizenship.lower() == "no":
    print("You are eligible to vote in local elections but not in national elections.")
else:
    print("You are not eligible to vote.")
