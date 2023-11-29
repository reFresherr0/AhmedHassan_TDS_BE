# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module: import re

# Search the string to see if it starts with "The" and ends with "Spain":
# txt = "The rain in Spain" 

# RegEx Functions
# findall Returns a list containing all matches                              x = re.findall("ai", txt)   print(x)
# search Returns a Match object if there is a match anywhere in the string   x = re.search("^The.*Spain$", txt)   print(x)
# split Returns a list where the string has been split at each match         x = re.split("\s", txt)   print(x)
# sub Replaces one or many matches with a string                             x = re.sub("\s", "9", txt)   print(x)
# Metacharacters
# [] A set of characters "[a-m]"   
# \ Signals a special sequence (can also be used to escape special characters) "\d"
# . Any character (except newline character) "he..o"   txt = "hello planet"   print(x)
# ^ Starts with "^hello"
# $ Ends with "world$"
# * Zero or more occurrences "he.*o"
# + One or more occurrences "he.+o"
# {} Exactly the specified number of occurrences "al{2}"
# | Either or "falls|stays" txt = "The rain in Spain falls mainly in the plain!"   #Check if the string contains either "falls" or "stays":   x = re.findall("falls|stays", txt)   print(x)
# ? Zero or one occurrences "he.?o"
# () Capture and group  (xyz),  (xyz)x,   (yz|zy),     (\d{2})-(\d{4}),       (?:xyz),   (\d+)\.(\d+),    (?:\d+)\.(?:\d+)

# Special Sequences
# \A Returns a match if the specified characters are at the beginning of the string "\AThe"
# \b Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string") r"\bain" r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
# \d Returns a match where the string contains digits (numbers from 0-9) "\d"
# \D Returns a match where the string DOES NOT contain digits "\D"
# \s Returns a match where the string contains a white space character "\s"
# \S Returns a match where the string DOES NOT contain a white space character "\S"
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character) "\w"
# \W Returns a match where the string DOES NOT contain any word characters "\W"
# \Z Returns a match if the specified characters are at the end of the string "Spain\Z"

# Sets
# [arn] Returns a match where one of the specified characters (a, r, or n) are present
# [a-n] Returns a match for any lower case character, alphabetically between a and n
# [^arn] Returns a match for any character EXCEPT a, r, and n
# [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# [0-9] Returns a match for any digit between 0 and 9
# [0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
# [a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case
# [+] In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

#.span() returns a tuple containing the start-, and end positions of the match.   txt = "The rain in Spain"         x = re.search(r"\bS\w+", txt)   print(x.span())
#.string returns the string passed into the function                              txt = "The rain in Spain"         x = re.search(r"\bS\w+", txt)   print(x.string)
#.group() returns the part of the string where there was a match                  txt = "The rain in Spain"         x = re.search(r"\bS\w+", txt)   print(x.group())