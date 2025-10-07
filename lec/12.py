xs = range(-10, 11)
ys = [x*x - 2*x + 1 for x in xs]

i = min(range(len(ys)), key=lambda i: ys[i])
xs[min(range(len(xs)), key=lambda i: ys[i])]


def park(n):
    """Return the ways to park cars and motorcycles in n adjacent spots.

    >>> park(1)
    ['%', '.']
    >>> park(2)
    ['%%', '%.', '.%', '..', '<>']
    >>> park(3)
    ['%%%', '%%.', '%.%', '%..', '%<>', '.%%', '.%.', '..%', '...', '.<>', '<>%', '<>.']
    >>> len(park(4))
    29
    """
    if n < 0:
        return []
    elif n == 0:
        return ['']
    else:
        return (['%'  + s for s in park(n-1)] +
                ['.'  + s for s in park(n-1)] +
                ['<>' + s for s in park(n-2)])


def dict_demos():
    numerals = {'I': 1, 'V': 5, 'X': 10}
    numerals['X']
    # numerals['X-ray']
    # numerals[10]
    len(numerals)
    list(numerals)
    numerals.values()
    list(numerals.values())
    sum(numerals.values())
    dict([[3, 9], [4, 16]])
    numerals.get('X', 0)
    numerals.get('X-ray', 0)
    numerals.get('X-ray')
    {1: 2, 1: 3}
    {[1]: 2}
    {1: [2]}



# Use of rational
def mul_rational(ra, rb):
    """User only know res = mul_rational(ra, rb)
    don't care about how r is represented
    """
    return rational(numer(ra) * numer(rb), denom(ra) * denom(rb))

from fractions import gcd
# Constructor for a rationnal
def rational(x, y):
    g = gcd(x, y)
    return [x // g, y // g]

# Selector for part of rational
def numer(r):
    return r[0]
def denom(r):
    return r[1]