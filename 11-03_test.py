import unittest

from eleven_per_three import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.marci = Employee('marci', 'urbán', 20_000)

    def test_give_default_raise(self):
        self.marci.give_raise()
        self.assertEqual(self.marci.salary, 25_000)

    def test_give_custom_raise(self):
        self.marci.give_raise(1000)
        self.assertEqual(self.marci.salary, 21_000)


if __name__ == '__main__':
    unittest.main()
