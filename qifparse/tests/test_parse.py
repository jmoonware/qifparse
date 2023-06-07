# -*- coding: utf-8 -*-
import unittest
import os
from qifparse.parser import QifParser
from decimal import Decimal


filename = os.path.join(os.path.dirname(__file__), 'file.qif')
filename2 = os.path.join(os.path.dirname(__file__), 'transactions_only.qif')
filename3 = os.path.join(os.path.dirname(__file__), 'comma_test.qif')


class TestQIFParsing(unittest.TestCase):

    def testParseFile(self):
        qif = QifParser().parse(open(filename))
        self.assertTrue(qif)

    def testWriteFile(self):
        data = open(filename).read()
        qif = QifParser().parse(open(filename))
#        out = open('out.qif', 'w')
#        out.write(str(qif))
#        out.close()
        self.assertEqual(data, str(qif))

    def testParseTransactionsFile(self):
        data = open(filename2).read()
        qif = QifParser().parse(open(filename2))
#        out = open('out.qif', 'w')
#        out.write(str(qif))
#        out.close()
        self.assertEqual(data, str(qif))

    def testParseTransactionsFileCommas(self):
        data = open(filename3).read()
        qif = QifParser(dayfirst=False).parse(open(filename3))
#        out = open('out.qif', 'w')
#        out.write(str(qif))
#        out.close()
        self.assertEqual(qif.get_transactions()[0][0].amount,Decimal('3137.91'))

if __name__ == "__main__":
    import unittest
    unittest.main()
