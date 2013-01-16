import unittest

from main import load_puzzle, solve

class TestFolding(unittest.TestCase):

	def test_simple_fold(self):

		simple_puzzle = {"snake" : [1, 1, 1, 1, 1, 1, 1],
		"shape" : {"len" : 2, "wid" : 2, "dep" : 2}}

		rectangle, s = load_puzzle(simple_puzzle)
		self.assertTrue(solve(rectangle, s))

	def test_wrong_simple_fold(self):

		simple_puzzle = {"snake" : [1, 2, 1, 1, 1, 1],
		"shape" : {"len" : 2, "wid" : 2, "dep" : 2}}

		rectangle, s = load_puzzle(simple_puzzle)
		self.assertFalse(solve(rectangle, s))

