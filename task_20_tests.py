import unittest
from task_20 import bast_shoe


class TankRushTest(unittest.TestCase):

    def test1(self):   # regression 1
        self.assertEqual(bast_shoe.BastShoe('1 Hello'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('1 , World!'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('1 ++'), 'Hello, World!++')
        self.assertEqual(bast_shoe.BastShoe('2 2'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, World!++')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('1 *'), 'Hello, World!*')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('3 6'), ',')
        self.assertEqual(bast_shoe.BastShoe('2 100'), '')

    def test2(self):    # regression 2
        self.assertEqual(bast_shoe.BastShoe('1 Hello'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('1 , World!'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('1 ++'), 'Hello, World!++')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hello, World!++')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hello, World!++')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hello, World!++')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, World!')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('2 2'), 'Hel')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hel')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hel')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hel')
        self.assertEqual(bast_shoe.BastShoe('2 99999'), '')

    def test3(self):    # false values
        self.assertEqual(bast_shoe.BastShoe('1 Hello'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('1'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('1123123123123'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('2 0'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('2 222'), '')
        self.assertEqual(bast_shoe.BastShoe('1 Hello'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('3'), '')
        self.assertEqual(bast_shoe.BastShoe('3 apple'), '')
        self.assertEqual(bast_shoe.BastShoe('1 , world'), 'Hello, world')
        self.assertEqual(bast_shoe.BastShoe('4 qwertyqwerty'), 'Hello, world')
        self.assertEqual(bast_shoe.BastShoe('5 qwertyqwerty'), 'Hello, world')
        self.assertEqual(bast_shoe.BastShoe('2 99999'), '')

    def test4(self):    # feedback_index tests
        self.assertEqual(bast_shoe.BastShoe('1 Hello'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('3'), '')
        self.assertEqual(bast_shoe.BastShoe('3 0'), '')
        self.assertEqual(bast_shoe.BastShoe('3 1'), 'H')
        self.assertEqual(bast_shoe.BastShoe('3 2'), 'e')
        self.assertEqual(bast_shoe.BastShoe('3 3'), 'l')
        self.assertEqual(bast_shoe.BastShoe('3 4'), 'l')
        self.assertEqual(bast_shoe.BastShoe('3 5'), 'o')
        self.assertEqual(bast_shoe.BastShoe('3 6'), '')
        self.assertEqual(bast_shoe.BastShoe('3 -1'), '')


if __name__ == '__main__':
    unittest.main()

