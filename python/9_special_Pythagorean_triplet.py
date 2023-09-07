'''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a² + b² = c²
For example, 3² + 4² = 9 + 16 = 25 = 5².
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.'''


def coprime(a, b):
    c = 1
    for n in range(2, a if a > b else b):
        if c > 1: break
        if a % n == 0 and b % n == 0:
            c += 1

    return True if c == 1 else False


print(coprime(8, 9))

'''
ab¹ + ac² = bc²

a = m² - n²   # multiplo de 3, 4 ou 5
b = 2mn       # multiplo de 3, 4 ou 5
c = m² + n²   # multiplo de 5'''

target = 1000
for m in range(2, 51):
    n = target / 2 / m - m
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    if a + b - c == 0:
        print(a, b, c)
    if n < 0 or n >= m:
        continue
    if 2 * m * (m + round(n)) == target:
        print(a, b, c)
        print(a * b * c)