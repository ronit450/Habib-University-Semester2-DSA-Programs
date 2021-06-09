n = int(input())
base = int(input())


def base_converter(n, base):
    temp = n % base
    n = int(n / base)
    if temp < 10:
        result = str(temp)
    else:
        result = capital_character(temp)
    if n == 0:
        return result
    else:
        return base_converter(n, base) + result


def capital_character(result):
    dictonary = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    temp = dictonary[result]
    return temp


print(base_converter(n, base))