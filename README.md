# ucb-cs61a-2024-fall

## Higher-Order Function

In Python, function can use functions as argument, and also use functino as return value

### Nested definition

When nested definition is called, environment for this call consists of sequence of frames, the local frame, the parent frame in which the nested function is defined, and trace back until the global frame

### Currying

**Curring** means that we transform a multi-argument function into a chain of nested defined function, which only take one argument respectively

e.g. f(x, y) -> g(x)(y), where g(x) itself is a function, and take one argument

### todo:
    - Figure out the Newtown's method, using nested function