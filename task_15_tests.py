import unittest
import random
from task_15 import tank_rush


class TankRushTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(tank_rush.TankRush(3, 4, "1234 2345 0987", 2, 2, "23 34"), True)

    def test2(self):
        self.assertEqual(tank_rush.TankRush(1, 3, '727', 1, 2, '72'), True)

    def test3(self):
        self.assertEqual(tank_rush.TankRush(3, 3, '321 694 798', 3, 2, '32 69 79'), True)

    def test4(self):
        self.assertEqual(tank_rush.TankRush(7, 3, '727 158 735 425 235 123 432',
                                            6, 2, '72 15 73 42 23 12'), True)

    def test5(self):
        self.assertEqual(tank_rush.TankRush(3, 4, "1234 2345 0987", 2, 2, "23 98"), False)

    def test6(self):
        self.assertEqual(tank_rush.TankRush(3, 8, '7277604 1583078 1427735', 3, 2, '78 35 20'), False)

    def test7(self):
        self.assertEqual(tank_rush.TankRush(3, 15, '993854324744973 768703404219199 630625270887199',
                                            2, 2, '99 99'), True)

    def test_random_true(self):
        first_map = ''
        second_map = ''

        for d in range(10000):
            first_map += str(random.randint(1000000, 9999999))
            if d < 10000:
                first_map += ' '

        for b in range(2):
            second_map += str(random.randint(10, 99))
            if b < 2:
                second_map += ' '

        self.assertEqual(tank_rush.TankRush(10000, 7, first_map, 2, 2, second_map), True)

    def test_random_false(self):
        first_map = ''
        second_map = ''

        for d in range(10000):
            first_map += str(random.randint(1000000, 9999999))
            if d < 10000:
                first_map += ' '

        for b in range(10000):
            second_map += str(random.randint(10, 99))
            if b < 10000:
                second_map += ' '

        self.assertEqual(tank_rush.TankRush(10000, 7, first_map, 10000, 2, second_map), False)


if __name__ == '__main__':
    unittest.main()

