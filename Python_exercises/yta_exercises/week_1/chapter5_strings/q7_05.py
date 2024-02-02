def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()

    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)

# Test
print(is_anagram('Listen', 'silent'))
print(is_anagram('Astronomer', 'Moon starer'))
print(is_anagram('Hello', 'World'))
