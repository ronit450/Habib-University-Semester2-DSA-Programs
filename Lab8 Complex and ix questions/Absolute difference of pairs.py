import ast
lst = input()
lst = ast.literal_eval(lst)

import math
def insertion_sort(lst):
    for i in range(1,len(lst)):
        for j in range (i,0,-1):
            if lst[j] < lst[j-1]:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp
            else :
                break
    return lst
def smallest_absdiff_pairs(lst):
    lst = insertion_sort(lst)
    smallest_number = abs(lst[0] - lst[1])
    final_lst = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            temp = abs(lst[i] - lst[j])
            if temp == smallest_number:
                tupple = (lst[i],lst[j])
                final_lst.append(tupple)
            elif temp < smallest_number:
                final_lst = []
                smallest_number = temp
                tupple = (lst[i],lst[j])
                final_lst.append(tupple)
            elif temp > smallest_number :
                break
    return final_lst

print(smallest_absdiff_pairs(lst))