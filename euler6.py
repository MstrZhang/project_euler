# from problem 1, the sum of the natural numbers is
def sum_of_naturals(n):
    return (n * (n + 1)) // 2

# from calculus, the sum of the squares of the natural numbers is
def sum_of_squares(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

print(sum_of_naturals(100) ** 2 - sum_of_squares(100))