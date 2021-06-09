import ast

points_list = input()
points_list = ast.literal_eval(points_list)
length = float(input())


def length_of_line(points_list, length):
    array = length1(points_list)
    index = binary_search_iterative(array, length)
    return index


def length1(points_list):
    distance_array = []
    import math
    for i in range(len(points_list)):
        point1 = points_list[i][0][0] - points_list[i][1][0]
        point2 = points_list[i][0][1] - points_list[i][1][1]
        temp = math.sqrt((point1 ** 2) + (point2 ** 2))
        temp = float(round(temp, 2))
        distance_array.append(temp)
    return distance_array


def binary_search_iterative(lst, item):
    before_lenghth = 0
    found = False
    index_found = 0
    plus_index = 0
    no_of_times_break_and_larger = 0
    while found == False:
        index = int(len(lst) / 2)
        if item == lst[index]:
            index_found = index + plus_index
            found = True
        if len(lst) == 1 and found == False:
            index_found = -1
            break
        elif item < lst[index]:
            lst = lst[0:index]
        elif item > lst[index]:
            if no_of_times_break_and_larger == 0:
                before_lenghth = len(lst)
            else:
                pass
            lst = lst[index:(len(lst))]
            plus_index = before_lenghth - len(lst)
            plus_index = removing_minus(plus_index)
            no_of_times_break_and_larger += 1
    return index_found


def removing_minus(number):
    if number < 0:
        number = number * -1
    return number


print(length_of_line(points_list, length))