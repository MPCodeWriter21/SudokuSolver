#!/usr/bin/python3

"""
Simple sudoku solver

GitHub: Https://GitHub.com/MPCodeWriter21
Telegram Channel: @CodeWriter21

"""

# We use `matrix` function to print solved data in a beautiful format.
from numpy import matrix
from typing import List


# Checks whether `n` can be placed in position [y, x]
def possible(grid: List[List[int]], y: int, x: int, n: int) -> bool:
    """

    Checks whether `n` can be placed in position [y, x]

    :param grid: the grid to check
    :param y: row of the grid to check
    :param x: column of the grid to check
    :param n: number to check
    :return: the possibility of putting n in position [y, x]
    :rtype: bool
    """
    # Checks the input values
    if type(grid) is not list:
        raise TypeError('`grid` must be a list!')
    if len(grid) is not 9:
        raise ValueError('`grid` must be a 9x9 list!')
    for item in grid:
        if type(item) is not list:
            raise TypeError('Each item in `grid` must be a list!')
        if len(item) is not 9:
            raise ValueError('`grid` must be a 9x9 list!')
        for i in item:
            if type(i) is not int:
                raise TypeError('Each item in each list in `grid` must be an integer!')
    if type(y) is not int:
        raise TypeError('`y` must be an integer!')
    if type(x) is not int:
        raise TypeError('`x` must be an integer!')
    if type(n) is not int:
        raise TypeError('`n` must be an integer!')

    # Checks for `n` in row y; returns False if `n` already exists.
    for i in range(9):
        if grid[y][i] == n:
            return False
    # Checks for `n` in column x; returns False if `n` already exists.
    for i in range(9):
        if grid[i][x] == n:
            return False
    # `y0` and `x0` represent the square of the [y, x] position
    y0 = (y // 3) * 3
    x0 = (x // 3) * 3
    # Checks for `n` in square; returns False if `n` already exists.
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False
    # Returns True
    return True


# Tries to find the solution for the grid
def solve(grid: List[List[int]]):
    """

    Tries to find the solution for the grid

    :param grid: the grid to solve
    :return: the solution to the grid or None if not found
    :rtype: List[List[int]]
    """

    # Checks the input value
    if type(grid) is not list:
        raise TypeError('`grid` must be a list!')
    if len(grid) is not 9:
        raise ValueError('`grid` must be a 9x9 list!')
    for item in grid:
        if type(item) is not list:
            raise TypeError('Each item in `grid` must be a list!')
        if len(item) is not 9:
            raise ValueError('`grid` must be a 9x9 list!')
        for i in item:
            if type(i) is not int:
                raise TypeError('Each item in each list in `grid` must be an integer!')

    # Trys to fill the blank cells in the grid
    for y in range(9):
        for x in range(9):
            # Checks if a cell is blank
            if grid[y][x] == 0:
                # Trys to find a possible number to put in the blank cell
                for n in range(1, 10):
                    # Checks if it is possible to put `n` in the blank cell
                    if possible(grid, y, x, n):
                        # Puts `n` in the blank cell
                        grid[y][x] = n
                        # Calls `solve` to find the solution
                        solution = solve(grid)
                        # Checks if the problem is solved
                        if not solution:
                            # Puts 0 in the cell
                            grid[y][x] = 0
                        else:
                            # Returns the solution
                            return solution
                # Returns None
                return
    # Returns the solution
    return grid


# Main function of the script
def main():
    # The sudoku grid to solve
    grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    # Prints solution in a beautiful shape
    print(matrix(solve(grid)))


if __name__ == '__main__':
    # Runs the main function
    main()
