import copy

DIR = {
    "E":  [0, 1],   # East
    "S":  [1, 0],   # South
    "W":  [0, -1],  # West
    "N":  [-1, 0],  # North
}


def get_input_grid(input: str, g, start_pos):
    for line_idx, line in enumerate(input.strip().split('\n')):
        new_line = []
        for char_idx, char in enumerate(line):
            if char == ".":
                new_line.append(0)
            elif char == "^":
                new_line.append(0)
                start_pos[0] = line_idx
                start_pos[1] = char_idx
            elif char == "#":
                new_line.append(-1)
        g.append(new_line)


def print_grid(g):
    grid_printout = ""
    for row in g:
        for col in row:
            if col == 0:
                grid_printout += "."
            elif col == -1:
                grid_printout += "#"
            elif col == 1:
                grid_printout += "X"
        grid_printout += '\n'
    print(grid_printout)


def is_in_g(pos, g):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(g) and pos[1] < len(g[0])


def pos_ahead(pos, dir):
    return [pos[0] + DIR[dir][0], pos[1] + DIR[dir][1]]


def next_pos(pos, dir, g):
    turn_right = {"E": "S", "S": "W", "W": "N", "N": "E"}
    next_pos = pos_ahead(pos, dir)
    if(is_in_g(next_pos, g)):

        if g[next_pos[0]][next_pos[1]] == -1:
            dir = turn_right[dir]
            next_pos = pos_ahead(pos, dir)

            if not (is_in_g(next_pos, g)):
                return [next_pos, dir]
            else:
                if g[next_pos[0]][next_pos[1]] == -1:
                    dir = turn_right[dir]

                    next_pos = pos_ahead(pos, dir)
                return [next_pos, dir]
        else:
            return [next_pos, dir]
    else:
        return [next_pos, dir]


def count_visited(g):
    visited = 0
    for row in g:
        for col in row:
            if col == 1:
                visited += 1
    return visited


# helpers for part 2
def print_gs(g, gs):
    grid_printout = ""
    for row in range(len(gs)):
        for col in range(len(gs[0])):
            if g[row][col] == -1:
                grid_printout += "*"
            else:    
                grid_printout += "." * (4-len(gs[row][col])) + gs[row][col] + " "
        grid_printout += '\n'
    print(grid_printout)



def part1(input):
    g = []
    # start/current position
    pos = [0, 0]
    get_input_grid(input, g, pos)
    dir = "N"
    g[pos[0]][pos[1]] = 1
    while is_in_g(next_pos(pos, dir, g)[0], g):
        pos, dir = next_pos(pos, dir, g)
        g[pos[0]][pos[1]] = 1
    return count_visited(g)



def part2(input):
    start_g = []
    # start/current position
    start_pos = [0, 0]
    start_dir = "N"
    # set initial grid and start_pos
    get_input_grid(input, start_g, start_pos)


    loops = 0
    for row in range(len(start_g)):
        for col in range(len(start_g[0])):
            obstacle_pos = start_g[row][col]
            # skip guard start position
            if obstacle_pos == start_pos:
                continue
            # skip existing obstacle positions
            elif obstacle_pos == -1:
                continue
            # check if obstacle position results in loop
            else:
                path: list[list[int, int], str] = []
                g = copy.deepcopy(start_g)
                # set obstacle
                g[row][col] = -1
                pos = start_pos
                dir = start_dir
                # grid of previous states
                gs = [["" for col in row] for row in g]

                is_loop = False
                g[pos[0]][pos[1]] = 1
                while is_in_g(next_pos(pos, dir, g)[0], g) and not is_loop:
                    pos, dir = next_pos(pos, dir, g)
                    g[pos[0]][pos[1]] = 1
                    if dir in gs[pos[0]][pos[1]]:
                        is_loop = True
                    else:
                        gs[pos[0]][pos[1]] += dir

                if is_loop:
                    loops += 1

    return loops