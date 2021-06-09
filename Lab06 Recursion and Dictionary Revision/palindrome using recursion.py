def is_palindrome(s):
    if len(s) == 1:
        return True
    elif s == "":
        return True
    if s[len(s) - 1] == s[0]:
        return True
    else:
        return False
    return is_palindrome(s[1:len(s) - 2])


s = input().strip()
print(is_palindrome(s))