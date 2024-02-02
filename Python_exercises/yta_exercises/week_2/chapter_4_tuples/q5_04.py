def unpack_tuple(t):
    if len(t) >= 3:
        a, b, c = t
        return a, b, c
    else:
        return "Tuple does not have enough elements."
    
# Test:
print(unpack_tuple((1, 2, 3)))