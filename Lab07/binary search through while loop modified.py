import ast

lst = input()
lst = ast.literal_eval(lst)
item = int(input())


def binary_search_iterative_modified(lst, item):
    answer = binary_search(lst, item)
    if answer == -1:
        before_lenghth = 0
        found = False
        index_found = 0
        plus_index = 0
        no_of_times_break_and_larger = 0
        while found == False:
            index = int(len(lst) / 2)
            if len(lst) == 1:
                if item < lst[index]:
                    index_found = index + plus_index
                    found = True
                elif item > lst[index]:
                    index_found = index + 1 + plus_index
                    found = True
            elif len(lst) > 2 and item > lst[index] and item < lst[index + 1]:
                index_found = index + 1 + plus_index
                found = True


            elif item < lst[index] and item > lst[index - 1] and len(lst) > 1:
                index_found = index - 1 + plus_index
                found = True
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
    else:
        return answer


def binary_search(lst, item):
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


print(binary_search_iterative_modified(lst, item))