'''
Task: Write a Python function that does the prime factorization of any number.
Input: Integer
Output: List of Prime Factors
Example: Input - 630 , Output - [2, 3, 3, 5, 7]
'''
def prime_fact(n):
    prime_factors = []
    divisor = 2
    while divisor <= n:
        if n%divisor == 0:
            prime_factors.append(divisor)
            n = n/divisor 
        else:
            divisor += 1 #divisor = divisor + 1
    return ("{}={}*{}".format(n, prime_factors[0], prime_factors[1]))

print(prime_fact(2497885147362973))
# print(prime_fact(13))
# print(prime_fact(250))