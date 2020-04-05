def words_until_sam(name_list):
    count = 0
    counting = True
    for name in name_list:

        if counting:
            count = count + 1
        
        if name == 'sam':
            counting = False
            return count
    
    return count

from TestClass import Tester

tester = Tester()

tester.test(words_until_sam(['a', 'sam', 'b', 'ads', '']) == 2)
tester.test(words_until_sam(['a', 'saam', 'b', 'ads', '']) == 5)
tester.test(words_until_sam(['sam']) == 1)
tester.test(words_until_sam(['saam'] ) == 1)
tester.test(words_until_sam(['saam', 'sama', 'sam', 'sam', 'sam'] ) == 3)

