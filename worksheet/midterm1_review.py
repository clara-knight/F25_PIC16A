# Create a list with the first 10 triangular numbers
# i-th triangular number := sum 1 to i

L = [sum(range(t + 1)) for t in range(1, 11)]
