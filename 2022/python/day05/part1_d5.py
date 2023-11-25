import string

def string_to_stacks(stack_part):
    stack_lines = stack_part.split("\n")
    length = len(stack_lines[0])
    stacks_num = (length+1)//4
    stacks = [[] for _ in range(stacks_num + 1)]
    for line in stack_lines:
        for i in range(stacks_num):
            if line[i*4+1] in string.ascii_uppercase:
                stacks[i+1].append(line[i*4+1])
    for stack in stacks:
        stack.reverse()
    return stacks

def string_to_moves(moves_part):
    moves = []
    for line in moves_part.split("\n"):
        split_line = line.split(" ")
        moves.append([int(split_line[1]), int(split_line[3]), int(split_line[5])])
    return moves

def read_data(input):
    stack_part, moves_part = input.rstrip().split("\n\n")
    stacks = string_to_stacks(stack_part)
    moves = string_to_moves(moves_part)
    return stacks, moves

def stack_tops_string(stacks):
    return "".join(stack[-1] for stack in stacks[1:])

def process_moves(input):
    stacks, moves = read_data(input)
    for move in moves:
        for i in range(move[0]):
            stacks[move[2]].append(stacks[move[1]].pop())
    return stack_tops_string(stacks)