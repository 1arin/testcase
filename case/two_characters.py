import math
import os
import random
import re
import sys
from itertools import combinations

def alternate(s):
    maxx=0
    c=list(combinations(list(set(s)), 2))
    for i in range(len(c)):
        a=True
        ls=[]
        for x in s:
            if x == c[i][0] or x == c[i][1]:
                ls.append(x)
        for i in range(len(ls) - 1):
            if ls[i]==ls[i+1]:
                a=False
                break
        if a:
            maxx=max(maxx, len(ls))
    return maxx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
