# unpredictable output handling
# ellipsis option tells doctest to ignore portions of the verification value.
# because the memory is loaded to different locations when the code is run ,so it is ignored by this method
# (#doctest: +ELLIPSIS)  ... replaces the memory address
class MyClass:
    pass


def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return [obj]