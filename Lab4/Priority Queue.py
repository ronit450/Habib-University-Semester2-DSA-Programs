import ast

queue = input()
queue = ast.literal_eval(queue)


def Enqueue(queue, item, priority):
    tupple = (item, priority)
    queue.append(tupple)
    length = length1(queue)
    i = 0
    while i < length:
        j = length - 1
        while j > 0:
            if top(queue, j) > top(queue, j - 1):
                queue[j], queue[j - 1] = queue[j - 1], queue[j]
            j -= 1
        i += 1


def length1(lst):
    counter = 0
    for i in lst:
        counter += 1
    return counter


def top(queue, counter):
    if is_empty(queue) == False:
        return queue[counter][1]
    else:
        return 0


def pop(queue):
    if is_empty(queue) == False:
        return queue.pop()
    else:
        return False


def is_empty(queue):
    if len(queue) == 0:
        return True
    else:
        return False


def push(queue, item):
    queue.append(item)


def Dequeue(queue):
    temp = queue.pop(0)
    return temp[0]


operation = input()

if operation == "Enqueue":
    item = input()
    priority = int(input())
    Enqueue(queue, item, priority)
    print(queue)
elif operation == "Dequeue":
    print(Dequeue(queue))
    print(queue)