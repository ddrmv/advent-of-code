from typing import List

class Coordinate():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f'r{self.row},c{self.col}'
    
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

class Universe():
    def __init__(self, input_array):
        self.grid: List[List[str]]
        self.galaxies: List[Coordinate]
        self.grid = input_array
        self.galaxies = []
        self.routes = []

    def __str__(self):
        output = ''
        for row in self.grid:
            for char in row:
                output += char
            output += '\n'
        return output

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

    def locate_galaxies(self):
        for row_i, row in enumerate(self.grid):
            for col_i, col in enumerate(row):
                if col == '#':
                    self.galaxies.append(Coordinate(row_i, col_i))

    def find_distance(self, a: Coordinate, b: Coordinate):
        x = abs(b.col - a.col)
        y = abs(b.row - a.row)
        return x + y
    
    def calculate_routes(self):
        routes = []
        for index, galaxy_a in enumerate(self.galaxies):
            for galaxy_b in self.galaxies[index + 1:len(self.galaxies)]:
                routes.append((galaxy_a, galaxy_b))
        return sum((self.find_distance(*route)) for route in routes)


def process_input(input):
    grid = []
    for line in input.rstrip().split('\n'):
        new_array = [char for char in line]
        grid.append(new_array)
    return grid


def part1(input):
    u = Universe(process_input(input))
    u.expand_universe()
    u.locate_galaxies()
    return u.calculate_routes()