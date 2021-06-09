import ast
coeffs = input()
coeffs = ast.literal_eval(coeffs)
def Solve(coeffs):
    pivot_value = 0
    for i in range(len(coeffs)):
        for j in range (len(coeffs[0])-1):
            if i == j :
                pivot_value = coeffs[i][j]
                if pivot_value == 0 :
                    if i != len(coeffs)-1 :
                        if coeffs[i+1][j] > 0 :
                            coeffs = swapping(coeffs,i,i+1)
                        else:
                            coeffs = swapping(coeffs,i,i+2)
                    else:
                        coeffs = swapping(coeffs,i,i-1)
                    pivot_value = coeffs[i][j]
                if pivot_value== 1 :
                    pass
                else:
                    temp = 1/pivot_value
                    for x in range(len(coeffs[0])):
                        coeffs[i][x] *=  temp
    for j in range(len(coeffs[0])-1):
        for i in range(len(coeffs)):
            if i != j :
                number = coeffs[i][j]
                if number == 0 :
                    pass
                else:
                    number *= -1
                    for x in range(len(coeffs[0])):
                        if coeffs[j][j] != 1 :
                            pivot = 1/coeffs[j][j]
                            for s in range(len(coeffs[0])):
                                coeffs[j][s] *= pivot
                        temp = number * coeffs[j][x]
                        coeffs[i][x] += temp
    faraz = []
    for i in range (len(coeffs)):
        for j in range(len(coeffs[0])):
            if j == len(coeffs[0])-1:
                temp = coeffs[i][j]
                temp = round(temp,1)
                temp = float(temp)
                faraz.append(temp)
    return faraz
def swapping(matrix,row_to_append,row_to_delete):
    temp = matrix[row_to_append]
    matrix[row_to_append] = matrix[row_to_delete]
    matrix[row_to_delete] = temp
    return coeffs
print(Solve(coeffs))