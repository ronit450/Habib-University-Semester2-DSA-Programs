import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())
def binary_search_recursive_modified(lst,item,low,high):
    index = int((low+high)/2)
    if low > high :
        lst.append(item)
        lst = sorted(lst)
        low = 0
        high = len(lst)-1
        return binary_search_recursive_modified(lst,item,low,high)
    if item == lst[index]:
         return index
    elif item < lst[index]:
        high = index -1
        return binary_search_recursive_modified(lst,item,low,high)
    elif item > lst[index]:
        low = index +1
        return binary_search_recursive_modified(lst,item,low,high)

print(binary_search_recursive_modified(lst, item, low, high))