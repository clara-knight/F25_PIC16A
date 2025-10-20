def check_same(L, M):
    if len(L) != len(M):
        return False
    else:
        for i in range(len(L)):
            if L[i] != M[i]:
                return False
        return True


def compare_val_w_idx(L):
    M = []
    for i in range(len(L)):
        if i > L[i]:
            M.extend([-1])
        elif i == L[i]:
            M.extend([0])
        else:
            M.extend([1])
    return M


def compare_val_w_idx_noret(L):
    for i in range(len(L)):
        if i > L[i]:
            L[i] = -1
        elif i == L[i]:
            L[i] = 0
        else:
            L[i] = 1


def count_characters(s):
    s_chars = {}
    for char in s:
        char = char.lower()
        if char not in s_chars:
            s_chars[char] = 1
        else:
            s_chars[char] += 1
    return s_chars


def find_primes(k):
    primes = []
    for i in range(2, k):
        for j in range(2, i):
            if not (i % j):
                break
        else:
            primes.append(i)
    return primes


def main():

    # Exercise 1
    L1 = [1, 2, 3, 4]
    L2 = [1, 2, 3, 4]
    assert check_same(L1, L2)

    L3 = [0, 1, 4, 0]
    assert not check_same(L1, L3)

    M = [4, 5, 6, 3, 4, 5, 2, 3, 4]
    assert not check_same(L1, M)

    # Exercise 2
    M2 = [1, 1, 1, 0, 0, 0, -1, -1, -1]
    assert compare_val_w_idx(M) == M2

    # Exercise 3
    compare_val_w_idx_noret(M)
    assert M == M2

    # Exercise 4
    s = "MAthematics"
    s4 = {"m": 2, "a": 2, "t": 2, "h": 1, "e": 1, "i": 1, "c": 1, "s": 1}
    assert count_characters(s) == s4

    # Exercise 5
    assert find_primes(10) == [2, 3, 5, 7]


if __name__ == "__main__":
    main()
