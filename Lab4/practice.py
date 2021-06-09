def addition(matrix,row_number,add_this):
    for i in range (len(matrix)):
        matrix[row_number][i] +=  add_this[i]
    return matrix

matrix = [[1,2,3],[4,5,6]]

x = [4,5,6]
s  = addition(matrix,1,x)

print(s)
print(matrix)