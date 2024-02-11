import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    ls = []
    allower = "abcdefghijklmnopqrstuvwxyz"
    alupper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in s:
        if x.isupper():
            ls.append(alupper[(alupper.index(x) + k) % 26])
        elif x.islower():
            ls.append(allower[(allower.index(x) + k) % 26])
        else:
            ls.append(x)
    return ''.join(ls)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
