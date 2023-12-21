import heapq

def process_input(input: str):
    grid = [[c for c in line] for line in input.rstrip().split('\n')]
    print()
    return grid

def grid_output(grid):
    output = ''
    for line in grid:
        output += ''.join((c for c in line)) + '\n'
    return output
    
def next_block(i, j, dir, rows, cols):
    directions = {0: (i, j+1), 1: (i+1, j), 2: (i, j-1), 3: (i-1, j)}
    i2, j2 = directions[dir]
    return (i2, j2) if 0 <= i2 < rows and 0 <= j2 < cols else (None, None)

def traverse_plots(grid, i, j, step_limit):
    rows = len(grid)
    cols = len(grid[0])
    print(rows, cols)
    step = 0
    q = [(i, j, step)]
    seen = {(i, j, 0)}
    heapq.heapify(q)
    while q:
        i, j, step = heapq.heappop(q)
        step += 1
        for dir in [0, 1, 2, 3]:
            if step > step_limit:
                continue
            i2, j2 = next_block(i, j, dir, rows, cols)
            if i2 == None:
                continue
            if grid[i2][j2] == '#':
                continue
            key = (i2, j2, step)
            if key not in seen:
                if step % 2:
                    grid[i2][j2] = '1'
                    heapq.heappush(q, (i2, j2, step))
                    seen.add(key)
                else:
                    grid[i2][j2] = '2'
                    heapq.heappush(q, (i2, j2, step))
                    seen.add(key)

def count(grid, char_to_count):
    counter = 0
    for line in grid:
        for char in line:
            counter += char == char_to_count
    return counter


def part1(input, step_limit):
    grid = process_input(input)
    start_at = (len(grid)//2, len(grid[0])//2)
    traverse_plots(grid, *start_at, step_limit)
    # print(grid_output(grid))
    return count(grid, '2')
    