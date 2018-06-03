#!/usr/bin/python
import unittest
from plus import plus

class TestPlus(unittest. TestCase):
	def test_int(self):
		self.assertEqual(plus(1,2),3,"errer on int")

	def test_float(self):
		self.assertTrue(3.29999 < plus(1.1,2.2) < 3.300001,"errer on float")

	def test_str(self):
		self.assertEqual(plus("ab","cd"),"abcd","errer on str")
unittest.main()
