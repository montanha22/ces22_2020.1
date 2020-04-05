def sum_to(n):
    return int((1+n)*n/2)

from TestClass import Tester

tester = Tester()

tester.test((sum_to(10) == 55))
tester.test((sum_to(1) == 1))
tester.test((sum_to(2) == 3))