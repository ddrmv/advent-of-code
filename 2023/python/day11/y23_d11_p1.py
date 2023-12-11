from typing import List

class Universe():
    def __init__(self, input_array):
        self.grid: List[List[str]]
        self.grid = input_array

    def is_col_empty(self, col):
        for row in self.grid:
            if row[col] != '.':
                return False
        return True

    def expand_universe(self):
        row_len = len(self.grid[0])
        empty_rows = [index for index, row in enumerate(self.grid) if row.count('.') == row_len]
        empty_cols = [col for col in range(0, row_len) if self.is_col_empty(col)]
        empty_row_fill = self.grid[empty_rows[0]]
        for empty_row_index in reversed(empty_rows):
            self.grid.insert(empty_row_index, empty_row_fill.copy())
        for row in self.grid:
            for empty_col_index in reversed(empty_cols):
                row.insert(empty_col_index, '.')

    def __str__(self):
        output = ''
        for row in self.grid:
            for char in row:
                output += char
            output += '\n'
        return output


def process_input(input):
    grid = []
    for line in input.rstrip().split('\n'):
        new_array = [char for char in line]
        grid.append(new_array)
    return grid


def part1(input):
    u = Universe(process_input(input))
    u.expand_universe()
    print(u)
    return u