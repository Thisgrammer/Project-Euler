def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)

sumFactorial = 0
for i in range(3, 146):
    string = str(i)
    stringlist = [int(i) for i in string]
    for s in stringlist:
        if 