def Merge_sort(lst,inversion):
    mid = int(len(lst) / 2)
    first_half = []
    second_half = []
    final_lst = []
    if len(lst) != 1:
        first_half = Merge_sort(lst[:mid],inversion)
        second_half = Merge_sort(lst[mid:],inversion)
        temp = merging(first_half, second_half,inversion)
        inversion += temp[1]
        return temp[0]
    else:
        return lst
    return inversion
def merging(first_half, second_half,inversion):
    i = j = k = 0
    final_lst = []
    temp_for_first_half = 0
    temp_for_second_half = 0
    while k != ((len(first_half)) + (len(second_half))):
        if i > (len(first_half) - 1) or j > (len(second_half) - 1):
            break
        if first_half[i] <= second_half[j]:
            final_lst.append(first_half[i])
            temp_for_first_half += 1
            i += 1
        else:
            inversion += int((len(first_half)+len(second_half))/2) - i
            final_lst.append(second_half[j])
            temp_for_second_half += 1
            j += 1
        k += 1
    if temp_for_first_half != len(first_half):
        for i in range(temp_for_first_half, len(first_half)):
            final_lst.append(first_half[i])
    if temp_for_second_half != len(second_half):
        for i in range(temp_for_second_half, len(second_half)):
            final_lst.append(second_half[i])
    lst = final_lst
    return lst,inversion


lst = [2,4,1,3,5]
inversion = 0
print(Merge_sort(lst,inversion))