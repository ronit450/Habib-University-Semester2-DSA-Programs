import ast
InputString = input()
G = int(input())

def is_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False
def push(lst, item):
    lst.append(item)
def pop(lst):
    if is_empty(lst) == False:
        lst.pop()
    else:
        return False
def l1(inputstring):
    stack = []
    for i in range(len(inputstring)):
        if inputstring[i] == '1' :
            push(stack, i)
        elif inputstring[i] == '0' :
            if is_empty(stack) == False:
                if i < (len(inputstring)-1):
                    if inputstring[i+1] == '0':
                        pop(stack)
                    else:
                        return False
                elif i == (len(inputstring)-1) :
                    pop(stack)
            else:
                return False
    return(is_empty(stack))
def l2(inputstring):
    stack = []
    for i in range(0,((len(inputstring)))):
        if inputstring[i] == '1':
            push(stack,i)
        elif inputstring[i] == '0':
            if is_empty(stack) == False:
                pop(stack)
                pop(stack)
            else:
                return False
    return(is_empty(stack))
def l3(inputstring):
    stack= []
    temp  =0
    if '1' not in inputstring or '0' not in inputstring or '2' not in inputstring or '3' not in inputstring :
        return False
    for i in inputstring:
        if i == '0' :
            push(stack, i)
        elif i == '1'  :
            if is_empty(stack) == False:
                pop(stack)
            else:
                return False
    if is_empty(stack) == True:
        temp =+ 1
    else:
        temp = 0
    while is_empty(stack) == False :
        pop(stack)
    for i in inputstring:
        if i == '2':
            push(stack,i)
        elif i == '3':
            if is_empty(stack) == False:
                pop(stack)
            else:
                return False
    if is_empty(stack) == True:
        temp = temp+1
    else:
        temp = 0
    if temp == 2 :
        return True
    else:
        return False
def l4(inputstring):
    stack = []
    if '1' not in inputstring or '0' not in inputstring:
        return False
    for i in inputstring:
        if i == '0' :
            push(stack, i)
        elif i == '1' :
            if is_empty(stack) == False:
                pop(stack)
            else:
                return False
    if is_empty(stack) == False:
        return True
    else:
        return False
def Verify(inputstring, g):
    if g ==1 :
        result = l1(inputstring)
    if g == 2:
        result = l2(inputstring)
    if g == 3 :
        result = l3(inputstring)
    if g == 4 :
        result = l4(inputstring)
    if result == True:
        return True
    else:
        return False

print(Verify(InputString, G))