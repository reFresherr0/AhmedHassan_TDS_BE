import string

def count_words(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Split text into words
    words = text.split()
    # Create dictionary to store word frequencies
    word_freq = {}
    # Iterate over words and update dictionary
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

# Example usage
text = "This is a sample text. It contains some words, and some punctuation!"
word_freq = count_words(text)
print(word_freq)
