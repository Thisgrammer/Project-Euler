'''The sum of the squares of the first ten natural numbers is, 1² + 2² +...+ 10² = 385
The square of the sum of the first ten natural numbers is, (1 + 2+...+10)² = 55² = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''


sumSquares = 0
squareSum = 0

for i in range(1, 101):
    sumSquares += i**2
    squareSum += i

squareSum **= 2

print('The sum of squares is:', sumSquares)
print('The square of the sum is:', squareSum)
print('And the difference between is:', squareSum - sumSquares)