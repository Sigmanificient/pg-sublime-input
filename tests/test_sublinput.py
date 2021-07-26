import sublinput
import unittest


class MyTestCase(unittest.TestCase):

    def test_string(self):
        self.assertIsInstance(input("Testing result value :"), str)

    def test_return_value(self):
        return_value = input("Type 'test': ")
        self.assertEqual(return_value, 'test')


if __name__ == '__main__':
    unittest.main()
