def createPrimes():
    k = 1000000
    marker = [True] * k
    marker[0] = marker[1] = False

    for n in range(2, round(k**0.5) + 1):
        if marker[n]:
            for multiple in range(n * n, k, n):
                marker[multiple] = False

    return [i for i, prime in enumerate(marker) if prime]

primes = createPrimes()


def checkCircular(prime):
    # convert prime to string
    t = str(prime)
    # create a list to store all rotations
    rotations = [int(t)]
    # loop through the length of the number
    for i in range(len(t)-1):
        # rotate the number
        t = t[1:] + t[0]
        # add the rotated number to the list
        rotations.append(int(t))
    # check if all rotations are prime numbers
    for rotation in rotations:
        if rotation not in primes:
            return False
    return True

c = 0
for i in range(1000000):
    if checkCircular(i):
        c += 1

print(c)