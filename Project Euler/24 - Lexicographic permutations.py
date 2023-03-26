from itertools import permutations


digits = '0123456789'
permutation = list(([''.join(p) for p in permutations(digits)]))
print(permutation[1000000-1])