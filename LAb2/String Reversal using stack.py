s = input()


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


def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


# main program
def string_reversal(s):
    new_stack = []
    final_stack = []
    for i in s:
        push(new_stack, i)
    while is_empty(new_stack) == False:
        temp = pop(new_stack)
        push(final_stack, temp)
    return "".join(final_stack)


print(string_reversal(s))