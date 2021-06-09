expression = input()


def push(lst, item):
    lst.append(item)


def pop(lst):
    if is_empty(lst) == False:
        return lst.pop()
    else:
        return False


def calculator(first_operand, second_operand, operator):
    if operator == '+':
        return first_operand + second_operand
    elif operator == '-':
        if first_operand < second_operand:
            return second_operand - first_operand
        else:
            return first_operand - second_operand
    elif operator == '*':
        return first_operand * second_operand
    elif operator == '/':
        if first_operand < second_operand:
            return second_operand / first_operand
        else:
            return first_operand / second_operand


def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False


def string_reversal(s):
    new_stack = []
    final_stack = []
    for i in s:
        push(new_stack, i)
    while is_empty(new_stack) == False:
        temp = pop(new_stack)
        push(final_stack, temp)
    return "".join(final_stack)


def EvalutePrefix(expression):
    first_pop = 0
    second_pop = 0
    operator_lst = ['*', '/', '+', '-']
    oper_and_stack = []
    reversed_string = string_reversal(expression)
    expression = str.split(reversed_string)
    for i in expression:

        if i not in operator_lst:
            i = int(i)
            push(oper_and_stack, i)
        else:
            first_pop = pop(oper_and_stack)
            second_pop = pop(oper_and_stack)
            result = calculator(first_pop, second_pop, i)
            push(oper_and_stack, result)
    return int(pop(oper_and_stack))


print(EvalutePrefix(expression))