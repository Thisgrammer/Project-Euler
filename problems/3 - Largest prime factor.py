'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?'''


number = 600851475143
divisor = 2

while number != 1:
    if number % divisor == 0:
        print('Number:', number)
        number /= divisor
        print('Factor prime:', divisor)
    else:
        divisor += 1