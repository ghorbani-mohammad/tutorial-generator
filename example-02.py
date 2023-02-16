# Fibonacci example


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


generator = fibonacci(2)
print(next(generator))
print(next(generator))

# Output:
#    0
#    1
