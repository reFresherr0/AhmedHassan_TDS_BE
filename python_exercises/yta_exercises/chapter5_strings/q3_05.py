# A function that checks if a string is a palindrome.
def is_palindrome(s):
    # Convert the string to lowercase and remove any non-alphanumeric characters
        # The isalnum() method returns True if all characters in the string are alphanumeric
    s = ''.join(e for e in s if e.isalnum()).lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test
print(is_palindrome("racecar")) 
print(is_palindrome("hello"))   
