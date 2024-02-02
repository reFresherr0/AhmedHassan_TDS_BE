string = 'The quick brown fox jumps over the lazy dog'
old_word = 'fox'
new_word = 'cat'

# split the string into a list of words
words = string.split()

# loop through the words and replace the old word with the new word
for i in range(len(words)):
    if words[i] == old_word:
        words[i] = new_word

# join the words back into a string
new_string = ' '.join(words)

print(new_string)
