'''The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''


def collatz(n):
    if n == 1:
        return 1
    return n//2 if n % 2 == 0 else 3*n + 1


terms = 1000000
longest_chain = []
saved_chains = {2: [2, 1]}
for i in range(2, terms):
    chain = []
    starting_number = i
    
    while starting_number != 1:
        if starting_number in saved_chains:
            chain.extend(saved_chains[starting_number])
            break
        else:
            chain.append(starting_number)
        starting_number = collatz(starting_number)
       
    if i not in saved_chains:
        saved_chains[i] = chain

    if len(saved_chains[i]) > len(longest_chain):
        longest_chain = saved_chains[i]


print(longest_chain[0])