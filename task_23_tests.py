import unittest
from task_23 import tree_of_life


class TankRushTest(unittest.TestCase):

    def test_regression(self):
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 1, [".+..", "..+.", ".+.."]), ['++++', '++++', '++++'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 2, [".+..", "..+.", ".+.."]), ['...+', '+...', '...+'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 3, [".+..", "..+.", ".+.."]), ['++++', '++++', '++++'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 4, [".+..", "..+.", ".+.."]), ['.+..', '..+.', '.+..'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 5, [".+..", "..+.", ".+.."]), ['++++', '++++', '++++'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 6, [".+..", "..+.", ".+.."]), ['...+', '+...', '...+'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 7, [".+..", "..+.", ".+.."]), ['++++', '++++', '++++'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 8, [".+..", "..+.", ".+.."]), ['.+..', '..+.', '.+..'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 9, [".+..", "..+.", ".+.."]), ['++++', '++++', '++++'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 10, [".+..", "..+.", ".+.."]), ['...+', '+...', '...+'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 11, [".+..", "..+.", ".+.."]), ['++++', '++++', '++++'])
        self.assertEqual(tree_of_life.TreeOfLife(3, 4, 12, [".+..", "..+.", ".+.."]), [".+..", "..+.", ".+.."])

    def test_regression_2(self):
        self.assertEqual(tree_of_life.TreeOfLife(1, 1, 1, ["+"]), ['+'])
        self.assertEqual(tree_of_life.TreeOfLife(1, 1, 2, ["+"]), ['.'])
        self.assertEqual(tree_of_life.TreeOfLife(1, 1, 3, ["+"]), ['+'])
        self.assertEqual(tree_of_life.TreeOfLife(1, 1, 4, ["+"]), ['+'])

if __name__ == '__main__':
    unittest.main()

