#!/usr/bin/env python
from nltk.corpus import words

letters = 'abcdefghijklmnopqrstuvwxyz'

# Rot13 alg for lowercase chars
def r13(char):
    return letters[(letters.index(char) + 13) % 26] if char in letters else char

# Rot13 alg for both lowercase and uppercase on whole lines
def rot13(lines):
    return "".join([r13(char.lower()).upper() if char.isupper() else r13(char) for char in [line for line in lines]])


words = words.words()
for word in words:
    print(rot13(word.lower()))
