'''Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?'''


def factorial(x):
    f = 1
    for i in range(x, 1, -1):
        f *= i
    return f


grid = 20

print(factorial(grid+grid) // (factorial(grid) * factorial(grid)))