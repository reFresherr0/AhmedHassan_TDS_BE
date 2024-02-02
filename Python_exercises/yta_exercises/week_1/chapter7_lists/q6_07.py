def longer_words(words_list, length):
    # This function takes a list of words and a specified length and returns the list of words
    # longer than the specified length.
    
    return [word for word in words_list if len(word) > length]

# Test
print(longer_words(['hello', 'goodbye', 'hi', 'bye', 'yes', 'no'], 3)) # ['hello', 'goodbye']
