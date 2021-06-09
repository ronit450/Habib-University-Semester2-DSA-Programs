import ast
lst = [10, 50, 30, 70, 80, 60, 20, 90, 40]
def selection_sort(lst):
    for i in range(0,len(lst)):
        starting_value = lst[i]
        no_of_swap = 0
        for j in range (i+1,len(lst)):
            if lst[j] < starting_value:
                starting_value = lst[j]
                lowest_index = j
                no_of_swap +=1
        if no_of_swap > 0 :
            temp = lst[i]
            lst[i] = starting_value
            lst[lowest_index] = temp
        print(lst)
selection_sort(lst)