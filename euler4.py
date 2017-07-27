products = []
for i in range(100, 1000):
    for j in range(100, 1000):
        products.append(i * j)
products.sort()

def is_palindrome(n):
    if len(n) == 0 or len(n) == 1:
        return True
    else:
        if n[0] == n[-1]:
            return is_palindrome(n[1:-1])
        else:
            return False

for i in range(len(products) - 1, 0, -1):
    if is_palindrome(str(products[i])):
        print(products[i])
        break