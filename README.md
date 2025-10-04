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