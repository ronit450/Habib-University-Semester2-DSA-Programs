n = int(input())
def sum_digits(n):
    if n <= 9 :
        return n
    else:
        temp = n% 10
        return sum_digits(int(n/10)) + temp

import inspect
source = inspect.getsource(sum_digits)
if '[' in source:
  print('Do not convert to string!')
elif 'for' in source or 'while' in source:
  print('Try to solve the problem recursively!')
else:
  print(sum_digits(n))