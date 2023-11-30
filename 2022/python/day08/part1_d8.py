def process_input(input):
    matrix = []
    for index, line in enumerate(input.strip().split("\n")):
        matrix.append([])
        for num in line:
            matrix[index].append(int(num))
    return matrix

def is_visible_row(matrix, row, col):
    tree = matrix[row][col]
    return max(matrix[row][:col]) < tree or max(matrix[row][col+1:]) < tree

def part1(input):
    matrix = process_input(input)
    transposed = list(map(list, zip(*matrix)))
    visible = 2 * len(matrix) + 2 * len(matrix[1]) - 4   # outer circle
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if is_visible_row(matrix, i, j) or is_visible_row(transposed, j, i):
                visible += 1
    return visible