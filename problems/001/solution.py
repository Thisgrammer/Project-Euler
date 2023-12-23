a = 3
b = 5
sum_multiples = 0

k = 1000

for i in range(1, k):
    if i % a == 0 or i % b == 0:
        sum_multiples += i

print(sum_multiples)