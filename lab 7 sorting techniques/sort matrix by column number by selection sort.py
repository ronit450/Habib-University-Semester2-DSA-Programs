import ast
lst = input()
lst = ast.literal_eval(lst)
column = int(input())
def sort_matrix_by_columnNumber(lst,column):
    for i in range(0,len(lst)):
        starting_value = lst[i][column]
        no_of_swap = 0
        for j in range (i+1,len(lst)):
            if lst[j][column] < starting_value:
                starting_value = lst[j][column]
                temp2  = lst[j]
                lowest_index = j
                no_of_swap +=1
        if no_of_swap > 0 :
            temp = lst[i]
            lst[i] = temp2
            lst[lowest_index] = temp
    return(lst)
print(sort_matrix_by_columnNumber(lst, column))