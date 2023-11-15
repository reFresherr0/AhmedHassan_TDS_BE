minutes = input("Enter number of minutes:")
hours_div = int(minutes) // 60      # integer division
minutes_rem = int(minutes) % 60     # remainder
print(str(minutes) + " minutes are equal to " + str(hours_div) + " hours and " + str(minutes_rem) + " minutes")
