def is_palindrome(list):
    # Returns True if the given list is a palindrome (reads the same forwards and backwards), False otherwise.

    # Compare the first and last elements, then the second and second-to-last elements, and so on.
    for i in range(len(list) // 2):
        if list[i] != list[-i - 1]:
            return False
    return True

# Test
list1 = [1, 2, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]
print(is_palindrome(list1))  # True
print(is_palindrome(list2))  # Falses