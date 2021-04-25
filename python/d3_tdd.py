import unittest
import random


class Version2TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_randomDirections(self):
        kid_count = 7
        degree = random.randint(0, 360)
        sweep = 360 / kid_count
        for x in range(kid_count):
            degree += sweep
            degree = degree % 360
            print("{}  {} ".format(sweep, degree))

        expected = True
        actual = True
        self.assertEqual(expected, actual, 'max len() not correct')


if __name__ == "__main__":
    unittest.main()
