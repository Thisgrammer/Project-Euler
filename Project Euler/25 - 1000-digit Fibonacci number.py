a, b, index = 1, 1, 0

while len(str(a)) < 1000:
    index += 2
    a += b
    b += a

print(index)