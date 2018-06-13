#!environment/bin/python3
"""Utility classes being used in solver to solve the Sudoku."""


class SudokuGrid():
    """Sudoku playing grid"""

    def __init__(self, grid=None, n=None):
        if grid is not None:
            if any(not isinstance(elem, list) for elem in grid):
                raise Exception('grid must be a list of lists.')
            self.grid = grid
            self._n = len(grid)
        elif grid is None and n is not None:
            self.grid = self.random_grid_generation(n)
            self._n = n

        else:
            raise Exception('grid or dimension value are required.')

    @property
    def dimension(self):
        return self._n

    def random_grid_generation(self, n):
        """When grid is not input, self generate a sudoku of dimension=n."""
        grid3 = [
            [2, 0, 3],
            [1, 0, 0],
            [0, 0, 1],
        ]

        grid4 = [
            [4, 0, 0, 0],
            [0, 2, 0, 4],
            [2, 0, 3, 0],
            [0, 0, 0, 2],
        ]

        grid9 = [
            [0, 0, 0, 0, 0, 0, 6, 8, 0],
            [0, 0, 0, 0, 7, 3, 0, 0, 9],
            [3, 0, 9, 0, 0, 0, 0, 4, 5],
            [4, 9, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 3, 0, 5, 0, 9, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 3, 6],
            [9, 6, 0, 0, 0, 0, 3, 0, 8],
            [7, 0, 0, 6, 8, 0, 0, 0, 0],
            [0, 2, 8, 0, 0, 0, 0, 0, 0],
        ]

        grids = {
            3: grid3,
            4: grid4,
            9: grid9,
        }

        if n in grids.keys():
            return grids[n]

    @property
    def grid_is_evenly_sized(self):
        """Return True if grid is n x n."""
        for row in range(len(self.grid)):
            if len(self.grid[row]) != len(self.grid):
                return False
        return True

    @property
    def rows_in_grid_have_unique_values(self, grid=None):
        """Return True if all rows have unique values from 1 to n or empty spaces."""
        if grid is None:
            grid = self.grid

        for row in range(len(grid)):
            value_counts = {0 for value in range(1, self._n + 1)}
            for column in range(len(grid[row])):
                if self.grid[row][column] > 0:
                    value_counts[grid[row][column]] += 1
            # Once we have counted, check for repeated values
            for value in value_counts.keys():
                if value_counts[value] > 1:
                    return False
        return True

    @property
    def columns_in_grid_have_unique_values(self):
        """
        Return True if all columns have unique values from 1 to n or empty spaces.
        If grid is not evenly sized, zip will chop away rows.
        """
        transposed_grid = list(map(list, zip(*self.grid)))
        return self.rows_in_grid_have_unique_values(transposed_grid)

    @property
    def is_valid_grid(self):
        """
        Return True if the Sudoku grid is valid:

        1. Each row has a unique numbers from 1 to n or empty spaces.
        2. Each column has unique numbers from 1 to n or empty spaces.

        3. Each subgrid (if any) has unique numbers from 1 to n or empty spaces.
            This one is tricky, as the definition of subgrid is based on the divisors of n.
        """

        if not self.grid_is_evenly_sized:
            return False

        if not self.rows_in_grid_have_unique_values:
            return False

        if not self.columns_in_grid_have_unique_values:
            return False

        # TODO: Rercursively find out if all subgrids also are valid grids
