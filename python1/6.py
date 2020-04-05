from math import sqrt, ceil
def is_prime (n):

    if n == 1:
        return False

    if n == 2:
        return True

    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

from TestClass import Tester

tester = Tester()

tester.test(is_prime(11))
tester.test(not is_prime(35))
tester.test(is_prime(19911121))
tester.test(not is_prime(1))
tester.test(not is_prime(9))
