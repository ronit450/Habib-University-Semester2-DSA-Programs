import ast
expression = 'A+((B+C)*(D+E))'
expression = ast.literal_eval(expression)


def push(lst, item):
    lst.append(item)


def top(lst):
    if is_empty(lst) == False:
        return lst[len(lst) - 1]
    else:
        return False


def pop(lst):
    if is_empty(lst) == False:
        return lst.pop()
    else:
        return False


def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


def precidence(stack, new_operator):
    if is_empty(stack) == True:
        return True
    else:
        temp = top(stack)
        if precidence_order(new_operator) <= precidence_order(temp):
            return False
        else:
            return True


def precidence_order(operator):
    if operator == '+' or operator == '-':
        return 4
    elif operator == '*' or operator == '/':
        return 6
    elif operator == '(':
        return 2


def Infix_to_Postfix(expression):
    op_stack = []
    lst_for_numbers = []
    operator_lst = ['*', '/', '+', '-']
    expression = str.split(expression)
    for i in expression:
        if i in operator_lst:
            if precidence(op_stack, i) == True:
                push(op_stack, i)
            else:
                while is_empty(op_stack) != True:
                    temp = pop(op_stack)
                    lst_for_numbers.append(temp)
                push(op_stack, i)

        elif i == '(':
            push(op_stack, i)
        elif i == ')':
            temp = ""
            while temp != '(':
                temp = pop(op_stack)
                if temp != '(':
                    lst_for_numbers.append(temp)
        else:
            lst_for_numbers.append((i))
    while is_empty(op_stack) != True:
        temp = pop(op_stack)
        lst_for_numbers.append(temp)
    return " ".join(lst_for_numbers)


X = Infix_to_Postfix(expression)
print(X)