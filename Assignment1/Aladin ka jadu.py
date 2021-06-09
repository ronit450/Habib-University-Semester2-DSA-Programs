#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'optimalPoint' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY magic
#  2. INTEGER_ARRAY dist
#

def optimalPoint(magic, dist):
    starting_magic = magic[0]
    result = 0
    counter = 1
    sum_for_magic = 0
    sum_for_dist = 0
    final_result = 0
    for i in magic:
        sum_for_magic += i
    for j in dist:
        sum_for_dist += j
    if sum_for_magic < sum_for_dist:
        return -1
    for i in range(len(magic)):
        temp = starting_magic - dist[i]
        if temp < 0:
            starting_magic = magic[counter]
            counter += 1
            final_result = counter - 1
        else:
            result = starting_magic - dist[i] + magic[counter]
            starting_magic = result
            counter += 1
        if counter >= len(magic):
            counter = 0

    return final_result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    magic_count = int(input().strip())

    magic = []

    for _ in range(magic_count):
        magic_item = int(input().strip())
        magic.append(magic_item)

    dist_count = int(input().strip())

    dist = []

    for _ in range(dist_count):
        dist_item = int(input().strip())
        dist.append(dist_item)

    result = optimalPoint(magic, dist)

    fptr.write(str(result) + '\n')

    fptr.close()