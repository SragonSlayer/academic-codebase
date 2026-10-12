# Factors is a function that takes in an integer and returns an array of its prime factors
# This is intended for primes that are larger than 1 based on an input integer n. If n is less than 2, it returns an empty array.
# Concept here is to loop through all values of n where n > 2 while finding divisors of n. 
# If a divisor is found, it is added to the array and n is divided by that divisor. This continues until n is less than 2.
def factors(n):
    if n < 2:
        return []
    factors = []
    divider = 2
    while n >= 2:
        while n % divider == 0:
            factors.append(divider)
            n //= divider
        divider += 1
    return factors