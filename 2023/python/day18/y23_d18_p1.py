import heapq

class Block():
    def __init__(self, row, col, color=None):
        self.row = row
        self.col = col
        self.color = color

    def __str__(self) -> str:
        return f'{self.row}x{self.col}'


def next_block(i, j, dir):
    directions = {0: (i, j+1), 1: (i+1, j), 2: (i, j-1), 3: (i-1, j)}
    return directions[dir]

def process_input(input: str):
    path_loop = []
    direction = {'R': 0, 'D': 1, 'L': 2, 'U': 3}
    i, j = 42, 69
    for line in input.rstrip().split('\n'):
        direction_part, length_part, color_part = line.split(' ')
        dir = direction[direction_part]
        len = int(length_part)
        color = f'0x{color_part[2:8]}'
        for _ in range(len):
            i,j = next_block(i, j, dir)
            path_loop.append(Block(i, j, color))
    return path_loop

def normalize_coords(path):
    min_i = min((block.row) for block in path)
    min_j = min((block.col) for block in path)
    for block in path:
        block.row -= min_i
        block.col -= min_j

def make_grid(rows, cols):
    grid: list[list]
    grid = []
    for row in range(rows):
        grid.append(list())
        for _ in range(cols):
            grid[row].append(None)
    return grid

def print_grid(grid):
    output = ''
    for line in grid:
        output += ''.join((char if char else '.' for char in line)) + '\n'
    return output

def find_coord_inside_loop(grid) -> (int, int):
    i, j = 0, 0
    while grid[i][j] == None and j < len(grid[0]):
        j += 1
    first_border = j
    assert grid[i+1][j] != None and grid[i][j+1] != None, 'should be corner'
    assert grid[i+1][j+1] == None, 'should be empty, inside loop'
    return i + 1, j + 1

def traverse_inside(grid, i, j):
    q = [(i, j)]
    seen = {(i, j)}
    heapq.heapify(q)
    inner_count = 0
    while q:
        inner_count += 1
        i, j = heapq.heappop(q)
        for dir in [0, 1, 2, 3]:
            i2, j2 = next_block(i, j, dir)
            if grid[i2][j2] != None:
                continue
            if grid[i2][j2] == None:
                grid[i2][j2] = '.'
            key = (i2, j2)
            if key not in seen:
                heapq.heappush(q, (i2, j2))
                seen.add(key)
    return inner_count


def part1(input):
    path = process_input(input)
    normalize_coords(path)
    grid_rows = max((block.row) for block in path) + 1
    grid_cols = max((block.col) for block in path) + 1
    grid = make_grid(grid_rows, grid_cols)
    block: Block
    for block in path:
        grid[block.row][block.col] = '#'
    in_i, in_j = find_coord_inside_loop(grid)
    inner = traverse_inside(grid, in_i, in_j)
    return len(path) + inner