# ucb-cs61a-2024-fall

My solutions to homework, lab, project for [cs61a-2024](https://insideempire.github.io/CS61A-Website-Archive/). Also including note and memo to lecture.

## Higher-Order Function

In Python, function can use functions as argument, and also use functino as return value

### Nested definition

When nested definition is called, environment for this call consists of sequence of frames, the local frame, the parent frame in which the nested function is defined, and trace back until the global frame

### Currying

**Curring** means that we transform a multi-argument function into a chain of nested defined function, which only take one argument respectively

e.g. f(x, y) -> g(x)(y), where g(x) itself is a function, and take one argument

### Note

- Return a nested defined function can take different arguments at different place in program. The whole function definition generate a pattern for a bunch of sub-functions which do the real compution.

### todo:
- Figure out the Newtown's method, using nested function
- What does function decorator exactly do?


## Recursive Function
Set the base case to stop recursive call, set recursive case, and take a leap of faith

Put an example shown in course:
```python
"""Show inverse cascade"""
def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)
```

### Tree Recursion
Tree recursion, function that call recursion function more than once in its body, the process of evalution looks like a tree

Fibonacci using recursion: `fib(n) = fib(n - 2) + fib(n - 1)`. Not efficient, evaluting on same arguments repeatly, will be improved later.

## Abstraction on data
Data may be compound of primitive data type, we can construct a new data type and treat it as a abstract. Just like we give a name to a process, and abstract it as function

### Abstraction barriers
Make barrier clearly among the represent of data sturcture,  the implement of methods calls on data, and the expose a brief part to user.

Abstraction as an important idea to module the code, helps to understand use of HOF

### Object Concept
- Object has attribute which bound to value, also has attribute bound to functions, those bound to functions, is called method

- Using method of object, is invoking the function on the object

- An object can has different name bound to it

- Object has mutable type and immutable type

### Mutation
`tuple` is a immutable object, but if the element in tuple is mutable, we can still change the contents, like:

```python
a = (1, 2, [3, 4])
a[2][1] = -3
```

Tuple can be used for key in dictionary, **ONLY if** the elements are all immutable 

Mutable defualt argument in function is dangerous
```python
def f(s=[]):
    s.append(1)
    return len(s)
f()
f()
f()
```
Will finally get a list with length equals to 3 

### Iterator
- iter(itrable) return a iterator object, and next(iterator) return the next value in iteration, and this value will not be in the iterator

- Some function (reversed, map, filter...) return a iterator, is lazy computation, compute only when data is used 

- Give a container to iterator so that we can know all the value **remained** in iterator, `list(reversed(l)) == l`

### Generator
- A generator function definition looks like normal function, but using *yield* instead of *return*

- A generator is returned from a generator function, and itself is a special iterator, iterate over the yield value in the function body

- Every time call next() on a generator, it will yield one value, and pause

- Notice the concept on lazy computation, make a good yield expression can shorten the run time for a small range of result. Compare two partition generator versions below: 

```python
def partition_gen(n, m):
        assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        # Version 1, good yield expression, calculate exact one next answer
        for b in partition_gen(n - m, m):
            yield b + ' + ' + str(m)
        
        # Version 2, bad yield from, list comprehension need all the partition result then turn to an iterator
        yield from iter([p + ' + ' + str(m) for p in partition_gen(n - m, m)])

    if m > 1:
        yield from partition_gen(n, m - 1)
```

## todo
- [x] Generator version on partition 