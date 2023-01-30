#!/usr/bin/python3

'''
Task: Write a Python function that does the prime factorization of any number.
Input: Integer
Output: List of Prime Factors
Example: Input - 630 , Output - [2, 3, 3, 5, 7]
'''


def prime_fact(x):
    prime_factors = []
    divisor = 2
    n = x

    while divisor <= x:
        if x % divisor == 0:
            prime_factors.append(divisor)
            x = x / divisor
        else:
            divisor += 1   # divisor = divisor + 1
    p = prime_factors[0]
    q = prime_factors[1]
    return ("{}={}*{}".format(n, p, q))


# print(prime_fact(2497885147362973))
# print(prime_fact(13))
# print(prime_fact(250))
