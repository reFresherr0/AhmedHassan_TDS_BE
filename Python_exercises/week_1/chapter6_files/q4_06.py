with open("my_file.txt", "r") as f:
    content = f.read()

with open("copy_of_file.txt", "w") as new_f:
    new_f.write(content)
