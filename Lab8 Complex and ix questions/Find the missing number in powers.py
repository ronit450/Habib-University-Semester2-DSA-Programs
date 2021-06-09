import ast
powerTwoList = input()
powerTwoList = ast.literal_eval(powerTwoList)
size = int(input())

import math
def findMissingNumber(powerTwoList, size):
    upper_bound = len(powerTwoList) -1
    lower_bound = 0
    while True:
        index = int((lower_bound+upper_bound)/2)
        if (upper_bound == lower_bound) or index == upper_bound  :
            if math.log2(powerTwoList[index]) != len(powerTwoList[0:index]):
                index_found = index
            else:
                index_found = index+1
            break
        else:
            if math.log2(powerTwoList[index]) != len(powerTwoList[0:index]):
                upper_bound = index- 1
            else:
                lower_bound = index+ 1
    return 2 ** index_found

print(findMissingNumber(powerTwoList, size))