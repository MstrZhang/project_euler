from math import sqrt
from functools import reduce

def generate_triangular(n):
    return sum(range(n + 1))

# modified factors function from agf from stackoverflow
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

i = 1
while len(factors(generate_triangular(i))) < 500:
    print(len(factors(generate_triangular(i))))
    i += 1

print(generate_triangular(i))