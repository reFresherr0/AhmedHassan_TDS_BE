sentence = input('Enter a sentence: ')
words = sentence.split()        # split the sentence into words
longest_word = ''            # initialize an empty string

for word in words:  
    if len(word) > len(longest_word):   
        longest_word = word

print('The longest word in the sentence is:', longest_word)
