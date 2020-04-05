import sys

class Tester:
    def __init__(self):
        pass

    def test(self, did_pass):

        linenum = sys._getframe(1).f_lineno

        if did_pass:
            msg = 'Test at line {} ok'.format(linenum)
        else:
            msg = 'Test at line {} FAILED'.format(linenum)
        
        print(msg)