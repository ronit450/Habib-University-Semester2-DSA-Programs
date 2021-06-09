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
    pivot = lst[low]
    i = j = 0
    less_than = []
    greater_than = []
    temp = 0
    while j < high:
        if lst[j] <= pivot:
            less_than.append(lst[j])
        elif lst[j] >=pivot :
            greater_than.append(lst[j])
        j += 1
    for i in range(len(less_than)):
        lst[i] = less_than[i]
        temp+=1
    lst[temp] = pivot
    for j in range(temp,len(greater_than)):
        lst[j] = greater_than[i]

    return i


lst = [92,5,85,2,69,4,878]
print(Quick_sort(lst))