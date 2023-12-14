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
        if direction == DIR['n'] or direction == DIR['w']:
            for row, line in enumerate(self.grid):
                for col, char in enumerate(line):
                    self.roll_one(row, col, direction)
        elif direction == DIR['e'] or direction == DIR['s']:
            for row, line in reversed(list(enumerate(self.grid))):
                for col, char in reversed(list(enumerate(line))):
                    self.roll_one(row, col, direction)
        else:
            assert False, 'Direction should be one of n,w,s,e'

    def weight_on_beams_for_direction(self, direction: Direction):
        total = 0
        assert direction == DIR['n']
        if direction == DIR['n']:
            for row, line in enumerate(self.grid):
                for col, char in enumerate(line):
                    if self.grid[row][col].rolls:
                        total += self.rows - row
        return total

    def cycle(self, times=1):
        for _ in range(times):
            self.roll_all(DIR['n'])
            self.roll_all(DIR['w'])
            self.roll_all(DIR['s'])
            self.roll_all(DIR['e'])

    def hash_grid(self):
        return hash(self.__str__())
    

def part1(input):
    g = Grid()
    g.build_grid(input)
    g.roll_all(DIR['n'])
    return g.weight_on_beams_for_direction(DIR['n'])

def part2(input):
    g = Grid()
    g.build_grid(input)

    BIL = 1_000_000_000
    hashes = []
    first_at = -1
    repeat_at = -1

    for i in range(BIL):
        g.cycle()
        current_hash = g.hash_grid()
        hashes.append(current_hash)

        if current_hash in hashes[:-1]:
            repeat_at = i
            first_at = hashes.index(current_hash)
            break

    cycle_length = repeat_at - first_at
    to_skip_cycles = ((BIL - repeat_at) // cycle_length) * cycle_length
    cycles_left = BIL - to_skip_cycles - repeat_at - 1

    for i in range(cycles_left):
        g.cycle()

    return g.weight_on_beams_for_direction(DIR['n'])