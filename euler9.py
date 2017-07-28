triples = []

# the sum of a, b, and c is 1000 so setting a max of 1000 will be more than sufficient

# generate pythagorean triples starting from 1 to 1000
# generator from joel.neely from stackoverflow
n = 1000
for a in range(1, n):
    b = a + 1
    c = b + 1
    while c <= n:
        while c * c < a * a + b * b:
            c += 1
        if c * c == a * a + b * b and c <= n:
            triples.append((a, b, c))
        b += 1

for triple in triples:
    if sum(triple) == 1000:
        print(triple)

# finding the product of this tuple
print(200 * 375 * 425)