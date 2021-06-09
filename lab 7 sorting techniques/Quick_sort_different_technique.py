def Quick_sort(lst):
    low = 0
    high = len(lst) - 1
    if low < high:
        pivot = pivot_finder(lst, low, high)
        first_half = Quick_sort(lst[0:pivot])
        second_half = Quick_sort(lst[pivot:len(lst)])
    else:
        return lst
    temp = 0
    for i in range(len(first_half)):
        lst[temp] = first_half[i]
        temp += 1
    for j in range(len(second_half)):
        lst[temp] = second_half[j]
        temp += 1

    return lst

def pivot_finder(lst, low, high):
    pivot = lst[high]
    i = j = 0
    while j < high:
        if lst[j] <= pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i = i +1
        j += 1
    lst[i], lst[j] = lst[j], lst[i]
    return i


lst = [9,7,5,1,10]
print(Quick_sort(lst))