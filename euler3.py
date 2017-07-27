import math
# this solution isn't great but still solves the problem fairly fast (around 4s)

# it's very convenient that in python this number can be held in the int type
num = 600851475143
# every number can have at most 1 prime factor greater than its square
# this cuts the amount of divisors we have to check by a fair amount
sqrt = math.sqrt(600851475143)

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

result = 0
# from 1 to the the square root
for i in range(1, int(sqrt)):
    # if the number is prime
    if is_prime(i):
        # check if it is a divisor
        if 600851475143 % i == 0:
            # if it is, save it as the biggest divisor we know so far
            if i > result:
                result = i
            # if the dividend is larger than the square root, by the theorem, it is the greatest prime divisor
            if 600851475143 / i > int(sqrt) and is_prime(600851475143 // i):
                result = 600851475143 / i
                break

print(result)
