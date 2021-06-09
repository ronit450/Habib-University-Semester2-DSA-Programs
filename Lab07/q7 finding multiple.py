import ast

lst = input()
lst = ast.literal_eval(lst)
item = int(input())


def finding_multiple(lst, item):
    before_lenghth = 0
    found = False
    index_found = 0
    plus_index = 0
    index_list = []
    no_of_times_break_and_larger = 0
    while found == False:
        index = int(len(lst) / 2)
        if item == lst[index]:
            index_found = index + plus_index
            index_list.append(index_found)
            linear_search(lst, item, index, index_list, plus_index)
            index_list.sort()
            return index_list

        if len(lst) == 1 and found == False:
            found = True
            return index_list

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
    return index_list


def removing_minus(number):
    if number < 0:
        number = number * -1
    return number


def linear_search(lst, item, index, index_list, plus_index):
    for i in range(index + 1, len(lst)):
        if lst[i] == item:
            temp = i + plus_index
            index_list.append(temp)
    for i in range(index - 1, -1, -1):
        if lst[i] == item:
            temp = i + plus_index
            index_list.append(temp)


print(finding_multiple(lst, item))