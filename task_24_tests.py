import unittest
from task_24 import matrix_turn


class TankRushTest(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(matrix_turn.MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 1),
                                                ['212345', '343456', '456767', '567898'])

        self.assertEqual(matrix_turn.MatrixTurn(["123456", "234567", "345678", "456789"], 4, 6, 3),
                                                ['432123', '565434', '676545', '789876'])


if __name__ == '__main__':
    unittest.main()

