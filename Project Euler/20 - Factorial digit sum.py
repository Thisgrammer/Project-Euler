'''n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!'''

from functools import reduce


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
    

print(sum([int(digit) for digit in str(factorial(100))]))

print(sum([int(digit) for digit in str(reduce(lambda x, y: x * y, range(1, 100)))]))