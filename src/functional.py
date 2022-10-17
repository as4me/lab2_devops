def fib_f(n):
    if n<3:
        return 1
    return fib_f(n-1) + fib_f(n-2)
