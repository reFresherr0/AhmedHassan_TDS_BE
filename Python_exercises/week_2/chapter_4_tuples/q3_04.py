def count_occurrences(tup, element):
    count = 0
    for item in tup:
        if item == element:
            count += 1
    return count

# Test:
print(count_occurrences((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 1))