'''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.'''


k = 2000000
marker = [True] * k

for num in range(2, round(k**0.5)):
    if marker[num]:
        for multiple in range(num + num, k, num):
            marker[multiple] = False

primes = list(range(2, k))
print(sum([prime for prime in primes if marker[prime]]))