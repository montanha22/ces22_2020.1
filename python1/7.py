def sum_of_squares(xs):
    return sum(
        [x ** 2 for x in xs]
    )

from TestClass import Tester

tester = Tester()

tester.test(
    sum_of_squares([0]) == 0
    )

tester.test(
    sum_of_squares([]) == 0
)

tester.test(
    sum_of_squares([1, 2, 3]) == 14
    )

tester.test(
    sum_of_squares([1, -1]) == 2
    )

tester.test(
    sum_of_squares([2, -3, 4]) == 29
    )