import heapq

def next_location(i, j, dir):
    next_location = {0: (i, j+1), 1: (i+1, j), 2: (i, j-1), 3: (i-1, j)}
    return next_location[dir]

def path(grid):
    g_rows = len(grid)
    g_cols = len(grid[0])
    q = [(0, 0, 0, 0, 0)]
    seen = {(0, 0, 0, 0)}
    heapq.heapify(q)
    while q:
        dist, i, j, dir, seq = heapq.heappop(q)
        for new_dir in [0, 1, 2, 3]:
            if new_dir == (dir + 2) % 4:
                continue
            i2, j2 = next_location(i, j, new_dir)
            if not (0 <= i2 < g_rows and 0 <= j2 < g_cols):
                continue
            new_seq = 1
            if new_dir == dir:
                if seq >= 3:
                    continue
                else:
                    new_seq = seq + 1
            if i2 == g_rows - 1 and j2 == g_cols - 1:
                return dist + grid[i2][j2]
            key = (i2, j2, new_dir, new_seq)
            if key not in seen:
                heapq.heappush(q, (dist + grid[i2][j2], i2, j2, new_dir, new_seq))
                seen.add(key)
    assert False, 'no path found'


def part1(input):
    grid = [[int(c) for c in line] for line in input.rstrip().split('\n')]
    return path(grid)