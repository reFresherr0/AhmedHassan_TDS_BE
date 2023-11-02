sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("The longest word in the sentence is:", longest_word)
