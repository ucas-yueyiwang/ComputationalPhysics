def is_prime(n):
    """

>>> is_prime(2)
True
>>> is_prime(4)
False
>>> is_prime(60)
False
>>> is_prime(36468436)
False

    :param n:
    :type n: int

    :return: prime factors of n
    :rtype: list
    """
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        else:
            i += 1
    return True
