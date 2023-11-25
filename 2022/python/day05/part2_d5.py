from part1_d5 import read_data, stack_tops_string

def process_moves_9001(input):
    stacks, moves = read_data(input)
    for move in moves:
        stacks[move[2]].extend(stacks[move[1]][-move[0]:])
        stacks[move[1]][-move[0]:] = []
    return stack_tops_string(stacks)