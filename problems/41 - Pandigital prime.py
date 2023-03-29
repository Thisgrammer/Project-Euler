def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i**2, n + 1, i):
                primes[j] = False
    return [x for x in range(n + 1) if primes[x]]


def pandigital(n):
    marker = True       
    for i in str(n):
        if str(n).count(i) != 1:
            marker = False
            break
    return marker

k = 9876543210+1
largest = 0

for i in range(k, 0, -1):
    if pandigital(i):
        print(i)
        break

print(largest)