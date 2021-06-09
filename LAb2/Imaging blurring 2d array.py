import ast

A = input()
A = ast.literal_eval(A)


def blur_image(a):
    import math
    temp = 0
    new_image = [[0 for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            temp = 0
            if i == 0 and j == 0:
                temp = (a[i][j] + a[i][j + 1] + a[i + 1][j]) / 3

            elif i == 0 and j > 0 and j < ((len(a[0])) - 1):
                temp = (a[i][j] + a[i][j + 1] + a[i][j - 1] + a[i + 1][j]) / 4

            elif i == 0 and j == ((len(a[0])) - 1):
                temp = (a[i][j] + a[i][j - 1] + a[i + 1][j]) / 3

            elif (i > 0 and i < len(a) - 1) and j == 0:
                temp = (a[i][j] + a[i][j + 1] + a[i - 1][j] + a[i + 1][j]) / 4

            elif j == 0 and i == len(a) - 1:
                temp = (a[i][j] + a[i - 1][j] + a[i][j + 1]) / 3

            elif i == len(a) - 1 and j > 0 and j < ((len(a[0])) - 1):
                temp = (a[i][j] + a[i - 1][j] + a[i][j - 1] + a[i][j + 1]) / 4

            elif i == ((len(a)) - 1) and j == ((len(a[0])) - 1):
                temp = (a[i][j] + a[i - 1][j] + a[i][j - 1]) / 3

            elif (i > 0 and i < ((len(a)) - 1) and j == ((len(a[0])) - 1)):
                temp = (a[i][j] + a[i][j - 1] + a[i + 1][j] + a[i - 1][j]) / 4

            elif (i > 0 and i < len(a)) and (j > 0 and j < (len(a[0]))):
                temp = (a[i][j] + a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1]) / 5
            temp = float(make_4_significant(temp))
            new_image[i][j] = (temp)
    return new_image


def make_4_significant(number):
    return ('{:.2f}'.format(number))


print(blur_image(A))