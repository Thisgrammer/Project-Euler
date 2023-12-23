def spiral_diagonal_sum(n):
    # n is the size of the grid (n*n)
    # Initialize the sum with the first element of the grid
    diagonal_sum = 1
    for i in range(3, n+1, 2):
        # For each layer of the spiral, add the 4 corner elements to the sum
        diagonal_sum += 4*i**2 - 6*(i-1)
    return diagonal_sum

n = 1001
print(spiral_diagonal_sum(n))
