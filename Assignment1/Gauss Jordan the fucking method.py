import ast
coeffs = input()
coeffs = ast.literal_eval(coeffs)
def Solve(coeffs):
    result_list = []
    pivot_pointer = 0
    coeffs = pivot(coeffs)
    for column in range((len(coeffs[0]))-1):
        for row in range(len(coeffs)):
            temp_row = []
            if column != row :
                temp = coeffs[row][column]
                if temp != 0:
                    temp = additive_inverse(temp)
                    if coeffs[column][column] == 1:
                        pivot_pointer = column
                    else:
                        coeffs = pivot(coeffs)
                        pivot_pointer = column
                    for x in range(len(coeffs[0])):
                        temp_row.append(coeffs[pivot_pointer][x])
                    after_scaling_temp_row = multiply_single_row(temp_row,temp)
                    coeffs = addition(coeffs,row,after_scaling_temp_row)
    for i in range (len(coeffs)):
        for j in range(len(coeffs[0])):
            if j == len(coeffs[0])-1 :
                temp = coeffs[i][j]
                temp = float(round(temp,1))
                result_list.append(temp)
    return result_list
def swap_rows(matrix,swap_from,swap_with):
    temp = matrix[swap_from]
    matrix[swap_from] = matrix[swap_with]
    matrix[swap_with] = temp
    return matrix
def addition(matrix,row_number,add_this):
    for i in range (len(matrix[0])):
        matrix[row_number][i] += + add_this[i]
    return matrix
def additive_inverse(number):
    number = number *-1
    return number
def multiply_row(matrix,row_number,number_with_being_multiplid):
    for j in range(len(matrix[0])):
        matrix[row_number][j] = matrix[row_number][j] * number_with_being_multiplid
    return matrix
def pivot(coeffs):
    swap = 0
    for i in range(0,len(coeffs)):
        pivot = coeffs[i][i]
        if pivot == 1 :
            pass
        elif pivot == 0 :
            for j in range(len(coeffs)):
                if coeffs[j][i] > 0 :
                    swap = j
            coeffs = swap_rows(coeffs,i,swap)
        else:
            scaler = 1/pivot
            coeffs = multiply_row(coeffs,i,scaler)
    return coeffs
def multiply_single_row(matrix_row,sclaer):
    for i in range(len(matrix_row)):
        matrix_row[i] = matrix_row[i] * sclaer
    return matrix_row
print(Solve(coeffs))