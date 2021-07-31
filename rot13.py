#!/usr/bin/env python
#rot13 cipher written in python
import sys

# Rot13 alg for lowercase chars
def r13(char):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if char not in letters:
        return char
    idx = letters.index(char)
    return letters[idx - 13] if idx > 12 else letters[idx + 13]

# Rot13 alg for both lowercase and uppercase
def rot13(char):
    return r13(char.tolower()).toupper() if char.isupper() else r13(char)

# Apply Rot13 alg to a file
with open(sys.argv[1], "r+") as f:
    lines = f.read()
    f.seek(0)
    f.write("".join([rot13(char) for char in [line for line in lines]]))
