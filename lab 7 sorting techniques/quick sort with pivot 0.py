def Quick_sort(lst,low,high):
    if low < high :
        pivot = pivot_finder(lst,low,high)
        first_half = Quick_sort(lst,low,pivot-1)
        second_half = Quick_sort(lst,pivot+1,high)
    else:
        return lst
    return lst
def pivot_finder(lst,low,high):
    pivot = lst[low]
    i = j = len(lst)-1
    while j > low :
        if lst[j] >= pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i = i - 1
        j -= 1
    lst[i], lst[j] = lst[j], lst[i]
    return i
lst = [7,9,5,10,1,3]
print(Quick_sort(lst,0,len(lst)-1))