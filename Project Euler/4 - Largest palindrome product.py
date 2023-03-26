'''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.'''


largest = 0

for n in range(999, 100, -1):
    for m in range(999, 100, -1):
        palindrome = n * m
        if palindrome > largest and str(palindrome) == str(palindrome)[::-1]:
            largest = palindrome
            break

print('The largest palindrome made from the product of two 3-digit numbers is:', largest)