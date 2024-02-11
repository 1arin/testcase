import math
import os
import random
import re
import sys

def gridChallenge(grid):
    if len(grid[0]) == 1:
        return 'YES'
    
    orderedGrid = [sorted(x) for x in grid]
    for i, string in enumerate(orderedGrid):
        if (i) != len(string):
            newString = ''.join([x[i] for x in orderedGrid])
            if newString != ''.join(sorted(newString)):
                return 'NO'
    return 'YES'

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
