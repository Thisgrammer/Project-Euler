'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?'''


def st_prime_number(n):
    k = n
    marker = [True] * k

    for num in range(2, round(k**0.5)):
        if marker[num]:
            for multiple in range(num + num, k, num):
                marker[multiple] = False

    primes = list(range(2, k))
    primes2 = [prime for prime in primes if marker[prime]]
    return primes2[n]


print(st_prime_number(10001))