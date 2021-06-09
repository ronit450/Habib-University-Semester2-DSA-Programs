import ast
lst = [16,9,81,3,5]

def insertion_sort(lst):
    for i in range(1,len(lst)):
        for j in range (i,0,-1):
            if lst[j] < lst[j-1]:
                temp = lst[j]
                lst[j] = lst[j-1]
                lst[j-1] = temp
            else :
                break
        print(lst)
insertion_sort(lst)