def is_palindrome(s):
    return s[::-1] == s[:]

from TestClass import Tester
tester = Tester()

tester.test(is_palindrome("abba"))
tester.test(not is_palindrome("abab"))
tester.test(is_palindrome("tenet"))