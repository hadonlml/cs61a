""" Optional problems for Lab 3 """

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 2:
        return True
    if n != 2 and n % 2 == 0:
        return False
    def fuc(y):
        if y == 1:
            return True
        if n % y == 0:
            return False
        else:
            return fuc(y - 1)
    return fuc(n // 2)

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)



def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    def ten_pairs_forone(n0,n1):
        sum = 0
        if n1 < 10:
            if n0 + n1 == 10:
                return sum + 1      
            else:
                return sum
        else:
            if (n0 + (n1 % 10)) == 10:
                sum += 1
            return sum + ten_pairs_forone(n0, n1//10)
    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + ten_pairs_forone((n % 10), (n // 10))
