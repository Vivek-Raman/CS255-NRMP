import nrmp, nrmp_testcase, nrmp_testcase_answer
import importlib
importlib.reload(nrmp)
importlib.reload(nrmp_testcase)
importlib.reload(nrmp_testcase_answer)

inputs = nrmp_testcase.nrmp_testcase()
outputs = nrmp_testcase_answer.answerKey()

import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        for i, input in enumerate (inputs[:] ):
            for j, answer in enumerate( outputs[i] ):
                print ( "test testcase", i, "quota =", j )
                ans = nrmp.nrmp(input, j) 
                # print ( i,j, answer, ans) 
                if ans.keys() != answer.keys() : 
                    print ("fails!")
                else:
                    for k in answer.keys() :
                        #print (i,j,k,ans[k], answer[k])
                        ok = set (ans[k]) == set (answer[k])
                        if not ok:
                            print (i,j, "fails!") 
                        #self.assertEqual(  set (ans[k]),  set (answer[k]), "fail !!!")

unittest.main(argv=[''], verbosity=2, exit=False)
