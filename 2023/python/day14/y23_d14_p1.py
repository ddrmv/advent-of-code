from typing import List


class Direction():
    def __init__(self, row_change, col_change):
        self.row = row_change
        self.col = col_change

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


DIR = {'s': Direction(+1, 0), 'n': Direction(-1, 0),
       'w': Direction(0, -1), 'e': Direction(0, +1)}


class Shape():
    def __init__(self, shape_str):
        self.type = shape_str
        self.rolls = True if shape_str == 'O' else False
        self.blocks = True if shape_str == '#' else False
        self.empty = True if shape_str == '.' else False

    def __str__(self):
        return self.type


class Grid():
    def __init__(self):
        self.grid: List[List[Shape]]
        self.grid = []
        self.rows = None
        self.cols = None

    def build_grid(self, input):
        lines = input.rstrip().split('\n')
        self.rows = len(lines)
        self.cols = len(lines[0])
        for line in lines:
            self.grid.append([Shape(char) for char in line])

    def __str__(self):
        line_str = lambda a: ''.join([str(shape) for shape in a]) + '\n'
        return ''.join([line_str(line) for line in self.grid])
    
    def get_shape_in_direction(self, g_row, g_col, direction: Direction, distance=1) -> Shape | None:
        new_row = g_row + direction.row * distance
        new_col = g_col + direction.col * distance
        if new_row < 0 or new_row >= self.rows or new_col < 0 or new_col >= self.cols:
            return None
        else:
            return self.grid[new_row][new_col]

    def swap_shapes(self, a_g_row, a_g_col, direction: Direction, distance):
        assert distance > 0
        a = self.grid[a_g_row][a_g_col]
        b = self.grid[a_g_row + direction.row * distance][a_g_col + direction.col * distance]
        self.grid[a_g_row + direction.row * distance][a_g_col + direction.col * distance] = a
        self.grid[a_g_row][a_g_col] = b

    def roll_one(self, g_row, g_col, direction: Direction):
        shape: Shape
        shape = self.grid[g_row][g_col]
        if shape.rolls:
            moves = 1
            to_shape = self.get_shape_in_direction(g_row, g_col, direction, moves)
            while to_shape and to_shape.empty:
                moves += 1
                to_shape = self.get_shape_in_direction(g_row, g_col, direction, moves)
            moves -= 1
            if moves > 0:
                self.swap_shapes(g_row, g_col, direction, moves)

    def roll_all(self, direction: Direction):
        for row, line in enumerate(self.grid):
            for col, char in enumerate(line):
                self.roll_one(row, col, direction)

    def weight_on_beams_for_direction(self, direction: Direction):
        total = 0
        assert direction == DIR['n']
        if direction == DIR['n']:
            for row, line in enumerate(self.grid):
                for col, char in enumerate(line):
                    if self.grid[row][col].rolls:
                        total += self.rows - row
        return total
    

def part1(input):
    g = Grid()
    g.build_grid(input)
    g.roll_all(DIR['n'])
    return g.weight_on_beams_for_direction(DIR['n'])