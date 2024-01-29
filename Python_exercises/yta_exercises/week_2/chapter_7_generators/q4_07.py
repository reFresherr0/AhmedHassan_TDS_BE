def square_generator():
    num = 1
    while True:
        yield num ** 2
        num += 1


for i in square_generator():
    if i > 100:
        break
    print(i)