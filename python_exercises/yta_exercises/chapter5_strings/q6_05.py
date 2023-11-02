def capitalize_sentence(sentence):
    words = sentence.split()   # split the sentence into words  
    capitalized_words = [word.capitalize() for word in words]   # The capitalize() method returns a string where the first character is upper case.
    return " ".join(capitalized_words)

# Test
print(capitalize_sentence("hello world"))
print(capitalize_sentence("how are you?"))
