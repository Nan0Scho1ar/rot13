#!/usr/bin/env python
import sys

letters = 'abcdefghijklmnopqrstuvwxyz'

# Rot13 alg for lowercase chars
def r13(char):
    return letters[(letters.index(char) + 13) % 26] if char in letters else char

# Rot13 alg for both lowercase and uppercase on whole lines
def rot13(lines):
    return "".join([r13(char.lower()).upper() if char.isupper() else r13(char) for char in [line for line in lines]])

a = " ".join(sys.argv[1:])
a2 = rot13(a)
print(a,"  ->  ",a2)


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
