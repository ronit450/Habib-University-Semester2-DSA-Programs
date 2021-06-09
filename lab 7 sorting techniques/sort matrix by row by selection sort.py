import ast
lst = input()
lst = ast.literal_eval(lst)
def sort_matrix_by_row(lst):
    for k in range(len(lst)):
        for i in range(0,len(lst)):
            starting_value = lst[k][i]
            no_of_swap = 0
            for j in range (i+1,len(lst)):
                if lst[k][j] < starting_value:
                    starting_value = lst[k][j]
                    lowest_index = j
                    no_of_swap +=1
            if no_of_swap > 0 :
                temp = lst[k][i]
                lst[k][i] = starting_value
                lst[k][lowest_index] = temp
    return lst
print(sort_matrix_by_row(lst))