'''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?'''


k = 20
n = 0

for i in range(2, k+1):
    c = 0
    for num in range(2, i+1):
        if i % num == 0:
            c += 1
    if c == 1:
        p = 1
        while True:
            if i ** p > k:
                if i == 2:
                    n = i ** (p-1)
                else:
                    n *= i ** (p-1)
                print(i ** (p-1), end = ' * ')
                break
            else:
                p += 1

print('=', n)



'''smallest = 0
n = 2520

while smallest == 0:
    for i in [11, 13, 14, 16, 17, 18, 19, 20]:
        if n % i != 0: 
            break
        if i == 20:
            smallest = n
    n += 2520

print(smallest)
'''