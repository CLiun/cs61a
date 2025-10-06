# HW03 note
Attention on the convertion between iteretion and recursion

```python
def fib(n):
    i = 1
    prev, curr = 1, 0
    while i <= n:
        prev, curr = curr, prev + curr
    return curr

def fib_recursion2(n):
    def f(i, prev, curr):
        if i == n:
            return curr
        else:
            return f(i + 1, curr, prev + curr)
    return f(0, 1, 0)
```
