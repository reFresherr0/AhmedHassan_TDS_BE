def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Test
print(get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])) # [2, 4, 6, 8]