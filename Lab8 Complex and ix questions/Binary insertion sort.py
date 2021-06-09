import ast

lst = input()
lst = ast.literal_eval(lst)


def BinaryInsertionSort(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            index = binary_search(lst[0:i], lst[i])
            for j in range(index, i):
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    return lst


def binary_search(lst, item):
    low = 0
    high = len(lst)
    while low <= high:
        index = int((high + low) / 2)
        if item == lst[index]:
            return index + 1
        if (len(lst) == 1 or (high - low) == 0) and (item > lst[index] or item == lst[index]):
            index_found = index + 1
            break
        elif (len(lst) == 1 or (high - low) == 0 or (high - low) == 1) and item < lst[index]:
            index_found = index
            break

        elif lst[index] > item:
            high = index - 1
        elif lst[index] < item:
            low = index + 1
    return index_found


print(BinaryInsertionSort(lst))
