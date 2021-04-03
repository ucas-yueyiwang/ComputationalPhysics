def fibonacci(n):
    """

    evaluates n! = n * (n - 1) * ... * 2 * 1
    0! evaluates to 1

    >>> fibonacci(0)
    0

    >>> fibonacci(10)
    55

    >>> fibonacci(-1)
    Illegal input!
    -1

    >>> fibonacci(3.14)
    Illegal input!
    -1

    :param n: element of the factorial sequence to be evaluated
    :type n: float

    :return: n!
    :rtype: float
    """
    if isinstance(n, int) is False or n < 0:
        print("Illegal input!")
        return -1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
