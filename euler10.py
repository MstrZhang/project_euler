import math

# brute force method to determine solution
# this method is fairly slow (around 15s)
# the most efficient method is to reduce the primes to check using a sieve of eratosthenes

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

result = 0
# 1 does not count as a prime number
for i in range(2, 2000000):
    if is_prime(i):
        result += i
        
print(result)