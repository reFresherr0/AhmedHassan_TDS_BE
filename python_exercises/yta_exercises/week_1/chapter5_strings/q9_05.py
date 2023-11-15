def unique_words(sentence):
    # split the sentence into words
    words = sentence.split()
    # create an empty set to store unique words
    unique_words = set()
    # iterate over the words and add them to the set
    for word in words:
        unique_words.add(word)
    # convert the set back to a list and return it
    return list(unique_words)

# Test
sentence = 'the quick brown fox jumps over the lazy dog'
print(unique_words(sentence))
