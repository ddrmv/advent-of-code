from collections import deque

def process_input(input: str):
    return [[int(char) for char in line] for line in input.strip().split("\n")]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_grid(g):
    grid_string = ""
    for row in g:
        grid_string += "".join([str(col) for col in row]) + "\n"
    print(grid_string)

# bfs part 1
def trailhead_score(g, i, j, visited):
    q = deque([(i, j, 0)])
    score = 0
    while q:
        i, j, step = q.popleft()
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if g[i][j] == 9:
            score += 1
        for dir in dirs:
            i2, j2 = i + dir[0], j + dir[1]
            if 0 <= i2 < len(g) and 0 <= j2 < len(g[0]) and g[i2][j2] == step + 1 and step < 9:
                q.append((i2, j2, step + 1))
    return score

# dfs part 2
def trailhead_score_part_2(g, i, j, visited):
    if g[i][j] == 9:
        return 1
    score = 0
    for dir in dirs:
        i2, j2 = i + dir[0], j + dir[1]
        if 0 <= i2 < len(g) and 0 <= j2 < len(g[0]) and (i2, j2) not in visited and g[i2][j2] == g[i][j] + 1:
            visited.add((i2, j2))
            score += trailhead_score_part_2(g, i2, j2, visited)
            visited.remove((i2, j2))
    return score


def part1(input):
    g = process_input(input)
    score = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 0:
                visited = set()
                score += trailhead_score(g, i, j, visited)
    return score


def part2(input):
    g = process_input(input)
    score = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 0:
                visited = set()
                score += trailhead_score_part_2(g, i, j, visited)
    return score
