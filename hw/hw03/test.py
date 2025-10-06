def fib_iteration(n):
    i = 1
    prev, curr = 1, 0
    while i <= n:
        prev, curr = curr, prev + curr
        i += 1
    return curr

def fib_recursion1(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib_recursion1(n - 2) + fib_recursion1(n - 1)
    
def fib_recursion2(n):
    def f(i, prev, curr):
        if i == n:
            return curr
        else:
            return f(i + 1, curr, prev + curr)
    return f(0, 1, 0)
