result = 0
# range from 0 to 999
for i in range(999, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        result += i

# a more efficient solution
def divisible_by(n):
    x = 999 // n
    # this is the formula for the sum of integers to x
    return n * (x * (x + 1)) // 2

print(divisible_by(3) + divisible_by(5) - divisible_by(15))