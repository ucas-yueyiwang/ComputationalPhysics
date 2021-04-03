from Question210316_2_isprime import is_prime

def prime_factors(n):
    """

>>> prime_factors(1)
[]
>>> prime_factors(2)
[2]
>>> prime_factors(4)
[2]
>>> prime_factors(60)
[2, 3, 5]

    :param n:
    :type n: int

    :return: prime factors of n
    :rtype: list
    """
    reslist = list()
    m = n
    i = 2
    while m > 1:
        if m % i != 0:
            i += 1
        elif is_prime(i):
            m /= i
            if len(reslist) > 0 and reslist[-1] != i:
                reslist.append(i)
            if len(reslist) == 0:
                reslist.append(i)
    print(reslist)


print(prime_factors(12345678901))
