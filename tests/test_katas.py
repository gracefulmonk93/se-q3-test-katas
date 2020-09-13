import unittest
import katas
import random


author = "Leann James with help from Kevin Clark"


class TestKatas(unittest.TestCase):
    def test_add(self):
        random_one = random.randrange(-100, 100)
        random_two = random.randrange(-99, 99)
        result = random_one + random_two
        self.assertEqual(katas.add(random_one, random_two), result)

    def test_multiply(self):
        random_one = random.randrange(-100, 100)
        random_two = random.randrange(-99, 99)
        result = random_one * random_two
        self.assertEqual(katas.multiply(random_one, random_two), result)

    def test_power(self):
        self.assertEqual(katas.power(2, 2), 4)
        self.assertRaises(ValueError, katas.power, 3, -3)
        self.assertRaises(ValueError, katas.power, 4, 0.4)

    def test_factorial(self):
        list_factorial = [
            1, 2, 6, 24, 120, 720, 5040, 40320, 362880,
            3628800, 39916800, 479001600, 6227020800,
            87178291200, 1307674368000
        ]
        for index, value in enumerate(list_factorial):
            self.assertEqual(katas.factorial(index + 1), value)
            self.assertRaises(ValueError, katas.factorial, -4)

    def test_fibonacci(self):
        list_fibonacci = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
            233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
            17711, 28657, 46368, 75025, 121393, 196418,
            317811, 514229
        ]
        for index, value in enumerate(list_fibonacci):
            self.assertEqual(katas.fibonacci(index), value)
            self.assertRaises(ValueError, katas.fibonacci, -4)


if __name__ == '__main__':
    unittest.main()
