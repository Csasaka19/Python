# doctest (doc string test __doc__)
# tests are passed in interpreter mode and written in a docstring
def my_function(a, b):
    """Returns a * b.

    Works with numbers:

    >>> my_function(2, 3)
    6

    and strings:

    >>> my_function('a', 3)
    'aaa'
    """
    return a * b