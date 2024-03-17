import random

# Generate 5 random numbers between 0 and 10
randomList = random.sample(range(1, 11), 5)
print(randomList)

numbers = randomList

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print('Maximum number is:', max_num)
print('Minimum number is:', min_num)
