with open("my_file.txt", "a") as f:
    f.write("\nThis is a new line\n")

with open("my_file.txt", "r") as f:
    print(f.read())
