from typing import List

def process_input(input):
    grid = []
    for line in input.rstrip().split('\n'):
        new_array = [char for char in line]
        grid.append(new_array)
    return grid

def is_col_empty(grid, col):
    for row in grid:
        if row[col] != '.':
            return False
    return True

def expand_universe(grid: List[List[str]]):
    row_len = len(grid[0])
    empty_rows = [index for index, row in enumerate(grid) if row.count('.') == row_len]
    empty_cols = [col for col in range(0, row_len) if is_col_empty(grid, col)]
    empty_row_fill = grid[empty_rows[0]]
    for empty_row_index in reversed(empty_rows):
        grid.insert(empty_row_index, empty_row_fill.copy())
    for row in grid:
        for empty_col_index in reversed(empty_cols):
            row.insert(empty_col_index, '.')
    return grid

def print_universe(grid):
    output = ''
    for row in grid:
        for char in row:
            output += char
        output += '\n'
    return output


def part1(input):
    grid = process_input(input)
    # print(grid[0])
    expand_universe(grid)
    print(print_universe(grid))
    return 0