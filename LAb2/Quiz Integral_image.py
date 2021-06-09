import ast
A = input()
A = ast.literal_eval(A)
def integral_image(A):
    integral_image = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            temp = 0
            if i == 0 and j == 0:
                temp = A[i][j]
            elif i == 0 and j > 0:
                temp_for_column = j
                while temp_for_column != -1:
                    temp += A[i][temp_for_column]
                    temp_for_column -= 1
            elif i > 0 and j == 0:
                temp_for_row = i
                while temp_for_row != -1:
                    temp += A[temp_for_row][j]
                    temp_for_row -= 1
            elif i > 0 and j > 0:
                temp_for_row = i
                temp_for_column = j
                while temp_for_row != -1:
                    while temp_for_column != -1:
                        temp += A[temp_for_row][temp_for_column]
                        temp_for_column -= 1
                    temp_for_column = j
                    temp_for_row -= 1
            integral_image[i][j] = temp
    return integral_image


print(integral_image(A))