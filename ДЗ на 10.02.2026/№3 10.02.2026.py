def golden_ratio(i):
    def fib(n):
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    if i == 1:
        print(1.0)
    else:
        result = fib(i) / fib(i - 1)
        print(result)