#!/usr/bin/env python

from nltk.corpus import words

def rot13(char):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if char not in letters:
        return char
    idx = letters.index(char)
    return letters[idx - 13] if idx > 12 else letters[idx + 13]

words = words.words()
for word in words:
    new = "".join([rot13(char) for char in word.lower()])
    if new in words:
        print(word,"  ->  ",new)
