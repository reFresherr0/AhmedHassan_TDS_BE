names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Isabel', 'Jack', 'Kate', 'Liam', 'Mia', 'Nancy', 'Oliver', 'Peter', 'Quinn', 'Rose', 'Sarah', 'Tom', 'Uma', 'Victor', 'Wendy', 'Xander', 'Yara', 'Zoe']

vowels = 'aeiou'

for name in names:
    if name[0].lower() in vowels:
        print(name)
