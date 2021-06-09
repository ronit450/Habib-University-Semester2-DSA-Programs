import ast

lst = input()
lst = ast.literal_eval(lst)


def InterLeaveQueue(lst):
    stack = []
    divide_number = (length(lst)) / 2
    counter = 0
    while counter < divide_number:
        temp = pop(lst)
        push(stack, temp)
        counter += 1
    counter = 0
    while counter < divide_number:
        temp = pop(stack)
        temp2 = deQueue(lst)
        enQueue(lst, temp2)
        enQueue(lst, temp)
        counter += 1
    return lst


def length(lst):
    counter = 0
    for i in lst:
        counter += 1
    return counter


def enQueue(lst, data):
    lst.append(data)


def deQueue(lst):
    if is_empty(lst) == False:
        return lst.pop(0)
    else:
        return False


def front(lst):
    if is_empty(lst) == False:
        return lst[0]
    else:
        return False


def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


# stack methods
def push(lst, item):
    lst.append(item)
def pop(lst):
    if is_empty(lst) == False:
        return lst.pop()
    else:
        return False


def top(lst):
    if is_empty(lst) == False:
        return lst[len(lst) - 1]
    else:
        return False


print(InterLeaveQueue(lst))