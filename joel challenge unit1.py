# Factorial of a number using recursion


def fact(n):
  if n == 1:
    return n
  else:
    return n * fact(n - 1)


num = int(input('Enter a number:'))

# check if the number is negative
if num < 0:
  print('Sorry, factorial does not exist for negative numbers')
else:
  print(num, 'factorial =', fact(num))
