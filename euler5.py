# no programming required for this one
# the naive approach is to take this number
big_num = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20

# prime factorization (this is equal to big_num)
prime_factor = 1 * 2 * 3 * (2 * 2) * 5 * (3 * 2) * 7 * (2 * 2 * 2) * (3 * 3) * (5 * 2) * 11 * (3 * 2 * 2) * 13 * (7 * 2) * (3 * 5) * (2 * 2 * 2 * 2) * 17 * (3 * 3 * 2) * 19 * (5 * 2 * 2)

# using the above we know we need:
    # four 2's
    # two 3's
    # one 5, 7, 19, 17, 13, and 11

# thus the number is
print(2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19)
