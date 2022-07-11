# When working with blanklines in docstrings instead of leaving a blank line...use the <BLANKLINE> keyword
# this is because the test fails, because it interprets the blank line after the line containing Line one
def double_space(lines):
    """Prints a list of lines double-spaced.

    >>> double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    """
    for l in lines:
        print(l)
        print()