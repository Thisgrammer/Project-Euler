with open("problems/p067_triangle.txt", "r") as f:
    triangle = [[int(n) for n in row.split()] for row in f.read().split("\n")]

def max_path(triangle):
    for i in range(len(triangle) -2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

print(max_path(triangle))