def is_palindrome(n):
    return str(n) == str(n)[::-1]


k = 1000000
print(sum([i for i in range(k) if is_palindrome(i) and is_palindrome(bin(i)[2:])]))