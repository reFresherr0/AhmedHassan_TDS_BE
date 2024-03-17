def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# example usage
sentence = "Hello world, how are you?"
reversed_sentence = reverse_words(sentence)
print(reversed_sentence)
