string = input('Enter a string: ')
vowels = 'aeiou'
count = 0

for char in string:
    if char.lower() in vowels:
        count += 1

print('Number of vowels in the string:', count)
