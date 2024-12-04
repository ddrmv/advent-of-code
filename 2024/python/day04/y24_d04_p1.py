DIRECTIONS = {
    "E":  {"row": 0, "col": 1},   # East [0, 1]
    "S":  {"row": 1, "col": 0},   # South [1, 0], 
    "SE": {"row": 1, "col": 1},   # South-East [1, 1], 
    "SW": {"row": 1, "col": -1},  # South-West [1, -1] 
}

def get_input_grid(input):
    grid = []
    for line in input[:-1].split('\n'):
        grid.append(list(line))
    return grid


def check_match(to_check: list, word: str):
    if "".join(to_check) == word:
        return True
    elif "".join(to_check[::-1]) == word:
        return True
    else:
        return False


# helpers for part 1

def get_matches_for_node(row, col, g, word):
    g_col_max = len(g[0])
    g_row_max = len(g)
    len_word = len(word)
    matches = 0
    for dir in DIRECTIONS:
        end_row = row + (len_word - 1) * DIRECTIONS[dir]["row"]
        end_col = col + (len_word - 1) * DIRECTIONS[dir]["col"]
        if end_row < g_row_max and end_col < g_col_max and end_col >= 0:
            new_candidate = ""
            for i in range(len(word)):
                new_candidate += g[row + DIRECTIONS[dir]["row"] * i][col + DIRECTIONS[dir]["col"] * i]
            if check_match(new_candidate, word):
                matches += 1
    return matches

# helpers for part 2
def is_match_for_node_part_2(row, col, g, word):
    # x center must be "A"
    if g[row][col] != "A":
        return False
    
    g_col_max = len(g[0])
    g_row_max = len(g)

    # hardcoded for 3-letter word length
    start_row = row - 1
    start_col = col - 1
    end_row = row + 1
    end_col = col + 1

    # return False if there is no space for x-shape around node
    if not (start_row >= 0 and start_col >= 0 and end_row < g_row_max and end_col < g_col_max):
        return False
    
    # get diagonals
    diag1 = [g[row-1][col-1], g[row][col], g[row+1][col+1]]
    diag2 = [g[row+1][col-1], g[row][col], g[row-1][col+1]]

    return check_match(diag1, "MAS") and check_match(diag2, "MAS")


def part1(input):
    g = get_input_grid(input)
    g_col_max = len(g[0])
    g_row_max = len(g)
    word = "XMAS"

    matches = 0
    for row in range(g_row_max):
        for col in range(g_col_max):
            new_matches = get_matches_for_node(row, col, g, word)
            matches += new_matches

    return matches

# part 2
def part2(input):
    g = get_input_grid(input)
    g_col_max = len(g[0])
    g_row_max = len(g)
    word = "MAS"

    matches = 0
    for row in range(g_row_max):
        for col in range(g_col_max):
            is_match = is_match_for_node_part_2(row, col, g, word)
            matches += is_match * 1

    return matches
