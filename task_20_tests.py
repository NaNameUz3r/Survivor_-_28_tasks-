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
        self.assertEqual(bast_shoe.BastShoe('3 3'), 'l')
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
        self.assertEqual(bast_shoe.BastShoe('3'), '')
        self.assertEqual(bast_shoe.BastShoe('3 1'), '')
        self.assertEqual(bast_shoe.BastShoe('3 0'), '')
        self.assertEqual(bast_shoe.BastShoe('3 -1'), '')
        self.assertEqual(bast_shoe.BastShoe('3 Where is my BUG?'), '')
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

        self.assertEqual(bast_shoe.BastShoe('1 , world!'), 'Hello, world!')
        self.assertEqual(bast_shoe.BastShoe('3 7'), ' ')  # Пробел ведь - Символ!! Символ есть - возвращаем!!!
        self.assertEqual(bast_shoe.BastShoe('3 13'), '!')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello')
        self.assertEqual(bast_shoe.BastShoe('3 0'), '')
        self.assertEqual(bast_shoe.BastShoe('3 1'), 'H')
        self.assertEqual(bast_shoe.BastShoe('3 2'), 'e')
        self.assertEqual(bast_shoe.BastShoe('3 3'), 'l')
        self.assertEqual(bast_shoe.BastShoe('3 4'), 'l')
        self.assertEqual(bast_shoe.BastShoe('3 5'), 'o')
        self.assertEqual(bast_shoe.BastShoe('3 6'), '')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hello, world!')
        self.assertEqual(bast_shoe.BastShoe('2 3'), 'Hello, wor')
        self.assertEqual(bast_shoe.BastShoe('3 6'), ',')
        self.assertEqual(bast_shoe.BastShoe('3 10'), 'r')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, world!')
        self.assertEqual(bast_shoe.BastShoe('3 0'), '')
        self.assertEqual(bast_shoe.BastShoe('3 13'), '!')
        self.assertEqual(bast_shoe.BastShoe('3 14'), '')
        self.assertEqual(bast_shoe.BastShoe('1  Stop hiding, buggy bug'), 'Hello, world! Stop hiding, buggy bug')
        self.assertEqual(bast_shoe.BastShoe('3 18'), 'p')
        self.assertEqual(bast_shoe.BastShoe('3 36'), 'g')
        self.assertEqual(bast_shoe.BastShoe('2 1'), 'Hello, world! Stop hiding, buggy bu')
        self.assertEqual(bast_shoe.BastShoe('3 36'), '')
        self.assertEqual(bast_shoe.BastShoe('4'), 'Hello, world! Stop hiding, buggy bug')
        self.assertEqual(bast_shoe.BastShoe('3 36'), 'g')
        self.assertEqual(bast_shoe.BastShoe('5'), 'Hello, world! Stop hiding, buggy bu')
        self.assertEqual(bast_shoe.BastShoe('3 36'), '')
        self.assertEqual(bast_shoe.BastShoe('3 35'), 'u')
        self.assertEqual(bast_shoe.BastShoe('3 -100'), '')
        self.assertEqual(bast_shoe.BastShoe('2 1000'), '')
        self.assertEqual(bast_shoe.BastShoe('3 1'), '')

        test_str = '1 Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut ' \
                   'labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris ' \
                   'nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate ' \
                   'velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non ' \
                   'proident, sunt in culpa qui officia deserunt mollit anim id est laborum. '

        self.assertEqual(bast_shoe.BastShoe(test_str), test_str[2:])

        for i in range(1, len(test_str[2:])):
            self.assertEqual(bast_shoe.BastShoe('3 ' + str(i)), test_str[2:][i - 1])


if __name__ == '__main__':
    unittest.main()

