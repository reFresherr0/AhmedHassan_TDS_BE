def char_generator(string):
    for char in string:
        yield char


for char in char_generator("Python"):
    print(char)
    