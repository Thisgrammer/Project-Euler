def digits_sum(digits):
    return sum([int(i) for i in str(digits)])


maximum = 0
for a in range(100):
    for b in range(100):
        if digits_sum(a**b) > maximum:
            maximum = digits_sum(a**b)

print(maximum)