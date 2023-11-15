month = input("Enter a month: ").lower()

if month in ["december", "january", "february"]:
    print("Winter")
elif month in ["march", "april", "may"]:
    print("Spring")
elif month in ["june", "july", "august"]:
    print("Summer")
elif month in ["september", "october", "november"]:
    print("Fall")
else:
    print("Invalid month entered.")
