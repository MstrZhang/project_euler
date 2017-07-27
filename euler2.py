# the even numbers of the fibonacci sequence follow a recursive relation
# there is a mathematical proof for this relation

# this is the brute force method of determining the solution
# solution is not very efficient (takes around 10s to process)
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

i = 1
result = 0
while fib(i) < 4000000:
    if fib(i) % 2 == 0:
        result += fib(i)
    i += 1

print(result)