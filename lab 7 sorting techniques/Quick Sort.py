def Quick_sort(lst,low,high):
    if low < high :
        pivot = pivot_finder(lst,low,high)
        first_half = Quick_sort(lst,low,pivot-1)
        second_half = Quick_sort(lst,pivot+1,high)
    else:
        return lst
    return lst
def pivot_finder(lst,low,high):
    pivot = lst[high]
    i =j=0
    while j < high:
        if lst[j] <= pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i = i + 1
        j += 1
    lst[i], lst[j] = lst[j], lst[i]
    return i
lst = [25,15,10,4,12,22,18,24,50,35,31,44,70,66,90]
print(Quick_sort(lst,0,len(lst)-1))