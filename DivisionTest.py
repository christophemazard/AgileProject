import unittest
import MyMathLib

class DivisionTest(unittest.TestCase):
    def testSumPositiveNumbersOneAndOne(self):
        div = MyMathLib.Division()
        self.assertEqual(1,div.execute(1,1))
        
    def testSumPositiveNumbersOneAndTwo(self):
        div = MyMathLib.Division()
        self.assertEqual(2,div.execute(2,1))
        
    def testSumPositiveNumbersTwoAndTwo(self):
        div = MyMathLib.Division()
        self.assertEqual(4,div.execute(8,2))
        
    def testSumZero(self):
        div = MyMathLib.Division()
        self.assertEqual(0,div.execute(0,1))
        
    def testSumNegativeNumbers(self):
        div = MyMathLib.Division()
        self.assertEqual(2,div.execute(-2,-1))


if __name__ == '__main__':
    unittest.main()
