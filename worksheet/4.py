# 3
def pythagorean_triplet(a, b, c):
    if not (a < b and b < c):
        return False
    elif a**2 + b**2 == c**2:
        return True
    else:
        return False


print(pythagorean_triplet(3, 4, 6))


# 4
# a
def addition(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# b
def recursive_addition(n):
    if n >= x
        return n + recursive_addition(n - 1)
    else:
        return 0


# 5
def get_list_of_even_powers(L, k):
    return [n**i for n in L for i in range(0, k, 2)]


print(get_list_of_even_powers([5, 6, 7], 8))
