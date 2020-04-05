def listsum(lis):
    even_flag = True
    mysum = 0

    for elem in lis:
        if elem % 2 == 0 and even_flag:
            even_flag = False
        else:
            mysum = mysum + elem
    
    return mysum



from TestClass import Tester

tester = Tester()

tester.test((listsum([1, 3, 5]) == 9))
tester.test((listsum([1, 2, 3, 5]) == 9))
tester.test(listsum([1, 2, 2, 3, 5]) == 11)
tester.test(listsum([0, 1, 2, 2, 3, 5]) == 13)
tester.test(listsum([1, 3, 5, 200]) == 9)