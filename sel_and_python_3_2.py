import unittest

class MyTest(unittest.TestCase):

	def test_abs1(self):
		self.assertEqual(abs(-42), 42, "Shoud be absolute value of a number")

	def test_abs2(self):
		self.assertEqual(abs(-42), -42, "Shoud be absolute value of a number")

if __name__ == "__main__":
	unittest.main()
