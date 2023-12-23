import heapq

def next_location(i, j, dir):
    next_location = {0: (i, j+1), 1: (i+1, j), 2: (i, j-1), 3: (i-1, j)}
    return next_location[dir]

def paths(grid):
    g_rows = len(grid)
    g_cols = len(grid[0])
    # distance, i, j, dir, prev_dir
    q = [(0, 0, 1, 0)]
    seen = {(0, 0, 1, 0)}
    heapq.heapify(q)
    paths = []
    while q:
        dist, i, j, dir = heapq.heappop(q)
        for new_dir in [0, 1, 2, 3]:
            if new_dir == (dir + 2) % 4:
                continue
            i2, j2 = next_location(i, j, new_dir)
            if not (0 <= i2 < g_rows and 0 <= j2 < g_cols):
                continue
            if grid[i2][j2] == '#':
                continue
            if grid[i][j] == '>':
                if i2 != i or j2 != j+1:
                    continue
            if grid[i][j] == 'v':
                if j2 != j or i2 != i+1:
                    continue
            if i2 == g_rows - 1 and j2 == g_cols - 2:
                paths.append(dist + 1)
            key = (dist, i2, j2, new_dir)
            if key not in seen:
                heapq.heappush(q, (dist + 1, i2, j2, new_dir))
                seen.add(key)
    return paths


def part1(input: str):
    grid = [[c for c in line] for line in input.rstrip().split('\n')]
    return max(paths(grid))

