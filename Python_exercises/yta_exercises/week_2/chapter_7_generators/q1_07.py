
def natural_numbers():
    num = 1
    while True:
        yield (num)
        num += 1
n_nums = natural_numbers()
print(next(n_nums))
print(next(n_nums))
print(next(n_nums))
print(next(n_nums))

