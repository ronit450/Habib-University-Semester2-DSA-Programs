import ast

student_records = input()
student_records = ast.literal_eval(student_records)
ID = input()
record_title = input()
data = input()


def update_record(student_records, ID, record_tittle, data):
    record_index = binary_search_iterative(student_records, ID)
    if record_index == -1:
        return 'Record not found'

    dictonary = {'ID': 0, 'Email': 1, 'Mid1': 2, 'Mid2': 3}
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    dictionary_index = dictonary[record_tittle]
    if dictionary_index == 0:
        if data[0] and data[1] not in numbers:
            return 'ID cannot be updated'
    student_records[record_index] = list(student_records[record_index])
    if dictionary_index == 2 or dictionary_index == 3:
        data = int(data)
    student_records[record_index][dictionary_index] = data
    student_records[record_index] = tuple(student_records[record_index])

    return student_records


def binary_search_iterative(lst, item):
    before_lenghth = 0
    found = False
    index_found = 0
    plus_index = 0
    no_of_times_break_and_larger = 0
    while found == False:
        index = int(len(lst) / 2)
        if item == lst[index][0]:
            index_found = index + plus_index
            found = True
        if len(lst) == 1 and found == False:
            index_found = -1
            break
        elif item < lst[index][0]:
            lst = lst[0:index]
        elif item > lst[index][0]:
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


print(update_record(student_records, ID, record_title, data))