#!/usr/bin/env python
#rot13 cipher written in python
import sys

letters = 'abcdefghijklmnopqrstuvwxyz'

# Rot13 alg for lowercase chars
def r13(char):
    return letters[letters.index(char)-13] if char in letters else char

# Rot13 alg for both lowercase and uppercase on whole lines
def rot13(lines):
    return "".join([r13(char.lower()).upper() if char.isupper() else r13(char) for char in lines])

# Apply Rot13 alg to a file
with open(sys.argv[1], "r+") as f:
    lines = f.read()
    print(lines)
    f.seek(0)
    f.write(rot13(lines))
