s = input()


def balanced_braces(s):
    stack = []
    if len(s) % 2 != 0:
        return False
    lst_for_open_paranthesis = ['[', '{', '(']
    lst_for_close_paranthesis = [']', '}', ')']
    for i in s:
        if i in lst_for_open_paranthesis:
            stack.append(i)
        elif i in lst_for_close_paranthesis and len(stack) > 0:
            x = stack.pop()
            if is_opening_close(x, i) == False:
                return False
        elif i in lst_for_close_paranthesis and len(stack) <= 0:
            return False
            break

    if len(stack) == 0:
        return True
    else:
        return False


def is_opening_close(a, b):
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'):
        return True
    else:
        return False


print(balanced_braces(s))