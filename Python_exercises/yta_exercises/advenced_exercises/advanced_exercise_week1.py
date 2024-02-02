import string

def read_file(file_path):   # A function to read a file and return a list of unique words and a list of all words
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()   # Remove punctuation and split into words
        unique_words = list(set(words))
        return unique_words, words

def count_word(word, words):    # A function to count the number of times a specified word appears in a list of words
    return words.count(word)

def print_word_frequencies(unique_words, words):    # A function to print the word frequencies to a file
    with open('word_frequencies.txt', 'w') as file:
        for word in unique_words:
            count = count_word(word, words)  # Count the number of times the word appears in the list of words
            print(f'{word}: {count}')
            file.write(f'{word}: {count}\n')    # Write the word and its frequency to the file

# Test
unique_words, words = read_file('input_file.txt')
print_word_frequencies(unique_words, words)
