def fib(n):
    """ Fibonacci sequence, start from f1 = 1, f2 = 1
    
    >>> fib(8)
    21

    >>> fib(5)
    5
    """
    prev, curr = 0, 1
    count = 1
    while count < n:
        prev, curr = curr, prev + curr
        count += 1
    return curr


def fizzbuzz(n):
    i = 1
    while i <= n:
        if i % 3 == 0:
            print("fizz", end='')
            if i % 5 == 0:
                print("buzz")
            else:
                print()
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
        i += 1


def is_prime(n):
    L, R = 2, n - 1
    if n == 2:
        return True
    while L <= R:
        if n % L == 0:
            return False
        else:
            L += 1
            R = n // L
    return True


def unique_digits(n):
    """Return number of unique digits in positive integer n
    
    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """

    # Loop from 0 to 9 check if is in number n, count up if so
    digit = 0
    count = 0
    while digit <= 9:
        if has_digit(n, digit):
            count += 1
        digit += 1
    return count


def has_digit(n, k):
    """Check if positive integer n has digit k
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k <= 9
    while n > 0:
        r = n % 10
        n = n // 10
        if k == r:
            return True
    return False

