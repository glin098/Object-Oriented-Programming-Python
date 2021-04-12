'''
There may be at most 4 people on the terrace at the same time.
The first thing that happens is 3 people entering the terrace.
Then, a group of 2 people attempt to enter. This would bring the
total number up to 3+2=5. Since this is larger than 4, this group
may not enter. A single person then leaves, meaning 2 people remain
on the terrace. That person then comes back, bringing the total
number up to three again. Finally, a pair of people try to enter
the terrace, but is again denied since this would bring the total
number up to 5. Thus, a total of 2 groups were not allowed to enter
the terrace.
'''

import unittest
from Terrace import *

class StandardTest(unittest.TestCase):

    def testInitialize(self):
        t = Terrace(5)
        self.assertEqual(t.getNumDenied(),0)

    def testExactCapacity(self):
        t = Terrace(25)
        self.assertTrue(t.processEnter(25))
        self.assertEqual(t.getNumDenied(),0)

    def testProcessEnter(self):
        t = Terrace(5)
        self.assertTrue(t.processEnter(4))
        self.assertEqual(t.getNumDenied(), 0)

    def testProcessLeave(self):
        t = Terrace(5)
        self.assertFalse(t.processLeave(5))
        self.assertEqual(t.getNumDenied(), 0)
        
    def testDenied(self):
        t = Terrace(5)
        self.assertFalse(t.processEnter(6))
        self.assertEqual(t.getNumDenied(), 1)

    def testNegativeNum(self):
        t = Terrace(5)
        self.assertTrue(t.processEnter(-1))
        self.assertEqual(t.getNumDenied(), 0)

    def testNoneEnters(self):
        t = Terrace(5)
        self.assertTrue(t.processEnter(0))
        self.assertEqual(t.getNumDenied(), 0)

    def testZero(self):
        t = Terrace(0)
        self.assertFalse(t.processEnter(1))
        self.assertEqual(t.getNumDenied(), 1)

    def testAdd(self):
        t = Terrace(5)
        self.assertTrue(t.processEnter(2))
        self.assertTrue(t.processEnter(1))
        self.assertEqual(t.getNumDenied(), 0)

    def testSub(self):
        t = Terrace(5)
        self.assertTrue(t.processEnter(3))
        self.assertTrue(t.processEnter(2))
        self.assertEqual(t.getNumDenied(), 0)    

        
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(StandardTest))
    unittest.TextTestRunner(verbosity=1).run(suite)
