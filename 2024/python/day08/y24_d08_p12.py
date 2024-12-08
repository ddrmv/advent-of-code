from itertools import combinations

def process_input(input: str):
    g = []
    # build grid
    for line in input.strip().split('\n'):
        nodes = [None if char == "." else char for char in list(line)]
        g.append(nodes)
    return g

def print_grid(g):
    grid_string = ""
    for row in g:
        newline = "".join(["." if not col else col for col in row])
        grid_string += newline + "\n"
    print(grid_string)

def print_antinodes_grid(g):
    grid_string = ""
    for row in g:
        newline = "".join(["." if not col else "#" for col in row])
        grid_string += newline + "\n"
    print(grid_string)



def part1(input):
    g = process_input(input)
    # print_grid(g)

    # get antenna locations by type
    row_num = len(g)
    col_num = len(g[0])
    ant = dict()
    for i in range(row_num):
        for j in range(col_num):
            node_content = g[i][j]
            if node_content:
                if node_content in ant:
                    ant[node_content].append((i, j))
                else:
                    ant[node_content] = [(i, j)]
    
    # set grid for antinodes
    ga = [[False for _ in range(row_num)] for _ in range(row_num)]
    
    # find antinodes
    for a in ant:
        locations = ant[a]

        # get unique combinations
        combinations_iter = combinations(locations, 2)

        # find antinodes for each pair
        for pair in combinations_iter:
            a1, a2 = pair
            y1, x1 = a1
            y2, x2 = a2
            p1 = (2*x1 - x2, 2*y1 - y2)
            p2 = (2*x2 - x1, 2*y2 - y1)

            for p in [p1, p2]:
                y, x = p
                if y >= 0 and y < row_num and x >= 0 and x < col_num:
                    ga[y][x] = True
    
    # count antinodes
    result = 0
    for row in ga:
        for col in row:
            if col:
                result += 1

    return result


def part2(input):
    g = process_input(input)
    # print_grid(g)

    # get antenna locations by type
    row_num = len(g)
    col_num = len(g[0])
    ant = dict()
    for i in range(row_num):
        for j in range(col_num):
            node_content = g[i][j]
            if node_content:
                if node_content in ant:
                    ant[node_content].append((i, j))
                else:
                    ant[node_content] = [(i, j)]
    
    # set grid for antinodes
    ga = [[False for _ in range(row_num)] for _ in range(row_num)]
    
    # set antenna locations as antinodes
    for type in ant:
        if len(ant[type]) > 1:
            for p in ant[type]:
                y, x = p
                ga[y][x] = True

    # find remaning antinodes
    for a in ant:
        # get locations per type a
        locations = ant[a]

        # get unique combinations per type
        combinations_iter = combinations(locations, 2)

        # find repeating antinodes per pair
        for pair in combinations_iter:
            # in both directions
            for o1, o2 in [pair, pair[::-1]]:
                y1, x1 = o1
                y2, x2 = o2
                p1 = (2*y1 - y2, 2*x1 - x2)
                y, x = p1
                # chain harmonics
                while y >= 0 and y < row_num and x >= 0 and x < col_num:
                    ga[y][x] = True
                    y1, x1 = p1
                    y2, x2 = o1
                    o1 = p1
                    p1 = (2*y1 - y2, 2*x1 - x2)
                    y, x = p1

    # count antinodes
    result = 0
    for row in ga:
        for col in row:
            if col:
                result += 1

    return result
