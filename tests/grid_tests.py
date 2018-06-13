#!environment/bin/python3

import unittest

import context
from sudoku import sudokugrid


class TestSudokuGrid(unittest.TestCase):
    """Test SudokuGrid class."""

    def test_with_n_equals_3(self):
        """Initialise the grid with n=3"""
        grid = [[2, 0, 3], [1, 0, 0], [0, 0, 1]]

        g = sudokugrid.SudokuGrid(grid=grid)

        self.assertEqual(g.dimension, 3)

    def test_only_with_n(self):
        """Test initialisation using only dimension n"""
        g = sudokugrid.SudokuGrid(n=9)

        self.assertEqual(g.dimension, 9)
        self.assertTrue(isinstance(g.grid, list))

    def test_exception_raised_when_nor_grid_nor_n(self):
        """Test that exception is raised when no grid or no n are given."""

        with self.assertRaises(Exception):
            g = sudokugrid.SudokuGrid()

        self.assertTrue('grid or dimension value are required.')

    def test_exception_raised_when_grid_not_list(self):
        """Test that exception is raised for invalid grid."""

        with self.assertRaises(Exception):
            g = sudokugrid.SudokuGrid(grid='string')




if __name__ == '__main__':
    unittest.main()