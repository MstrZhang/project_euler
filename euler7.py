import math

# this approach is very naive but is very fast for this particular case

# from problem 3
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primes = []
i = 2
while len(primes) < 10001:
    if is_prime(i):
        primes.append(i)
    i += 1

print(primes[-1])