import ast

queue = input()
queue = ast.literal_eval(queue)


# Queue methods
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





def mirror(queue):
    stack = []
    final_queue = []
    while is_empty(queue) != True:
        temp = deQueue(queue)
        enQueue(final_queue, temp)
        push(stack, temp)
    while is_empty(stack) != True:
        temp1 = pop(stack)
        enQueue(final_queue, temp1)
    return final_queue


print(mirror(queue))