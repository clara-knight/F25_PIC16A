# 1
def filter_and_sum(t):
    s = 0
    for item in t:
        if item < 0:
            pass
        elif item > 1000:
            return s
        else:
            s += item
    return s


def longest_path_length(d):
    pass


def math_operation(operation, *args, **kwargs):
    pass


def remove_elements(L1, L2):
    for i in L2:
        while i in L1:
            L1.remove(i)
