#!/usr/bin/env python
import sys

def rot13(char):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if char not in letters:
        return char
    idx = letters.index(char)
    return letters[idx - 13] if idx > 12 else letters[idx + 13]

with open("newdict.txt", "r") as f:
    with open("rotdict.txt", "w") as o:
        for word in f.readlines():
            o.write("".join([rot13(char) for char in word.lower()]))

# 4 state cycle
# 0 -> 2 -> 0
# 1 -> 3 -> 1
# a = a > 2 ? a - 2 : a + 2
#
# 6 state cycle
# 0 -> 3 -> 0
# 1 -> 4 -> 1
# 2 -> 5 -> 2
# a = a > 3 ? a - 3 : a + 3
#
# 8 state cycle
# 0 -> 4 -> 0
# 1 -> 5 -> 1
# 2 -> 6 -> 2
# 3 -> 7 -> 3
# a = a > 4 ? a - 4 : a + 4
