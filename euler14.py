# brute force method
# this method is extermely slow (around 48s)

def get_collatz_chain(n, counter=0):
    if n == 1:
        return counter
    else:
        if n % 2 == 0:
            return get_collatz_chain(n / 2, counter + 1)
        else:
            return get_collatz_chain(3 * n + 1, counter + 1)

counter = 0
result = 0

for i in range(1, 1000000):
    if get_collatz_chain(i) > result:
        result = get_collatz_chain(i)
        counter = i

print(counter)