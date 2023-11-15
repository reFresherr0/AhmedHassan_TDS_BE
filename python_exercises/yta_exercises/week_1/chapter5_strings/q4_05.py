# A function that removes all the vowels from a given string
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return(''.join([char for char in string if char not in vowels]))

# Test
print(remove_vowels('hello world'))
print(remove_vowels('Python is awesome'))
print(remove_vowels('AEIOU'))
print(remove_vowels(''))
print(remove_vowels('abcdefghijklmnopqrstuvwxyz'))